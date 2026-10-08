# Map repositories, hosting platforms and the model taxonomy: subtasks

Status as of 7 October 2026. Research cut-off 6 October 2026.

Precondition: the glossary exists. The terms used below (file format, model type, modality, adapter,
quantised copy) are defined once in the report's glossary and are used here as labels, not explained.
Any term the tables need and the glossary lacks is added to the glossary, not defined in the tables.

| # | Subtask | What it delivers | Status | Est. |
|---|---|---|---|---|
| 1 | **Taxonomy table** | A table with model types as rows (quantised, classification, generative, embedding, multimodal, adapters) and artefact formats as columns (pickle, safetensors, GGUF, ONNX). Each cell holds one of three values: common, possible but uncommon, not applicable. Delivered with the written rule that decides the value, the dated evidence behind every cell, and the glossary entries for any row or column label the glossary lacks. | Draft done | 0.5d (spent) |
| 2 | **Agree the taxonomy with Dan and freeze it** | One session. The table leaves it with a version number and a date, as the single segmentation used across Parts I-IV. Must close before S2. | To do | 2h |
| 3 | **Platform comparison table** | A table with one row per platform: Hugging Face, Kaggle, ModelScope, Ollama/GGUF, GitHub releases, cloud model gardens (the gardens broken out into Google, AWS, Microsoft, NVIDIA). Four columns, the ones the item names: governance (who may publish, how takedown works); platform-side controls (scanning, conversion, signing, gating); guaranteed metadata (enforced fields, hashes, history); distribution mechanism (how the file reaches the organisation). A fifth column, what the platform carries, stated in the taxonomy's labels only: which model types and formats its catalogue holds, with the platform's own counts where published, and a one-off mapping of each platform's own task and format names onto the taxonomy's labels. Plus a source column. Every cell is a factual statement with a dated source of a declared class; a property no platform documents reads "not established". | Four columns done; the carries column and the mapping to add from existing evidence | 1d (spent) + 2h |
| 4 | **Draft the subsection and hand the results on** | The subsection in the order above: the frozen taxonomy table, then the platforms and what their controls do and do not establish, with the comparison table. Every claim sourced. Then the frozen row and column labels go to LAND-2, THR-2 and THR-3, and the dated sources into the report's single bibliography. | Platform half drafted; the rest after subtask 2 | 4h |

Subtask 2 is the only dependency; 4 follows it. Subtask 3 can be completed now.
