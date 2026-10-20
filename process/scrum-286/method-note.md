# Method note: the model index pulls (subtask 1)

Cut-off date: 12 October 2026 for all three repositories. Hub pull 14:50 to 15:01 UTC; ModelScope and Kaggle Models pulls 16:00 to 18:00 UTC, the same day. This note gives the Hub first, then the two other repositories. Script: `development/pull_index.py`; aggregation: `development/analyse_index.py`; derived tables: `development/tables/2026-10-12/`. The raw records (823 MB, one JSON line per model) are kept locally under `development/data/2026-10-12/` and are not committed; the pull log with the exact request URLs, page counts and timings is `pull.log` in that folder and is reproduced below.

## What was pulled

The model index for the five task tags that the segmentation of SCRUM-280 (Table 4) counts: the generative row (`text-generation`), its modality qualifier (`image-text-to-text`), the classification row (`text-classification`) and the embedding row (`feature-extraction`, `sentence-similarity`). Everything else on the Hub, image generation, speech, vision, and so on, is outside the report's segmentation and was not pulled.

Request, one per task tag, followed through the `Link: rel="next"` cursor until exhausted:

```
GET https://huggingface.co/api/models?pipeline_tag=<tag>&limit=1000
    &expand[]=author&expand[]=createdAt&expand[]=lastModified&expand[]=downloads
    &expand[]=downloadsAllTime&expand[]=likes&expand[]=pipeline_tag&expand[]=library_name
    &expand[]=tags&expand[]=gated&expand[]=private&expand[]=cardData&expand[]=sha
```

Fields kept per model: repository id and the account that holds it (`author`; a producer only when it trained the model), creation date of the Hub record (`createdAt`), last modification, 30-day and all-time downloads, likes, task tag, library, gated flag, the tag list (which carries `license:*`, `dataset:*` and the typed base-model relations `base_model:finetune|quantized|adapter|merge:*`), the model card's front matter (`cardData`: licence, base model, datasets, language) and the current commit hash.

## Record counts, against the Hub's own totals

| Task tag | Records pulled | Pages | Hub search page total, same day | Difference |
|---|---|---|---|---|
| text-generation | 422,885 | 423 | 422,888 | 3 |
| text-classification | 124,152 | 125 | 124,152 | 0 |
| feature-extraction | 21,537 | 22 | 21,535 | 2 |
| sentence-similarity | 20,412 | 21 | 20,412 | 0 |
| image-text-to-text | 42,143 | 43 | 42,141 | 2 |
| **total** | **631,129** | 634 | 631,128 | |

The search-page total is the `numTotalItems` value in the page data of `https://huggingface.co/models?pipeline_tag=<tag>`, read in the same hour. Differences of a few records are models created or removed between the two reads. A model is counted once per task tag; a repository carries one `pipeline_tag`, so the five sets do not overlap.

## How to re-run

```
cd process/scrum-286/development
python3 pull_index.py --date YYYY-MM-DD        # about 11 minutes, 634 requests, 823 MB
python3 analyse_index.py --date YYYY-MM-DD --topn 1000
```

No key or account is needed. Both scripts use only the Python standard library.

## Definitions used by the aggregation

- Publication date: the `createdAt` of the Hub record. It is the date the repository was created on the Hub, not the model's release date; for a model first published elsewhere the two differ.
- Derivative kind: from the typed base-model relation in the tag list, with one kind per model in the order quantised, adapter, merged, fine-tune; a model with no typed relation is "no typed relation", which includes base models and derivatives whose card does not declare a parent. The relation is declared by the uploader in the card's front matter and the Hub types it; it is a declared field, not a verified one.
- Licence family: from the `license:` tag, grouped as permissive (Apache, MIT, BSD, CC-BY, CC0), producer licence (Llama, Gemma, DeepSeek, Qwen), open rail, non-commercial, copyleft, "other" as stated, "unknown" as stated, other named licence; a model with no `license:` tag is "no licence field". The grouping table is in `analyse_index.py`.
- Card completeness: presence of the card's front matter and of its licence, base model, datasets and language fields.
- Widely used: the top 1,000 models across the five tags by 30-day downloads on the cut-off date. The threshold and the full sample are in `widely_used_sample.csv`.

