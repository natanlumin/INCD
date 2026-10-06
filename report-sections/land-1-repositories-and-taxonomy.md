# Where open models live and move, and what they are

**LAND-1 deliverable.** Covers the two halves of the Jira item: where open-source models actually live
and move, with each platform's governance, platform-side controls, guaranteed metadata and
distribution mechanism; and the working segmentation of model types against artefact formats.

Research cut-off and access date 2026-10-06. Source identifiers resolve in the log at the end and in
`../landscape/landscape-platform-comparison.md`. Draft 1.

---

## 1. What each platform carries

Governance, platform-side controls, guaranteed metadata and distribution mechanism are tabulated in
`../landscape/landscape-platform-comparison.md` and are not repeated here. This section answers the
question that table does not: what is actually inside each platform, and in whose vocabulary.

### 1.1 Hugging Face Hub

The only platform here that publishes a closed, machine-readable vocabulary for all three dimensions,
and by a wide margin the largest: **3,127,450 model repositories** as at 2026-10-06 [LD-08].

**Tasks and modalities.** Sixty-three task names, which the Hub calls pipeline tags, grouped into six
published modality headings: multimodal (9 tasks), natural language processing (12), computer vision
(19), audio (4), tabular (2) and reinforcement learning (1) [LD-01]. The task is declared per
repository in the model card, drives the filters, and selects which inference widget and API the Hub
uses [LD-02]. Counts for the tasks this report cares about, as at 2026-10-06 [LD-08]:

| Task | Repositories |
|---|---|
| text generation | 420,432 |
| text classification | 123,517 |
| text to image | 111,121 |
| image-text to text | 41,388 |
| automatic speech recognition | 37,185 |
| feature extraction | 21,283 |
| object detection | 6,931 |

Two readings matter. Text generation, the class the six tests address, is about one repository in
seven. And those seven tasks together account for roughly 762,000 of 3.13 million repositories, so
**about three quarters of the Hub carries no pipeline tag at all** [LD-08]. The untagged remainder is
largely adapters, quantisations and other derivatives, which means any statement about what the
ecosystem contains, built on task counts alone, undercounts derivative artefacts severely.

**Formats.** The Hub's own libraries facet enumerates fifty-four values [LD-04], and a parallel
documented table lists the integrated libraries with what each supports [LD-05]. The format is
declared per repository, and where it is absent the Hub infers it from the files present, for example
recognising a NeMo or Core ML model by extension [LD-03].

That facet is the single most important thing in this section, and not for the reason it looks like.
**It mixes three different kinds of thing under one name.** Serialisation formats are there, such as
safetensors, GGUF, ONNX, Core ML, LiteRT and DDUF. So are training libraries, such as Transformers,
Diffusers and timm. So, in a second facet of seventeen values, are the local runners and applications
that can consume the artefact, among them llama.cpp, vLLM, SGLang, Ollama, LM Studio and Docker Model
Runner [LD-06]. Only the first kind carries load-time execution risk. A security taxonomy that adopts
the Hub's facet wholesale inherits a category error, which is the argument for section 4 keeping its
format axis to serialisation formats alone.

The Hub also publishes twelve parameter-size bands, from under one billion to over five hundred
billion [LD-07], which is the closest thing in the ecosystem to a published scale axis.

### 1.2 Kaggle Models

**Formats.** Kaggle treats framework structurally rather than as a tag: it is a mandatory segment of
every model's address, so one logical model fans out into one artefact per framework [LD-10]. The
documented enumeration is nonetheless open-ended, published as a list of examples ending in an
ellipsis rather than a closed set [LD-09]. Values observed in the catalogue go beyond the seven
documented ones, GGUF among them [LD-12].

**Tasks and modalities.** The index offers nine filter groups, including a task facet and a data-type
facet, which is Kaggle's modality axis [LD-11]. The values inside them are loaded on expansion and
appear in no published document. The documentation treats task as free-text guidance for naming a
variation rather than a controlled vocabulary [LD-12]. So Kaggle has the axes without publishing the
vocabulary, and a report cannot key a matrix off it.

**A composition point.** Part of the Kaggle catalogue is not Kaggle's. Entries appear under a Hugging
Face surface and resolve to links out rather than to files Kaggle holds [LD-13]. An organisation that
believes it is sourcing from Kaggle may be sourcing from the Hub.

### 1.3 ModelScope

**Modalities.** Six top-level groups, from the platform's own tag service: text, image, audio, video,
multimodal and scientific computing [LD-15]. The last of these has no counterpart among the Hub's six
headings, and the catalogue backs it with a science facet covering life sciences, earth science,
physics and the social sciences [LD-18].

**Tasks.** Two hundred and nineteen task strings across five fields, published in ModelScope's own
open-source toolkit: 130 in computer vision, 47 in natural language processing, 21 in audio, 20
multimodal and one in science [LD-16]. This is more than three times the granularity of the Hub's
taxonomy, and it is weighted differently, with heavy coverage of document and character recognition,
face and person analysis, and Chinese-language processing. It is also the taxonomy of record only
because the website's own task filter does not publish its values [LD-17].

