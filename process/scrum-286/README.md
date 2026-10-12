# SCRUM-286: Quantify the ecosystem (LAND-2)

Subtask texts for Jira, one file each. Status as of 12 October 2026: to do; blocked by LAND-1 (SCRUM-280), which is drafted and awaiting the taxonomy freeze. Blocks ASM-2 and RPT-3. Effort: Natan 1.25d (10h, planned below), Lior 0.25d, Dan 0.25d.

| # | Subtask | Est. |
|---|---|---|
| 1 | Build the model index: retrievable data, method and cut-off date | 3h |
| 2 | Release trends: volume, derivatives, producer concentration | 2h |
| 3 | What is knowable before running: licence, card, training data, provenance | 2.5h |
| 4 | Forward view, 12 to 24 months, with confidence labels | 1.5h |
| 5 | Draft the subsections and hand to the reviewers | 1h |

Skeleton map: 3.3 Release trends and ecosystem growth (subtask 2), 3.4 Licensing and provenance in practice (subtask 3), 3.5 Ecosystem outlook (subtask 4). 3.1 and 3.2 are SCRUM-280's.

## What SCRUM-280 hands over

- The platform tables and the segmentation (Table 4) with the Hub counts per cell, source TX-01, read from the Hub search page on a stated date. The same page exposes a total per filter in its page data (`numTotalItems`), so every count can be re-run from its URL.
- The source log with its ID scheme and the [CHECKED] / [PARTIAL] marks; this item continues the log (new prefix for the index pulls).
- The glossary words for everything counted: producer, model repository, redistributor, derivative kinds (fine-tune, adapter, merge, quantisation, conversion), guaranteed metadata, declared, provenance.

## Data: what is retrievable, verified 12 October 2026

- The Hub API (`/api/models`) returns, per model: `id`, `author`, `createdAt`, `lastModified`, `downloads` (30-day) and `downloadsAllTime`, `pipeline_tag`, `library`, `gated`, `tags` (including `license:*`, `dataset:*`, `base_model:*` and the typed relations `base_model:finetune:*`, `base_model:quantized:*`, `base_model:adapter:*`, `base_model:merge:*`), and on request the model card's front matter (`cardData`: licence, base model, datasets, language). Paged at up to 1000 records per request with a cursor; no total-count header.
- The Hub search page returns the total for any filter combination (`numTotalItems`), which is how TX-01's counts were read.
- So one enumeration of the index, filtered to the segmentation's model types and dated, gives every chart: volume by creation month and by pipeline tag; derivative and quantised share by the typed base-model relations; producer concentration by author; licence families, card completeness, training-data disclosure and provenance metadata from the same records. The "widely used" sample for the provenance fraction is defined on the same data: the top N by 30-day downloads within the segmentation, N stated.
- Not retrievable this way: publication dates before a repository's creation on the Hub (createdAt is the Hub record, not the model's release), and counts from the other platforms except as catalogue sizes already in 280.

## Rules carried from the style guide

Every count carries its method and cut-off date so INCD can re-run it. Forecast items carry the forecast label and a date and sit in their own subsection, apart from observed trend; emerging where a result is extended beyond what was measured. Charts: one message each, caption states what is shown and from which pull. Sources: official (the Hub's own documentation and API) and research only.