## Limits

- The Hub only. The other platforms of SCRUM-280 contribute catalogue sizes, not per-model records.
- Private repositories are not in the index; gated ones are, and are counted.
- Downloads are the Hub's 30-day counter on the cut-off date, so "widely used" is a snapshot, not a lifetime measure; all-time downloads are kept in the records for a second cut if wanted.

## ModelScope

Interface: `PUT https://www.modelscope.cn/api/v1/dolphin/models` with a JSON body, `PageSize` 100, `PageNumber` n, `SortBy` one of Default, DownloadsCount, StarsCount, GmtModified, and a `Criterion` list; the tasks filter takes the same five task names as the Hub. The response carries `TotalCount`, the records, and facet counts (`FiledAgg`) for licence, library and model type. No key needed. Script: `development/pull_modelscope.py` for a tag under the cap, `development/pull_modelscope_partitioned.py` above it.

Limit and how it was handled: a query stops answering beyond an offset of 10,000 records (`list_models_failed`). Four task tags are under the cap and were pulled whole: text-classification 2,426, feature-extraction 1,273, sentence-similarity 914, image-text-to-text 8,620, each equal to its TotalCount. Text-generation, TotalCount 48,730, was assembled from partitioned queries: the whole tag under each of the four sort orders, then one query per licence value, per model type and per library from the facet counts, with any facet value above the cap split by model type; records united by Id. Coverage is reported in the task as distinct Ids against TotalCount. The records a partition cannot reach are those with no licence, no model type and no library value that also fall outside the top 10,000 of every sort order.

Fields kept: Id, Name, Path (the account), CreatedTime, LastUpdatedTime, Downloads, Stars, License and LicenseName, BaseModel and BaseModelRelation (the typed parent relation: finetune, quantized, adapter, merge), Datasets, Libraries, Frameworks, ModelSource, FromSite, IsCertification, StorageSize, Tags, Language, Tasks, Organization.

Definitions mapped to the Hub's: licence family from LicenseName, else License, through the same grouping table; derivative kind from BaseModelRelation; base-model field present when BaseModel is non-empty; datasets field present when Datasets is non-empty; account = Path; widely used = top 1,000 by Downloads, ModelScope's own counter.

## Kaggle Models

Interface: `GET https://www.kaggle.com/api/v1/models/list?pageSize=100[&sortBy=...][&pageToken=...]`, following `nextPageToken`. No key needed for the public list. Script: `development/pull_kaggle.py`.

Limit and how it was handled: the listing reports `totalResults` 10,000 whatever the order, and the default order stops answering after about 5,800 records (HTTP 500). Three orders were pulled, default, createTime and voteCount, and united by id; the union exceeds 10,000, so that figure is a cap on the listing, not the catalogue's size.

Fields kept: id, ref (account/slug), title, author, tags, provenanceSources, voteCount, updateTime, instances, modelVersionLinks. No task, licence, base-model or download field at list level, so Kaggle enters the tables as a count, an account concentration and the share of models with a provenance-sources value; its date is the last update, not creation, so it is not a series.

## Re-run, all three

```
cd process/scrum-286/development
python3 pull_index.py --date D                       # Hub, about 11 minutes
python3 pull_modelscope.py --date D --tags text-classification,feature-extraction,sentence-similarity,image-text-to-text
python3 pull_modelscope_partitioned.py --date D --tag text-generation --shard 0/3   # and 1/3, 2/3 in parallel; about an hour
python3 pull_kaggle.py --date D; python3 pull_kaggle.py --date D --sort createTime; python3 pull_kaggle.py --date D --sort voteCount
python3 analyse_index.py --date D --topn 1000; python3 analyse_ecosystem.py --date D --topn 1000
python3 make_charts.py --date D; python3 make_eco_charts.py --date D; python3 build_repository_section.py --date D
```