**Formats.** Sixty-nine library values across a catalogue of 264,794 models, with counts [LD-18]. The
top of the distribution tells the story:

| Value | Models |
|---|---|
| PyTorch | 230,091 |
| safetensors | 194,143 |
| LoRA | 114,361 |
| GGUF | 20,918 |
| MLX | 9,823 |
| ONNX | 7,353 |

**Adapters are 43 per cent of that catalogue.** They are not an edge case in the ecosystem; on this
platform they are the third-largest population and larger than every format except the two dominant
ones. Any matrix that treats an adapter as a minor row misdescribes what is actually in circulation.

### 1.4 Ollama library

**Formats.** Two accepted inputs, documented: a directory of safetensors weights, or a GGUF file,
single or sharded. Ollama states it does not quantise GGUF models on import, so the compression is
done before the file arrives [LD-14]. What the library then distributes is Ollama's own layered
packaging, so neither input format survives to the consumer as such.

**What it can run, in place of a task taxonomy.** The documentation enumerates eight capabilities:
streaming, thinking, structured outputs, decision, vision, embeddings, tool calling and web search
[LD-19]. Vision models taking images alongside text are served [LD-20], and dedicated embedding models
are distributed with their own API endpoint [LD-21]. The library labels every entry with capability
chips, and across the index those labels occur as tools 94 times, thinking 44, vision 41, cloud 16,
embedding 12, decision 4 and audio once [LD-22].

That is the answer to what Ollama carries, and it is a different shape of answer from the Hub's. It
is a few hundred curated entries described by what the runtime can do with them, not a taxonomy of
what the models are.

### 1.5 GitHub releases

No taxonomy of any kind: not formats, not modalities, not tasks. The only constraints that shape the
artefact are mechanical, up to a thousand assets per release and under two gibibytes per file, with no
limit on total size or bandwidth [LD-23]. That per-file ceiling is why large models arrive here as
multi-part shards.

This is the uncontrolled channel, and it is uncontrolled in a specific sense: not that it is permissive
about content, but that it holds no description of what a file is. Everything a reader could key a
matrix off has to come from outside the platform.

### 1.6 Cloud model gardens

The gardens enumerate deployment and commerce, not artefacts. None of the four publishes an artefact
format vocabulary, because in a garden the weights are not the unit of distribution.

**Amazon Bedrock** publishes the cleanest modality enumeration of any platform here, and it is also the
narrowest: text, image and embedding [LD-24]. The catalogue itself is wider than its own filter,
carrying video, speech, reranking and more across eighteen provider rows [LD-25]. The page that used to
hold the modality table now redirects to a provider-organised catalogue [LD-25].

**Microsoft Foundry** states a catalogue of over ten thousand models growing by about fifty a month,
split commercially into models sold by Azure and models from partners and community, with eight filter
axes including an explicit inference-task axis whose values are given only as examples [LD-26]. Its
catalogue includes a Hugging Face collection served on managed compute [LD-27].

**Google's Model Garden** documents three catalogue categories, foundation models, fine-tunable models
and task-specific solutions, and a four-axis filter pane covering tasks, collections, providers and
features. The values inside tasks and features are not published [LD-28].

**NVIDIA NIM** is the outlier and publishes the richest category list, seventeen families spanning
large language and vision-language models, embedding and reranking, optical character recognition and
object detection, speech recognition, translation and synthesis, safety guardrails, digital humans,
medical imaging, protein and molecular biology, weather and physics simulation [LD-29]. It is also the
one whose unit of distribution is explicitly a container rather than a weight file [LD-30].

### 1.7 What the comparison shows

**Only two platforms publish a closed task vocabulary**, the Hugging Face Hub with 63 and ModelScope
with 219. Kaggle, Google, Microsoft and AWS all document that a task filter exists without publishing
what is in it. A report that needs a stable task axis has two sources and must pick one or reconcile
them.

**The supply chains are nested, and a finding propagates.** Kaggle surfaces Hugging Face repositories
as links [LD-13], Microsoft Foundry hosts a Hugging Face collection [LD-27], and Google's Model Garden
relies on Hugging Face's own scanners for the Hugging Face models it serves, blocking what they call
unsafe and merely flagging what they call suspicious [LD-28]. A weakness in one platform's hygiene is
therefore not contained to that platform.

**Derivatives dominate and are invisible in task counts.** Adapters are 43 per cent of ModelScope's
catalogue [LD-18], and roughly three quarters of Hugging Face repositories carry no task tag at all
[LD-08]. The ecosystem is mostly derivative artefacts, and the published taxonomies describe the
minority.

## 2. Artefact formats

This section reworks the treatment in the ecosystems document. It keeps that document's definitions and
adds three things the report needs and that document does not carry: what loading each format can do,
how many files an artefact actually is, and which formats the platform controls of section 2 can
actually read.

### 2.1 The word "format" is being used for three different things

Before any list, a distinction that the platforms themselves do not draw. Hugging Face's format filter
enumerates fifty-four values in a single list [LD-04], and they are not the same kind of thing:

- **Serialisation formats**, how the numbers are written to disk: safetensors, GGUF, ONNX, Core ML,
  LiteRT, DDUF, and PyTorch's pickle.
- **Training and modelling libraries**, which imply a format without being one: Transformers,
  Diffusers, timm, PEFT, sentence-transformers.
- **Consumption runtimes**, which are not properties of the file at all but of what can read it. These
  appear in a second facet of seventeen values, among them llama.cpp, vLLM, SGLang, Ollama, LM Studio
  and Docker Model Runner [LD-06].

Kaggle collapses the same three into one mandatory path segment it calls the framework [LD-10].

Only the first kind determines what happens when a file is opened. The rest describe provenance or
compatibility. This report therefore uses **format** for the first kind only, and the segmentation in
section 4 keys off that. Where a later chapter needs to say what can read a file, it says runtime.

### 2.2 The four storage formats

A model file arrives in one of four formats, and the format matters independently of the model inside
it. Each entry below states what loading it can do, because that, not the layout of the bytes, is why
the report cares.

**Pickle checkpoints** (`.bin`, `.pt`, `.pth`, `.ckpt`) are serialised with Python's pickle module. The
extension is a convention and not a guarantee in either direction: `pytorch_model.bin` and
`adapter_model.bin` are pickle, while other toolchains write `.bin` files that are raw tensor data and
contain no pickle at all. What makes a file pickle is its content, which is why the Hub's scanner
extracts the import list from anything pickled rather than trusting the name, and why a control keyed
on the extension would both miss and over-flag.

Loading a pickle file can execute arbitrary code embedded in it; Python's own documentation says the module
is not secure and that data from an untrusted source should never be unpickled [LD-31]. It remains
PyTorch's default serialisation, which is why it is still everywhere: 230,091 models on ModelScope
carry it [LD-18], and it is present in about one text-generation repository in seven on the Hub [LD-32].
The direction of travel is away from it. Safetensors has been the default save format in Transformers
since version 4.35, the Hub's own client marks pickle saving deprecated, and PyTorch has loaded
weights-only by default since version 2.6 [LD-33]. A C in this format's row means still in circulation,
not still being produced.

**safetensors** stores tensors and nothing else, so loading it cannot run code [LD-34]. It is the
default for new uploads and the format repositories convert to. It is now the majority format
wherever it is counted: 194,143 models on ModelScope [LD-18] and about four fifths of text-generation
repositories on the Hub [LD-32]. The guarantee is precise and narrow, and worth stating because it is
routinely overstated: the container cannot execute. It says nothing whatever about the behaviour of
the model inside it.

**GGUF** is a format for quantised models that carries its metadata inside the file, used by the
llama.cpp family and by Ollama [LD-35]. Quantisation is not an option here but the normal state, since
the quantisation scheme is expressed in the tensor types themselves. Two things the ecosystems
treatment does not say. It is **not always one file**: a multimodal GGUF is the model plus a separate
projector file, so an artefact that is scanned or hashed as a unit may be half the model [LD-36]. And
it is a conversion endpoint rather than a format models are trained in, so a GGUF file is always a
derivative of something, usually several steps removed.

**ONNX** is a graph-based interchange format for running a model outside the framework it was trained
in, common for classification and embedding models in production pipelines [LD-37]. It carries the
load-time risk that is least discussed. A graph can reference an operator from a custom domain, and the
implementation of that operator is an arbitrary native library that the runtime loads into the
inference process [LD-38]. The format cannot execute code by itself; it can name code that will be
executed. No repository control described in section 2 inspects that reference.

### 2.3 Two things an organisation receives that are not storage formats

**Container images** bundle a model with its runtime and its serving software into one deployable unit.
What is received is not just the model but the stack around it, and a vulnerability in the stack
arrives with it. They are listed here because an organisation can receive one in place of a weight
file, and because their security properties run opposite to the storage formats: opaque to inspection,
but signed, scanned and shipped with a software bill of materials in the one catalogue that documents
it [LD-39].

**Compiled engines** are the output of building a checkpoint for a particular target. By default a
TensorRT engine runs only on the device type, the library version and the host platform it was built
for, each relaxable only at a stated cost in performance [LD-40]. They are genuinely distributed, not
merely built locally: NVIDIA's inference microservices download pre-compiled engines for their
optimised profiles, falling back to local compilation only for generic ones [LD-41]. No vendor
documents whether the original parameters can be recovered from one, and none claims they are
protected; what is established is that the tools which inspect weight files cannot read it [LD-42].

Both are built artefacts and neither is portable: a container pins the software around the model, an
engine pins the hardware under it. Neither is a way of storing parameters, which is why section 3 keeps
them off the format axis and treats them in 3.1 of the report as a question of distribution.

### 2.4 What the format decides about assessment

Three consequences, and they are the reason this section exists at all.

**The platform controls are pickle-shaped.** The scanning described in section 1 was built for the
format that executes on load. It reads pickle imports, and it runs an antivirus engine over files.
Nothing in it inspects an ONNX graph for custom-operator references, and nothing reads a compiled
engine at all. So the value of a platform's controls depends on which format the organisation receives,
and the platform that scans most thoroughly scans the format that is on its way out.

