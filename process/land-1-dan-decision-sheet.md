# Taxonomy freeze: four decisions

For the session with Dan. The segmentation below becomes the single one used across Parts I-IV of the
report: the threat x model-type matrix (4.5) uses its row and column labels verbatim, and the
threat-to-control coverage matrix (5.3) inherits the model-type axis from 4.5.
Once frozen it carries a version and a date, and changing it later means reopening those three matrices.
Evidence for every cell, with sources dated 2026-10-06, is in `landscape-platform-comparison.md` §3.

## The table proposed for the freeze

| Model type \ format | pickle checkpoint | safetensors | GGUF | ONNX | container / image |
|---|---|---|---|---|---|
| generative (instruct / chat) | C | C | C | P | C |
| generative (base) | C | C | C | P | P |
| classification | C | C | P | P | P |
| embedding | C | C | P | C | P |
| multimodal | C | C | C | P | C |
| adapter | C | C | P | P | – |
| quantised (any task) | P | C | C | P | C |

C common, P possible but uncommon, – not applicable. Six cells differ from the working proposal in the
style guide: classification x GGUF and x ONNX, multimodal x GGUF, adapter x GGUF and x ONNX, quantised
x ONNX. Each difference follows from decision 1 below plus a dated source.

## Decision 1. The rule for C, P and –

There is currently no written rule, and six cells turn on it. Proposed:

- **C**: a documented first-class path exists, and for formats distributed through a repository the
  format appears in at least one in twenty repositories of that model type. For the container column,
  which is not a repository artefact: a product line ships that model type as containers.
- **P**: a documented path exists, but the share is below one in twenty, or the path exists in only one
  runtime family.
- **–**: no documented path.

Why it matters: without the rule, "common" is a judgement each author makes again, and the matrices in
Chapters 4, 5 and 7 will drift apart. The one-in-twenty threshold is a proposal, not a finding; any
threshold works provided it is written down.

## Decision 2. Is container / image a format or a packaging layer?

The Jira item names four formats: pickle, safetensors, GGUF, ONNX. The style guide added a fifth
column, container or image. A container holds a model together with its runtime and serving code, so it
is arguably a layer above the format rather than a format.

- **Keep the column**: the cloud gardens and NVIDIA NIM distribute models this way, and Chapter 4 needs
  a row to hang "the serving code ships with the weights" on.
- **Drop the column**: describe containers in 3.1 as a distribution channel instead, and keep the
  taxonomy to the four formats the Jira item names.

Either answer is workable. The one to avoid is keeping the column without deciding what it means,
because that is also decision 4 below.

## Decision 3. May the generative (base) row inherit from the generative (instruct) row?

The Hugging Face Hub has a base-only filter in its interface but exposes no parameter that returns
base-only counts, so the base row cannot be measured the way the others were. Its save paths and
converters are identical to the instruct row.

- **Inherit** (proposed): the base row takes the instruct row's values, with a footnote stating that it
  is inherited and why.
- **Measure**: someone samples the Hub by base-model relation to produce real counts, which is a
  measurement item of roughly a day and would be class S5, our own measurement.

## Decision 4. Does the adapter x container cell read – or P?

It depends on what the container column means.

- If the column means **the artefact is shipped as an image**, the cell is –: no source shows adapters
  distributed as container images.
- If it means **the format is handled inside container deployments**, the cell is P: NVIDIA NIM mounts
  parameter-efficient adapters into a running container, accepting either the safetensors or the pickle
  form, and serves several at once.

The second reading carries a threat-landscape consequence worth surfacing in Chapter 4: a pickle-format
adapter mounted into a vendor container is executable content entering a deployment whose image was
signed and scanned, and the signature covers the image, not the adapter.

## Secondary point, not a decision

The pickle column is a legacy population. Pickle remains the PyTorch default, but the major libraries
now steer away from it: safetensors has been the default save format in Transformers since v4.35, the
Hub client marks pickle saving deprecated, and `torch.load` has defaulted to weights-only loading since
version 2.6. A C in that column therefore means "still in circulation", not "still being produced".
Worth a marker in the frozen table if Dan agrees.

## What is needed from the session

The four answers, recorded in the Jira item, and a version number and date on the table. Everything
downstream of the taxonomy is blocked until then.
