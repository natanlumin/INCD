#!/usr/bin/env python3
"""SCRUM-286 subtask 1: pull the Kaggle Models public listing.
Method: GET https://www.kaggle.com/api/v1/models/list?pageSize=100[&pageToken=...] following nextPageToken
until exhausted. One JSONL, data/<date>/kaggle/models.jsonl, fields in KEEP. No key needed for the public list.
Re-run: python3 pull_kaggle.py [--date YYYY-MM-DD] [--sort createTime|voteCount]; the default order stops answering
after about 5,800 records (HTTP 500), so three orders are pulled and united by id in analyse_ecosystem.py.
"""
import json, os, sys, time, urllib.request, urllib.parse, datetime
KEEP = ["id", "ref", "title", "author", "slug", "isPrivate", "tags", "provenanceSources", "url", "voteCount", "updateTime", "instances", "modelVersionLinks"]
BASE = "https://www.kaggle.com/api/v1/models/list"
def get(url, tries=6):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "INCD-report-index-pull/1.0"})
            with urllib.request.urlopen(req, timeout=120) as r: return json.load(r)
        except Exception as e:
            wait = 5 * (i + 1); print(f"  retry {i+1} after {e}; sleeping {wait}s", flush=True); time.sleep(wait)
    raise SystemExit("gave up on " + url)
if __name__ == "__main__":
    a = sys.argv[1:]; date = a[a.index("--date") + 1] if "--date" in a else datetime.date.today().isoformat()
    sort = a[a.index("--sort") + 1] if "--sort" in a else None
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", date, "kaggle"); os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, f"models-{sort}.jsonl" if sort else "models.jsonl"); token = None; n = 0; pages = 0; t0 = time.time(); total = None; seen = set()
    with open(path, "w") as f, open(os.path.join(outdir, "pull.log"), "a") as log:
        log.write(f"{datetime.datetime.utcnow().isoformat()}Z START {BASE}?pageSize=100 sortBy={sort}\n")
        while True:
            q = {"pageSize": "100"}
            if sort: q["sortBy"] = sort
            
            if token: q["pageToken"] = token
            d = get(BASE + "?" + urllib.parse.urlencode(q)); pages += 1; total = d.get("totalResults", total)
            for m in d.get("models", []):
                if m.get("id") in seen: continue
                seen.add(m.get("id")); f.write(json.dumps({k: m.get(k) for k in KEEP}, ensure_ascii=False) + "\n"); n += 1
            token = d.get("nextPageToken")
            if pages % 20 == 0: print(f"  kaggle: {pages} pages, {n} records, {time.time()-t0:.0f}s", flush=True)
            if not token or not d.get("models"): break
            time.sleep(0.2)
        log.write(f"{datetime.datetime.utcnow().isoformat()}Z END records={n} pages={pages} totalResults={total} seconds={time.time()-t0:.0f}\n")
    print(f"kaggle: {n} records in {pages} pages; totalResults {total}; {time.time()-t0:.0f}s")