**A safe format is a statement about the container, not the contents.** A safetensors file can hold a
model whose behaviour has been altered in any way its publisher chose. This is the boundary the six
tests exist to cross, and it is why no amount of format hygiene substitutes for behavioural testing.

**The format decides what can be tested at all.** The tests in Chapter 7 that need weights or internal
activations need a file that exposes them. A storage format does. A compiled engine, on present
evidence, does not. An organisation that receives a model only as an engine has not merely lost a
scanning opportunity; it has lost the ability to run a whole class of assessment, and the acceptance
criteria have to say what happens then.

## 3. The segmentation

The Jira item asks for one segmentation, used consistently across Parts I to IV, that every later
matrix keys off. This section gives it, built in three parts that each answer one question: what kind
of file is this, what does the model produce, and how are the numbers written down. A fourth property,
modality, qualifies the second rather than competing with it.

They are kept apart deliberately. The version this replaces answered all three at once and produced
rows that could not be compared with one another.

### 3.1 Three kinds of model file

What an organisation receives is a file. Three kinds circulate, and they differ in what they contain
rather than in what the model does.

**A model.** A complete set of weights, sufficient on its own to produce output once loaded by an
inference server. This is the ordinary case and the one every control in section 1 is designed around.

**An adapter.** A fragment: a collection of layers and weights that is not the whole model. It is
produced by training, like a model, but only a small part is trained, which is why the file is
megabytes where its parent is gigabytes. It is not runnable alone and is meaningful only against the
parent it was computed from.

**A quantised copy.** A complete set of weights at reduced numeric precision, produced by converting an
existing model rather than by training one. Behaviour is close to the parent's and not identical.
Quantisation-aware training, where the reduced precision is present during training, yields the same
kind of artefact and does not change the classification.

**Alongside these, a container**, which packages any of the three together with the software that runs
it. It belongs in the list because it is received in place of a weight file, and it is distinguished
from the other three by containing something that is not the model at all.

Two of these properties are readable from the file itself. Whether a set of weights is complete or a
fragment is visible from the tensors present and the adapter configuration beside them; whether the
numbers are at full or reduced precision is visible from their data types. That matters in 3.9.

### 3.2 Models by what they produce

The useful way to classify a model is by its output, because the output is what an attacker
manipulates and what a test measures. Three classes.

**Prediction.** The model maps an input to a value from a fixed space: a label, in classification, or a
number, in regression. The output space is defined in advance and the model cannot leave it.

**Embedding.** The model maps an input to a vector used for search, retrieval, clustering or
similarity. The vector is the product, not an intermediate.

One clarification belongs here, because the confusion is common. *Every* model that processes text
embeds it internally: text becomes vectors before any computation happens, in a classifier and in a
generative model alike. That internal step does not make a model an embedding model. An embedding model
is one whose output is the representation and nothing else.

**Generation.** The model produces free text, token by token, from a prompt. The output space is
unbounded, which is what makes this class different in kind from prediction, and why most of the threat
landscape concentrates here.

There is no fourth row for instruction-tuned models, and 3.7 explains why.

### 3.3 Modality qualifies the output class; it is not an alternative to it

Modality is a statement about what goes in and what comes out: text, image, audio, video, or a
combination. Multimodal means more than one modality is involved on at least one side.

It is not a kind of model. A vision-language model is a generative model whose input includes images. A
zero-shot image classifier is a prediction model whose input includes both an image and candidate
labels. The platforms' own task names make the decomposition explicit by reading as input-to-output
pairs: image-text-to-text, text-to-image, audio-text-to-text [LD-01].

Treating multimodal as a row beside classification was a category error, and it is why vision-language
models never sat comfortably anywhere. Modality therefore qualifies a row rather than forming one.

### 3.4 Formats

The four serialisation formats of section 2 apply across every row: pickle, safetensors, GGUF and ONNX.
They describe how the numbers are written to disk and say nothing about what the model does.

### 3.5 The segmentation, and the rule that keeps it coherent

**A row is content. A column is file manner. Nothing crosses the two.** The test is whether the
property can be read from the bytes. You cannot tell from a file whether a model predicts or generates,
so that is a row. You can tell whether it is pickle or safetensors, and whether its numbers are reduced,
so those are columns.

| Output class | pickle | safetensors | GGUF | ONNX |
|---|---|---|---|---|
| prediction (classification, regression) | C | C | P | P |
| embedding | C | C | P | C |
| generation | C | C | C | P |

C common, P possible but uncommon, under the rule in the decision sheet. Evidence per cell in
`../landscape/landscape-platform-comparison.md` §3.

Qualifiers, recorded where they change the answer rather than as rows or columns of their own:

- **Modality**, on the row: a generative row whose input is image and text.
- **Precision**, on the columns: the same four formats carry quantised weights at P, C, C, P
  respectively, which is a statement about the columns and not a fourth row.
- **Completeness**, on the file: whether the artefact assessed was a whole model or a model with an
  adapter loaded.

### 3.6 What an adapter does to this

