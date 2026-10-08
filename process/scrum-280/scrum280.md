# SCRUM-280: repositories, hosting platforms and the model taxonomy

Version 1, 7 October 2026. Research cut-off and access date 6 October 2026.

Section 1 is the drafted subsection on repositories and hosting platforms, with the platform comparison
in Table 1 and Table 2. Section 2 is the segmentation of model types and artefact formats, with the
taxonomy in Table 3, proposed and awaiting agreement with Dan before it is frozen. Section 3 is the source
log. Vocabulary and sources follow the report style guide (SCRUM-281); citations in brackets resolve to
rows of section 3.

## 1. Repositories and hosting platforms

This section answers three questions about an open model before any threat is discussed: where its
file is published, which is the subject of 1.1; through which channels it reaches an organisation and in
what form, which is 1.2; and what each platform does to the file on the way, which Table 1 and Table 2
record in 1.3 and 1.4 interprets. Four properties are recorded for every platform, and they are the
columns of Table 1: governance, platform-side controls, guaranteed metadata, and distribution mechanism.

**Notation.** Terms fixed in the report's glossary are used as defined there and are not redefined here;
in this section they are producer, model repository, redistributor, platform-side control, guaranteed
metadata, distribution mechanism, inference server, in possession and by proxy. A bracketed identifier
such as [HF-18] names a row of the source log in section 3, and every factual statement carries one. The
prefix says which block of the log the row is in: HF Hugging Face Hub, KG Kaggle Models, MS ModelScope,
OL Ollama library, GH GitHub releases, CG cloud model gardens, LD what the platforms carry, SG safeguard
state at scale. A cell or sentence that reads *not established* means that no page published by the
platform states the property; it is never inferred from another platform.

**Abbreviations.** Every abbreviation used in sections 1 and 2, expanded once here; the report's
glossary is the place where the expansions are listed for the whole report.

| Abbreviation | Expansion |
|---|---|
| AI | artificial intelligence |
| API | application programming interface |
| ARN | Amazon Resource Name |
| AUP | acceptable-use policy |
| AWS | Amazon Web Services |
| CDN | content delivery network |
| CLI | command-line interface |
| CN | ModelScope's China site (modelscope.cn) as against its international site |
| CVE | Common Vulnerabilities and Exposures |
| DDUF | a Hugging Face bundle format for diffusion models |
| DMCA | the United States Digital Millennium Copyright Act |
| DSA | the European Union Digital Services Act |
| EOL | end of life |
| EULA | end-user licence agreement |
| FP8 | 8-bit floating-point precision |
| GA | general availability |
| GGUF | the llama.cpp family's file format, whose letters have no official expansion |
| GKE | Google Kubernetes Engine |
| GPG | GNU Privacy Guard, a signing tool |
| GPU | graphics processing unit |
| HTTPS | HTTP over TLS, that is, encrypted web transport |
| IAM | identity and access management |
| KMS | key management service |
| LFS | Git Large File Storage |
| LLM | large language model |
| LoRA | low-rank adaptation, a kind of adapter |
| ML | machine learning |
| NGC | NVIDIA's software and model catalogue (originally NVIDIA GPU Cloud) |
| NIM | NVIDIA Inference Microservices |
| ONNX | Open Neural Network Exchange |
| PEFT | parameter-efficient fine-tuning |
| PRC | People's Republic of China |
| REST | a style of web API |
| SBOM | software bill of materials |
| SDK | software development kit |
| SHA-256 | the 256-bit Secure Hash Algorithm |
| SLSA | Supply-chain Levels for Software Artifacts |
| TGI | Text Generation Inference, a Hugging Face inference server |
| TLS | Transport Layer Security |
| ToS | terms of service |
| UI | user interface |
| URL | web address |
| VEX | Vulnerability Exploitability eXchange |
| VPC | virtual private cloud |
| YAML | the text format of model-card metadata |

### 1.1 The repositories

Published models live in a small number of model repositories that host the files, their metadata and
their revision history: the Hugging Face Hub, the largest and the ecosystem's default address; Kaggle
Models and ModelScope for most of the rest; plain GitHub releases and the package registries for the
remainder.

An entry holds the files, a commit history, a model card, a licence field and, where the producer
declares it, the relation to a parent model. The declared relations, fine-tune, adapter, merge and
quantisation, link entries into a tree in which a popular base model may have thousands of descendants.
Three properties of that tree carry through the report. The relation is declared by the producer and
verified by no repository examined [HF-14, KG-05, MS-04]. Many producers do not declare it, since no
repository requires it [HF-15]. And a derivative is a different model from its parent, so a verdict on
the parent does not carry to the child.

What each repository does to the files it hosts is in Table 1, and the range is wide. The Hugging Face
Hub scans every file at every commit and extracts the imports of every pickle file [HF-05, HF-06].
Kaggle and ModelScope document no scanning, signing or conversion at all [KG-04, MS-02, MS-05]. The
Ollama library and GitHub verify digests but document no review of content [OL-03, OL-09, GH-05, GH-10].

Two cautions. ModelScope documents no mirroring of the Hugging Face Hub; its re-uploads are ordinary
user uploads carrying ModelScope's own hashes, so provenance must be re-established rather than assumed
to carry across [MS-04, MS-07]. GitHub Models, the hosted catalogue beside GitHub releases, was retired
on 30 July 2026 [GH-11] and appears here only because earlier material refers to it.

### 1.2 Distribution channels beyond the repositories

Between the repository and the organisation that runs a model sit redistributors, which repackage a
published model for a particular way of running it. What they hand over is either a file or a key: the
organisation then holds the model in possession, running it on an inference server it operates, or by
proxy, calling a provider's copy through an API. The licence is the same in both cases. What differs is
what the organisation can inspect, what it is accountable for, which of the risks in Chapter 4 are its
own and, in section 7.4, which tests it can run at all. The line runs through platforms, not between
them: Hugging Face hands out files and sells an API over them [HF-18], NVIDIA ships containers and hosts
endpoints for the same models [CG-13], and the cloud gardens do both [CG-01, CG-04, CG-08].

Five kinds of redistributor, each placed in Table 1 by what it hands over:

- **Cloud model gardens.** Google's Model Garden, Amazon Bedrock with SageMaker JumpStart, Microsoft
  Foundry and NVIDIA's NGC: provider-curated catalogues with no community publishing path, deploying a
  copy the provider often optimises or quantises [CG-01, CG-03, CG-07, CG-09, CG-13]. Their controls
  differ more than any other group's, which is why Table 2 breaks them out.
- **Packaged inference microservices.** NVIDIA's NIM: the model, an inference server and a serving API
  in one container, available to pull or to call [CG-13].
- **Local inference servers with their own libraries.** Ollama and the llama.cpp family, distributing
  quantised GGUF files for a workstation or a single server [OL-01, OL-06]; the one channel whose default
  artefact is a derivative rather than the producer's original.
- **Deployment and orchestration platforms.** Manage the accelerators and the serving workloads; the
  organisation chooses the model and the serving stack.
- **Hosted inference providers.** Open models behind a pay-per-token API; the organisation never handles
  the file.

### 1.3 The comparison

Table 1 summarises the platforms on the four dimensions the report uses throughout: governance,
the controls the platform applies itself, the metadata it guarantees, and the mechanism by which the
file reaches the organisation. Every cell resolves to a dated source in the log. A cell that reads *not
established* means that no page published by the platform states the property; it is left as such and
is never inferred from another platform, because the platforms differ precisely where an inference
would be convenient.

Table 2 breaks the cloud-garden row of Table 1 into its four providers, because they differ
materially on scanning and signing; a single row would have to say "varies" in every cell.

