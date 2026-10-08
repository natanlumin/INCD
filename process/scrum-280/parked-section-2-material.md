# Parked from the SCRUM-280 deliverable, 8 October 2026

Material removed from `scrum280.md` section 2 because it does not answer the item: it restates glossary
definitions from the style guide or is input for Chapters 4, 6 and 7 (format consequences, the adapter
effect, safeguard state as a result, abliteration at scale, readable against claimed). Kept verbatim with
its source identifiers; the log rows those identifiers resolve to are at the end. Not part of the deliverable.

---

## 2. Model types, tasks and artefact formats

The segmentation below is the one the report uses across Parts I to IV: the threat by model-type matrix
and the threat-to-control coverage take its row and column labels verbatim. It is built in three parts
that each answer one question: what kind of file is this, what does the model produce, and how are the
numbers written down. Modality qualifies the second rather than competing with it. The table itself
(Table 4) is proposed; it is frozen, with a version and a date, only after agreement with Dan. The rows
are not taken from any platform's task vocabulary: only two platforms publish a closed one, the Hugging
Face Hub with 63 task names [LD-01] and ModelScope with 219 [LD-16], and roughly three quarters of Hub
repositories carry no task tag at all [LD-08].

### 2.1 The word "format" is used for three different things

Before any list, a distinction that the platforms themselves do not draw. Hugging Face's format filter
enumerates fifty-four values in a single list [LD-04], and they are not the same kind of thing:

- **Artefact formats**, how the numbers are written to disk: safetensors, GGUF, ONNX, Core ML,
  LiteRT, DDUF, and PyTorch's pickle.
- **Training and modelling libraries**, which imply a format without being one: Transformers,
  Diffusers, timm, PEFT, sentence-transformers.
- **Inference servers**, which are not properties of the file at all but of what can read it. These
  appear in a second facet of seventeen values, among them llama.cpp, vLLM, SGLang, Ollama, LM Studio
  and Docker Model Runner [LD-06].

Kaggle collapses the same three into one mandatory path segment it calls the framework [LD-10].

Only the first kind determines what happens when a file is opened. The rest describe provenance or
compatibility. This report therefore uses **format** for the first kind only, and the segmentation in
2.5 and 2.6 keys off that. Where a later chapter needs to say what can read a file, it says inference server.

### 2.2 The four artefact formats

The four formats are defined in the glossary. What this section adds is where each stands in the
ecosystem, with the evidence.

**Pickle checkpoints** remain PyTorch's default serialisation and are still everywhere: 230,091 models
on ModelScope carry one [LD-18], and about one text-generation repository in seven on the Hub [LD-32].
The direction of travel is away from it: safetensors has been the default save format in Transformers
since version 4.35, the Hub's client marks pickle saving deprecated, and PyTorch has loaded weights-only
by default since version 2.6 [LD-31, LD-33]. A C in this column means still in circulation, not still
being produced. The extension is a convention, not a guarantee: `pytorch_model.bin` is pickle while other
`.bin` files are raw tensors, so a control keyed on the extension both misses and over-flags.

**safetensors** is the default for new uploads and the format repositories convert to, and the majority
wherever it is counted: 194,143 models on ModelScope [LD-18] and about four fifths of text-generation
repositories on the Hub [LD-32, LD-34].

**GGUF** is a conversion endpoint rather than a format models are trained in, so a GGUF file is always a
derivative, usually several steps removed [LD-35]. A multimodal GGUF is two files, so an artefact scanned
or hashed as a unit may be half the model [LD-36].

**ONNX** is common for classification and embedding models in production pipelines [LD-37]. Its
load-time risk, a custom operator whose implementation is a native library loaded into the inference
process [LD-38], is inspected by no repository control in section 1.

### 2.3 Two things an organisation receives that are not artefact formats

Container images and compiled engines are received in place of a weight file; the glossary defines them
and section 1 treats them as distribution. The evidence that matters for the segmentation: containers are
signed, scanned and shipped with a software bill of materials in the one catalogue that documents it
[LD-39]. Engines are genuinely distributed, not only built locally: NVIDIA's inference microservices
download pre-compiled engines for their optimised profiles [LD-41]; a TensorRT engine runs only on the
device type, library version and host it was built for [LD-40]; whether the parameters can be recovered
from one is not established, and the tools that inspect weight files cannot read it [LD-42]. Neither is a
way of storing parameters, so neither is on the format axis.

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
activations need a file that exposes them. An artefact format does. A compiled engine, on present
evidence, does not. An organisation that receives a model only as an engine has not merely lost a
scanning opportunity; it has lost the ability to run a whole class of assessment, and the acceptance
criteria have to say what happens then.