An adapter is a file, classified in 3.1. But combining one with a parent produces an effective model
whose output class may differ from the parent's. A low-rank adapter trained on a generative model to
classify transactions yields a prediction model: the parent sits in one row, the product in another.

Three consequences, none of them bookkeeping.

**The row assessed need not be the row running.** An organisation assesses a generative model, an
adapter is loaded, and what serves requests is a prediction model, or a generative model whose
safeguard has been suppressed. The parent file is unchanged throughout, with the same hash and the same
signature.

**The applicable tests change with the row.** If the product is a prediction model, safeguard tests have
nothing to measure. If it is still generative but stripped, they apply and would fail.

**The pair is the only assessable unit**, since the adapter alone has no behaviour and the parent alone
is not what runs. Every recorded assessment therefore names the pair it was performed on, not the
parent.

### 3.7 Why the safeguard is not a row

The obvious fourth row would be the instruction-tuned generative model, distinguished from the plain
generative one by carrying a refusal safeguard. It is deliberately absent, for two reasons.

**It is not readable.** You cannot tell from a complete set of weights whether it was instruction-tuned.
It is a publisher's claim, and section 1 established that no repository verifies such claims.

**It is what the assessment measures.** Putting safeguard state on the axis would mean taking the
publisher's word for precisely the thing the tests in Chapter 7 exist to determine. A taxonomy should
not pre-classify its own measurement.

So safeguard state is recorded as a result, not a row, and it has three values.

**Present.** The model refuses as its publisher describes. The question for Chapter 7 is how firmly,
which is what the tests report.

**Absent by design.** A base model, published without instruction tuning, has no refusal behaviour
because none was ever trained in. This is not a finding. It is the specification, and the publisher
claimed nothing else. Such models exist at the largest scales: Mistral publishes a 675-billion-parameter
base described on its own card as "the base pre-trained version, not fine-tuned for instruction or
reasoning tasks" [SG-02]; NVIDIA publishes a 550-billion base [SG-03]; DeepSeek, Moonshot and Z.AI
publish bases at 1.6 trillion, 1 trillion and 110 billion respectively [SG-04, SG-05, SG-06].

**Absent by removal.** An instruction-tuned model whose refusal behaviour was deliberately stripped and
republished. This is the finding, because the artefact claims one state and exhibits another: the
lineage, the name and the model card all say instruction-tuned, and the behaviour does not.

### 3.8 The evidence that removal is routine, and at every scale

This subsection exists because the scale of the stripped population is the single strongest piece of
evidence for why the report's acceptance criteria cannot rest on a publisher's claim.

At 100 billion parameters and above, as at 2026-10-06 [SG-01]:

| Hub query | Repositories listed |
|---|---|
| matching "abliterated" | 365 |
| matching "uncensored" | 262 |

Counts are repositories rather than distinct models, since community quantisations of the same strip
dominate. The figure to take from them is that this is a routine practice at flagship scale, not a
marginal one.

**The largest is a 2.8-trillion-parameter strip**, whose own card states that "more than 98% of the
safeguards have been removed", with removal percentages given per attention projection, expert layer
and embedding token [SG-07]. Strips exist throughout the range below it, at 763, 756, 753 and 561
billion [SG-08].

Three cases are worth naming, because each defeats a different assumption.

**Withholding the base does not withhold the capability.** DeepSeek publishes no base variant for V4.1
at 763 billion [SG-09]. Four independent stripped republications of it exist at 753 to 763 billion
[SG-08]. A lab that declines to release the safeguard-free version does not thereby prevent one
existing.

**A vendor safety process does not survive republication.** NVIDIA's 550-billion release has an
abliterated derivative at full 561-billion weight [SG-10].

**Nor does a delayed release.** Z.AI held back the weights of its 753-billion model for a two-week
safety evaluation with vetted partners, on the grounds that its skill at finding and exploiting
software vulnerabilities warranted testing first [SG-11]. Stripped versions of it are published [SG-08].

The conclusion the report should draw is narrow and well supported: **an intrinsic safeguard is not a
property the file carries, but a property someone can remove from the file**, at any scale reached so
far, including scales where the publisher deliberately tried to control release. That is why the
segmentation above records safeguard state as a measurement and not as a declaration, and why Chapter 7
cannot accept a model card as evidence of it.

### 3.9 Readable against claimed

One split runs through all of the above, and Chapter 6 divides on exactly this line.

**Readable from the file**: the serialisation format; whether the weights are complete or a fragment;
the numeric precision. Any holder of the artefact can verify these.

**Claimed, and not readable**: which model this derives from; whether a complete set of weights is a
base or an instruction-tuned model; what it was trained on; whether a safeguard is present. None can be
determined from the bytes, and no repository verifies any of them.

A practical warning follows from the same evidence. Card metadata is not a reliable discriminator even
where it appears to be: Qwen's base repositories carry the same training-stage field as its
instruction-tuned ones, so an automated census built on that field will misclassify [SG-12].

The segmentation is therefore partly verifiable and partly taken on trust, and the line falls where a
reader would not expect. The column side is verifiable. The row side, which decides which threats and
which tests apply, rests on a publisher's declaration until something is measured.

