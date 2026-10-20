# SCRUM-286: Quantify the ecosystem (LAND-2)

Subtask texts for Jira, one file each. Status as of 12 October 2026: first draft of subtasks 1 to 4 built on the Hugging Face Hub alone; replanned the same day to rely on all the repositories and channels of the landscape item, because the Jira says ecosystem. All three repository pulls done (Hub complete; ModelScope four tags complete and text generation at 99% coverage under its 10,000-record paging cap; Kaggle 16,123 distinct from three sort orders); Ollama and the redistributors mentioned with 280's sizes, no series; the task carries the Hub's series in sections 1 and 2 and the per-repository comparison in section 1a, Tables 8 to 13 and Figures 4 to 6; subtask 5 pending the reviewers. LAND-1 (SCRUM-280) is drafted and awaiting the taxonomy freeze. Blocks ASM-2 and RPT-3. Effort: Natan 1.25d planned (10h); the replanned total is 13h = 1.6d, 3h over, all of it in subtask 1 and the per-platform tables. Lior 0.25d, Dan 0.25d.

| # | Subtask | Est. |
|---|---|---|
| 1 | Build the model index across the repositories: retrievable data, method and cut-off date | 5h, done 12 Oct (three repositories; coverage stated) |
| 2 | Release trends: volume, derivatives, publisher concentration | 2.5h, drafted: Hub series plus per-repository comparison |
| 3 | What is knowable before running: licence, card, training data, provenance | 3h, drafted: Hub series plus per-repository comparison |
| 4 | Forward view, 12 to 24 months, with confidence labels | 1.5h, drafted on the Hub series, with the ModelScope series confirming the derivative trend |
| 5 | Draft the subsections and hand to the reviewers | 1h, pending Lior and Dan |

Skeleton map: 3.3 Release trends and ecosystem growth (subtask 2), 3.4 Licensing and provenance in practice (subtask 3), 3.5 Ecosystem outlook (subtask 4). 3.1 and 3.2 are SCRUM-280's.

## The ecosystem, as this item counts it

The ecosystem is the platform set of the landscape item (SCRUM-280), not one repository. The task relies on all of them, each with what it exposes, and says so in its opening:

| Platform | Role in 280 | What this item takes from it | Per-model fields |
|---|---|---|---|
| Hugging Face Hub | model repository | the full index under the five task tags | creation date, downloads, licence, typed parent relation, datasets, task, account |
| ModelScope | model repository | the full index under the same tasks | creation date, downloads, licence, typed parent relation, datasets, task, organisation |
| Kaggle Models | model repository | the full listing | author, tags, update time, provenance-sources field |
| Ollama library, cloud model gardens (Bedrock), packaged inference microservices (NIM), hosted inference providers (Together AI) | package registry and redistributors | mentioned with their catalogue sizes from 280, and Ollama's pull counts, as the channels through which the repositories' models reach use; no series built on them | none, or pulls only |

Publication counts (volume, derivatives, concentration) and the provenance fields come from the three repositories, the Hub and ModelScope as the two series and Kaggle where it has the field. Use-weighted findings (the widely used sample) come from Hub downloads, the one channel with per-model counts. The registry and the redistributors are named with their sizes as the channels through which the repositories' models reach use. Where a platform lacks a field the table says so rather than dropping the platform.

Developer clarifications (what SCRUM-280 hands over, what data is retrievable, the style-guide rules that apply) are in `developer-notes.md`; they are not part of the task.

## Files

- `scrum286.md`: the deliverable, sections for 3.3, 3.4, 3.5, hand-on list, source log.
- `method-note.md`: the pull, queries, counts against the Hub's totals, definitions, how to re-run.
- `development/pull_index.py` (Hub), `pull_modelscope.py` and `pull_modelscope_partitioned.py` (ModelScope), `pull_kaggle.py` (Kaggle); `analyse_index.py` and `analyse_ecosystem.py`; `make_charts.py`, `make_eco_charts.py`, `build_repository_section.py`: standard library only; `development/tables/2026-10-12/` the derived CSVs; `development/charts/2026-10-12/` the three charts (SVG and PNG). Raw records in `development/data/` are git-ignored (823 MB).