**Table 1. Where open models live and move: governance, controls, metadata and distribution by platform.** All
sources official (the platform's own documentation and terms), accessed 6 October 2026; the identifiers resolve in
section 3.

| Platform | Kind; hands you | Governance | Platform-side controls | Guaranteed metadata | Distribution mechanism |
|---|---|---|---|---|---|
| Hugging Face Hub | Model repository; a file (in possession). A hosted API is sold beside it [HF-18] | Anyone 13+ or a legal entity may publish; the uploader is responsible [HF-01]. Content policy, graduated moderation, removal at discretion [HF-01, HF-02]. DMCA with counter-notice; public takedown log [HF-02, HF-04] | Antivirus on every commit; pickle import scan; two third-party scanners; all advisory [HF-05, HF-06, HF-07, HF-08]. Safetensors conversion on request [HF-10]. Optional signed commits [HF-11]. Gating with author approval, optional geo-restriction [HF-12] | Card fields machine-read but author-supplied; none mandatory [HF-14, HF-15]. Parent relation declared, not verified [HF-14]. SHA-256 per file; full commit history [HF-13, HF-16, HF-17] | Library, CLI or git clone; Xet and LFS storage; separate CDN [HF-16, HF-17] |
| Kaggle Models | Model repository; a file (in possession) | Any registered user or organisation; one account each [KG-01, KG-02]. Community guidelines; human and automated moderation; removal without notice [KG-02, KG-03] | Gating behind an accepted agreement [KG-01]. Scanning, signing, conversion, pre-publication review: not established [KG-02, KG-04] | Licence from a fixed list; framework and version in every handle [KG-01, KG-05]. Parent relation self-declared, not verified; numbered versions kept [KG-05]. Per-file hashes: not established [KG-05] | kagglehub, CLI or a REST tar.gz; no git [KG-01, KG-06] |
| ModelScope | Model repository; a file (in possession). Mirroring of the Hugging Face Hub: not established [MS-04, MS-07] | Persons or entities, one account; PRC content law on the CN site; "not verified or approved" on the international site [MS-01, MS-02]. Takedown by written notice, counter-notice route [MS-01, MS-02] | Gating with a download agreement and approval [MS-04]. Scanning, signing, conversion, review: not established [MS-02, MS-05] | Licence a required field; base model and relation parsed into a lineage view, not verified [MS-04]. Git history; revision pinning [MS-04, MS-06]. Per-file SHA-256 only via the API (partial) [MS-07] | CLI, SDK or git clone with LFS; CN endpoint by default [MS-06, MS-08] |
| Ollama library | Package registry (GGUF); a file pulled by a local inference server (in possession) | Any registered user, own namespace, registered key; curation of the official namespace not documented [OL-01, OL-03]. Terms: 18+, suspension; DMCA notice without counter-notice or log [OL-02] | Digest verified per layer on pull [OL-03]. Scanning, review, licence check: not established [OL-09] | Content-addressed manifest and layers [OL-04]. Modelfile with optional free-text licence; parent survives only as a comment (partial) [OL-05]. No publisher identity beyond the namespace [OL-06] | ollama pull over HTTPS into a local store [OL-07] |
| GitHub releases | Package registry; a file attached to a software release (in possession). GitHub Models retired 2026-07-30 [GH-11] | Repository write permission required [GH-01]. Terms and AUP; dual-use research allowed; removal a last resort [GH-02, GH-03]. DMCA with counter-notice; notices published [GH-04] | Malware scanning of assets: not established [GH-10]. SHA-256 per asset since 2025-06-03 [GH-05]. Opt-in immutable releases with a Sigstore attestation [GH-06]; opt-in build provenance [GH-07] | Release bound to a tag; tags movable unless immutable [GH-01, GH-06]. Per-asset digest [GH-05]. Model-specific metadata: not established [GH-10] | HTTPS download or the gh CLI; assets up to 2 GiB [GH-08, GH-09] |
| Cloud model gardens | Redistributor (model garden); a deployed copy (in possession) or an endpoint (by proxy) | Provider-curated; no community publishing. Detail in Table 2 | From no documented pre-listing scanning (AWS) to signed images and models with an SBOM (NVIDIA). Table 2 | Cards, versions and licence acceptance in all four; digests, signing and SBOM only at NVIDIA. Table 2 | Deploy into the customer's account, or call a hosted endpoint. Table 2 |

**Table 2. The four cloud model gardens.** All sources official (provider documentation dated June to October 2026), accessed 6 October 2026; the identifiers resolve in section 3.

| Provider | Governance | Platform-side controls | Guaranteed metadata | Distribution mechanism |
|---|---|---|---|---|
| Google, Model Garden (Vertex AI now "Gemini Enterprise Agent Platform") | Google-curated; popular Hugging Face models added automatically; malware-flagged models removed; deprecation then retirement [CG-01, CG-02] | Serving containers vulnerability-scanned; Hugging Face models blocked if "unsafe", flagged if "suspicious"; no guarantee against malicious code stated [CG-01]. Google-built serving containers [CG-03] | Card per listing; publisher/model@version; EULA at deploy. Immutability, signing, SBOM: not established [CG-03] | Google-hosted endpoint (by proxy) or deployment into the customer's project (copy in possession); partner weights not exportable [CG-01, CG-03] |
| AWS, Amazon Bedrock, Bedrock Marketplace and SageMaker JumpStart | AWS-curated; lifecycle Active, Legacy, EOL; delistings on 2026-03-13 [CG-04, CG-05, CG-06] | Pre-listing scanning: not established [CG-04, CG-06]. Network isolation enforced; provider artefacts immutable [CG-04, CG-06]. Custom import requires safetensors [CG-07] | Card and lifecycle field; version pinning; EULA per channel [CG-04, CG-05, CG-06]. Signing, digests, SBOM: not established [CG-06] | Serverless endpoint (by proxy) or a SageMaker endpoint in the customer's account (copy); weight download not stated (partial) [CG-04, CG-06, CG-07] |
| Microsoft, Foundry Models (Azure AI Foundry now "Microsoft Foundry") | Two tiers, Microsoft-evaluated or provider-validated; a Hugging Face collection; lifecycle ending in retirement [CG-08, CG-10] | New Foundry: mandatory malware scan, remote-code models disallowed, safetensors only, signed runtime containers [CG-09]. Classic: Hugging Face models "not tested or evaluated" [CG-08] | Card with licence tab; versioned registry assets; GA weights fixed [CG-08, CG-10]. Digests or SBOM to customers: not established [CG-09] | Serverless (by proxy) or managed compute in the customer's subscription (copy); weights not obtainable through the catalogue [CG-08, CG-09] |
| NVIDIA, NGC Catalog and NIM | NVIDIA-curated; partners through a programme with scanning and sign-off; branch lifecycle; takedown policy not stated [CG-11, CG-14] | Images scanned on a schedule and signed since 2023; models signed since 2025; NIM verifies checksums at start [CG-11, CG-12, CG-13]. NVIDIA converts and quantises upstream models [CG-13] | SBOM, VEX and scan results by image digest [CG-11]. Terms accepted once per organisation; upstream licence shown [CG-11, CG-12, CG-13] | Signed container from nvcr.io, run anywhere (in possession); weights fetched at start from several stores; or hosted endpoints (by proxy) [CG-13] |

Each cell is a summary; the full statement behind it, with every source, is in the landscape evidence file.


### 1.4 What the platform controls establish, and what they do not

Three findings follow from the comparison, and each one shapes a later chapter.

**The controls act on the file as an artefact, not on the model as a behaviour.** Scanning looks for
executable content and known malware signatures; conversion changes the container the numbers sit in;
signing establishes who published a file and that it has not changed since. None of these examines what
the model does when it runs. No platform examined claims otherwise, and one states the limit explicitly,
noting that a model designated as supported has been tested for deployability but carries no guarantee
of the absence of vulnerabilities or malicious code [CG-01]. This is the boundary that section 6.3
builds on: the properties discoverable only by testing are precisely those the platform layer cannot
reach.

**Almost every control is advisory.** The scanners described in this section produce badges, warnings
and reports; a flagged file generally remains downloadable. Two documented exceptions exist, both at
the redistribution layer rather than the repository layer: Google's Model Garden blocks deployment of
models that the upstream repository's scanners deem unsafe, while flagging rather than blocking those
it deems suspicious or capable of executing remote code [CG-01]; and the newer Microsoft Foundry path
refuses models requiring remote code execution and enforces a safetensors-only rule on the collection
it manages [CG-09]. The practical consequence for Chapter 5 is that a control inventory built on
platform scanning inherits an advisory posture by default, and an organisation that wants a blocking
posture must impose it itself.

**Provenance is declared, not verified.** Every repository examined records a licence field and, where
the producer supplies it, a parent-model relation; none verifies either [HF-14, KG-05, MS-04]. The
digests and signatures that do exist establish that a file has not changed since it was published; they
say nothing about whether the published file is what its model card claims. This is the gap that
Chapter 6 divides into publicly attestable properties and properties discoverable only by testing, and
it is the reason the acceptance criteria in Chapter 7 cannot rest on repository metadata alone.

## 2. Model types, tasks and artefact formats

The segmentation below is the one the report uses across Parts I to IV: the threat by model-type matrix
and the threat-to-control coverage take its row and column labels verbatim. It is built in three parts
that each answer one question: what kind of file is this, what does the model produce, and how are the
numbers written down. Modality qualifies the second rather than competing with it. The table itself
(Table 3) is proposed; it is frozen, with a version and a date, only after agreement with Dan.

### 2.1 The task vocabularies the platforms publish

Each platform describes what it carries in its own task and format names; the detail per platform is
in the landscape evidence file. Three things follow from comparing them.

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

Three things decide how the format matters to the report: what loading each format can do,
how many files an artefact actually is, and which formats the platform controls of section 1 can
actually read.

### 2.2 The word "format" is used for three different things

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
2.6 and 2.7 keys off that. Where a later chapter needs to say what can read a file, it says inference server.

### 2.3 The four artefact formats

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

### 2.4 Two things an organisation receives that are not artefact formats

Container images and compiled engines are received in place of a weight file; the glossary defines them
and section 1 treats them as distribution. The evidence that matters for the segmentation: containers are
signed, scanned and shipped with a software bill of materials in the one catalogue that documents it
[LD-39]. Engines are genuinely distributed, not only built locally: NVIDIA's inference microservices
download pre-compiled engines for their optimised profiles [LD-41]; a TensorRT engine runs only on the
device type, library version and host it was built for [LD-40]; whether the parameters can be recovered
from one is not established, and the tools that inspect weight files cannot read it [LD-42]. Neither is a
way of storing parameters, so neither is on the format axis.

### 2.5 What the format decides about assessment

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

### 2.6 The rows and the file kinds

The glossary fixes three model types by what goes in and what comes out, classification, embedding and
generative, with modality as a qualifier and not a type; and three kinds of file in hand, the model, the
adapter and the quantised model. This section uses them as labels. Two points the segmentation rests on.

The type is the right row because the output is what an attacker manipulates and what a test measures.
The platforms' own task names decompose the same way, as input-to-output pairs such as image-text-to-text
[LD-01], which is why multimodal is a qualifier on a row and not a row of its own.

Two properties are readable from the file itself: whether the weights are complete or a fragment, from
the tensors present and the adapter configuration beside them; and whether the numbers are at full or
reduced precision, from their data types. Everything else about the model is a claim, which is what 2.11
turns on. There is no row for the instruct stage; 2.9 explains why.

### 2.7 The segmentation, and the rule that keeps it coherent

The four artefact formats of 2.3 apply across every row: pickle, safetensors, GGUF and ONNX.
They describe how the numbers are written to disk and say nothing about what the model does.

**A row is content. A column is file manner. Nothing crosses the two.** The test is whether the
property can be read from the bytes. You cannot tell from a file whether a model predicts or generates,
so that is a row. You can tell whether it is pickle or safetensors, and whether its numbers are reduced,
so those are columns.

**Table 3. The segmentation: model type against artefact format.** C common, P possible but
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
  adapter loaded.

### 2.8 What an adapter does to this

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

### 2.9 Why the safeguard is not a row

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

### 2.10 The evidence that removal is routine, and at every scale

This subsection exists because the scale of the abliterated population is the single strongest piece of
evidence for why the report's acceptance criteria cannot rest on a publisher's claim.

At 100 billion parameters and above, as at 6 October 2026 [SG-01], Table 4 gives the counts.

**Table 4. Abliterated republications at 100 billion parameters and above.** Hugging Face Hub search, counts
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

### 2.11 Readable against claimed

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

## 3. Source log

Every claim in sections 1 and 2 resolves to a row in this section. Class per the citation policy: Official (the
platform, producer, specification owner or standards body writing about its own artefact or service) or
Research; a row marked "motivating only" is press or an issue tracker, records why a question was asked,
and supports no claim. Access date 6 October 2026 throughout, which is also the date the landscape was
frozen. Tags: [CHECKED] the page states the claim; [PARTIAL] implied but not stated, with the gap named;
[NOT ESTABLISHED] no page states it after the searches named.

Method note. Several platform pages are JavaScript applications that return only a shell to a plain
fetch; those were rendered through a headless-render proxy at the same address, and where a list was
collapsed in the rendering it was read from the page's own embedded data. Where huggingface.co
rate-limited, the same documentation files were read from their public source repository. Counts drawn
from live catalogue pages are quoted as at the access date and will drift.

### 3.1 Platforms (Table 1 and Table 2): HF, KG, MS, OL, GH, CG

| ID | Class | Source | Owner | URL | Date or version on page | Tag | What was verified |
|---|---|---|---|---|---|---|---|
| HF-01 | Official | Terms of Service | Hugging Face | https://huggingface.co/terms-of-service | Effective 2022-09-15 | [CHECKED] | account open to natural persons 13+ or registered legal entities; publisher solely responsible for content; removal and termination at sole discretion; DMCA notices to dmca@huggingface.co; New York law and venue |
| HF-02 | Official | Content Policy | Hugging Face | https://huggingface.co/content-policy (final URL of /content-guidelines) | Effective 2025-04-10 | [CHECKED] | five prohibited categories incl. malware; Report button and safety@huggingface.co; graduated moderation actions (edit request, unranking, NFAA tag, removal, restriction, suspension); DMCA review, uploader informed and content disabled, counter-notification, 14 U.S. business days before restoration; appeals to safety@huggingface.co |
| HF-03 | Official | Moderation | Hugging Face | https://huggingface.co/docs/hub/moderation | no date shown | [CHECKED] | repository reports open a public discussion; comment reports reviewed by the moderation team |
| HF-04 | Official | huggingface-legal/takedown-notices (dataset) | Hugging Face | https://huggingface.co/datasets/huggingface-legal/takedown-notices | entries 2022-06 to 2026-09 | [CHECKED] | public log of takedown notices received |
| HF-05 | Official | Malware Scanning | Hugging Face | https://huggingface.co/docs/hub/security-malware | no date shown | [CHECKED] | every file scanned with ClamAV at each commit; unsafe file produces a warning and advice to remove; no blocking statement |
| HF-06 | Official | Pickle Scanning | Hugging Face | https://huggingface.co/docs/hub/security-pickle | no date shown | [CHECKED] | pickle import scan on every pickled upload via pickletools.genops; suspicious imports highlighted; disclaimer "not 100% foolproof", best-effort lists; GPG signing guarantees origin, not safety |
| HF-07 | Official | Third-party scanner: Protect AI | Hugging Face | https://huggingface.co/docs/hub/security-protectai | no date shown | [CHECKED] | Guardian scans public repositories' files; results shown on the Hub |
| HF-08 | Official | Third-party scanner: JFrog; blog "Hugging Face and JFrog partner…" | Hugging Face | https://huggingface.co/docs/hub/security-jfrog ; https://huggingface.co/blog/jfrog | blog 2025-03-04 | [CHECKED] | all public model repos scanned by JFrog on push; results exposed in the UI; no blocking statement |
| HF-09 | Official | Secrets Scanning | Hugging Face | https://huggingface.co/docs/hub/security-secrets | no date shown | [CHECKED] | TruffleHog on each push; e-mail on verified secrets only |
| HF-10 | Official | Convert weights to safetensors; Safetensors; Model(s) Release Checklist | Hugging Face | https://huggingface.co/docs/safetensors/convert-weights ; https://huggingface.co/docs/safetensors/index ; https://huggingface.co/docs/hub/model-release-checklist | no date shown | [CHECKED] | Convert Space downloads pickled weights, converts, opens a Pull Request (owner merges); "prefer safetensors over pickle". /docs/hub/safetensors returns 404; bot account name not on any docs page |
| HF-11 | Official | Signing commits with GPG | Hugging Face | https://huggingface.co/docs/hub/security-gpg | no date shown | [CHECKED] | optional; Verified only when the public key is on the account and e-mail matches; unsigned commits have no status |
| HF-12 | Official | Gated models | Hugging Face | https://huggingface.co/docs/hub/models-gated | no date shown | [CHECKED] | gated download requires login and sharing username/e-mail; automatic or manual approval; author can revoke without notice; optional IP-based geo-restriction; licence acceptance implemented through the gating prompt (extra_gated_prompt) |
| HF-13 | Official | Hub OpenAPI (openapi.md) | Hugging Face | https://huggingface.co/.well-known/openapi.md | no date shown | [CHECKED] | GET /api/models/{ns}/{repo}/scan returns security status; tree listing with expand returns scanner metadata; commit files schema requires sha256 and xetHash |
| HF-14 | Official | Model Cards; Licenses | Hugging Face | https://huggingface.co/docs/hub/model-cards ; https://huggingface.co/docs/hub/repositories-licenses | no date shown | [CHECKED] | license, base_model, pipeline_tag, library_name, datasets are machine-read (filters, licence display, widgets, model tree) but author-supplied; license uses a controlled identifier list; pipeline_tag validated by the metadata UI; base_model relation type inferred (adapter/merge/quantized/finetune); NO statement that the relation is verified → [NOT ESTABLISHED] for verification |
| HF-15 | Official | Getting Started with Repositories | Hugging Face | https://huggingface.co/docs/hub/repositories-getting-started | no date shown | [CHECKED] | licence field may be left blank; model card is best practice, not required; full commit history with diffs |
| HF-16 | Official | Xet overview; Backward compatibility with LFS; Xet security; Storage backends; Using Xet | Hugging Face | https://huggingface.co/docs/hub/xet/overview ; https://huggingface.co/docs/hub/xet/legacy-git-lfs ; https://huggingface.co/docs/hub/xet/security ; https://huggingface.co/docs/hub/storage-backends ; https://huggingface.co/docs/hub/xet/using-xet-storage | no date shown | [CHECKED] | LFS pointer carries SHA-256 of contents; Xet keeps the LFS pointer format and adds a Xet hash; Xet is the storage backend with an LFS bridge for legacy clients; chunk access bound to repository permissions |
| HF-17 | Official | Download files from the Hub (huggingface_hub v2.1.1); Downloading models | Hugging Face | https://huggingface.co/docs/huggingface_hub/guides/download ; https://huggingface.co/docs/hub/models-downloading | library v2.1.1 shown | [CHECKED] | huggingface_hub, hf CLI (hf download), git clone with git-xet + git-lfs; pin to full commit hash; file contents served from separate CDN/Xet hostnames |
| HF-18 | Official | Inference Endpoints; About Inference Endpoints | Hugging Face | https://huggingface.co/docs/inference-endpoints ; https://huggingface.co/docs/inference-endpoints/about | no date shown | [CHECKED] | managed hosted API; weights pulled from the Hub into a container; user receives an API, not a file |
| HF-19 | Official | Security | Hugging Face | https://huggingface.co/docs/hub/security | no date shown | [CHECKED] | "SOC2 Type 2 certified" |
| KG-01 | Official | Models Documentation | Kaggle | https://www.kaggle.com/docs/models | no date shown | [CHECKED] | any user or Organization profile publishes via UI, kagglehub or CLI; Hugging Face model pages auto-created when a notebook uses them; gated models require accepting an agreement (status banner, only "accepted" can download), Kaggle credentials needed for such downloads; handle = owner/model/framework/variation/version, framework enumerated; licence selected in the upload flow; download via kagglehub, kaggle CLI or REST URL returning tar.gz |
| KG-02 | Official | Terms of Use | Kaggle | https://www.kaggle.com/terms | no date in rendered text | [CHECKED] | one account per user; minors need parental consent; IP complaints via Google's report-content troubleshooter, repeat infringers may be suspended; content removable without notice; no endorsement, no warranty on content (→ [PARTIAL] for "no pre-publication review") |
| KG-03 | Official | Kaggle Community Guidelines | Kaggle | https://www.kaggle.com/community-guidelines | "Updated March 4, 2026" | [CHECKED] | models must not be plagiarised or misrepresent their source licence; NSFW, spam, misinformation, IP-infringing content removed; moderation by people and machine learning; report option on model pages; removal, suspension, ban, law-enforcement referral; appeal path and EU DSA out-of-court option |
| KG-04 | Official | Acceptable Use Policy | Kaggle | https://www.kaggle.com/aup | "Version June 22, 2025" | [PARTIAL] | prohibits distributing viruses, Trojan horses, corrupted files; policy only, no scanning statement → scanning, signing, conversion [NOT ESTABLISHED] |
| KG-05 | Official | kaggle-cli docs: models_metadata.md; model_variations_versions.md | Kaggle (GitHub) | https://raw.githubusercontent.com/Kaggle/kaggle-cli/main/docs/models_metadata.md ; https://raw.githubusercontent.com/Kaggle/kaggle-cli/main/docs/model_variations_versions.md | no date shown | [CHECKED] | licenseName chosen from a fixed list (Apache 2.0, MIT, GPL 3, CC variants…); modelInstanceType, baseModelInstance, externalBaseModelUrl, provenanceSources self-declared; each upload creates a numbered version, previous versions remain downloadable; files listing has no hash field → file hashes [NOT ESTABLISHED]; licence and parent verification [NOT ESTABLISHED] |
| KG-06 | Official | kagglehub README | Kaggle (GitHub) | https://github.com/Kaggle/kagglehub | no version shown | [CHECKED] | kagglehub.model_download; licence optional on upload; authentication only for consent-gated or private resources |
| KG-07 | Official | Improving Hugging Face Model Access for Kaggle Users (blog); Find Pre-trained Models | Kaggle | https://www.kaggle.com/blog/kaggle-hugging-face-integration ; https://www.kaggle.com/models | no date shown (assets 2025-05) | [CHECKED] | auto-generated "Linked from Hugging Face" pages; HF-side gating applies |
| MS-01 | Official | Terms and Conditions (CN site, served in English) | ModelScope (Alibaba, with CCF) | https://modelscope.cn/protocol/Terms-and-Condition | updated 2025-08-20, effective 2025-08-27 | [CHECKED] | registration by natural persons or legal entities with full civil capacity, not under sanctions, one account, mobile-phone registration with SMS verification (nationality of the number not stated → [PARTIAL]); PRC-law content prohibitions; downloaders bound by each model's Custom License; platform may review content "through technical or manual methods" and delete; accounts frozen on evidenced complaints; written infringement notice with identity, proof of rights, URLs, truthfulness statement; notice forwarded to uploader, removal "as appropriate", counter-notice route |
| MS-02 | Official | Terms and Conditions (international site) | Alibaba Cloud (Singapore) Pte Ltd | https://www.modelscope.ai/protocol/Terms-and-Condition | "Last updated: August 21, 2025" | [CHECKED] | under-18s barred; "User Content is not verified or approved by us. We do not assume any obligation to remove, validate, screen, verify or edit any User Content"; removal at discretion with or without notice; Singapore Copyright Act 2021 notice to a dedicated e-mail |
| MS-03 | Official | Code of Conduct | ModelScope | https://modelscope.cn/protocol/code-of-conduct | Contributor Covenant 1.4, no date | [CHECKED] | reports to contact@modelscope.cn |
| MS-04 | Official | Models intro; Model card; Overview; Quick Start | ModelScope | https://www.modelscope.ai/docs/models/intro ; https://www.modelscope.ai/docs/models/model-card ; https://www.modelscope.ai/docs/overview ; https://modelscope.ai/docs/intro/quickstart | docs build 2026-09-01 | [CHECKED] | account needed to create a model; public models downloadable by all; "application-based" models require accepting a download agreement and sharing e-mail/username, optional extra_gated_* fields, manual or automatic approval; licence is a required form choice, create_model defaults to Apache-2.0 if omitted; README YAML fields license, frameworks, base_model, base_model_relation (adapter/merge/quantized/finetune, may be inferred by the platform), new_version, datasets parsed for filtering and lineage; repos Git-backed; verification of licence or base_model [NOT ESTABLISHED]; launched November 2022 by Alibaba with the CCF Open Source Development Technical Committee; Transformers/Diffusers loading compatibility (no mirroring statement) |
| MS-05 | Official | Model upload | ModelScope | https://modelscope.cn/docs/models/upload | docs build 2026-09-01 | [PARTIAL] | files over 5 MB or with weight extensions (.bin, .pt, .pth, .safetensors, .ckpt, .gguf…) auto-routed to Git LFS; upload API hashes files (buffer_size_mb); versions advised; no scanning, signing, conversion or review statement → [NOT ESTABLISHED] |
| MS-06 | Official | Model download (CN and international copies) | ModelScope | https://modelscope.cn/docs/models/download ; https://www.modelscope.ai/docs/models/download | docs build 2026-09-01 | [CHECKED] | three channels: modelscope download CLI, Python SDK (snapshot_download, model_file_download, from_pretrained), git clone with Git LFS; revision pinning (branch or tag), default = last version before the library release; cache ~/.cache/modelscope/hub; login/token only for private or application-gated models; default endpoint modelscope.cn, MODELSCOPE_DOMAIN=www.modelscope.ai for the international site |
| MS-07 | Official | repo files API; model API (AI-ModelScope/bert-base-uncased; Qwen/Qwen2.5-0.5B-Instruct); AI-ModelScope organisation page | ModelScope | https://www.modelscope.cn/api/v1/models/Qwen/Qwen2.5-0.5B-Instruct/repo/files?Revision=master ; https://www.modelscope.cn/api/v1/models/AI-ModelScope/bert-base-uncased ; https://www.modelscope.cn/organization/AI-ModelScope | 2026-10-06 | [PARTIAL] | per-file Sha256, Size, IsLFS, commit message and committer returned by the API; no documentation page promises hashes or client-side verification; AI-ModelScope organisation holds 1,997 models reproducing HF model cards, commits "Upload folder using huggingface_hub" by ai-modelscope, ModelSource "USER_UPLOAD"; no documented mirroring or syncing process → [NOT ESTABLISHED]; hash/metadata preservation across platforms [NOT ESTABLISHED] |
| MS-08 | Official | modelscope/modelscope README | ModelScope (GitHub) | https://github.com/modelscope/modelscope | no date shown | [CHECKED] | "Most models on ModelScope are public and can be downloaded directly from the website" |
| OL-01 | Official | Importing a Model | Ollama Inc. | https://docs.ollama.com/import (old github docs/import.md is 404) | no date shown | [CHECKED] | any registered user publishes under their own namespace after registering a public key, via ollama push; GGUF taken as-is, no re-quantisation on import; Safetensors import for supported architectures |
| OL-02 | Official | Terms of Service | Ollama Inc. | https://ollama.com/terms | "Last updated: May 2026" | [CHECKED] | users 18+; prohibited unlawful, infringing, harmful content; suspension or termination; copyright/trademark notice to hello@ollama.com per 17 U.S.C. §512(c)(3); repeat-infringer policy; no counter-notice procedure or transparency log published |
| OL-03 | Official | docs/api.md (Push a Model; Pull a Model) | ollama/ollama repository | https://raw.githubusercontent.com/ollama/ollama/main/docs/api.md | no date shown | [CHECKED] | push requires an ollama.com account plus a registered public key; pull streams "pulling manifest", "pulling <digest>", "verifying sha256 digest", "writing manifest"; behaviour on mismatch not stated → [PARTIAL]; consumer-side signature verification not described → [NOT ESTABLISHED] |
| OL-04 | Official | registry manifest, library/llama3.2:latest (primary artefact) | Ollama Inc. registry | https://registry.ollama.ai/v2/library/llama3.2/manifests/latest | no date shown | [CHECKED] | Docker distribution v2 manifest; layers content-addressed by sha256 with mediaTypes application/vnd.ollama.image.{model,template,license,params} |
| OL-05 | Official | Modelfile Reference; Show model details | Ollama Inc. | https://docs.ollama.com/modelfile ; https://docs.ollama.com/api-reference/show-model-details | no date shown | [CHECKED] | Modelfile records FROM, PARAMETER, TEMPLATE, SYSTEM and optional free-text LICENSE; shown Modelfile keeps the parent as a comment and FROM points to a local sha256 blob; show API has details.parent_model, empty for base models → [PARTIAL] for parent recording |
| OL-06 | Official | llama3.2:latest library page | Ollama Inc. | https://ollama.com/library/llama3.2:latest | "Updated 2 years ago" | [CHECKED] | tag page lists content-addressed layers with digest prefixes and sizes, arch/parameters/quantisation, licence layer names; no publisher identity beyond the namespace |
| OL-07 | Official | CLI Reference; FAQ; API pull; API push | Ollama Inc. | https://docs.ollama.com/cli ; https://docs.ollama.com/faq ; https://docs.ollama.com/api/pull ; https://docs.ollama.com/api/push | no date shown | [CHECKED] | ollama pull over HTTPS only into a local blob store; POST /api/pull and /api/push with an insecure flag for non-TLS registries |
| OL-08 | motivating only | Issue #7923 "Improve handling of pushes without namespace prefix" | ollama/ollama issue tracker | https://github.com/ollama/ollama/issues/7923 | opened 2024-12-03 | [PARTIAL] | pushes to the un-prefixed library/ namespace are refused ("not authorized to push to this namespace"); curation process for official library models documented nowhere → [NOT ESTABLISHED] |
| OL-09 | none (searched) | searched: docs.ollama.com (import, cli, faq, api, llms.txt), ollama.com/terms, ollama.com/library, GitHub README | — | — | — | [NOT ESTABLISHED] | no documented malware, content or licence scanning or review of pushed models |
| GH-01 | Official | About releases | GitHub | https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases | no date shown | [CHECKED] | only users with write permission manage releases; releases bound to Git tags; automatic zip/tarball of the repository at the tag; each asset under 2 GiB; up to 1000 assets; no total-size or bandwidth cap |
| GH-02 | Official | GitHub Terms of Service | GitHub | https://docs.github.com/en/site-policy/github-terms/github-terms-of-service | "Effective: April 27, 2026" | [CHECKED] | human accounts 13+; GitHub may refuse or remove content violating law or policy |
| GH-03 | Official | GitHub Acceptable Use Policies; Active Malware or Exploits | GitHub | https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies ; https://docs.github.com/en/site-policy/acceptable-use-policies/github-active-malware-or-exploits | no date shown | [CHECKED] | bans unlawful content and direct support of active attack or malware campaigns; dual-use security research content explicitly allowed; removal as last resort; suspension, termination or removal at GitHub's discretion |
| GH-04 | Official | DMCA Takedown Policy | GitHub | https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy | no date shown | [CHECKED] | notice processed by GitHub; about 1 business day to fix; counter-notice; forks not automatically disabled; redacted notices published at github/dmca |
| GH-05 | Official | Releases now expose digests for release assets (changelog); REST API endpoints for release assets | GitHub | https://github.blog/changelog/2025-06-03-releases-now-expose-digests-for-release-assets/ ; https://docs.github.com/en/rest/releases/assets | 2025-06-03 | [CHECKED] | SHA-256 digest computed at upload for every release asset, immutable, shown in UI, REST (field digest, string or null), GraphQL and gh CLI |
| GH-06 | Official | Immutable releases (concept); Immutable releases are now generally available (changelog); gh release verify; gh release verify-asset; Managing releases in a repository | GitHub | https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases ; https://github.blog/changelog/2025-10-28-immutable-releases-are-now-generally-available/ ; https://cli.github.com/manual/gh_release_verify ; https://cli.github.com/manual/gh_release_verify-asset ; https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository | GA 2025-10-28 | [CHECKED] | opt-in per repository or organisation; assets and tag locked after publication; Sigstore-format release attestation over tag, commit SHA and asset digests; verified with gh release verify / verify-asset |
| GH-07 | Official | Artifact attestations (concept); Using artifact attestations to establish provenance for builds | GitHub | https://docs.github.com/en/actions/concepts/security/artifact-attestations ; https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds | no date shown | [CHECKED] | opt-in Sigstore build provenance, SLSA v1.0 Build L2 (L3 with reusable workflows); verified with gh attestation verify; "not a guarantee that an artifact is secure" |
| GH-08 | Official | About large files on GitHub; About Git Large File Storage; Git LFS billing | GitHub | https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github ; https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage ; https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-git-large-file-storage/about-billing-for-git-large-file-storage | no date shown | [CHECKED] | git blocks files over 100 MiB; LFS per-file 2 GB Free/Pro, 4 GB Team, 5 GB Enterprise Cloud; 10 GiB free LFS storage and bandwidth; large binaries steered to releases; the asset cap on this page is tied to the LFS plan limit (differs from GH-01's flat 2 GiB) |
| GH-09 | Official | gh release download | GitHub CLI manual | https://cli.github.com/manual/gh_release_download | no date shown | [CHECKED] | assets downloaded by direct HTTPS or gh release download with --pattern / --archive |
| GH-10 | none (searched) | searched: docs.github.com AUP and malware pages, REST release assets, web search | — | — | — | [NOT ESTABLISHED] | no documented malware or antivirus scanning of release assets; no model-specific metadata (licence, base model) guaranteed for assets |
| GH-11 | Official | GitHub Models (retirement notice); changelog 2026-07-01 "GitHub Models is being fully retired on July 30, 2026"; changelog 2026-07-30 "GitHub Models is now retired" | GitHub | https://docs.github.com/en/github-models ; https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026/ ; https://github.blog/changelog/2026-07-30-github-models-is-now-retired/ | 2026-07-30 | [CHECKED] | playground, model catalogue, inference API and BYOK fully retired 2026-07-30; migration path Microsoft Foundry or GitHub Copilot |
| GH-12 | Official | Solving the inference problem for open source AI projects with GitHub Models (blog, 2025-07-23); Deprecation of Azure endpoint for GitHub Models (changelog 2025-07-17); Introducing GitHub Models (blog 2024-08-01) | GitHub | https://github.blog/ai-and-ml/llms/solving-the-inference-problem-for-open-source-ai-projects-with-github-models/ ; https://github.blog/changelog/2025-07-17-deprecation-of-azure-endpoint-for-github-models/ ; https://github.blog/news-insights/product-news/introducing-github-models/ | 2025-07-23; 2025-07-17; 2024-08-01 | [CHECKED] | while live it exposed a hosted OpenAI-compatible endpoint (models.github.ai) under a GitHub token; models from Meta, Mistral, Azure OpenAI Service, Microsoft and others; "never distributed weights" by absence → [PARTIAL] |
| CG-01 | Official | Overview of Model Garden; Use Hugging Face Models; Overview of self-deployed models (Model Garden on Gemini Enterprise Agent Platform, the renamed Vertex AI) | Google Cloud | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-hugging-face-models ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/self-deployed-models | last updated 2026-10-05 | [CHECKED] | Google-curated: models from Google and partners; popular Hugging Face models added automatically by Google; partner proprietary models via Cloud Marketplace; models flagged as malware removed immediately; Google vulnerability-scans its serving containers; partner checkpoints get authenticity scans; HF models scanned by HF and its third-party scanner, "unsafe" blocked from deployment, "suspicious" or remote-code flagged but still deployable; daily HF malware scan; "we don't guarantee the absence of vulnerabilities or malicious code"; "verified by Google" = deployment settings, not weights; licence compliance is the user's; self-deployment runs in the customer's project and VPC |
| CG-02 | Official | Open model deprecations; Control access to Model Garden models | Google Cloud | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/open-models ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/control-model-access | last updated 2026-10-05 | [CHECKED] | deprecation then retirement (endpoint deactivated); preview open models available at least 45 days; organisation policy allow-lists models |
| CG-03 | Official | Open models overview (choose serving option); Deploy open models from Model Garden; Deploy models with custom weights (Preview) | Google Cloud | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/choose-serving-option ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/deploy-model-garden ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/deploy-models-with-custom-weights | last updated 2026-10-05 | [CHECKED] / [PARTIAL] | Google-optimised prebuilt containers (vLLM, Hex-LLM, SGLang, TGI, TensorRT-LLM); provider-prepared variants such as an FP8 Llama 3.3 (who converted not stated → PARTIAL); models addressed as publisher/model@version and containers by dated tag, no digest or immutability guarantee stated (PARTIAL); accept_eula=True at deploy; custom weights in Hugging Face format from Cloud Storage; partner-model weights cannot be exported; no signing, digest or SBOM statement → [NOT ESTABLISHED] |
| CG-04 | Official | Overview - Amazon Bedrock; Amazon Bedrock Marketplace; Subscribe to a model; Deploy a model; Bring your own endpoint; End-to-end workflow; Request access to models | AWS | https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html (the older bedrock-marketplace.html redirects to the guide root) ; …/bedrock-marketplace-subscribe-to-a-model.html ; …/bedrock-marketplace-deploy-a-model.html ; …/bedrock-marketplace-bring-your-own-endpoint.html ; …/bedrock-marketplace-end-to-end-workflow.html ; …/model-access.html | no date shown | [CHECKED] | AWS-curated; Marketplace: 100+ third-party models, public or proprietary, subscription accepts provider prices and EULAs; AcceptEula flag; first invocation of a serverless third-party model = EULA agreement; Marketplace models deploy to a SageMaker endpoint in the customer's account (VPC, KMS, IAM) and are called through Bedrock APIs; registration checks compatibility and requires network isolation; "a HuggingFace model" is a public model needing no subscription; no pre-listing scanning statement → [NOT ESTABLISHED] |
| CG-05 | Official | Model lifecycle (and legacy policy) - Amazon Bedrock | AWS | https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html ; …/model-lifecycle-legacy.html | applies to models launched on/after 2026-09-07; legacy: at least 12 months on Bedrock | [CHECKED] | Active, Legacy (6 months or 45 days), EOL (removed from all Regions); model card states the EOL policy; modelLifecycle API field |
| CG-06 | Official | SageMaker JumpStart pretrained models; JumpStart Foundation Models; Model sources and license agreements; Deploy a Model; ModelBuilder class; Use your JumpStart models in Bedrock; HubContentDocument schema; JumpStart marketing page | AWS | https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html ; …/jumpstart-foundation-models.html ; …/jumpstart-foundation-models-choose.html ; …/jumpstart-deploy.html ; …/jumpstart-foundation-models-use-python-sdk-model-class.html ; …/jumpstart-foundation-models-use-studio-updated-register-bedrock.html ; …/hub-content-document-schema.html ; https://aws.amazon.com/sagemaker/jumpstart/ | delisting notice dated 2026-03-13 | [CHECKED] | JumpStart "onboards and maintains" public models from third-party sources under the source's licence plus proprietary ones; delisted some models 2026-03-13, existing endpoints keep working, licence info for delisted open-weight models "refer to the Hugging Face listing"; accept_eula default False, must be set True; all JumpStart models run in network isolation; artefacts served from the AWS-managed bucket jumpstart-cache-prod-<region>; model_version pinning; semantic version in the hub-content ARN; model IDs prefixed huggingface-; whether catalogue weights may be downloaded not stated → [PARTIAL]; no signing, digest or SBOM statement → [NOT ESTABLISHED] |
| CG-07 | Official | Use Custom model import to import a customized open-source model into Amazon Bedrock | AWS | https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html | no date shown | [CHECKED] | import from the customer's S3 in Hugging Face safetensors format; Bedrock detects the architecture, pins transformers 4.51.3, overrides Llama 3 rope_scaling; licence compliance is the customer's |
| CG-08 | Official | Microsoft Foundry Models overview (classic); Foundry Models from partners and community; Deploy models with managed compute (classic); Deploy Hugging Face Hub models in Microsoft Foundry (classic) | Microsoft Learn | https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/foundry-models-overview ; https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-from-partners ; https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/deploy-models-managed ; https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/deploy-models-managed-hugging-face | ms.date 2026-07-28; 2026-09-21; 2026-01-22; 2026-05-14 | [CHECKED] | two tiers: "sold by Azure" (Microsoft evaluates, internal Responsible AI review) vs "partners and community" (validated by providers themselves); Hugging Face maintains its own collection; customers can only request additions; model card with License tab; partner licences and billing via Azure Marketplace; registry asset IDs with versions (azureml://registries/…/versions/N); versionUpgradeOption; classic: weights download from Hugging Face Hub to the endpoint at deploy time, not hosted on Azure, not usable as job inputs; models needing trust_remote_code "aren't supported for security reasons"; "Non-Microsoft Products that aren't tested or evaluated by Microsoft" |
| CG-09 | Official | Hugging Face models in Microsoft Foundry (preview); Managed compute in Microsoft Foundry (preview) | Microsoft Learn | https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/hugging-face-models ; https://learn.microsoft.com/en-us/azure/foundry/concepts/managed-compute-overview | ms.date 2026-06-16 (updated 2026-09-28); 2026-06-01 (updated 2026-09-28) | [CHECKED] | new Foundry: mandatory malware scanning, trust_remote_code disallowed unless HF-verified or trusted org, Safetensors-only, runtime validation; runtime containers built, CVE-scanned and signed by Microsoft; deployment templates pin runtime and quantisation; weights "pulled from Hugging Face once, validated, and stored in Microsoft-managed Azure storage"; dedicated Microsoft-owned GPU capacity, no egress needed; gated HF models not available (use classic); upstream licence metadata preserved; no digest or SBOM statement → [NOT ESTABLISHED] |
| CG-10 | Official | Foundry Models lifecycle and support policy; Model retirement schedule | Microsoft Learn | https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements ; https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule | ms.date 2026-07-24; 2026-09-21 | [CHECKED] | Preview, GA, Legacy, Deprecated, Retired (410 Gone); GA retirement set at launch (18 months; 12 for Anthropic, DeepSeek, Fireworks, Mistral); emergency retirement for security or compliance issues; GA weights and APIs fixed |
| CG-11 | Official | NGC Catalog User Guide; Join the NGC Software Partner Network | NVIDIA | https://docs.nvidia.com/ngc/latest/ngc-catalog-user-guide.html ; https://www.nvidia.com/en-us/gpu-cloud/ngc-software-partners/ | no date shown (version selector) | [CHECKED] | NVIDIA-curated; third-party ISVs via a partner programme with legal agreement, staging push, security scanning, QA and sign-off; every image security-scanned under the NGC Container Security Policy, public images rescanned every 30 days, NVIDIA AI Enterprise and NIM images weekly, Security Scanning tab; all NVIDIA container images signed since July 2023 (cosign); all NVIDIA models signed since April 2025 (OpenSSF Model Signing, model_signing verify); SBOM (CycloneDX), VEX and scan results retrievable by image digest via NGC API or ORAS; governing terms accepted once per NGC org before download; ngc registry model download-version |
| CG-12 | Official | Llama-3.1-8B-Instruct NIM container page (NGC) | NVIDIA | https://catalog.ngc.nvidia.com/orgs/nim/teams/meta/containers/llama-3.1-8b-instruct | tags latest, 2.0.13, 2.0.12; updated 2026-09-16 | [CHECKED] | Signed badge; Security Scanning tab; source linked to huggingface.co/meta-llama/Llama-3.1-8B-Instruct; "governed by the NVIDIA Open Model Agreement" plus the Llama 3.1 Community License; container under the NVIDIA Software License Agreement and Product-Specific Terms |
| CG-13 | Official | NIM for LLM and VLM: Get Started (1.11.0); Prerequisites; Quickstart; Model Profiles and Selection; Model Download; Model Signature Verification; overview | NVIDIA | https://docs.nvidia.com/nim/large-language-models/1.11.0/getting-started.html ; https://docs.nvidia.com/nim/large-language-models/latest/get-started/prerequisites.html ; …/latest/get-started/quickstart.html ; …/latest/deployment/model-profiles-and-selection.html ; …/latest/deployment/model-download.html ; …/latest/reference/model-signature-verification.html ; …/latest/about-nim-llm/overview.html | 1.11.0 and latest (2.0.x), no date shown | [CHECKED] | pull from nvcr.io with an NGC API key (keyless for eligible public NIMs); self-hosting under the NVIDIA AI Enterprise licence; pre-built optimised profiles (vllm, sglang, trtllm at bf16, fp8, mxfp4, nvfp4), "curated weights"; 64-char profile IDs; weights downloaded at startup from ngc://, hf://, s3://, gs://, modelscope://, local://; mirror to S3; NIM_MODEL_PATH for own weights; internal checksum verification; hosted alternative build.nvidia.com |
| CG-14 | Official | NVIDIA AI Enterprise Lifecycle Policy: Application Layer Software; End of Life Notices | NVIDIA | https://docs.nvidia.com/ai-enterprise/lifecycle/latest/application-software.html ; https://docs.nvidia.com/ai-enterprise/lifecycle/latest/eol-notices.html | last updated 2026-08-20; 2026-09-09 | [CHECKED] | Feature Branch supported one month, Production Branch 9 months; public EOL notices (e.g. NIM Llama-3.1-70b-instruct end of support July 2026); support lifecycle, not an explicit catalogue takedown policy |

### 3.2 What the platforms carry: LD-01 to LD-30

| ID | Class | Source | URL | Tag | What was verified |
|---|---|---|---|---|---|
| LD-01 | Official | Tasks, Hugging Face | https://huggingface.co/tasks | [CHECKED] | 63 task names in six modality groups: multimodal 9, natural language processing 12, computer vision 19, audio 4, tabular 2, reinforcement learning 1; names read as input-to-output pairs |
| LD-02 | Official | Model Cards, Hugging Face Hub docs | https://huggingface.co/docs/hub/model-cards | [CHECKED] | the task is declared per repository as `pipeline_tag`, drives filtering, and selects the widget and API |
| LD-03 | Official | Model Cards, Hugging Face Hub docs | https://huggingface.co/docs/hub/model-cards | [CHECKED] | format declared as `library_name`; where absent the Hub infers it from files present |
| LD-04 | Official | Models index, libraries facet | https://huggingface.co/models | [CHECKED] | 54 values mixing serialisation formats, training libraries and other tooling; read from the page's own data because the rendering collapses the list |
| LD-05 | Official | Libraries, Hugging Face Hub docs | https://huggingface.co/docs/hub/models-libraries | [CHECKED] | parallel documented table of integrated libraries |
| LD-06 | Official | Models index, apps facet | https://huggingface.co/models | [CHECKED] | 17 downstream runners and applications including llama.cpp, vLLM, SGLang, Ollama, LM Studio, Docker Model Runner |
| LD-07 | Official | Models index, parameter facet | https://huggingface.co/models | [CHECKED] | 12 published parameter bands from under 1B to over 500B |
| LD-08 | Official | Models index, filtered counts | https://huggingface.co/models?pipeline_tag=… | [CHECKED] | total 3,127,450; text generation 420,432; text classification 123,517; text to image 111,121; image-text to text 41,388; speech recognition 37,185; feature extraction 21,283; object detection 6,931. Live counters, quoted as at the access date |
| LD-09 | Official | Kaggle CLI model metadata | https://raw.githubusercontent.com/Kaggle/kaggle-cli/main/docs/models_metadata.md | [PARTIAL] | the framework field is enumerated only as examples ending in an ellipsis; no closed list is published |
| LD-10 | Official | Models Documentation, Kaggle | https://www.kaggle.com/docs/models | [CHECKED] | framework is a mandatory path segment of every handle, so one model fans out into one artefact per framework |
| LD-11 | Official | Find Pre-trained Models, Kaggle | https://www.kaggle.com/models | [PARTIAL] | nine filter groups including a task facet and a data-type facet; the values inside are not published |
| LD-12 | Official | Models Documentation, Kaggle | https://www.kaggle.com/docs/models | [CHECKED] | task treated as free-text guidance for naming a variation, not a controlled vocabulary; GGUF observed as a framework value in the catalogue |
| LD-13 | Official | Kaggle models index and Hugging Face integration blog | https://www.kaggle.com/models ; https://www.kaggle.com/blog/kaggle-hugging-face-integration | [CHECKED] | a distinct Hugging Face surface whose entries are links out rather than Kaggle-held files |
| LD-14 | Official | Importing a Model, Ollama | https://docs.ollama.com/import | [CHECKED] | two documented inputs, a safetensors directory or a GGUF file, single or sharded; GGUF not quantised on import |
| LD-15 | Official | ModelScope tag service | https://www.modelscope.cn/api/v1/tags | [CHECKED] | six top-level modality groups: text, image, audio, video, multimodal, scientific computing |
| LD-16 | Official | ModelScope toolkit, constant definitions | https://raw.githubusercontent.com/modelscope/modelscope/master/modelscope/utils/constant.py | [CHECKED] | 219 task strings across five fields: 130 computer vision, 47 natural language processing, 21 audio, 20 multimodal, 1 science |
| LD-17 | Official | ModelScope models index | https://www.modelscope.cn/models | [NOT ESTABLISHED] | a task filter tab exists but its values do not render and no catalogue facet returns them; the toolkit of LD-16 is the vocabulary of record |
| LD-18 | Official | ModelScope catalogue aggregation | https://www.modelscope.cn/api/v1/dolphin/models | [CHECKED] | 69 library values over 264,794 models: PyTorch 230,091; safetensors 194,143; LoRA 114,361; GGUF 20,918; MLX 9,823; ONNX 7,353. Also an architecture facet and a science facet |
| LD-19 | Official | Ollama documentation index | https://docs.ollama.com/llms.txt | [CHECKED] | eight capabilities: streaming, thinking, structured outputs, decision, vision, embeddings, tool calling, web search |
| LD-20 | Official | Vision, Ollama | https://docs.ollama.com/capabilities/vision | [CHECKED] | image-input multimodal models are served |
| LD-21 | Official | Embeddings, Ollama | https://docs.ollama.com/capabilities/embeddings | [CHECKED] | dedicated embedding models distributed with their own API endpoint |
| LD-22 | Official | Ollama model library | https://ollama.com/library | [CHECKED] | capability labels across the index: tools 94, thinking 44, vision 41, cloud 16, embedding 12, decision 4, audio 1 |
| LD-23 | Official | About releases, GitHub | https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases | [CHECKED] | no format, modality or task taxonomy; up to 1000 assets per release, each under 2 GiB, no total size or bandwidth limit |
| LD-24 | Official | ListFoundationModels, Amazon Bedrock API reference | https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListFoundationModels.html | [CHECKED] | output modality enumeration is TEXT, IMAGE, EMBEDDING; input and output modality exposed per model |
| LD-25 | Official | Models at a glance, Amazon Bedrock | https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html | [CHECKED] | catalogue organised by provider across 18 rows and wider than the filter enumeration, covering video, speech, embedding and reranking. The former modality page now redirects here |
| LD-26 | Official | Microsoft Foundry Models overview | https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/foundry-models-overview | [PARTIAL] | over 10,000 models, about 50 new a month; two commercial tiers; eight filter axes including inference tasks, whose values are given only as examples |
| LD-27 | Official | as LD-26 | as LD-26 | [CHECKED] | the catalogue includes a Hugging Face collection served on managed compute |
| LD-28 | Official | Overview of Model Garden, Google Cloud | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models | [PARTIAL] | three catalogue categories and a four-axis filter pane; task and feature values not published. Also states that Hugging Face models deemed unsafe by that platform's scanners are blocked from deployment while suspicious or remote-code ones are flagged and remain deployable |
| LD-29 | Official | NVIDIA NIM documentation index | https://docs.nvidia.com/nim/index.html | [CHECKED] | 17 model families spanning language, vision-language, embedding, reranking, optical character recognition, object detection, speech, safety, digital human, medical imaging, molecular biology, weather and simulation |
| LD-30 | Official | as LD-29 | as LD-29 | [CHECKED] | the unit of distribution is a containerised microservice rather than a weight file |

### 3.3 Formats: LD-31 to LD-42

| ID | Class | Source | URL | Tag | What was verified |
|---|---|---|---|---|---|
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

### 3.4 Safeguard state at scale: SG-01 to SG-12

| ID | Class | Source | URL | Tag | What was verified |
|---|---|---|---|---|---|
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

### 3.5 Unreachable, redirected or otherwise noted

The former Bedrock modality page now redirects to a provider-organised catalogue. Google's Model Garden
documentation resolves under a renamed product path, Vertex AI having become Gemini Enterprise Agent
Platform, and Azure AI Foundry having become Microsoft Foundry, with separate classic and current
portals that differ in substance. ModelScope's documented metadata page returns navigation only on both
its domains. The unsuffixed Nemotron Ultra base repository returns unauthorised. The Z.AI blog post that
is the primary source for SG-11 returns an empty body. Counts from live catalogue pages drift between
readings and are quoted as at the access date.