## 4. Source log

Every claim in this document resolves to a row below. Class per the citation policy: S1 standards and
specifications, S4 vendor and platform documentation. Access date 2026-10-06 throughout, which is also
the research cut-off. Tags: [CHECKED] the page states the claim; [PARTIAL] implied but not stated, with
the gap named; [NOT ESTABLISHED] no page states it after the searches named.

Method note. Several platform pages are JavaScript applications that return only a shell to a plain
fetch; those were rendered through a headless-render proxy at the same address, and where a list was
collapsed in the rendering it was read from the page's own embedded data. Where huggingface.co
rate-limited, the same documentation files were read from their public source repository. Counts drawn
from live catalogue pages are quoted as at the access date and will drift.

### Platform coverage (LD-01 to LD-30)

| ID | Class | Source | URL | Tag | Verified |
|---|---|---|---|---|---|
| LD-01 | S4 | Tasks, Hugging Face | https://huggingface.co/tasks | [CHECKED] | 63 task names in six modality groups: multimodal 9, natural language processing 12, computer vision 19, audio 4, tabular 2, reinforcement learning 1; names read as input-to-output pairs |
| LD-02 | S4 | Model Cards, Hugging Face Hub docs | https://huggingface.co/docs/hub/model-cards | [CHECKED] | the task is declared per repository as `pipeline_tag`, drives filtering, and selects the widget and API |
| LD-03 | S4 | Model Cards, Hugging Face Hub docs | https://huggingface.co/docs/hub/model-cards | [CHECKED] | format declared as `library_name`; where absent the Hub infers it from files present |
| LD-04 | S4 | Models index, libraries facet | https://huggingface.co/models | [CHECKED] | 54 values mixing serialisation formats, training libraries and other tooling; read from the page's own data because the rendering collapses the list |
| LD-05 | S4 | Libraries, Hugging Face Hub docs | https://huggingface.co/docs/hub/models-libraries | [CHECKED] | parallel documented table of integrated libraries |
| LD-06 | S4 | Models index, apps facet | https://huggingface.co/models | [CHECKED] | 17 downstream runners and applications including llama.cpp, vLLM, SGLang, Ollama, LM Studio, Docker Model Runner |
| LD-07 | S4 | Models index, parameter facet | https://huggingface.co/models | [CHECKED] | 12 published parameter bands from under 1B to over 500B |
| LD-08 | S4 | Models index, filtered counts | https://huggingface.co/models?pipeline_tag=… | [CHECKED] | total 3,127,450; text generation 420,432; text classification 123,517; text to image 111,121; image-text to text 41,388; speech recognition 37,185; feature extraction 21,283; object detection 6,931. Live counters, quoted as at the access date |
| LD-09 | S4 | Kaggle CLI model metadata | https://raw.githubusercontent.com/Kaggle/kaggle-cli/main/docs/models_metadata.md | [PARTIAL] | the framework field is enumerated only as examples ending in an ellipsis; no closed list is published |
| LD-10 | S4 | Models Documentation, Kaggle | https://www.kaggle.com/docs/models | [CHECKED] | framework is a mandatory path segment of every handle, so one model fans out into one artefact per framework |
| LD-11 | S4 | Find Pre-trained Models, Kaggle | https://www.kaggle.com/models | [PARTIAL] | nine filter groups including a task facet and a data-type facet; the values inside are not published |
| LD-12 | S4 | Models Documentation, Kaggle | https://www.kaggle.com/docs/models | [CHECKED] | task treated as free-text guidance for naming a variation, not a controlled vocabulary; GGUF observed as a framework value in the catalogue |
| LD-13 | S4 | Kaggle models index and Hugging Face integration blog | https://www.kaggle.com/models ; https://www.kaggle.com/blog/kaggle-hugging-face-integration | [CHECKED] | a distinct Hugging Face surface whose entries are links out rather than Kaggle-held files |
| LD-14 | S4 | Importing a Model, Ollama | https://docs.ollama.com/import | [CHECKED] | two documented inputs, a safetensors directory or a GGUF file, single or sharded; GGUF not quantised on import |
| LD-15 | S4 | ModelScope tag service | https://www.modelscope.cn/api/v1/tags | [CHECKED] | six top-level modality groups: text, image, audio, video, multimodal, scientific computing |
| LD-16 | S4 | ModelScope toolkit, constant definitions | https://raw.githubusercontent.com/modelscope/modelscope/master/modelscope/utils/constant.py | [CHECKED] | 219 task strings across five fields: 130 computer vision, 47 natural language processing, 21 audio, 20 multimodal, 1 science |
| LD-17 | S4 | ModelScope models index | https://www.modelscope.cn/models | [NOT ESTABLISHED] | a task filter tab exists but its values do not render and no catalogue facet returns them; the toolkit of LD-16 is the vocabulary of record |
| LD-18 | S4 | ModelScope catalogue aggregation | https://www.modelscope.cn/api/v1/dolphin/models | [CHECKED] | 69 library values over 264,794 models: PyTorch 230,091; safetensors 194,143; LoRA 114,361; GGUF 20,918; MLX 9,823; ONNX 7,353. Also an architecture facet and a science facet |
| LD-19 | S4 | Ollama documentation index | https://docs.ollama.com/llms.txt | [CHECKED] | eight capabilities: streaming, thinking, structured outputs, decision, vision, embeddings, tool calling, web search |
| LD-20 | S4 | Vision, Ollama | https://docs.ollama.com/capabilities/vision | [CHECKED] | image-input multimodal models are served |
| LD-21 | S4 | Embeddings, Ollama | https://docs.ollama.com/capabilities/embeddings | [CHECKED] | dedicated embedding models distributed with their own API endpoint |
| LD-22 | S4 | Ollama model library | https://ollama.com/library | [CHECKED] | capability labels across the index: tools 94, thinking 44, vision 41, cloud 16, embedding 12, decision 4, audio 1 |
| LD-23 | S4 | About releases, GitHub | https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases | [CHECKED] | no format, modality or task taxonomy; up to 1000 assets per release, each under 2 GiB, no total size or bandwidth limit |
| LD-24 | S4 | ListFoundationModels, Amazon Bedrock API reference | https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListFoundationModels.html | [CHECKED] | output modality enumeration is TEXT, IMAGE, EMBEDDING; input and output modality exposed per model |
| LD-25 | S4 | Models at a glance, Amazon Bedrock | https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html | [CHECKED] | catalogue organised by provider across 18 rows and wider than the filter enumeration, covering video, speech, embedding and reranking. The former modality page now redirects here |
| LD-26 | S4 | Microsoft Foundry Models overview | https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/foundry-models-overview | [PARTIAL] | over 10,000 models, about 50 new a month; two commercial tiers; eight filter axes including inference tasks, whose values are given only as examples |
| LD-27 | S4 | as LD-26 | as LD-26 | [CHECKED] | the catalogue includes a Hugging Face collection served on managed compute |
| LD-28 | S4 | Overview of Model Garden, Google Cloud | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models | [PARTIAL] | three catalogue categories and a four-axis filter pane; task and feature values not published. Also states that Hugging Face models deemed unsafe by that platform's scanners are blocked from deployment while suspicious or remote-code ones are flagged and remain deployable |
| LD-29 | S4 | NVIDIA NIM documentation index | https://docs.nvidia.com/nim/index.html | [CHECKED] | 17 model families spanning language, vision-language, embedding, reranking, optical character recognition, object detection, speech, safety, digital human, medical imaging, molecular biology, weather and simulation |
| LD-30 | S4 | as LD-29 | as LD-29 | [CHECKED] | the unit of distribution is a containerised microservice rather than a weight file |

