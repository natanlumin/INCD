# SCRUM-281: glossary and citation policy

Version 1.2, 7 October 2026.

## 1. Terminology glossary (agreed once, used everywhere)

Rules: one canonical term per concept; the canonical term is used in all prose; the technical anchor
may appear once per section as a tag in parentheses; "avoid" words are not used in customer-facing or
executive text and may appear in technical appendices only when the anchor is being defined. A term
not in this glossary is not introduced by any chapter on its own; it is added here first.

Four areas, in the order a reader meets them: where models live and move; the segmentation; what is
in hand; the assessment vocabulary. The vocabulary of the demonstration set (the techniques executed
for this report) is not part of this glossary; it is kept beside its evidence in
`foundation/demonstration-terms.md` and appears in the report only in the demonstration-evidence
appendix and the platform-alignment chapter.

### 1.1 Where models live and move (platforms and distribution)

| Canonical term | Definition | Technical anchor | Avoid |
|---|---|---|---|
| producer | the organisation that trains a model and first publishes its file | model publisher, lab | "vendor" for a producer whose file is free to download |
| model repository | a public platform that hosts model files and their metadata for download; the platforms call it a hub | Hugging Face Hub, Kaggle Models, ModelScope | "marketplace"; calling ModelScope a mirror of Hugging Face: no mirroring process is documented and its re-uploads carry their own hashes |
| redistributor | a platform that re-hosts or repackages a model published elsewhere for a particular way of running it. Kinds: cloud model gardens, curated catalogues deployable on that provider; package registries, which ship the model with its runtime; packaged inference microservices; hosted inference providers | Google Model Garden (Gemini Enterprise Agent Platform, formerly Vertex AI), Amazon Bedrock and SageMaker JumpStart, Microsoft Foundry (formerly Azure AI Foundry), NVIDIA NGC and NIM; Ollama library, GitHub releases; hosted API providers | treating a redistributor as the source of the file; the retired product names; "repository" for Ollama or GitHub releases |
| in possession | the organisation holds the model file and runs it on hardware and serving software it chooses and operates | self-hosted, downloaded weights | "open" for a model the organisation only calls |
| by proxy | the organisation holds an API key to a provider's copy of the model and never touches the file or the software that serves it | hosted inference endpoint, managed serving | "closed" for an open model served by a provider; assuming a test that needs the file can be run |
| distribution mechanism | how the file moves from publisher to operator: direct download, git-LFS clone, API pull, container image, package manager | `huggingface_hub`, git LFS, `ollama pull`, OCI image | implying one mechanism for all platforms |
| platform-side control | a protection the platform applies to hosted files before or at download: malware and pickle scanning, format conversion, signing, gating behind accepted terms, licence acceptance | Hugging Face pickle scanning and safetensors conversion; gated repositories; Kaggle moderation | assuming a control exists without a dated source; assuming a control blocks when it only flags |
| guaranteed metadata | fields the platform enforces or verifies, as opposed to fields the publisher fills in freely | model card YAML (`base_model`, `license`, `pipeline_tag`), file hashes, commit history | treating free-text model-card claims as guaranteed; treating a declared parent relation as verified |
| provenance | the recorded chain from a base model to the file in hand: base model, derivation kind, author, commit, hash | model tree, `base_model` relations, SHA-256 of each file | "provenance" for a licence statement alone |
| governance | who may publish, what is removed, how disputes and takedowns work on the platform | terms of service, content policy, DMCA process | "governance" for the operator's own policy (say "organisational practice") |
| inference server | the software that loads a model file and executes it, as a library inside an application or as a service with an API; chosen, operated and patched separately from the model | vLLM, SGLang, Text Generation Inference, the llama.cpp server, Ollama's server | "framework" (reserved for ATLAS, OWASP, NIST, ISO); listing it among artefact formats |
| received instead of a file | two things an organisation may receive in place of a weight file. A container image: a runnable bundle of the model with its inference server and serving code. A compiled engine: the model built for one hardware target, library version and host platform, not portable and unreadable by the tools that inspect weight files | OCI image, NIM container; TensorRT engine, ExecuTorch `.pte` | assessing the model without the software around it; listing either as a storage format; asserting that an engine's weights are protected or recoverable (not established) |

### 1.2 The single segmentation: model type × artefact format (the taxonomy)

Every later matrix (threat × model type, control × model type, test family × model type) keys off
this segmentation. Rows are what the model produces; columns are how its numbers are written to disk.
Modality qualifies a row and numeric precision qualifies a column. Adapters and quantised copies are
file kinds, defined in §1.3; an adapter changes which row applies. The row set and the cell values are frozen with Dan and published with the landscape item; the
terms below are fixed now.

