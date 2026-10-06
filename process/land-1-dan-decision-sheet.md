# The segmentation: what is settled, and what we need from you

Version 3, 2026-10-06. Supersedes version 2. Two questions have closed since, and the remaining ones
are sharper because the axis itself turned out to be flattening several different properties into one
list.

The segmentation agreed here becomes the single one used across Parts I to IV. The threat by
model-type matrix in 4.5 uses its labels verbatim and the coverage matrix in 5.3 inherits the axis
from it, so reopening this means reopening those. Evidence: `../landscape/landscape-platform-comparison.md`
and `../report-sections/land-1-repositories-and-taxonomy.md`.

---

# Part A. Settled, for your confirmation rather than your decision

## A1. The rule separating common from uncommon

**C** where a documented first-class path exists and the format appears in at least one in twenty
repositories of that model type. **P** where a documented path exists below that share, or in only one
runtime family. The threshold is a convention, not a finding; what matters is that it is written down,
because without it "common" is re-decided by every author and the matrices drift apart.

## A2. The format axis is the four serialisation formats

Pickle, safetensors, GGUF, ONNX. Three reasons, and they agree.

The Jira item names those four. The ecosystems document already draws the line in its own words,
between ways of storing parameters, which are portable, and built artefacts, which are not. And
Hugging Face's own format filter mixes fifty-four values that are three different kinds of thing:
serialisation formats, training libraries such as Transformers and Diffusers, and the runtimes that can
read a file, among them vLLM and Ollama. Only the first decides what happens when a file is opened, so
a taxonomy that adopts a platform facet wholesale inherits a category error.

Container images and compiled engines are things an organisation receives, and they are covered as
distribution in 3.1, where their actual security properties belong: opaque to inspection, but signed
and documented in a way no weight file is.

## A3. The old axis was flattening six properties into one list

This is the substantive change, and it came from reading the rows rather than the cells. The seven rows
answered different questions:

| Property | Values | Belongs to |
|---|---|---|
| what goes in | text; image and text; audio and text | the model |
| what comes out | free text; a label; a vector; an image | the model |
| whether it carries a safeguard | base, which has none; instruct, which does | the model, acquired by derivation |
| whether it stands alone | standalone; adapter, a delta against a named parent | the relationship between two artefacts |
| numeric precision | full; quantised | the file |
| serialisation | pickle, safetensors, GGUF, ONNX | the file |

Three consequences follow, and all three are improvements.

**Multimodal was never a peer of classification.** One says what goes in, the other what comes out, so
a multimodal model is also a generative or a classification model. Listing them as alternative rows is
why vision-language models never fitted anywhere cleanly. Hugging Face's own task names confirm the
decomposition: they are input-to-output pairs, such as image-text-to-text and text-to-image.

**Quantised belongs on the file side.** It describes how the numbers are stored, exactly as the format
does, and GGUF is quantised by construction. It moves next to the format and leaves the model axis.

**Instruct is a derivation of base, not a sibling of it.** An instruct model is a base model trained
further to follow instructions, so the pair sits on the derivation dimension rather than the task one.

---

# Part B. What we need from you

## B1. Which of those properties become matrix rows?

This is the question that matters, because every later matrix inherits the answer.

Proposed: **the rows are what comes out, plus the safeguard flag**, giving four:

| Row | |
|---|---|
| generative, instruct | carries an intrinsic safeguard |
| generative, base | carries none |
| classification | |
| embedding | |

and the other three properties are recorded as qualifiers where they change the answer, not as rows:
input modality, numeric precision, and whether the artefact is standalone or an adapter.

Why this split rather than another. The threats in Chapter 4 divide most sharply on what a model
produces and on whether it has a safeguard to attack. They divide far less on what it ingests. And
keeping the matrices two-dimensional keeps the cost of this decision inside this item rather than
pushing it into Chapters 4, 5 and 7.

The alternative is to make derivation a second full axis, which describes reality better and makes
every later matrix three-dimensional. If you want that, it should be decided now and not after S2.

## B2. Is base a row, or a qualifier on one generative row?

It follows from B1 and is worth deciding explicitly, because of what hangs on it.

**The intrinsic safeguard exists only in the instruct variant.** A base model has no refusal behaviour
to measure, so all six tests, and most of the model-integrity threats in 4.3, apply to instruct models
and are meaningless against base ones. Whatever shape the taxonomy takes, it has to be able to express
that, or 4.5 cannot state it.

Proposed: two rows, as in B1, so the distinction is visible in every matrix without a third dimension.

## B3. Where does the adapter go?

An adapter is the one entry that is not a property of a model at all. It is a delta against a named
parent, a few megabytes against the parent's gigabytes, not runnable alone, and meaningful only as a
pair. It can suppress a model's refusal behaviour while the parent file keeps its hash and its
signature. On ModelScope it is 114,361 of 264,794 models, forty-three per cent, so it is not a corner
case.

Three options. Treat it as a fifth row, which is what the current table does and which is wrong in kind.
Treat it as a qualifier, so that every row can be marked as standalone or adapter-modified. Or give it
its own short treatment in the text, on the grounds that the unit of assessment is always the pair and
never the file.

My own view is the second plus the third: a qualifier in the matrices, and a paragraph that says the
pair is the unit.

## B4. If a chapter needs a task vocabulary, whose?

Only two platforms publish a closed one, and they differ. Hugging Face has 63 task names in six
modality groups. ModelScope has 219 across five fields, 130 of them in computer vision, plus a
scientific-computing modality the Hub has no counterpart for. Kaggle, Google, Microsoft and AWS all
document that a task filter exists without publishing its values.

The report's own segmentation needs only the handful above. But any chapter that counts what the
ecosystem contains, or maps threats to tasks, has to pick one or reconcile two. Proposed: the Hub's six
modality headings as the coarse frame, citing ModelScope's where the finer granularity or the different
weighting is the point.

---

## The table this produces, for the freeze

| Model row \ format | pickle checkpoint | safetensors | GGUF | ONNX |
|---|---|---|---|---|
| generative, instruct | C | C | C | P |
| generative, base | C | C | C | P |
| classification | C | C | P | P |
| embedding | C | C | P | C |

Qualifiers recorded per model rather than as rows: input modality; numeric precision, where quantised
reads P, C, C, P across the same four formats; and standalone against adapter-modified, where an
adapter reads C, C, P, P.

## What is needed from the session

Four answers and a confirmation of Part A, recorded in the Jira item, with a version number and date on
the table. Everything downstream is blocked until then.

## One note, not a question

The pickle column is a legacy population. Pickle is still PyTorch's default, but safetensors has been
the default save format in Transformers since v4.35, the Hub's client marks pickle saving deprecated,
and PyTorch has loaded weights-only by default since 2.6. A C there means still in circulation, not
still being produced.