### Formats (LD-31 to LD-42)

| ID | Class | Source | URL | Tag | Verified |
|---|---|---|---|---|---|
| LD-31 | S1 | pickle, Python documentation | https://docs.python.org/3/library/pickle.html | [CHECKED] | "The pickle module is not secure. Only unpickle data you trust." |
| LD-32 | S4 | Hugging Face models index, format counts by task | https://huggingface.co/models?pipeline_tag=…&library=… | [CHECKED] | for text generation: safetensors 328,892, pickle-bearing 56,780, GGUF 39,152, ONNX 2,310 of 420,353; equivalents for classification, embedding and multimodal tasks |
| LD-33 | S1, S4 | PyTorch serialization semantics; Transformers model documentation; Hugging Face Hub client serialization | https://docs.pytorch.org/docs/2.14/notes/serialization.html ; https://huggingface.co/docs/transformers/v4.35.0/en/main_classes/model ; https://huggingface.co/docs/huggingface_hub/en/package_reference/serialization | [CHECKED] | pickle is PyTorch's default; weights-only loading is the default since 2.6; safetensors has been the default save format since Transformers v4.35; the Hub client marks pickle saving deprecated |
| LD-34 | S4 | Safetensors documentation | https://huggingface.co/docs/safetensors/index | [CHECKED] | stores tensors only, as opposed to pickle |
| LD-35 | S1 | GGUF specification | https://github.com/ggml-org/ggml/blob/master/docs/gguf.md | [CHECKED] | single-file format for GGML executors; quantisation expressed in the tensor types; a LoRA file type and an mmproj sidecar are named |
| LD-36 | S4 | Multimodal, llama.cpp | https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md | [CHECKED] | multimodal use requires the model plus a separate projector file |
| LD-37 | S4 | Export to ONNX, Transformers; Optimum exporter task manager | https://huggingface.co/docs/optimum/exporters/onnx/overview | [CHECKED] | graph-based interchange format; exporter task coverage includes generation, classification and feature extraction |
| LD-38 | S4 | Custom operators, ONNX Runtime | https://onnxruntime.ai/docs/reference/operators/add-custom-op.html | [CHECKED] | a session registers a custom-operator library by path; the shared library is loaded into the inference process |
| LD-39 | S4 | NGC Catalog User Guide | https://docs.nvidia.com/ngc/latest/ngc-catalog-user-guide.html | [CHECKED] | container images signed since July 2023 and models since April 2025; software bill of materials, vulnerability-exchange documents and scan results retrievable by image digest |
| LD-40 | S4 | Engine Compatibility; Support Matrix, NVIDIA TensorRT | https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/engine-compatibility.html ; …/getting-started/support-matrix.html | [CHECKED] | by default an engine is compatible only with the TensorRT version, the device type and the host platform it was built on, each relaxable at a stated performance cost |
| LD-41 | S4 | Model Profiles, NVIDIA NIM for LLMs | https://docs.nvidia.com/nim/large-language-models/1.8.0/profiles.html | [CHECKED] | pre-compiled engines are downloaded for optimised profiles; generic profiles download raw weights and compile locally |
| LD-42 | S4 | Refitting an Engine, NVIDIA TensorRT | https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/refitting-engines.html | [NOT ESTABLISHED] | writing weights into a plan and omitting them are documented; no page states whether the original parameters can be recovered from an ordinary engine, and none claims they are protected |

