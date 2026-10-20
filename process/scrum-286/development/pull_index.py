#!/usr/bin/env python3
"""SCRUM-286 subtask 1: pull the Hugging Face Hub model index for the segmentation's task tags.

Method: GET https://huggingface.co/api/models?pipeline_tag=<tag>&limit=1000&expand[]=... following the
cursor in the Link header until exhausted. One JSONL file per tag in data/<date>/, one record per model
with the fields listed in FIELDS. Re-run: python3 pull_index.py [--date YYYY-MM-DD] [--tags a,b].
"""
import json, os, re, sys, time, urllib.request, urllib.parse, datetime
TAGS = ["text-generation", "text-classification", "feature-extraction", "sentence-similarity", "image-text-to-text"]
EXPAND = ["author", "createdAt", "lastModified", "downloads", "downloadsAllTime", "likes", "pipeline_tag",
          "library_name", "tags", "gated", "private", "cardData", "sha"]
BASE = "https://huggingface.co/api/models"
def get(url, tries=6):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "INCD-report-index-pull/1.0"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read(), r.headers.get("Link", "")
        except Exception as e:
            wait = 5 * (i + 1); print(f"  retry {i+1} after error {e}; sleeping {wait}s", flush=True); time.sleep(wait)
    raise SystemExit("gave up on " + url)
def pull(tag, outdir):
    path = os.path.join(outdir, f"{tag}.jsonl"); logp = os.path.join(outdir, "pull.log")
    q = {"pipeline_tag": tag, "limit": "1000"}
    url = BASE + "?" + urllib.parse.urlencode(q) + "".join("&expand[]=" + e for e in EXPAND)
    n = 0; pages = 0; t0 = time.time()
    with open(path, "w") as f, open(logp, "a") as log:
        log.write(f"{datetime.datetime.utcnow().isoformat()}Z START {tag} {url}\n")
        while url:
            body, link = get(url); pages += 1
            recs = json.loads(body)
            for m in recs:
                f.write(json.dumps({k: m.get(k) for k in ["id", "_id", "sha"] + EXPAND}, ensure_ascii=False) + "\n")
            n += len(recs)
            nxt = re.search(r'<([^>]+)>;\s*rel="next"', link or "")
            url = nxt.group(1) if nxt else None
            if pages % 20 == 0: print(f"  {tag}: {pages} pages, {n} records, {time.time()-t0:.0f}s", flush=True)
        log.write(f"{datetime.datetime.utcnow().isoformat()}Z END {tag} pages={pages} records={n} seconds={time.time()-t0:.0f}\n")
    print(f"{tag}: {n} records in {pages} pages, {time.time()-t0:.0f}s", flush=True)
    return n
if __name__ == "__main__":
    args = sys.argv[1:]
    date = args[args.index("--date") + 1] if "--date" in args else datetime.date.today().isoformat()
    tags = args[args.index("--tags") + 1].split(",") if "--tags" in args else TAGS
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", date); os.makedirs(outdir, exist_ok=True)
    total = sum(pull(t, outdir) for t in tags)
    with open(os.path.join(outdir, "pull.log"), "a") as log: log.write(f"TOTAL records={total} tags={','.join(tags)}\n")
    print("total", total)