The report uses one segmentation across Parts I to IV, and every later matrix keys off it. It is built in three parts that each answer one question: what kind
of file is this, what does the model produce, and how are the numbers written down. A fourth property,
modality, qualifies the second rather than competing with it.

They are kept apart deliberately. An earlier version answered all three at once and produced
rows that could not be compared with one another.

### 2.5 The rows and the file kinds

The glossary fixes three model types by what goes in and what comes out, classification, embedding and
generative, with modality as a qualifier and not a type; and three kinds of file in hand, the model, the
adapter and the quantised model. This section uses them as labels. Two points the segmentation rests on.

The type is the right row because the output is what an attacker manipulates and what a test measures.
The platforms' own task names decompose the same way, as input-to-output pairs such as image-text-to-text
[LD-01], which is why multimodal is a qualifier on a row and not a row of its own.

Two properties are readable from the file itself: whether the weights are complete or a fragment, from
the tensors present and the adapter configuration beside them; and whether the numbers are at full or
reduced precision, from their data types. Everything else about the model is a claim, which is what 2.10
turns on. There is no row for the instruct stage; 2.8 explains why.

### 2.6 The segmentation, and the rule that keeps it coherent

The four artefact formats of 2.2 apply across every row: pickle, safetensors, GGUF and ONNX.
They describe how the numbers are written to disk and say nothing about what the model does.

**A row is content. A column is file manner. Nothing crosses the two.** The test is whether the
property can be read from the bytes. You cannot tell from a file whether a model predicts or generates,
so that is a row. You can tell whether it is pickle or safetensors, and whether its numbers are reduced,
so those are columns.

**Table 4. The segmentation: model type against artefact format.** C common, P possible but
uncommon, under the rule proposed for the freeze; evidence per cell in the source log. Proposed, pending
agreement with Dan.

| Model type | pickle | safetensors | GGUF | ONNX |
|---|---|---|---|---|
| classification model | C | C | P | P |
| embedding model | C | C | P | C |
| generative model | C | C | C | P |

Qualifiers, recorded where they change the answer rather than as rows or columns of their own:

- **Modality**, on the row: a generative row whose input is image and text.
- **Precision**, on the columns: the same four formats carry quantised weights at P, C, C, P
  respectively, which is a statement about the columns and not a fourth row.
- **Completeness**, on the file: whether the artefact assessed was a whole model or a model with an
  adapter loaded. Adapters are 43 per cent of ModelScope's catalogue [LD-18]; recording them on the file
  rather than as a row keeps that share visible.

### 2.7 What an adapter does to this

Loading an adapter on a parent produces an effective model whose type may differ from the parent's. A low-rank adapter trained on a generative model to
classify transactions yields a classification model: the parent sits in one row, the product in another.

Three consequences, none of them bookkeeping.

**The row assessed need not be the row running.** An organisation assesses a generative model, an
adapter is loaded, and what serves requests is a classification model, or a generative model whose
safeguard has been suppressed. The parent file is unchanged throughout, with the same hash and the same
signature.

**The applicable tests change with the row.** If the product is a classification model, safeguard tests have
nothing to measure. If it is still generative but abliterated, they apply and would fail.

**The pair is the only assessable unit**, since the adapter alone has no behaviour and the parent alone
is not what runs. Every recorded assessment therefore names the pair it was performed on, not the
parent.

### 2.8 Why the safeguard is not a row

The obvious fourth row would be the generative model at the instruct stage, distinguished from the plain
generative one by carrying a refusal safeguard. It is deliberately absent, for two reasons.

**It is not readable.** You cannot tell from a complete set of weights whether it is at the instruct stage.
It is a publisher's claim, and 1.1 established that no repository verifies such claims.

**It is what the assessment measures.** Putting safeguard state on the axis would mean taking the
publisher's word for precisely the thing the tests in Chapter 7 exist to determine. A taxonomy should
not pre-classify its own measurement.

So safeguard state is recorded as a result, not a row, and it has three values.

**Present.** The model refuses as its producer describes. The question for Chapter 7 is how firmly,
which is what the tests report.

