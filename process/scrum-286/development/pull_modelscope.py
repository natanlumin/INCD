#!/usr/bin/env python3
"""SCRUM-286 subtask 1: pull the ModelScope model index for the segmentation's five task tags.
Method: PUT https://www.modelscope.cn/api/v1/dolphin/models with JSON body {PageSize:100, PageNumber:n,
Criterion:[{category:"tasks", predicate:"contains", values:[<tag>]}]}, pages 1..ceil(TotalCount/100).
One JSONL per tag in data/<date>/modelscope/, fields in KEEP. Records de-duplicated by Id across pages.
Re-run: python3 pull_modelscope.py [--date YYYY-MM-DD] [--tags a,b]
"""
import json, os, sys, time, math, urllib.request, datetime
TAGS = ["text-generation", "text-classification", "feature-extraction", "sentence-similarity", "image-text-to-text"]
KEEP = ["Id", "Name", "Path", "CreatedTime", "LastUpdatedTime", "Downloads", "Stars", "License", "LicenseName", "BaseModel",
        "BaseModelRelation", "Datasets", "Libraries", "Frameworks", "ModelSource", "FromSite", "IsCertification", "StorageSize", "Tags", "Language", "Visibility"]
URL = "https://www.modelscope.cn/api/v1/dolphin/models"
def page(tag, n, tries=6):
    body = json.dumps({"PageSize": 100, "PageNumber": n, "SortBy": "Default", "Target": "", "SingleCriterion": [],
                       "Criterion": [{"category": "tasks", "predicate": "contains", "values": [tag]}]}).encode()
    for i in range(tries):
        try:
            req = urllib.request.Request(URL, data=body, method="PUT", headers={"Content-Type": "application/json", "User-Agent": "INCD-report-index-pull/1.0"})
            with urllib.request.urlopen(req, timeout=120) as r: d = json.load(r)["Data"]["Model"]
            return d.get("TotalCount"), d.get("Models") or []
        except Exception as e:
            wait = 5 * (i + 1); print(f"  retry {i+1} page {n} after {e}; sleeping {wait}s", flush=True); time.sleep(wait)
    raise SystemExit(f"gave up on {tag} page {n}")
def pull(tag, outdir):
    path = os.path.join(outdir, f"{tag}.jsonl"); logp = os.path.join(outdir, "pull.log"); seen = set(); t0 = time.time()
    total, recs = page(tag, 1); pages = math.ceil(total / 100)
    with open(path, "w") as f, open(logp, "a") as log:
        log.write(f"{datetime.datetime.utcnow().isoformat()}Z START {tag} TotalCount={total} pages={pages}\n")
        n = 1
        while True:
            for m in recs:
                if m["Id"] in seen: continue
                seen.add(m["Id"]); rec = {k: m.get(k) for k in KEEP}
                rec["Tasks"] = [t.get("Name") for t in (m.get("Tasks") or [])]; rec["Organization"] = (m.get("Organization") or {}).get("Name") if isinstance(m.get("Organization"), dict) else None
                rec["CreatedAt"] = datetime.datetime.utcfromtimestamp(m["CreatedTime"]).isoformat() + "Z" if m.get("CreatedTime") else None
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            if n >= pages: break
            n += 1; _, recs = page(tag, n); time.sleep(0.2)
            if n % 50 == 0: print(f"  {tag}: page {n}/{pages}, {len(seen)} records, {time.time()-t0:.0f}s", flush=True)
        log.write(f"{datetime.datetime.utcnow().isoformat()}Z END {tag} records={len(seen)} pages={pages} seconds={time.time()-t0:.0f}\n")
    print(f"{tag}: {len(seen)} records of TotalCount {total} in {pages} pages, {time.time()-t0:.0f}s", flush=True); return len(seen)
if __name__ == "__main__":
    a = sys.argv[1:]; date = a[a.index("--date") + 1] if "--date" in a else datetime.date.today().isoformat()
    tags = a[a.index("--tags") + 1].split(",") if "--tags" in a else TAGS
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", date, "modelscope"); os.makedirs(outdir, exist_ok=True)
    total = sum(pull(t, outdir) for t in tags)
    with open(os.path.join(outdir, "pull.log"), "a") as log: log.write(f"TOTAL records={total} tags={','.join(tags)}\n")
    print("total", total)