**Axis A, model type.** A model type is defined by what goes in and what comes out. The first three rows
are the types; modality qualifies them; base and instruct are two stages of the same model, not types.

| Canonical term | Takes in | Gives out | Note | Avoid |
|---|---|---|---|---|
| generative model | a prompt: text, and for some models images or audio as well | free text, one word at a time, with no limit on what it may say | the type most threats in this report concern | "LLM" for a model that does not produce text |
| classification model | text, an image or audio | one label from a fixed list, or a number | it cannot produce anything outside that list | "generative" for a classifier whose label is a word |
| embedding model | text, an image or audio | a list of numbers used to compare, search or cluster inputs | nothing readable comes out; every model represents its input as numbers internally, but only here is that the product | "generative"; "embedding model" for any model because it embeds internally |
| modality | the kinds of data a model takes in and gives out: text, image, audio, video | | a property of a model type, not a type of its own; multimodal means more than one kind on at least one side | "multimodal" as a row beside classification |
| base model | text | the continuation of that text | not a fourth type but a stage: the model as it leaves pre-training, before any instruction tuning. Any type can be released at this stage; a base model follows no instructions and has no trained refusal | "base" for an instruction-tuned release; reading base against instruct from card metadata alone |
| instruct / chat model | an instruction or a conversation | an answer, or a refusal | the same stage distinction, after further training to follow instructions and, usually, to refuse some. In practice almost always a generative model; it is the variant that carries the publisher's safeguard | "aligned" as a guarantee |

**Axis B, artefact format** (how the numbers are stored):

| Canonical term | Definition | Technical anchor | Avoid |
|---|---|---|---|
| pickle checkpoint | a file serialised with Python's pickle; loading it can execute arbitrary code, so the format itself is a threat surface. The extension is a convention; the content decides | `.bin`, `.pt`, `.pth`, `.ckpt`; specification: the Python Software Foundation's pickle module, with PyTorch for the checkpoint convention | loading one from an unverified source; "legacy" without saying it still exists; a control keyed on the extension |
| safetensors | a format that stores tensors only, with no executable content; loading cannot run code | `.safetensors`; specification: Hugging Face | treating it as a guarantee about behaviour (it guarantees only the container) |
| GGUF | a single-file format for quantised models used by llama.cpp-family runtimes, with metadata inside the file; a multimodal model is two files, the model and a projector | `.gguf` (successor of GGML), `mmproj`; specification: ggml-org, the llama.cpp project | "GGML" for current files; scanning or hashing half of a two-file artefact as the whole |
| ONNX | a graph-based interchange format for running models outside their training framework; a graph can name a custom operator whose implementation is a native library the runtime loads | `.onnx`; specification: the ONNX project (Linux Foundation), with ONNX Runtime for what loading does | assuming the ONNX export behaves identically to the source; assuming the format cannot name code |

Container images and compiled engines are things an organisation receives in place of a weight file,
not ways of storing parameters; they are defined in §1.1 and treated as distribution.

### 1.3 Artefacts and derivatives (what is in hand)

**The file.**

| Canonical term | Definition | Technical anchor | Avoid |
|---|---|---|---|
| model file, the file | the downloaded artefact; all knowledge and behaviour are its numbers | weights, checkpoint | "weights" as the subject of a sentence |
| open-source model | a model whose file is publicly downloadable, whatever its licence | open-weights model | "open source" for a hosted API |

**Derivatives.** A derivative model is any file produced from another model file. Four kinds, and the
adapter that produces one of them; each is a different model from its parent and gets its own
assessment. Never carry a parent's result to a derivative.

| Canonical term | Definition | Technical anchor | Avoid |
|---|---|---|---|
| quantised model | the same model stored with less precise numbers; behaviour close to the parent's, not identical, and the safeguard can shift | INT8, FP8, 4-bit, GGUF quantisation levels | "the same model" as its parent |
| fine-tuned model | a model changed by further training on new examples; its safeguard may differ from the parent's in either direction | fine-tuning, SFT, RLHF, DPO | assuming the parent's assessment covers it |
| adapter | a small file loaded together with a model that changes what it does; not runnable alone; the model-plus-adapter pair is what is assessed, and its type may differ from the parent's | LoRA, QLoRA, PEFT adapter | assessing an adapter without its base; carrying a parent's result to the pair |
| merged model | a model made by combining the numbers of two or more model files; no parent's safeguard is assumed to survive | weight averaging, SLERP, TIES | "merge" without saying which parents |
| abliterated model | a copy from which the refusal behaviour was located and removed, then published, often as "uncensored" | abliteration, refusal-direction ablation | calling it a jailbreak (it needs no prompt); "uncensored" without quotation marks |