**Absent by design.** A base model: no refusal was ever trained in, so its absence is the specification
and not a finding. Such models exist at the largest scales: Mistral publishes a 675-billion-parameter
base described on its own card as "the base pre-trained version, not fine-tuned for instruction or
reasoning tasks" [SG-02]; NVIDIA publishes a 550-billion base [SG-03]; DeepSeek, Moonshot and Z.AI
publish bases at 1.6 trillion, 1 trillion and 110 billion respectively [SG-04, SG-05, SG-06].

**Absent by removal.** An abliterated model: an instruct model whose refusal behaviour was deliberately
removed and republished. This is the finding, because the artefact claims one state and exhibits another: the
lineage, the name and the model card all say instruct, and the behaviour does not.

### 2.9 The evidence that removal is routine, and at every scale

This subsection exists because the scale of the abliterated population is the single strongest piece of
evidence for why the report's acceptance criteria cannot rest on a publisher's claim.

At 100 billion parameters and above, as at 6 October 2026 [SG-01], Table 5 gives the counts.

**Table 5. Abliterated republications at 100 billion parameters and above.** Hugging Face Hub search, counts
as at 6 October 2026; repositories, not distinct models.

| Hub query | Repositories listed |
|---|---|
| matching "abliterated" | 365 |
| matching "uncensored" | 262 |

Counts are repositories rather than distinct models, since community quantisations of the same abliterated model
dominate. The figure to take from them is that this is a routine practice at flagship scale, not a
marginal one.

**The largest is a 2.8-trillion-parameter abliterated model**, whose own card states that "more than 98% of the
safeguards have been removed", with removal percentages given per attention projection, expert layer
and embedding token [SG-07]. Abliterated models exist throughout the range below it, at 763, 756, 753 and 561
billion [SG-08].

Three cases are worth naming, because each defeats a different assumption.

**Withholding the base does not withhold the capability.** DeepSeek publishes no base variant for V4.1
at 763 billion [SG-09]. Four independent abliterated republications of it exist at 753 to 763 billion
[SG-08]. A lab that declines to release the safeguard-free version does not thereby prevent one
existing.

**A vendor safety process does not survive republication.** NVIDIA's 550-billion release has an
abliterated derivative at full 561-billion weight [SG-10].

**Nor does a delayed release.** Z.AI held back the weights of its 753-billion model for a two-week
safety evaluation with vetted partners, on the grounds that its skill at finding and exploiting
software vulnerabilities warranted testing first [SG-11]. Abliterated versions of it are published [SG-08].

The conclusion the report should draw is narrow and well supported: **an intrinsic safeguard is not a
property the file carries, but a property someone can remove from the file**, at any scale reached so
far, including scales where the producer deliberately tried to control release. That is why the
segmentation records safeguard state as a measurement and not as a declaration, and why Chapter 7
cannot accept a model card as evidence of it.

### 2.10 Readable against claimed

One split runs through all of the above, and Chapter 6 divides on exactly this line.

**Readable from the file**: the artefact format; whether the weights are complete or a fragment;
the numeric precision. Any holder of the artefact can verify these.

**Claimed, and not readable**: which model this derives from; whether a complete set of weights is a
base or an instruct model; what it was trained on; whether a safeguard is present. None can be
determined from the bytes, and no repository verifies any of them.

A practical warning follows from the same evidence. Card metadata is not a reliable discriminator even
where it appears to be: Qwen's base repositories carry the same training-stage field as its
instruct ones, so an automated census built on that field will misclassify [SG-12].

The segmentation is therefore partly verifiable and partly taken on trust, and the line falls where a
reader would not expect. The column side is verifiable. The row side, which decides which threats and
which tests apply, rests on a publisher's declaration until something is measured.


---

## Log rows moved with the text

