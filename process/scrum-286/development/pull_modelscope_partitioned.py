#!/usr/bin/env python3
"""SCRUM-286 subtask 1: ModelScope, partitioned pull for a task tag whose TotalCount exceeds the interface's
10,000-record paging cap (pages beyond offset 10,000 return list_models_failed).
Method: read the facet counts (FiledAgg) for the tag, then run one query per facet value (licence, model
type, library), splitting any facet value above the cap by model type, and finally the whole tag under each
of the four sort orders (Default, DownloadsCount, StarsCount, GmtModified). Every query pages to its end
or to the cap. Records are written as they arrive; duplicates across queries are removed by Id downstream
(analyse_ecosystem.py) and the coverage, distinct Ids against TotalCount, is logged.
Usage: python3 pull_modelscope_partitioned.py --date D --tag text-generation [--shard i/n]
"""
import json, os, sys, time, math, urllib.request, datetime
URL = "https://www.modelscope.cn/api/v1/dolphin/models"; CAP = 10000
KEEP = ["Id", "Name", "Path", "CreatedTime", "LastUpdatedTime", "Downloads", "Stars", "License", "LicenseName", "BaseModel", "BaseModelRelation", "Datasets", "Libraries", "Frameworks", "ModelSource", "FromSite", "IsCertification", "StorageSize", "Tags", "Language", "Visibility"]
def call(criteria, n, size, sort="Default", tries=5):
    body = json.dumps({"PageSize": size, "PageNumber": n, "SortBy": sort, "Target": "", "SingleCriterion": [], "Criterion": criteria}).encode()
    for i in range(tries):
        try:
            req = urllib.request.Request(URL, data=body, method="PUT", headers={"Content-Type": "application/json", "User-Agent": "INCD-report-index-pull/1.0"})
            with urllib.request.urlopen(req, timeout=120) as r: d = json.load(r)
            if not d.get("Success", True) and d.get("Code") != 200: return None, [], {}
            D = d["Data"]; return D["Model"].get("TotalCount"), D["Model"].get("Models") or [], D.get("FiledAgg") or {}
        except Exception as e:
            time.sleep(4 * (i + 1))
    return None, [], {}
def crit(tag, extra=None):
    c = [{"category": "tasks", "predicate": "contains", "values": [tag]}]
    if extra: c.append({"category": extra[0], "predicate": "contains", "values": [extra[1]]})
    return c
def rec(m):
    r = {k: m.get(k) for k in KEEP}; r["Tasks"] = [t.get("Name") for t in (m.get("Tasks") or [])]
    r["Organization"] = (m.get("Organization") or {}).get("Name") if isinstance(m.get("Organization"), dict) else None
    r["CreatedAt"] = datetime.datetime.utcfromtimestamp(m["CreatedTime"]).isoformat() + "Z" if m.get("CreatedTime") else None
    return r
if __name__ == "__main__":
    a = sys.argv[1:]; date = a[a.index("--date") + 1]; tag = a[a.index("--tag") + 1]
    shard, nshards = (map(int, a[a.index("--shard") + 1].split("/")) if "--shard" in a else (0, 1))
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", date, "modelscope"); os.makedirs(outdir, exist_ok=True)
    total, _, agg = call(crit(tag), 1, 1)
    queries = [(crit(tag), s) for s in ("Default", "DownloadsCount", "StarsCount", "GmtModified")]
    for facet in ("license", "model_type", "libraries"):
        for v in agg.get(facet, []):
            if v["Count"] <= CAP: queries.append((crit(tag, (facet, v["Value"])), "Default"))
            else:
                for s in ("Default", "DownloadsCount", "StarsCount", "GmtModified"): queries.append((crit(tag, (facet, v["Value"])), s))
                for mt in agg.get("model_type", []): queries.append((crit(tag, (facet, v["Value"])) + [{"category": "model_type", "predicate": "contains", "values": [mt["Value"]]}], "Default"))
    mine = [q for i, q in enumerate(queries) if i % nshards == shard]
    path = os.path.join(outdir, f"{tag}.part{shard}.jsonl"); seen = set(); t0 = time.time()
    with open(path, "w") as f, open(os.path.join(outdir, "pull.log"), "a") as log:
        log.write(f"{datetime.datetime.utcnow().isoformat()}Z START partitioned {tag} shard {shard}/{nshards} TotalCount={total} queries={len(mine)} of {len(queries)}\n")
        for qi, (c, s) in enumerate(mine):
            n = 1; got = 0
            while True:
                tc, recs, _ = call(c, n, 100, s)
                if not recs: break
                for m in recs:
                    if m["Id"] not in seen: seen.add(m["Id"]); f.write(json.dumps(rec(m), ensure_ascii=False) + "\n")
                got += len(recs)
                if got >= min(tc or 0, CAP) or n >= CAP // 100: break
                n += 1; time.sleep(0.15)
            if qi % 10 == 0: print(f"shard {shard}: query {qi+1}/{len(mine)}, distinct {len(seen)}, {time.time()-t0:.0f}s", flush=True)
        log.write(f"{datetime.datetime.utcnow().isoformat()}Z END partitioned {tag} shard {shard}/{nshards} distinct={len(seen)} seconds={time.time()-t0:.0f}\n")
    print(f"shard {shard}: distinct {len(seen)} records, {time.time()-t0:.0f}s")