**Inside and around the file.**

| Canonical term | Definition | Technical anchor | Avoid |
|---|---|---|---|
| safeguard and guard | safeguard: the model's own refusal behaviour, trained in by its publisher, inside the file. Guard: a control placed around the model, in front of or behind it | safety alignment; guardrail, input and output filter | "guardrail" for the model's own refusal; "safeguard" for an external control |

### 1.4 Assessment vocabulary (the report's own words)

The terms the threat, control, assessment and acceptance chapters are written in, as the skeleton
names them, one row per thing the report talks about, with its qualifiers inside the row. Rules about
evidence are in §2.

| Canonical term | Definition | Avoid |
|---|---|---|
| threat | an attack vector against an open-source model, its artefact or its serving. Each threat is placed in one of three families (supply-chain and artefact-level; model-integrity; inference-time and runtime), marked as acting at model level or system level, and rated for orchestration complexity: the access, skill, cost and detectability it needs | "risk" or "vulnerability" for a threat; a threat without its family and level; treating all threats as equal |
| control | a protection a defender applies against a threat: existing, emerging or missing, and scored for maturity on evidence base, tooling, operational cost and false-positive burden | assuming a control exists in production because it exists in a paper; "mature" without the rubric |
| trust tier | the protection level a deployment requires, set by the trust placed in the system; criteria are stated per tier | tiers without the criteria that go with them |
| lifecycle stage | selection, adjustment, deployment, runtime: the four points at which a question about a model is answered | "deployment" for the whole lifecycle |
| attestable and testable properties | attestable: established from what publisher and platform expose, origin, training data, model card, bill of materials, signing. Testable: a behavioural property no metadata reveals, hidden triggers, latent contamination, the safeguard's behaviour | treating a model-card claim as attested; assuming metadata covers behaviour |
| test family | static, dynamic, behavioural, provenance: each stated with what it detects, what it cannot, and the access it needs, black-box (input and output only) or white-box (the file or its internals) | "scanner" for a family; a white-box result for a model held only by proxy |
| acceptance criterion | what a model must pass before it is selected, adjusted, deployed or left running, per test family and trust tier, stated so it can be contracted against | a criterion that cannot be met with available tooling, which is a gap |
| gap | a threat with no adequate control, no reliable detection, or a criterion that cannot be met: mitigation, assessment and criteria gaps | "gap" without saying which kind |
| demonstration set | the techniques executed for this report, with an explicit statement of what they do and do not demonstrate; its vocabulary lives beside its evidence | citing a demonstration result as a landscape fact; its vocabulary in the body of the report |

---

## 2. Citation policy and source-quality bar

### 2.1 Minimum standard

Every factual claim rests on a dated source of a kind in Table 2.1. A property no such source states
is written "not established" and is never inferred from a neighbouring case; a judgement without a
source is the authors' own and carries the forecast label. Every source is recorded in one dated log,
with the sections that cite it.

### 2.2 Source classes

**Table 2.1. Admissible sources**

| Source | Who | Examples | Evidence for |
|---|---|---|---|
| Official | standards and framework bodies; government and regulators; owners of a format specification; a producer, repository, redistributor or software maintainer writing about its own artefact or service | OWASP Top 10 for LLM Applications; MITRE ATLAS; NIST AI RMF; ISO/IEC 42001; EU AI Act; Hugging Face Hub documentation; Amazon Bedrock documentation; a publisher's model card | what that body owns, and nothing beyond it |
| Research | peer-reviewed or accepted-venue publications; preprints, labelled | a USENIX Security paper; a NeurIPS paper; an IEEE S&P paper; an arXiv paper | a result |

Excluded: press, blogs, talks and news. They never support a factual claim; they may motivate a
question, and are then recorded in the log as motivating only.

Measurements and interview statements are not sources; each is cited under the provenance and
attribution rules of the chapter that produces it.

### 2.3 Confidence labels

Every finding in the threat and outlook chapters carries one of three labels that tell the reader how
well it is supported: by a source, by a weaker source, or by the authors' judgement alone.

**Table 2.3. Confidence labels**

| Label | Meaning |
|---|---|
| established | supported by an official or research source, or by measured data |
| emerging | supported only by a labelled preprint, by a single party's statement about itself, or by extending a measured result to a case that was not itself run, which the sentence then says |
| forecast | the authors' assessment, dated; kept apart from established findings |