| ID | Class | Source | Owner | URL | Date or version on page | Tag | What was verified |
|---|---|---|---|---|---|---|---|
| HF-03 | Official | Moderation | Hugging Face | https://huggingface.co/docs/hub/moderation | no date shown | [CHECKED] | repository reports open a public discussion; comment reports reviewed by the moderation team |
| HF-09 | Official | Secrets Scanning | Hugging Face | https://huggingface.co/docs/hub/security-secrets | no date shown | [CHECKED] | TruffleHog on each push; e-mail on verified secrets only |
| HF-19 | Official | Security | Hugging Face | https://huggingface.co/docs/hub/security | no date shown | [CHECKED] | "SOC2 Type 2 certified" |
| KG-07 | Official | Improving Hugging Face Model Access for Kaggle Users (blog); Find Pre-trained Models | Kaggle | https://www.kaggle.com/blog/kaggle-hugging-face-integration ; https://www.kaggle.com/models | no date shown (assets 2025-05) | [CHECKED] | auto-generated "Linked from Hugging Face" pages; HF-side gating applies |
| MS-03 | Official | Code of Conduct | ModelScope | https://modelscope.cn/protocol/code-of-conduct | Contributor Covenant 1.4, no date | [CHECKED] | reports to contact@modelscope.cn |
| OL-08 | motivating only | Issue #7923 "Improve handling of pushes without namespace prefix" | ollama/ollama issue tracker | https://github.com/ollama/ollama/issues/7923 | opened 2024-12-03 | [PARTIAL] | pushes to the un-prefixed library/ namespace are refused ("not authorized to push to this namespace"); curation process for official library models documented nowhere → [NOT ESTABLISHED] |
| LD-02 | Official | Model Cards, Hugging Face Hub docs | https://huggingface.co/docs/hub/model-cards | [CHECKED] | the task is declared per repository as `pipeline_tag`, drives filtering, and selects the widget and API |
| LD-03 | Official | Model Cards, Hugging Face Hub docs | https://huggingface.co/docs/hub/model-cards | [CHECKED] | format declared as `library_name`; where absent the Hub infers it from files present |
| LD-04 | Official | Models index, libraries facet | https://huggingface.co/models | [CHECKED] | 54 values mixing serialisation formats, training libraries and other tooling; read from the page's own data because the rendering collapses the list |
| LD-05 | Official | Libraries, Hugging Face Hub docs | https://huggingface.co/docs/hub/models-libraries | [CHECKED] | parallel documented table of integrated libraries |
| LD-06 | Official | Models index, apps facet | https://huggingface.co/models | [CHECKED] | 17 downstream runners and applications including llama.cpp, vLLM, SGLang, Ollama, LM Studio, Docker Model Runner |
| LD-07 | Official | Models index, parameter facet | https://huggingface.co/models | [CHECKED] | 12 published parameter bands from under 1B to over 500B |
| LD-09 | Official | Kaggle CLI model metadata | https://raw.githubusercontent.com/Kaggle/kaggle-cli/main/docs/models_metadata.md | [PARTIAL] | the framework field is enumerated only as examples ending in an ellipsis; no closed list is published |
| LD-10 | Official | Models Documentation, Kaggle | https://www.kaggle.com/docs/models | [CHECKED] | framework is a mandatory path segment of every handle, so one model fans out into one artefact per framework |
| LD-11 | Official | Find Pre-trained Models, Kaggle | https://www.kaggle.com/models | [PARTIAL] | nine filter groups including a task facet and a data-type facet; the values inside are not published |
| LD-12 | Official | Models Documentation, Kaggle | https://www.kaggle.com/docs/models | [CHECKED] | task treated as free-text guidance for naming a variation, not a controlled vocabulary; GGUF observed as a framework value in the catalogue |
| LD-14 | Official | Importing a Model, Ollama | https://docs.ollama.com/import | [CHECKED] | two documented inputs, a safetensors directory or a GGUF file, single or sharded; GGUF not quantised on import |
| LD-15 | Official | ModelScope tag service | https://www.modelscope.cn/api/v1/tags | [CHECKED] | six top-level modality groups: text, image, audio, video, multimodal, scientific computing |
| LD-17 | Official | ModelScope models index | https://www.modelscope.cn/models | [NOT ESTABLISHED] | a task filter tab exists but its values do not render and no catalogue facet returns them; the toolkit of LD-16 is the vocabulary of record |
| LD-19 | Official | Ollama documentation index | https://docs.ollama.com/llms.txt | [CHECKED] | eight capabilities: streaming, thinking, structured outputs, decision, vision, embeddings, tool calling, web search |
| LD-20 | Official | Vision, Ollama | https://docs.ollama.com/capabilities/vision | [CHECKED] | image-input multimodal models are served |
| LD-21 | Official | Embeddings, Ollama | https://docs.ollama.com/capabilities/embeddings | [CHECKED] | dedicated embedding models distributed with their own API endpoint |
| LD-22 | Official | Ollama model library | https://ollama.com/library | [CHECKED] | capability labels across the index: tools 94, thinking 44, vision 41, cloud 16, embedding 12, decision 4, audio 1 |
| LD-23 | Official | About releases, GitHub | https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases | [CHECKED] | no format, modality or task taxonomy; up to 1000 assets per release, each under 2 GiB, no total size or bandwidth limit |
| LD-24 | Official | ListFoundationModels, Amazon Bedrock API reference | https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListFoundationModels.html | [CHECKED] | output modality enumeration is TEXT, IMAGE, EMBEDDING; input and output modality exposed per model |
| LD-25 | Official | Models at a glance, Amazon Bedrock | https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html | [CHECKED] | catalogue organised by provider across 18 rows and wider than the filter enumeration, covering video, speech, embedding and reranking. The former modality page now redirects here |
| LD-26 | Official | Microsoft Foundry Models overview | https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/foundry-models-overview | [PARTIAL] | over 10,000 models, about 50 new a month; two commercial tiers; eight filter axes including inference tasks, whose values are given only as examples |
| LD-29 | Official | NVIDIA NIM documentation index | https://docs.nvidia.com/nim/index.html | [CHECKED] | 17 model families spanning language, vision-language, embedding, reranking, optical character recognition, object detection, speech, safety, digital human, medical imaging, molecular biology, weather and simulation |
| LD-30 | Official | as LD-29 | as LD-29 | [CHECKED] | the unit of distribution is a containerised microservice rather than a weight file |
| LD-31 | Official | pickle, Python documentation | https://docs.python.org/3/library/pickle.html | [CHECKED] | "The pickle module is not secure. Only unpickle data you trust." |
| LD-32 | Official | Hugging Face models index, format counts by task | https://huggingface.co/models?pipeline_tag=…&library=… | [CHECKED] | for text generation: safetensors 328,892, pickle-bearing 56,780, GGUF 39,152, ONNX 2,310 of 420,353; equivalents for classification, embedding and multimodal tasks |
| LD-33 | Official | PyTorch serialization semantics; Transformers model documentation; Hugging Face Hub client serialization | https://docs.pytorch.org/docs/2.14/notes/serialization.html ; https://huggingface.co/docs/transformers/v4.35.0/en/main_classes/model ; https://huggingface.co/docs/huggingface_hub/en/package_reference/serialization | [CHECKED] | pickle is PyTorch's default; weights-only loading is the default since 2.6; safetensors has been the default save format since Transformers v4.35; the Hub client marks pickle saving deprecated |
| LD-34 | Official | Safetensors documentation | https://huggingface.co/docs/safetensors/index | [CHECKED] | stores tensors only, as opposed to pickle |
| LD-35 | Official | GGUF specification | https://github.com/ggml-org/ggml/blob/master/docs/gguf.md | [CHECKED] | single-file format for GGML executors; quantisation expressed in the tensor types; a LoRA file type and an mmproj sidecar are named |
| LD-36 | Official | Multimodal, llama.cpp | https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md | [CHECKED] | multimodal use requires the model plus a separate projector file |
| LD-37 | Official | Export to ONNX, Transformers; Optimum exporter task manager | https://huggingface.co/docs/optimum/exporters/onnx/overview | [CHECKED] | graph-based interchange format; exporter task coverage includes generation, classification and feature extraction |
| LD-38 | Official | Custom operators, ONNX Runtime | https://onnxruntime.ai/docs/reference/operators/add-custom-op.html | [CHECKED] | a session registers a custom-operator library by path; the shared library is loaded into the inference process |
| LD-39 | Official | NGC Catalog User Guide | https://docs.nvidia.com/ngc/latest/ngc-catalog-user-guide.html | [CHECKED] | container images signed since July 2023 and models since April 2025; software bill of materials, vulnerability-exchange documents and scan results retrievable by image digest |
| LD-40 | Official | Engine Compatibility; Support Matrix, NVIDIA TensorRT | https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/engine-compatibility.html ; …/getting-started/support-matrix.html | [CHECKED] | by default an engine is compatible only with the TensorRT version, the device type and the host platform it was built on, each relaxable at a stated performance cost |
| LD-41 | Official | Model Profiles, NVIDIA NIM for LLMs | https://docs.nvidia.com/nim/large-language-models/1.8.0/profiles.html | [CHECKED] | pre-compiled engines are downloaded for optimised profiles; generic profiles download raw weights and compile locally |
| LD-42 | Official | Refitting an Engine, NVIDIA TensorRT | https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/refitting-engines.html | [NOT ESTABLISHED] | writing weights into a plan and omitting them are documented; no page states whether the original parameters can be recovered from an ordinary engine, and none claims they are protected |
| SG-01 | Official | Hugging Face models index, filtered by parameter count | https://huggingface.co/models?search=abliterated&num_parameters=min:100B ; …?search=uncensored&num_parameters=min:100B | [CHECKED] | 365 and 262 repositories respectively at 100B and above. The parameter facet is driven by a `num_parameters` range parameter; the index page itself does not expose the parameter name, which was established by construction and confirmed by the band the page then reported |
| SG-02 | Official | Mistral Large 3 675B Base | https://huggingface.co/mistralai/Mistral-Large-3-675B-Base-2512 | [CHECKED] | "the base pre-trained version, not fine-tuned for instruction or reasoning tasks"; the card carries no statement about absent refusal behaviour |
| SG-03 | Official | NVIDIA Nemotron 3 Ultra 550B Base | https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-Base-BF16 | [CHECKED] | pre-training stage only, 550B total with 55B active. The unsuffixed repository name returns unauthorised, so the publicly readable one is the suffixed variant |
| SG-04 | Official | DeepSeek organisation listing | https://huggingface.co/models?search=deepseek-ai%2FDeepSeek-V4 | [CHECKED] | base checkpoints published at V4: 292B and 1.6T |
| SG-05 | Official | Moonshot organisation listing | https://huggingface.co/models?search=moonshotai%2FKimi | [CHECKED] | a 1T base published for the K2 generation; none for K3, K2.5, K2.6 or K2.7 |
| SG-06 | Official | Z.AI organisation listing | https://huggingface.co/models?search=zai-org%2FGLM | [CHECKED] | one base at 110B; none for the 753B flagship line |
| SG-07 | Official | Kimi K3 abliterated | https://huggingface.co/Uniboshi/Kimi-K3-Abliterated-V1 | [CHECKED] | 2.8T parameters; "more than 98% of the safeguards have been removed", with per-layer removal percentages |
| SG-08 | Official | Hugging Face models index, filtered | as SG-01 | [CHECKED] | strips at 763B, 756B, 755B, 753B and 561B across DeepSeek V4.1, GLM 5.3 and Nemotron Ultra; further strips throughout the 100B to 400B band |
| SG-09 | Official | DeepSeek listing and V4.1-Flash card | https://huggingface.co/models?search=deepseek-ai%2FDeepSeek-V4 ; https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | [CHECKED] | no base variant published at V4.1; the released model is described through its post-training pipeline |
| SG-10 | Official | Hugging Face search, Nemotron Ultra | https://huggingface.co/models?search=Nemotron-3-Ultra-550B | [CHECKED] | an abliterated derivative at 561B |
| SG-11 | motivating only | trade reporting of a vendor statement on GLM 5.3 | https://www.deeplearning.ai/the-batch/glm-5-3-makes-cybersecurity-gains | [PARTIAL] | weights released only after a two-week safety evaluation with vetted partners, on the grounds that the model's skill at finding and exploiting software vulnerabilities warranted testing first. The vendor's own page did not render, so this is not first-party and is not admissible for a technical claim |
| SG-12 | Official | Qwen base and instruct model cards | https://huggingface.co/Qwen/Qwen3.5-9B-Base ; https://huggingface.co/Qwen/Qwen3.5-122B-A10B | [CHECKED] | the training-stage field reads identically on base and instruction-tuned cards; the reliable discriminators are the name suffix and the sentence describing the repository as containing the pre-trained only model |
| LD-01 | Official | Tasks, Hugging Face | https://huggingface.co/tasks | [CHECKED] | 63 task names in six modality groups: multimodal 9, natural language processing 12, computer vision 19, audio 4, tabular 2, reinforcement learning 1; names read as input-to-output pairs |
| LD-08 | Official | Models index, filtered counts | https://huggingface.co/models?pipeline_tag=… | [CHECKED] | total 3,127,450; text generation 420,432; text classification 123,517; text to image 111,121; image-text to text 41,388; speech recognition 37,185; feature extraction 21,283; object detection 6,931. Live counters, quoted as at the access date |
| LD-16 | Official | ModelScope toolkit, constant definitions | https://raw.githubusercontent.com/modelscope/modelscope/master/modelscope/utils/constant.py | [CHECKED] | 219 task strings across five fields: 130 computer vision, 47 natural language processing, 21 audio, 20 multimodal, 1 science |
| LD-18 | Official | ModelScope catalogue aggregation | https://www.modelscope.cn/api/v1/dolphin/models | [CHECKED] | 69 library values over 264,794 models: PyTorch 230,091; safetensors 194,143; LoRA 114,361; GGUF 20,918; MLX 9,823; ONNX 7,353. Also an architecture facet and a science facet |
