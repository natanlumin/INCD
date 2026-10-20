#!/usr/bin/env python3
"""SCRUM-286 subtasks 2 and 3: aggregate the pulled index into the tables the charts and the provenance
fraction are built from. Reads data/<date>/*.jsonl, writes tables/<date>/*.csv. Pure counting, no sampling
except the stated top-N by 30-day downloads for the 'widely used' set.
Usage: python3 analyse_index.py --date 2026-10-12 [--topn 1000]
"""
import json, os, sys, csv, collections, datetime
args = sys.argv[1:]
date = args[args.index("--date") + 1] if "--date" in args else datetime.date.today().isoformat()
TOPN = int(args[args.index("--topn") + 1]) if "--topn" in args else 1000
here = os.path.dirname(os.path.abspath(__file__)); ddir = os.path.join(here, "data", date); tdir = os.path.join(here, "tables", date)
os.makedirs(tdir, exist_ok=True)
REL = ("finetune", "quantized", "adapter", "merge")
LICENCE_FAMILY = {  # licence tag -> family (style: words, not numbers); unknown tags fall to "other named licence"
    "apache-2.0": "permissive", "mit": "permissive", "bsd-3-clause": "permissive", "bsd-2-clause": "permissive", "bsd": "permissive",
    "cc-by-4.0": "permissive", "cc0-1.0": "permissive", "unlicense": "permissive", "openrail": "open rail", "openrail++": "open rail",
    "creativeml-openrail-m": "open rail", "bigscience-openrail-m": "open rail", "bigscience-bloom-rail-1.0": "open rail", "bigcode-openrail-m": "open rail",
    "llama2": "producer licence", "llama3": "producer licence", "llama3.1": "producer licence", "llama3.2": "producer licence", "llama3.3": "producer licence", "llama4": "producer licence",
    "gemma": "producer licence", "deepseek": "producer licence", "qwen-research": "producer licence", "tongyi-qianwen": "producer licence", "tongyi-qianwen-research": "producer licence",
    "cc-by-nc-4.0": "non-commercial", "cc-by-nc-sa-4.0": "non-commercial", "cc-by-nc-nd-4.0": "non-commercial", "cc-by-sa-4.0": "copyleft", "gpl-3.0": "copyleft", "gpl": "copyleft", "agpl-3.0": "copyleft", "lgpl-3.0": "copyleft", "mpl-2.0": "copyleft", "cc-by-nd-4.0": "non-commercial",
    "other": "other, stated as 'other'", "unknown": "stated as unknown",
}
def month(s): return s[:7] if s else "unknown"
def rels(tags): return {t.split(":")[1] for t in tags if t.startswith("base_model:") and t.count(":") >= 2 and t.split(":")[1] in REL}
if __name__ == "__main__":
    records = 0; by_month_tag = collections.Counter(); by_month_kind = collections.Counter(); by_author_tag = collections.Counter(); by_year_lib = collections.Counter()
    lic = collections.Counter(); lic_by_year = collections.Counter(); card = collections.Counter(); prov = collections.Counter(); top = []
    gated = collections.Counter()
    for fn in sorted(os.listdir(ddir)):
        if not fn.endswith(".jsonl"): continue
        tag = fn[:-6]
        with open(os.path.join(ddir, fn)) as f:
            for line in f:
                m = json.loads(line); records += 1
                tags = m.get("tags") or []; cd = m.get("cardData") or {}; mo = month(m.get("createdAt")); yr = mo[:4]
                r = rels(tags); kind = "quantised" if "quantized" in r else ("adapter" if "adapter" in r else ("merged" if "merge" in r else ("fine-tune" if "finetune" in r else "no typed relation")))
                by_month_tag[(mo, tag)] += 1; by_month_kind[(mo, kind)] += 1; by_author_tag[(m.get("author") or "unknown", tag)] += 1
                by_year_lib[(yr, m.get("library_name") or "none")] += 1
                lt = [t[8:] for t in tags if t.startswith("license:")]; fam = LICENCE_FAMILY.get(lt[0], "other named licence") if lt else "no licence field"
                lic[fam] += 1; lic_by_year[(yr, fam)] += 1
                has_lic = bool(lt); has_base = bool(cd.get("base_model")) or any(t.startswith("base_model:") for t in tags); has_ds = bool(cd.get("datasets")) or any(t.startswith("dataset:") for t in tags)
                has_card = bool(cd); has_lang = bool(cd.get("language"))
                card[("card front matter present", has_card)] += 1; card[("licence field", has_lic)] += 1; card[("base model field", has_base)] += 1; card[("datasets field", has_ds)] += 1; card[("language field", has_lang)] += 1
                gated[bool(m.get("gated"))] += 1
                top.append((m.get("downloads") or 0, m["id"], tag, has_lic, has_base, has_ds, has_card, kind))
    top.sort(reverse=True); widely = top[:TOPN]
    def w(name, header, rows):
        with open(os.path.join(tdir, name), "w", newline="") as f: cw = csv.writer(f); cw.writerow(header); cw.writerows(rows)
    w("volume_by_month_tag.csv", ["month", "task_tag", "models_created"], sorted((k[0], k[1], v) for k, v in by_month_tag.items()))
    w("volume_by_month_kind.csv", ["month", "derivative_kind", "models_created"], sorted((k[0], k[1], v) for k, v in by_month_kind.items()))
    w("library_by_year.csv", ["year", "library", "models_created"], sorted((k[0], k[1], v) for k, v in by_year_lib.items()))
    auth = collections.Counter(); [auth.update({k[0]: v}) for k, v in by_author_tag.items()]
    w("accounts_top100.csv", ["account", "models", "share_of_index"], [(a, n, round(n / records, 5)) for a, n in auth.most_common(100)])
    tot = sum(auth.values()); cum = 0; conc = []
    for i, (a, n) in enumerate(auth.most_common(), 1):
        cum += n
        if i in (1, 10, 100, 1000, 10000): conc.append((i, cum, round(cum / tot, 4)))
    w("account_concentration.csv", ["top_n_accounts", "models", "share_of_index"], conc + [("all accounts", tot, 1.0), ("number of accounts", len(auth), "")])
    w("licence_families.csv", ["licence_family", "models", "share"], [(k, v, round(v / records, 4)) for k, v in lic.most_common()])
    w("licence_families_by_year.csv", ["year", "licence_family", "models"], sorted((k[0], k[1], v) for k, v in lic_by_year.items()))
    w("card_completeness.csv", ["field", "present", "models", "share"], [(k[0], k[1], v, round(v / records, 4)) for k, v in sorted(card.items())])
    w("gated.csv", ["gated", "models", "share"], [(k, v, round(v / records, 4)) for k, v in gated.items()])
    def frac(rows, idx): return round(sum(1 for r in rows if r[idx]) / len(rows), 4) if rows else ""
    def both(rows): return round(sum(1 for r in rows if r[3] and r[4]) / len(rows), 4) if rows else ""
    def any3(rows): return round(sum(1 for r in rows if r[3] and r[4] and r[5]) / len(rows), 4) if rows else ""
    prov_rows = [("all models in the index", records, frac(top, 3), frac(top, 4), frac(top, 5), frac(top, 6), both(top), any3(top)),
                 (f"widely used: top {TOPN} by 30-day downloads", len(widely), frac(widely, 3), frac(widely, 4), frac(widely, 5), frac(widely, 6), both(widely), any3(widely))]
    for n in (100, 10000):
        sub = top[:n]; prov_rows.append((f"top {n} by 30-day downloads", len(sub), frac(sub, 3), frac(sub, 4), frac(sub, 5), frac(sub, 6), both(sub), any3(sub)))
    w("provenance_metadata.csv", ["population", "models", "licence_field", "base_model_field", "datasets_field", "card_front_matter", "licence_and_base_model", "licence_base_model_and_datasets"], prov_rows)
    w("widely_used_sample.csv", ["downloads_30d", "model", "task_tag", "licence", "base_model", "datasets", "card", "derivative_kind"], widely)
    with open(os.path.join(tdir, "README.md"), "w") as f:
        f.write(f"Tables derived from data/{date} by analyse_index.py on {datetime.date.today().isoformat()}; records read: {records}; widely-used sample: top {TOPN} by 30-day downloads across the five task tags.\n")
    print("records", records, "tables in", tdir)
