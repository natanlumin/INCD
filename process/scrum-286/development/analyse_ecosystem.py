#!/usr/bin/env python3
"""SCRUM-286 subtasks 2 and 3, ecosystem version: normalise the pulled indices of the repositories (Hub,
ModelScope, Kaggle) into one record shape and aggregate per repository. Reads data/<date>/, writes
tables/<date>/eco_*.csv. Standard library only. Usage: python3 analyse_ecosystem.py --date 2026-10-12 --topn 1000
"""
import json, os, sys, csv, collections, datetime
a = sys.argv[1:]; date = a[a.index("--date") + 1] if "--date" in a else datetime.date.today().isoformat()
TOPN = int(a[a.index("--topn") + 1]) if "--topn" in a else 1000
here = os.path.dirname(os.path.abspath(__file__)); ddir = os.path.join(here, "data", date); tdir = os.path.join(here, "tables", date); os.makedirs(tdir, exist_ok=True)
from analyse_index import LICENCE_FAMILY  # same grouping for every repository
REL = {"finetune": "fine-tune", "quantized": "quantised", "adapter": "adapter", "merge": "merged"}
ORDER = ["quantised", "adapter", "merged", "fine-tune"]
def kind_of(rels):
    for k in ORDER:
        if k in rels: return k
    return "no typed relation"
def hub():
    for fn in sorted(os.listdir(ddir)):
        if not fn.endswith(".jsonl"): continue
        tag = fn[:-6]
        for line in open(os.path.join(ddir, fn)):
            m = json.loads(line); tags = m.get("tags") or []; cd = m.get("cardData") or {}
            rels = {REL[t.split(":")[1]] for t in tags if t.startswith("base_model:") and t.count(":") >= 2 and t.split(":")[1] in REL}
            lic = [t[8:] for t in tags if t.startswith("license:")]
            yield {"platform": "Hugging Face Hub", "id": m["id"], "account": m.get("author") or "unknown", "created": (m.get("createdAt") or "")[:7], "downloads": m.get("downloads") or 0,
                   "task": tag, "licence": lic[0] if lic else None, "base_model": bool(cd.get("base_model")) or any(t.startswith("base_model:") for t in tags),
                   "datasets": bool(cd.get("datasets")) or any(t.startswith("dataset:") for t in tags), "card": bool(cd), "kind": kind_of(rels)}
def modelscope():
    d = os.path.join(ddir, "modelscope")
    if not os.path.isdir(d): return
    seen = set()
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".jsonl"): continue
        tag = fn.split(".")[0]
        for line in open(os.path.join(d, fn)):
            m = json.loads(line)
            if m["Id"] in seen: continue
            seen.add(m["Id"]); rel = m.get("BaseModelRelation"); rels = {REL[rel]} if rel in REL else set()
            lic = (m.get("LicenseName") or m.get("License") or "").strip().lower() or None
            ds = m.get("Datasets"); ds = bool(ds) and ds not in ("{}", "[]", {}, [])
            yield {"platform": "ModelScope", "id": m["Path"] + "/" + m["Name"], "account": m.get("Path") or "unknown", "created": (m.get("CreatedAt") or "")[:7], "downloads": m.get("Downloads") or 0,
                   "task": tag, "licence": lic, "base_model": bool(m.get("BaseModel")) and m.get("BaseModel") not in ("[]", []), "datasets": ds, "card": None, "kind": kind_of(rels)}
def kaggle():
    d = os.path.join(ddir, "kaggle"); seen = set()
    if not os.path.isdir(d): return
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".jsonl"): continue
        for line in open(os.path.join(d, fn)):
            m = json.loads(line)
            if m.get("id") in seen: continue
            seen.add(m.get("id")); yield {"platform": "Kaggle Models", "id": m.get("ref"), "account": (m.get("ref") or "/").split("/")[0], "created": (m.get("updateTime") or "")[:7], "downloads": None,
               "task": None, "licence": None, "base_model": None, "datasets": None, "card": None, "kind": None, "provenance_sources": bool(m.get("provenanceSources"))}
recs = collections.defaultdict(int); vol = collections.Counter(); kinds = collections.Counter(); lic = collections.Counter(); fields = collections.Counter(); acc = collections.defaultdict(collections.Counter); top = collections.defaultdict(list); kag_prov = collections.Counter()
for r in list(hub()) + list(modelscope()) + list(kaggle()):
    P = r["platform"]; recs[P] += 1; y = r["created"][:4] or "unknown"
    vol[(P, y, r["task"] or "all")] += 1
    if r["kind"] is not None: kinds[(P, y, r["kind"])] += 1
    if P != "Kaggle Models":
        fam = LICENCE_FAMILY.get(r["licence"], "other named licence") if r["licence"] else "no licence field"; lic[(P, fam)] += 1
        for f, v in (("licence field", bool(r["licence"])), ("base model field", r["base_model"]), ("datasets field", r["datasets"])): fields[(P, f, bool(v))] += 1
        top[P].append((r["downloads"], r["id"], bool(r["licence"]), bool(r["base_model"]), bool(r["datasets"])))
    else: kag_prov[r["provenance_sources"]] += 1
    acc[P][r["account"]] += 1
def w(name, header, rows):
    with open(os.path.join(tdir, name), "w", newline="") as f: cw = csv.writer(f); cw.writerow(header); cw.writerows(rows)
w("eco_records.csv", ["platform", "records"], sorted(recs.items()))
w("eco_volume_by_year.csv", ["platform", "year", "task", "models"], sorted((k[0], k[1], k[2], v) for k, v in vol.items()))
w("eco_kind_by_year.csv", ["platform", "year", "kind", "models"], sorted((k[0], k[1], k[2], v) for k, v in kinds.items()))
w("eco_licence_families.csv", ["platform", "licence_family", "models", "share"], sorted((k[0], k[1], v, round(v / recs[k[0]], 4)) for k, v in lic.items()))
w("eco_fields.csv", ["platform", "field", "present", "models", "share"], sorted((k[0], k[1], k[2], v, round(v / recs[k[0]], 4)) for k, v in fields.items()))
conc = []
for P, c in acc.items():
    tot = sum(c.values()); cum = 0
    for i, (_, n) in enumerate(c.most_common(), 1):
        cum += n
        if i in (1, 10, 100, 1000, 10000): conc.append((P, i, cum, round(cum / tot, 4)))
    conc.append((P, "number of accounts", len(c), ""))
w("eco_account_concentration.csv", ["platform", "top_n_accounts", "models", "share"], conc)
prov = []
for P, rows in top.items():
    rows.sort(reverse=True)
    for label, sub in (("all", rows), (f"top {TOPN} by downloads", rows[:TOPN]), ("top 100 by downloads", rows[:100])):
        n = len(sub); prov.append((P, label, n, round(sum(1 for r in sub if r[2]) / n, 4), round(sum(1 for r in sub if r[3]) / n, 4), round(sum(1 for r in sub if r[4]) / n, 4), round(sum(1 for r in sub if r[2] and r[3]) / n, 4), round(sum(1 for r in sub if r[2] and r[3] and r[4]) / n, 4), sub[-1][0] if sub else ""))
w("eco_provenance_by_population.csv", ["platform", "population", "models", "licence_field", "base_model_field", "datasets_field", "licence_and_base_model", "all_three", "download_threshold"], prov)
w("eco_kaggle_provenance_sources.csv", ["provenance_sources_present", "models"], sorted(kag_prov.items()))
print("records", dict(recs), "tables in", tdir)
