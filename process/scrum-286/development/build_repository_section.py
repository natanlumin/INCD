#!/usr/bin/env python3
"""SCRUM-286: build the per-repository tables of the task (scrum286.md) from tables/<date>/eco_*.csv and
place them between the markers <!-- eco:start --> and <!-- eco:end -->. Usage: python3 build_repository_section.py --date D
"""
import csv, os, sys, collections, re, json
a = sys.argv[1:]; date = a[a.index("--date") + 1]
here = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(here, "tables", date); task = os.path.join(os.path.dirname(here), "scrum286.md")
def rd(n): return list(csv.DictReader(open(os.path.join(T, n))))
recs = {r["platform"]: int(r["records"]) for r in rd("eco_records.csv")}
P = ["Hugging Face Hub", "ModelScope"]; years = ["2022", "2023", "2024", "2025", "2026"]
# coverage of ModelScope text generation
ms_tg = 0; seen = set()
d = os.path.join(here, "data", date, "modelscope")
for fn in os.listdir(d):
    if fn.startswith("text-generation") and fn.endswith(".jsonl"):
        for line in open(os.path.join(d, fn)): seen.add(json.loads(line)["Id"])
ms_tg = len(seen)
vol = collections.Counter(); tot = collections.Counter(); kind = collections.Counter()
for r in rd("eco_volume_by_year.csv"): vol[(r["platform"], r["year"])] += int(r["models"])
for r in rd("eco_kind_by_year.csv"):
    tot[(r["platform"], r["year"])] += int(r["models"])
    if r["kind"] != "no typed relation": kind[(r["platform"], r["year"])] += int(r["models"])
t8 = "| Year | " + " | ".join(P) + " |\n|---|---|---|\n" + "\n".join(f"| {y}{' (to 12 Oct)' if y=='2026' else ''} | " + " | ".join(f"{vol[(p,y)]:,}" for p in P) + " |" for y in years)
t9 = "| Year | " + " | ".join(f"{p}: typed relation, share" for p in P) + " |\n|---|---|---|\n" + "\n".join(f"| {y} | " + " | ".join((f"{kind[(p,y)]/tot[(p,y)]*100:.0f}%" if tot[(p,y)] else "–") for p in P) + " |" for y in years[1:])
lic = collections.defaultdict(dict)
for r in rd("eco_licence_families.csv"): lic[r["platform"]][r["licence_family"]] = float(r["share"])
fams = ["no licence field", "permissive", "producer licence", "other, stated as 'other'", "non-commercial", "copyleft", "open rail", "other named licence", "stated as unknown"]
t10 = "| Licence family | " + " | ".join(P) + " |\n|---|---|---|\n" + "\n".join(f"| {f} | " + " | ".join(f"{lic[p].get(f,0)*100:.1f}%" for p in P) + " |" for f in fams)
fld = {}
for r in rd("eco_fields.csv"):
    if r["present"] == "True": fld[(r["platform"], r["field"])] = float(r["share"])
t11 = "| Field | " + " | ".join(P) + " |\n|---|---|---|\n" + "\n".join(f"| {f} | " + " | ".join(f"{fld.get((p,f),0)*100:.0f}%" for p in P) + " |" for f in ["licence field", "base model field", "datasets field"])
prov = {(r["platform"], r["population"]): r for r in rd("eco_provenance_by_population.csv")}
pops = [("top 100 by downloads", "top 100 by downloads"), ("top 1000 by downloads", "top 1,000 (the widely used sample)"), ("all", "all models in the index")]
t12 = "| Population | Repository | Models | Licence field | Base-model field | Datasets field | Licence and base model | All three | Download threshold |\n|---|---|---|---|---|---|---|---|---|\n" + "\n".join(
    f"| {lab} | {p} | {int(prov[(p,k)]['models']):,} | {float(prov[(p,k)]['licence_field'])*100:.0f}% | {float(prov[(p,k)]['base_model_field'])*100:.0f}% | {float(prov[(p,k)]['datasets_field'])*100:.0f}% | {float(prov[(p,k)]['licence_and_base_model'])*100:.0f}% | {float(prov[(p,k)]['all_three'])*100:.0f}% | {int(float(prov[(p,k)]['download_threshold'] or 0)):,} |"
    for k, lab in pops for p in P if (p, k) in prov)
conc = collections.defaultdict(dict); nacc = {}
for r in rd("eco_account_concentration.csv"):
    if r["top_n_accounts"].isdigit(): conc[r["platform"]][int(r["top_n_accounts"])] = float(r["share"])
    else: nacc[r["platform"]] = int(r["models"])
