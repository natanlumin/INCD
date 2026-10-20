# SCRUM-286: developer notes

Clarifications for whoever does the work. Not part of the task or its Jira text; the plan is in `README.md`.

## What SCRUM-280 hands over

- The platform tables and the segmentation (Table 4) with the Hub counts per cell, source TX-01, read from the Hub search page on a stated date. The same page exposes a total per filter in its page data (`numTotalItems`), so every count can be re-run from its URL.
- The source log with its ID scheme and the [CHECKED] / [PARTIAL] marks; this item continues the log (new prefix for the index pulls).
- The glossary words for everything counted: producer, model repository, redistributor, derivative kinds (fine-tune, adapter, merge, quantisation, conversion), guaranteed metadata, declared, provenance.

## Data: what is retrievable, verified 12 October 2026

- The Hub API (`/api/models`) returns, per model: `id`, `author`, `createdAt`, `lastModified`, `downloads` (30-day) and `downloadsAllTime`, `pipeline_tag`, `library`, `gated`, `tags` (including `license:*`, `dataset:*`, `base_model:*` and the typed relations `base_model:finetune:*`, `base_model:quantized:*`, `base_model:adapter:*`, `base_model:merge:*`), and on request the model card's front matter (`cardData`: licence, base model, datasets, language). Paged at up to 1000 records per request with a cursor; no total-count header.
- The Hub search page returns the total for any filter combination (`numTotalItems`), which is how TX-01's counts were read.
- So one enumeration of the index, filtered to the segmentation's model types and dated, gives every chart: volume by creation month and by pipeline tag; derivative and quantised share by the typed base-model relations; account concentration by author; licence families, card completeness, training-data disclosure and provenance metadata from the same records. The "widely used" sample for the provenance fraction is defined on the same data: the top N by 30-day downloads within the segmentation, N stated.
- Not retrievable this way: publication dates before a repository's creation on the Hub (createdAt is the Hub record, not the model's release), and counts from the other platforms except as catalogue sizes already in 280.

## Rules carried from the style guide

Every count carries its method and cut-off date so INCD can re-run it. Forecast items carry the forecast label and a date and sit in their own subsection, apart from observed trend; emerging where a result is extended beyond what was measured. Charts: one message each, caption states what is shown and from which pull. Sources: official (the Hub's own documentation and API) and research only.

## Platforms beyond the Hub, verified 12 October 2026

- ModelScope: `PUT https://www.modelscope.cn/api/v1/dolphin/models` with a JSON body (`PageSize` up to 100, `PageNumber`, optional `Criterion` on `tasks`) returns `Data.Model.TotalCount` and records with `CreatedTime`, `Downloads`, `License` and `LicenseName`, `BaseModel` and `BaseModelRelation`, `Datasets`, `Tasks`, `Organization`, `Path`, `ModelSource`. 268,137 models in all; 48,730 under text-generation, 2,426 under text-classification. No key needed.
- Kaggle Models: `GET https://www.kaggle.com/api/v1/models/list?pageSize=N` with `nextPageToken`; `totalResults` 10,000; records carry `author`, `tags`, `updateTime`, `provenanceSources`, no download count at list level.
- Ollama library: `https://ollama.com/library` lists 245 models with pull counts, tag counts and last update; per-model pages list the quantised tags. No licence, parent or dataset fields.
- The redistributors (gardens, microservices, hosted providers) expose no per-model index; their catalogue sizes are in 280's Tables 1 to 3.