### Safeguard state at scale (SG-01 to SG-12)

| ID | Class | Source | URL | Tag | Verified |
|---|---|---|---|---|---|
| SG-01 | S4 | Hugging Face models index, filtered by parameter count | https://huggingface.co/models?search=abliterated&num_parameters=min:100B ; …?search=uncensored&num_parameters=min:100B | [CHECKED] | 365 and 262 repositories respectively at 100B and above. The parameter facet is driven by a `num_parameters` range parameter; the index page itself does not expose the parameter name, which was established by construction and confirmed by the band the page then reported |
| SG-02 | S4 | Mistral Large 3 675B Base | https://huggingface.co/mistralai/Mistral-Large-3-675B-Base-2512 | [CHECKED] | "the base pre-trained version, not fine-tuned for instruction or reasoning tasks"; the card carries no statement about absent refusal behaviour |
| SG-03 | S4 | NVIDIA Nemotron 3 Ultra 550B Base | https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-Base-BF16 | [CHECKED] | pre-training stage only, 550B total with 55B active. The unsuffixed repository name returns unauthorised, so the publicly readable one is the suffixed variant |
| SG-04 | S4 | DeepSeek organisation listing | https://huggingface.co/models?search=deepseek-ai%2FDeepSeek-V4 | [CHECKED] | base checkpoints published at V4: 292B and 1.6T |
| SG-05 | S4 | Moonshot organisation listing | https://huggingface.co/models?search=moonshotai%2FKimi | [CHECKED] | a 1T base published for the K2 generation; none for K3, K2.5, K2.6 or K2.7 |
| SG-06 | S4 | Z.AI organisation listing | https://huggingface.co/models?search=zai-org%2FGLM | [CHECKED] | one base at 110B; none for the 753B flagship line |
| SG-07 | S4 | Kimi K3 abliterated | https://huggingface.co/Uniboshi/Kimi-K3-Abliterated-V1 | [CHECKED] | 2.8T parameters; "more than 98% of the safeguards have been removed", with per-layer removal percentages |
| SG-08 | S4 | Hugging Face models index, filtered | as SG-01 | [CHECKED] | strips at 763B, 756B, 755B, 753B and 561B across DeepSeek V4.1, GLM 5.3 and Nemotron Ultra; further strips throughout the 100B to 400B band |
| SG-09 | S4 | DeepSeek listing and V4.1-Flash card | https://huggingface.co/models?search=deepseek-ai%2FDeepSeek-V4 ; https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | [CHECKED] | no base variant published at V4.1; the released model is described through its post-training pipeline |
| SG-10 | S4 | Hugging Face search, Nemotron Ultra | https://huggingface.co/models?search=Nemotron-3-Ultra-550B | [CHECKED] | an abliterated derivative at 561B |
| SG-11 | S7, motivating only | trade reporting of a vendor statement on GLM 5.3 | https://www.deeplearning.ai/the-batch/glm-5-3-makes-cybersecurity-gains | [PARTIAL] | weights released only after a two-week safety evaluation with vetted partners, on the grounds that the model's skill at finding and exploiting software vulnerabilities warranted testing first. The vendor's own page did not render, so this is not first-party and is not admissible for a technical claim |
| SG-12 | S4 | Qwen base and instruct model cards | https://huggingface.co/Qwen/Qwen3.5-9B-Base ; https://huggingface.co/Qwen/Qwen3.5-122B-A10B | [CHECKED] | the training-stage field reads identically on base and instruction-tuned cards; the reliable discriminators are the name suffix and the sentence describing the repository as containing the pre-trained only model |

### Unreachable, redirected or otherwise noted

The former Bedrock modality page now redirects to a provider-organised catalogue. Google's Model Garden
documentation resolves under a renamed product path, Vertex AI having become Gemini Enterprise Agent
Platform, and Azure AI Foundry having become Microsoft Foundry, with separate classic and current
portals that differ in substance. ModelScope's documented metadata page returns navigation only on both
its domains. The unsuffixed Nemotron Ultra base repository returns unauthorised. The Z.AI blog post that
is the primary source for SG-11 returns an empty body. Counts from live catalogue pages drift between
readings and are quoted as at the access date.
