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

**The governing rule, which decides everything below: a row is content, a column is file manner.** The
test is whether the property can be read off the bytes. You cannot tell from a file whether a model
refuses, or whether it classifies or generates; that is content and it belongs in a row. You can tell
whether it is pickle or safetensors, and whether the numbers are at full or reduced precision; that is
file manner and it belongs in a column. A property that is neither does not belong in the table at all.

Three consequences follow, and all three are improvements.

**Multimodal was never a peer of classification.** One says what goes in, the other what comes out, so
a multimodal model is also a generative or a classification model. Listing them as alternative rows is
why vision-language models never fitted anywhere cleanly. Hugging Face's own task names confirm the
decomposition: they are input-to-output pairs, such as image-text-to-text and text-to-image.

**Quantised belongs on the column side, not as a row.** It describes how the numbers are stored, which
is what the columns already describe, so putting it in a row would cross a file property with a file
property and ask what file manner a file manner has. It becomes a qualifier on the format columns,
where GGUF being quantised by construction shows it always belonged.

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

Input modality stays a qualifier on the row, since it is content but not what the row is keyed on.
Numeric precision becomes a qualifier on the columns, since it is file manner. The adapter is not in
the table at all, for the reason in B3.

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

Under the rule in A3 it cannot be a row, because it is not content: a delta has no behaviour of its own
to describe. Nor is it a column, because its file question is the same as any other safetensors file's.
It is a relation between two artefacts, and the only honest description of it is that the unit of
assessment is the pair.

Proposed: it leaves the table and gets its own treatment in the text, plus a qualifier on each row
saying whether the model as assessed was standalone or adapter-modified. What we need from you is
whether that treatment sits in Chapter 3, as a fact about what circulates, or in Chapter 7, as a rule
about what must be tested together.

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

Rows are content, columns are file manner, and nothing crosses the two. Input modality qualifies a row:
a vision-language model is a generative row whose input is image and text. Numeric precision qualifies
a column: the same four formats carry quantised weights at P, C, C, P respectively, which is a
statement about the columns and not a fifth row. The adapter does not appear, because it is a relation
rather than a model.

## What is needed from the session

Four answers and a confirmation of Part A, recorded in the Jira item, with a version number and date on
the table. Everything downstream is blocked until then.

## One note, not a question

The pickle column is a legacy population. Pickle is still PyTorch's default, but safetensors has been
the default save format in Transformers since v4.35, the Hub's client marks pickle saving deprecated,
and PyTorch has loaded weights-only by default since 2.6. A C there means still in circulation, not
still being produced.
