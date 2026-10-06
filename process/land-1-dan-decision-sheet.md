# Taxonomy freeze: five questions for Dan

Version 2, 2026-10-06. Supersedes version 1: question 2 is reshaped and questions 4 and 5 are new,
all three because of evidence gathered since. The old question on the adapter-and-container cell has
gone, because it dissolves under question 2.

The segmentation agreed here becomes the single one used across Parts I to IV. The threat by
model-type matrix in 4.5 uses its row and column labels verbatim, and the threat-to-control coverage
matrix in 5.3 inherits the model-type axis from it. Once frozen it carries a version and a date, and
reopening it means reopening those matrices. Evidence for every cell is in
`../landscape/landscape-platform-comparison.md` §3 and `../report-sections/land-1-repositories-and-taxonomy.md`.

## The table proposed for the freeze

| Model type \ format | pickle checkpoint | safetensors | GGUF | ONNX |
|---|---|---|---|---|
| generative (instruct / chat) | C | C | C | P |
| generative (base) | C | C | C | P |
| classification | C | C | P | P |
| embedding | C | C | P | C |
| multimodal | C | C | C | P |
| adapter | C | C | P | P |
| quantised (any task) | P | C | C | P |

C common, P possible but uncommon. Four columns, not five: see question 2.

---

## 1. What rule separates C from P?

No rule is written down, and six cells turn on it. Without one, "common" is a judgement each author
makes afresh and the matrices in Chapters 4, 5 and 7 drift apart.

Proposed: **C** where a documented first-class path exists and the format appears in at least one in
twenty repositories of that model type; **P** where a documented path exists below that share, or in
only one runtime family; **–** where no documented path exists. The one-in-twenty threshold is a
proposal, not a finding. Any threshold works provided it is written down.

## 2. Is the format axis serialisation formats only?

Version 1 asked whether the container column was a format or a packaging layer. The evidence has made
that the wrong shape of question, and the answer now looks clear.

Three facts. The Jira item itself names four formats: pickle, safetensors, GGUF, ONNX. The ecosystems
document already draws the line in its own words, that the first four are ways of storing parameters
and are portable while the rest are built artefacts and are not. And Hugging Face's own format filter
mixes three different kinds of thing under one name: serialisation formats, training libraries such as
Transformers and Diffusers, and the runtimes that can consume a file, among them vLLM and Ollama. Only
the first kind carries load-time execution risk, so a taxonomy that adopts a platform facet wholesale
inherits a category error.

**Proposed: the axis is the four serialisation formats.** Container images and compiled engines are
things an organisation receives, and they are covered in 3.1 as distribution, where their security
properties, signing and opacity, actually belong. This also disposes of the old question about the
adapter-and-container cell, which exists only if the column does.

## 3. May the generative base row inherit from the generative instruct row?

The Hub has a base-only filter in its interface but exposes no parameter that returns base-only
counts, so that row cannot be measured the way the others were. Its save paths and converters are
identical to the instruct row.

Proposed: inherit, with a footnote saying so and why. The alternative is a measurement item of about
a day, sampling the Hub by declared parent relation, which would be our own measurement rather than
platform documentation.

## 4. Should derivation kind be its own axis?

This is new, and the numbers are the reason. ModelScope's own catalogue aggregation reports 114,361
adapters out of 264,794 models, **43 per cent**, making them the third-largest population on that
platform and larger than every format except the two dominant ones. On Hugging Face, roughly three
quarters of 3.13 million repositories carry no task tag at all, and that untagged remainder is largely
adapters, quantisations and other derivatives.

The current proposal keeps adapter and quantised as rows on the model-type axis alongside task kinds
such as classification and embedding, with a note that two are derivation kinds and four are task
kinds. That was defensible when derivatives looked like a minority. It is harder to defend now: a
quantised multimodal adapter has to be counted once, in whichever row the chapter happens to be about,
and the report loses the ability to say anything about derivation and task together.

Two options. **Keep one axis**, accepting that derivation and task are mixed and that each artefact is
counted once. Or **split into two axes**, task on one and derivation kind on the other, which describes
reality better and makes every later matrix three-dimensional. The second is more honest and more
expensive. My own view is to keep one axis for the freeze and record the limitation explicitly, because
the cost of a three-dimensional matrix lands on Chapters 4, 5 and 7, not here.

## 5. If the report needs a task vocabulary, whose?

Also new. Only two platforms publish a closed, machine-readable task vocabulary, and they disagree in
size and in emphasis. Hugging Face publishes 63 task names in six modality groups. ModelScope publishes
219 task strings in five fields, with 130 of them in computer vision, and a scientific-computing
modality the Hub has no counterpart for. Kaggle, Google, Microsoft and AWS all document that a task
filter exists without publishing what is inside it.

The report's own segmentation needs only a handful of task kinds, the six the Jira names. But any
chapter that counts what the ecosystem contains, or that maps threats to tasks, has to pick a
vocabulary or reconcile two. Proposed: use the Hub's six modality headings as the coarse frame, since
they are the smaller and better-known set, and cite ModelScope's where its finer granularity or its
different weighting is the point.

---

## What is needed from the session

Five answers recorded in the Jira item, and a version number and date on the table. Everything
downstream of the taxonomy is blocked until then.

## One thing that is not a question

The pickle column is a legacy population. Pickle remains PyTorch's default, but safetensors has been
the default save format in Transformers since v4.35, the Hub's own client marks pickle saving
deprecated, and loading has defaulted to weights-only since PyTorch 2.6. A C in that column means
"still in circulation", not "still being produced". Worth a marker in the frozen table if you agree.