P3 = P + ["Kaggle Models"]
t13 = "| Accounts, ranked by models | " + " | ".join(P3) + " |\n|---|---|---|---|\n" + "\n".join(f"| top {n:,} | " + " | ".join((f"{conc[p][n]*100:.1f}%" if n in conc[p] else "–") for p in P3) + " |" for n in (1, 10, 100, 1000, 10000)) + "\n| number of accounts | " + " | ".join(f"{nacc.get(p,0):,}" for p in P3) + " |"
kp = {r["provenance_sources_present"]: int(r["models"]) for r in rd("eco_kaggle_provenance_sources.csv")}; kag = recs.get("Kaggle Models", 0)
section = f"""<!-- eco:start -->
## 1a. The other repositories beside the Hub

The sections above are the Hub's series. This section puts ModelScope beside it on the same method, and Kaggle Models where it has the field, so that each finding can be read as a property of the ecosystem or of one repository. Pulls of 12 October 2026, method in the annex; ModelScope's text-generation index is {ms_tg:,} of 48,730 distinct records ({ms_tg/48730*100:.0f}%), assembled from partitioned queries because the interface caps paging at 10,000, and its four other task tags are complete; Kaggle Models is {kag:,} distinct records from three sort orders of a listing that reports at most 10,000 per query.

**Table 8. Model repositories created per year, Hub and ModelScope** (same five task tags; creation date of the repository record)

{t8}

ModelScope's index under the five tags is {recs.get('ModelScope',0):,} records against the Hub's {recs.get('Hugging Face Hub',0):,}, a fourteenth, and its growth starts two years later: almost nothing before 2024, then a year-on-year rise of the same shape as the Hub's. Kaggle Models lists {kag:,} models in all, without a task field, and its date is the last update rather than creation, so it is not a series here.

**Table 9. Share of new repositories that declare a typed parent relation, Hub and ModelScope**

{t9}

The derivative trend is the ecosystem's, not the Hub's: ModelScope records the same typed relation and shows the same rise, from a quarter of new repositories in 2024 to two thirds in 2026.

**Table 10. Licence families, Hub and ModelScope** (share of each repository's index)

{t10}

**Table 11. Card fields present, Hub and ModelScope**

{t11}

The licence field is where the repositories differ. ModelScope's upload flow records a licence on {fld.get(('ModelScope','licence field'),0)*100:.0f}% of its index against the Hub's {fld.get(('Hugging Face Hub','licence field'),0)*100:.0f}%, so a blank licence is a Hub habit, not an ecosystem one. The parent and datasets fields are filled at the same low rates on both, which makes the assessment gap at selection, parent relation and training data, an ecosystem finding. Kaggle Models has one provenance field of its own, a free-text "provenance sources", present on {kp.get('True',0)/kag*100 if kag else 0:.0f}% of its models.

**Table 12. Declared fields present, by population and repository** (downloads are each repository's own counter on the cut-off date)

{t12}

The widely used fraction holds across the two repositories: with the same definition, a licence and a declared parent both present, the top thousand by downloads give {float(prov[('Hugging Face Hub','top 1000 by downloads')]['licence_and_base_model'])*100:.0f}% on the Hub and {float(prov[('ModelScope','top 1000 by downloads')]['licence_and_base_model'])*100:.0f}% on ModelScope, and the stricter cut with training data is below one in ten on both.

**Table 13. Account concentration, by repository**

{t13}

Concentration is where the repositories differ most. The Hub's index is spread over {nacc.get('Hugging Face Hub',0):,} accounts and its hundred largest hold {conc['Hugging Face Hub'].get(100,0)*100:.0f}%; ModelScope's {nacc.get('ModelScope',0):,} accounts have their hundred largest holding {conc['ModelScope'].get(100,0)*100:.0f}%, and its ten largest {conc['ModelScope'].get(10,0)*100:.0f}%, the producers and mirrors of the Chinese model families. Kaggle Models sits between. For selection this means the account name carries more information on ModelScope than on the Hub, and the forecast on account reputation in section 3 is a Hub finding.

**Figures 4 to 6**, the Hub and ModelScope side by side: models created per year, the typed-relation share per year, and account concentration.

![Models created per year by repository](development/charts/2026-10-12/eco1_volume_by_year_repository.png)

![Typed relation share by repository](development/charts/2026-10-12/eco2_derivative_share_by_year_repository.png)

![Account concentration by repository](development/charts/2026-10-12/eco3_account_concentration_repository.png)

The registry and the redistributors, Ollama, the cloud model gardens, the packaged inference microservices and the hosted inference providers, expose no per-model index of this kind and enter the report with their catalogue sizes in the landscape item; they are the channels through which the repositories' models reach use, not places where models are published first.
<!-- eco:end -->"""
s = open(task).read()
if "<!-- eco:start -->" in s: s = re.sub(r"<!-- eco:start -->.*?<!-- eco:end -->", lambda m: section, s, flags=re.S)
else: s = s.replace("## 2. Licensing and provenance in practice", section + "\n\n## 2. Licensing and provenance in practice", 1)
open(task, "w").write(s); print("section written; ModelScope text-generation coverage", ms_tg)
