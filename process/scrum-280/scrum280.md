# SCRUM-280: repositories, hosting platforms and the model taxonomy

Version 1, 8 October 2026. Research cut-off and access date 6 October 2026; Together AI and Docker Hub added 8 October 2026.

Section 1 is the drafted subsection on repositories and hosting platforms, with the platform comparison
in Table 1 to Table 3. Section 2 is the segmentation of model types against artefact formats, with the
taxonomy in Table 4, proposed and awaiting agreement with Dan before it is frozen. Section 3 is the source
log. Vocabulary and sources follow the report style guide (SCRUM-281); citations in brackets resolve to
rows of section 3.

## 1. Repositories and hosting platforms

This section answers three questions about an open model before any threat is discussed: where its
file is published, which is the subject of 1.1; through which channels it reaches an organisation and in
what form, which is 1.2; and what each platform does to the file on the way, which Table 1 to Table 3
record and 1.3 interprets. Four properties are recorded for every platform, and they are the
columns of all three: governance, platform-side controls, guaranteed metadata, and distribution mechanism.

**Notation.** Terms fixed in the report's glossary are used as defined there and are not redefined here;
in this section they are producer, model repository, redistributor, platform-side control, guaranteed
metadata, distribution mechanism, inference server, in possession and by proxy. A bracketed identifier
such as [HF-18] names a row of the source log in section 3, and every factual statement carries one. The
prefix says which block of the log the row is in: HF Hugging Face Hub, KG Kaggle Models, MS ModelScope,
OL Ollama library, GH GitHub releases, TA Together AI, DK Docker Hub, CG cloud model gardens, LD what the platforms carry, TX taxonomy
evidence. A cell or sentence that reads *not established* means that no page published by the
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
| BYOK | bring your own key, calling a hosted model with the customer's own provider key |
| CDN | content delivery network |
| CLI | command-line interface |
| CN | ModelScope's China site (modelscope.cn) as against its international site |
| CVE | Common Vulnerabilities and Exposures |
| DMCA | the United States Digital Millennium Copyright Act |
| DSA | the European Union Digital Services Act |
| EOL | end of life |
| EULA | end-user licence agreement |
| FP8 | 8-bit floating-point precision |
| GA | general availability |
| GGUF | the llama.cpp family's file format, whose letters have no official expansion |
| GPG | GNU Privacy Guard, a signing tool |
| GPU | graphics processing unit |
| HTTPS | HTTP over TLS, that is, encrypted web transport |
| IAM | identity and access management |
| KMS | key management service |
| LFS | Git Large File Storage |
| LLM | large language model |
| LoRA | low-rank adaptation, a kind of adapter |
| NGC | NVIDIA's software and model catalogue (originally NVIDIA GPU Cloud) |
| NIM | NVIDIA Inference Microservices |
| OCI | Open Container Initiative, the standard for container images and the artefacts stored beside them |
| ONNX | Open Neural Network Exchange |
| PEFT | parameter-efficient fine-tuning |
| PRC | People's Republic of China |
| REST | a style of web API |
| S3 | Amazon Simple Storage Service, the cloud object store |
| SBOM | software bill of materials |
| SDK | software development kit |
| SHA-256 | the 256-bit Secure Hash Algorithm |
| SLSA | Supply-chain Levels for Software Artifacts |
| TGI | Text Generation Inference, a Hugging Face inference server |
| TLS | Transport Layer Security |
| UI | user interface |
| URL | web address |
| VEX | Vulnerability Exploitability eXchange |
| VPC | virtual private cloud |
| YAML | the text format of model-card metadata |

### 1.1 The repositories

Published models live in three model repositories: the Hugging Face Hub, Kaggle Models and ModelScope.
A producer that attaches its file to a GitHub release is using a package registry, which 1.2 covers.

An entry holds the files, a commit history, a model card, a licence field and, where the producer
declares it, the relation to a parent model: fine-tune, adapter, merge or quantisation. Three facts
about that relation carry through the report. It is declared by the producer and verified by no
repository examined [HF-14, KG-05, MS-04]. Many producers do not declare it, since no repository
requires it [HF-15]. And a derivative is a different model from its parent, so a verdict on the parent
does not carry to the child.

Table 1 records the four properties for each of the three. The guaranteed metadata column lists only the fields
the platform enforces or verifies; a field the publisher fills in freely is marked not guaranteed.

**Table 1. The model repositories: governance, controls, metadata and distribution.** All sources official
(the platform's own documentation and terms), accessed 6 October 2026; the identifiers resolve in section 3.

| Platform | Kind; hands over | Governance | Platform-side controls | Guaranteed metadata | Distribution mechanism |
|---|---|---|---|---|---|
| Hugging Face Hub | Model repository; a file (in possession). An endpoint (by proxy) sold beside it [HF-18] | Anyone 13+ or a legal entity may publish; the uploader is responsible [HF-01]. Content policy, graduated moderation, removal at discretion [HF-01, HF-02]. DMCA with counter-notice; public takedown log [HF-02, HF-04] | Malware scan (ClamAV) on every commit; pickle import scan; Protect AI and JFrog scans; all advisory [HF-05, HF-06, HF-07, HF-08]. Safetensors conversion on request [HF-10]. Optional signed commits [HF-11]. Gating with author approval, optional geo-restriction [HF-12] | SHA-256 per file; full commit history [HF-13, HF-16, HF-17]. Licence, parent relation and every card field publisher-filled, none mandatory, none verified: not guaranteed [HF-14, HF-15] | Library, CLI or git clone over HTTPS [HF-16, HF-17] |
| Kaggle Models | Model repository; a file (in possession) | Any registered user or organisation; one account each [KG-01, KG-02]. Community guidelines; human and automated moderation; removal without notice [KG-02, KG-03] | Gating behind an accepted agreement [KG-01]. Scanning, signing, conversion, review: not established [KG-02, KG-04] | Licence required, chosen from a fixed list; framework in every handle; numbered versions [KG-01, KG-05]. Parent relation publisher-filled, not verified: not guaranteed [KG-05]. Per-file digest: not established [KG-05] | kagglehub, CLI or a REST tar.gz; no git [KG-01, KG-06] |
| ModelScope | Model repository; a file (in possession) | Persons or entities, one account; PRC content law on the CN site; "not verified or approved" on the international site [MS-01, MS-02]. Takedown by written notice, counter-notice route [MS-01, MS-02] | Gating with a download agreement and approval [MS-04]. Scanning, signing, conversion, review: not established [MS-02, MS-05] | Licence a required field; git history; revision pinning [MS-04, MS-06]. Per-file SHA-256 only via the API (partial) [MS-07]. Parent relation publisher-filled, parsed into a lineage view, not verified: not guaranteed [MS-04]. Re-uploads of Hugging Face models carry ModelScope's own hashes; mirroring: not established [MS-04, MS-07] | CLI, SDK or git clone with LFS; CN endpoint by default [MS-06, MS-08] |

### 1.2 Distribution channels beyond the repositories

Between the repository and the organisation that runs a model sit redistributors, which repackage a
published model for a particular way of running it. What they hand over is either a file or a key: the
organisation then holds the model in possession, running it on an inference server it operates, or by
proxy, calling a provider's copy through an API. The licence is the same in both cases; what differs is
what the organisation can inspect, what it is accountable for and which tests it can run at all. The
line runs through platforms, not between them: Hugging Face hands out files and sells an API over them
[HF-18], NVIDIA ships containers and hosts endpoints for the same models [CG-13], and the cloud gardens
do both [CG-01, CG-04, CG-08].

Table 2 records the same four properties for the redistributors, one row per kind the glossary names,
and Table 3 opens the cloud-garden row into its four providers, whose controls differ more than any
other group's. Together AI stands for the hosted inference providers; Fireworks, Groq and OpenRouter,
named beside it in the foundation document, were not examined.

**Table 2. The redistributors: governance, controls, metadata and distribution.** All sources official (the
platform's own documentation and terms), accessed 6 October 2026, the TA and DK rows 8 October 2026; the identifiers
resolve in section 3.

| Platform | Kind; hands over | Governance | Platform-side controls | Guaranteed metadata | Distribution mechanism |
|---|---|---|---|---|---|
| Ollama library | Redistributor (package registry); a repackaged GGUF file pulled by a local inference server (in possession) | Any registered user, own namespace, registered key; curation of the official namespace not documented [OL-01, OL-03]. Terms: 18+, suspension; DMCA notice without counter-notice or log [OL-02] | Digest verified per layer on pull [OL-03]. Scanning, signing, conversion, review: not established [OL-09] | Content-addressed manifest and layer digests [OL-04]. Licence optional free text and parent only a comment in the Modelfile, no publisher identity beyond the namespace: not guaranteed [OL-05, OL-06] | ollama pull over HTTPS into a local store [OL-07] |
| GitHub releases | Redistributor (package registry); a file attached to a software release (in possession) | Repository write permission required [GH-01]. Terms and AUP; dual-use research allowed; removal a last resort [GH-02, GH-03]. DMCA with counter-notice; notices published [GH-04] | Opt-in immutable releases with a Sigstore attestation [GH-06]; opt-in build provenance [GH-07]. Scanning, conversion, review: not established [GH-10] | SHA-256 per asset since 2025-06-03 [GH-05]. Release bound to a tag; tags movable unless immutable [GH-01, GH-06]. Licence and parent relation: no model-specific field, nothing guaranteed [GH-10] | HTTPS download or the gh CLI; assets up to 2 GiB [GH-08, GH-09] |
| Docker Hub, ai namespace | Redistributor (package registry); a GGUF or safetensors file packaged as an OCI artefact, pulled by Docker Model Runner (in possession) [DK-01] | ai namespace published by Docker as verified publisher, 118 repositories [DK-02]; any account holder may push a model to a namespace or to the Hugging Face Hub [DK-03]. Terms effective 2026-08-26: 13+, removal at Docker's discretion, DMCA with counter-notice [DK-04] | Scanning, signing, review of model artefacts: not established [DK-01, DK-03] | Licence, parent relation, digests for model artefacts: not established [DK-01, DK-02] | docker model pull from Docker Hub, any OCI registry or the Hugging Face Hub into a local store [DK-01] |
| GitHub Models (retired) | Redistributor (hosted catalogue); an endpoint (by proxy), never a file [GH-12]. Retired 2026-07-30 [GH-11] | GitHub-curated catalogue of third-party models (Meta, Mistral, Azure OpenAI, Microsoft and others); no community publishing [GH-12]. Playground, catalogue, API and BYOK all retired 2026-07-30; migration to Microsoft Foundry or GitHub Copilot [GH-11] | No file handed over, so file scanning, signing and conversion do not arise. Content review of listed models: not established [GH-12] | Enforced fields: not established [GH-12] | OpenAI-compatible hosted endpoint (models.github.ai) under a GitHub token; BYOK option [GH-11, GH-12] |
| Together AI | Redistributor (hosted inference provider); an endpoint (by proxy). Only the customer's own fine-tune is downloadable [TA-05] | Together-curated serverless catalogue of third-party models (Meta, Qwen, DeepSeek, OpenAI, Google and others); community publishing: not established [TA-02]. Terms updated 2026-05-19: 13+, no resale, third-party models remain their owner's property [TA-03]. Deprecation with two to three weeks' notice by email, less for preview models [TA-01] | Custom upload accepts safetensors only and validates format, config and architecture against a supported base [TA-04]. Scanning, signing, review of catalogue models: not established [TA-02] | Removal date and migration target per deprecated model [TA-01]. Licence, parent relation, digests: not established [TA-02, TA-03] | Serverless API per token, or a dedicated endpoint; custom weights uploaded from a local machine, the Hugging Face Hub or S3 [TA-02, TA-04] |
| Cloud model gardens (Table 3) | Redistributor (model garden); a deployed copy (in possession) or an endpoint (by proxy) | Provider-curated; no community publishing | From no documented pre-listing scanning (AWS) to signed images and models with an SBOM (NVIDIA) | Versions and licence acceptance enforced in all four; digests, signing and SBOM only at NVIDIA; card content provider-filled | Deploy into the customer's account (in possession), or call a hosted endpoint (by proxy) |

**Table 3. The four cloud model gardens.** All sources official (provider documentation dated June to October 2026), accessed 6 October 2026; the identifiers resolve in section 3.

| Provider | Governance | Platform-side controls | Guaranteed metadata | Distribution mechanism |
|---|---|---|---|---|
| Google, Model Garden (Vertex AI now "Gemini Enterprise Agent Platform") | Google-curated; popular Hugging Face models added automatically; malware-flagged models removed; deprecation then retirement [CG-01, CG-02] | Hugging Face models blocked if "unsafe", flagged if "suspicious"; no guarantee against malicious code stated [CG-01]. Google-built serving containers, vulnerability-scanned [CG-01, CG-03] | Version in every identifier; EULA acceptance at deploy [CG-03]. Card content provider-filled: not guaranteed. Immutability, signing, SBOM: not established [CG-03] | Hosted endpoint (by proxy) or deployment into the customer's project (in possession); partner weights not exportable [CG-01, CG-03] |
| AWS, Amazon Bedrock, Bedrock Marketplace and SageMaker JumpStart | AWS-curated; lifecycle Active, Legacy, EOL; delistings on 2026-03-13 [CG-04, CG-05, CG-06] | Pre-listing scanning: not established [CG-04, CG-06]. Network isolation enforced; provider artefacts immutable [CG-04, CG-06]. Custom import requires safetensors [CG-07] | Lifecycle field; version pinning; EULA per channel [CG-04, CG-05, CG-06]. Card content provider-filled: not guaranteed. Signing, digests, SBOM: not established [CG-06] | Serverless endpoint (by proxy) or a SageMaker endpoint in the customer's account (in possession); weight download not stated (partial) [CG-04, CG-06, CG-07] |
| Microsoft, Foundry Models (Azure AI Foundry now "Microsoft Foundry") | Two tiers, Microsoft-evaluated or provider-validated; a Hugging Face collection; lifecycle ending in retirement [CG-08, CG-10] | New Foundry: mandatory malware scan, remote-code models disallowed, safetensors only, signed runtime containers [CG-09]. Classic: Hugging Face models "not tested or evaluated" [CG-08] | Versioned registry assets; GA weights fixed [CG-08, CG-10]. Card and licence tab provider-filled: not guaranteed. Digests or SBOM to customers: not established [CG-09] | Serverless endpoint (by proxy) or managed compute in the customer's subscription (in possession); weights not obtainable through the catalogue [CG-08, CG-09] |
| NVIDIA, NGC Catalog and NIM | NVIDIA-curated; partners through a programme with scanning and sign-off; branch lifecycle; takedown policy not stated [CG-11, CG-14] | Images scanned on a schedule and signed since 2023; models signed since 2025; NIM verifies checksums at start [CG-11, CG-12, CG-13]. NVIDIA converts and quantises upstream models [CG-13] | SBOM, VEX and scan results by image digest; terms accepted once per organisation [CG-11, CG-12, CG-13]. Upstream licence shown, not verified: not guaranteed [CG-13] | Signed container from nvcr.io, run anywhere (in possession); weights fetched at start from several stores; or hosted endpoints (by proxy) [CG-13] |

### 1.3 What the platform controls establish, and what they do not

Three findings follow from Table 1 to Table 3.

**The controls act on the file, not on the model's behaviour.** Malware scanning compares each file
with signatures of known malicious files; pickle scanning reads the instruction stream of a pickle
checkpoint without loading it and lists the imports it would make, since loading a pickle can execute
code [HF-05, HF-06]. Conversion changes the container the numbers sit in [HF-10, CG-13], and signing
establishes who published a file and that it has not changed since [HF-11, GH-06, CG-12]. No platform
examined claims more, and one states the limit: a supported model has been tested for deployability, with no guarantee of the
absence of vulnerabilities or malicious code [CG-01].

**Almost every control is advisory.** The malware and pickle scanning in Table 1, ClamAV and the pickle
import scan on the Hugging Face Hub with the Protect AI and JFrog scans beside them, produces warnings and
badges, and a flagged file remains downloadable [HF-05, HF-06, HF-07, HF-08]. The blocking controls all
sit at the redistribution layer, in Table 2 and Table 3: Google's Model Garden blocks deployment of models
the Hugging Face scans marked unsafe [CG-01]; the newer Microsoft Foundry path runs its own mandatory
malware scan, refuses models requiring remote code execution and enforces safetensors only [CG-09]; and
AWS custom import and Together AI custom upload accept safetensors only [CG-07, TA-04]. Each applies to
the copy that platform serves, not to the file where it was published. Three platforms lean on the Hub's
hygiene rather than their own: Kaggle surfaces Hub repositories as links [LD-13], Microsoft Foundry hosts
a Hub collection [LD-27], and Google decides on the Hub's scan verdicts [LD-28, CG-01], so a weakness
there is not contained to the Hub.

**Provenance is declared, not verified.** Every repository records a licence field and, where the
producer supplies it, a parent-model relation; none verifies either [HF-14, KG-05, MS-04]. No
redistributor in Table 2 adds what the repository lacks: the Ollama library carries the licence as
optional free text and the parent as a comment [OL-05], GitHub releases and Docker Hub have no
model-specific field [GH-10, DK-01], and Together AI states nothing [TA-02, TA-03]. Digests and
signatures establish that a file has not changed since publication, not that it is what its model card
claims.

## 2. The segmentation: model types against artefact formats

One segmentation, reused verbatim by every later matrix; every cell carries a dated source; frozen with
a version and a date after agreement with Dan (2.2). The axes and labels are the glossary's: of the six
types the item names, classification, embedding and generative are the rows; multimodal is the glossary's modality
qualifier on the generative row; quantised model and adapter are the glossary's file kinds, not types, and
appear in Table 6 only. A cell holds one of three values:

- **C, common.** A documented first-class path exists in an official source, and the format appears
  in at least one repository in twenty of that type on the Hugging Face Hub, measured as 5 per cent of
  the row's safetensors count.
- **P, possible but uncommon.** A documented path exists, but the share is below one in twenty or the
  path exists in one runtime family only.
- **–, not applicable.** No documented path.

The share is read from Table 5, the Hub's model search by task tag and library tag as at 6 October 2026
[TX-01]; the PyTorch tag marks repositories that carry pickle weights. The generative row is measured
on text-generation, the embedding row on both of its tags, the modality qualifier on image-text-to-text
and the precision qualifier on the 4-bit tag across all tasks.

**Table 4. The segmentation: model type against artefact format.** Row and column terms as the glossary
defines them; modality is the glossary's qualifier on the generative row. C, P and – as defined above; the
evidence for every row is in Table 6. Proposed, pending agreement with Dan.

| Model type | pickle checkpoint | safetensors | GGUF | ONNX |
|---|---|---|---|---|
| classification model | C | C | P | P |
| embedding model | C | C | P | C |
| generative model | C | C | C | P |
| qualifier: modality on the generative row, image and text input | C | C | C | P |

**Table 5. Hugging Face Hub repositories by task tag and library tag.** Counts as at 6 October 2026
[TX-01].

| Task tag | safetensors | PyTorch (pickle) | GGUF | ONNX |
|---|---|---|---|---|
| text-generation | 328,892 | 56,780 | 39,152 | 2,310 |
| text-classification | 76,892 | 39,688 | 424 | 1,644 |
| feature-extraction | 11,532 | 7,402 | 696 | 1,033 |
| sentence-similarity | 16,192 | 3,204 | 530 | 980 |
| image-text-to-text | 32,525 | 2,399 | 5,765 | 235 |
| 4-bit, all tasks | 47,666 | 3,013 | – | 96 |

### 2.1 The evidence per cell

**Table 6. Evidence per cell, in the shape of Table 4.** Each cell gives the value, the share (the format's
count as a fraction of the row's safetensors count in Table 5; "base" marks the denominator itself), the
documented path, and the sources. The last two rows evidence the glossary's two file kinds, quantised
model and adapter, which are not model types and so are not rows of Table 4. Access date 6 October 2026.

| Row of Table 4 | pickle checkpoint | safetensors | GGUF | ONNX |
|---|---|---|---|---|
| classification model | **C** 52 %. PyTorch default for the older classifier population [TX-01, TX-03] | **C** base. Transformers default since 4.35 [TX-01, TX-04] | **P** 0.6 %. Rerankers and small heads; llama.cpp serves rerankers [TX-01, TX-13] | **P** 2.1 %. Export through Optimum and Transformers.js; below one in twenty [TX-01, TX-08] |
| embedding model | **C** 64 % and 20 % on the two tags [TX-01, TX-03] | **C** base [TX-01, TX-04] | **P** 6 % and 3 %. llama.cpp embedding endpoint; one tag above the threshold, one below [TX-01, TX-13] | **C** 9 % and 6 %. sentence-transformers ONNX backend with quantised variants [TX-01, TX-08] |
| generative model | **C** 17 %. PyTorch default, trend away: safetensors the Transformers default since 4.35, pickle saving deprecated, weights-only loading since PyTorch 2.6. In circulation, not produced [TX-01, TX-03, TX-04] | **C** base. Transformers default [TX-01, TX-04, TX-05] | **C** 12 %. The local-inference distribution: Ollama, llama.cpp, Docker Model Runner [TX-01, TX-07, TX-11] | **P** 0.7 %. ONNX Runtime GenAI runs the major families [TX-01, TX-09] |
| modality, on the generative row: image and text input | **C** 7 % [TX-01] | **C** base [TX-01] | **C** 18 %, above the text-only share; the artefact is two files, model and projector [TX-01, TX-06, TX-13] | **P** 0.7 %. ONNX Runtime GenAI vision models [TX-01, TX-09] |
| quantised model: precision, on the columns | **P** 6 % of 4-bit repositories. Pickle path version-gated in bitsandbytes [TX-01, TX-15] | **C** 94 % of 4-bit repositories. Every method Transformers can serialise saves safetensors [TX-01, TX-15] | **C** Quantisation is the normal state of a GGUF file; tensor types in the specification; Ollama's default pull is 4-bit [TX-06, TX-07] | **P** 0.2 % of 4-bit repositories, a lower bound: int4 and int8 ONNX exist but rarely carry the tag [TX-01, TX-08, TX-09] |
| adapter: completeness, on the file | **C** share not measured. PEFT saves a pickle adapter as the alternative to safetensors, interchangeably [TX-14] | **C** PEFT default [TX-14] | **P** no Hub count. llama.cpp converts a PEFT adapter to the GGUF adapter file type and loads it beside the model [TX-06, TX-13] | **P** no Hub count. ONNX Runtime GenAI loads adapters converted to its own file type [TX-09] |

### 2.2 To settle with Dan at the freeze

1. **The rule.** Accept or amend the C and P definitions above, the one-in-twenty threshold and the
   safetensors denominator. Four cells sit within a factor of two of the threshold and would move if it
   moved: classification × ONNX at 2.1 per cent, embedding × GGUF at 6 and 3 per cent, precision ×
   pickle at 6 per cent, and the modality pickle share at 7 per cent.
2. **The pickle column.** Whether the frozen table carries a marker that C in this column means in
   circulation and not in production, given the evidence in the generative × pickle row of Table 6.
3. **The modality qualifier.** Whether image-and-text input stays a qualifier row, as proposed, or
   becomes a model type of its own in the frozen table because its GGUF artefact is two files, which changes
   what a scan or a hash covers.
4. **The generative row.** Whether it needs a base-only count. The Hub shows a base-only toggle but
   exposes no URL parameter for it, so no count is obtainable and the row covers base and instruct
   together [TX-16].

Once these are agreed, Table 4 is frozen with a version and a date, and every later matrix takes its row
and column labels verbatim.

## 3. Source log

Every claim in sections 1 and 2 resolves to a row in this section. Every row is class Official under the
citation policy, the platform, producer or specification owner writing about its own artefact or
service, except the two marked none, which record the searches made for a property no page states.
Access date 6 October 2026 throughout, the date the landscape was frozen, except the TA and DK rows,
accessed 8 October 2026. Tags: [CHECKED] the page states the claim; [PARTIAL] implied but not stated, with the gap named;
[NOT ESTABLISHED] no page states it after the searches named.

Method note. Several platform pages are JavaScript applications that return only a shell to a plain
fetch; those were rendered through a headless-render proxy at the same address, and where a list was
collapsed in the rendering it was read from the page's own embedded data. Where huggingface.co
rate-limited, the same documentation files were read from their public source repository. Counts drawn
from live catalogue pages are quoted as at the access date and will drift.

### 3.1 Platforms (Table 1 to Table 3): HF, KG, MS, OL, GH, TA, DK, CG

| ID | Source | URL | Date or version on page | Verified |
|---|---|---|---|---|
| HF-01 | Terms of Service; Hugging Face | https://huggingface.co/terms-of-service | Effective 2022-09-15 | [CHECKED] account open to natural persons 13+ or registered legal entities; publisher solely responsible for content; removal and termination at sole discretion; DMCA notices to dmca@huggingface.co; New York law and venue |
| HF-02 | Content Policy; Hugging Face | https://huggingface.co/content-policy (final URL of /content-guidelines) | Effective 2025-04-10 | [CHECKED] five prohibited categories incl. malware; Report button and safety@huggingface.co; graduated moderation actions (edit request, unranking, NFAA tag, removal, restriction, suspension); DMCA review, uploader informed and content disabled, counter-notification, 14 U.S. business days before restoration; appeals to safety@huggingface.co |
| HF-04 | huggingface-legal/takedown-notices (dataset); Hugging Face | https://huggingface.co/datasets/huggingface-legal/takedown-notices | entries 2022-06 to 2026-09 | [CHECKED] public log of takedown notices received |
| HF-05 | Malware Scanning; Hugging Face | https://huggingface.co/docs/hub/security-malware | no date shown | [CHECKED] every file scanned with ClamAV at each commit; unsafe file produces a warning and advice to remove; no blocking statement |
| HF-06 | Pickle Scanning; Hugging Face | https://huggingface.co/docs/hub/security-pickle | no date shown | [CHECKED] pickle import scan on every pickled upload via pickletools.genops; suspicious imports highlighted; disclaimer "not 100% foolproof", best-effort lists; GPG signing guarantees origin, not safety |
| HF-07 | Third-party scanner: Protect AI; Hugging Face | https://huggingface.co/docs/hub/security-protectai | no date shown | [CHECKED] Guardian scans public repositories' files; results shown on the Hub |
| HF-08 | Third-party scanner: JFrog; blog "Hugging Face and JFrog partner…"; Hugging Face | https://huggingface.co/docs/hub/security-jfrog ; https://huggingface.co/blog/jfrog | blog 2025-03-04 | [CHECKED] all public model repos scanned by JFrog on push; results exposed in the UI; no blocking statement |
| HF-10 | Convert weights to safetensors; Safetensors; Model(s) Release Checklist; Hugging Face | https://huggingface.co/docs/safetensors/convert-weights ; https://huggingface.co/docs/safetensors/index ; https://huggingface.co/docs/hub/model-release-checklist | no date shown | [CHECKED] Convert Space downloads pickled weights, converts, opens a Pull Request (owner merges); "prefer safetensors over pickle". /docs/hub/safetensors returns 404; bot account name not on any docs page |
| HF-11 | Signing commits with GPG; Hugging Face | https://huggingface.co/docs/hub/security-gpg | no date shown | [CHECKED] optional; Verified only when the public key is on the account and e-mail matches; unsigned commits have no status |
| HF-12 | Gated models; Hugging Face | https://huggingface.co/docs/hub/models-gated | no date shown | [CHECKED] gated download requires login and sharing username/e-mail; automatic or manual approval; author can revoke without notice; optional IP-based geo-restriction; licence acceptance implemented through the gating prompt (extra_gated_prompt) |
| HF-13 | Hub OpenAPI (openapi.md); Hugging Face | https://huggingface.co/.well-known/openapi.md | no date shown | [CHECKED] GET /api/models/{ns}/{repo}/scan returns security status; tree listing with expand returns scanner metadata; commit files schema requires sha256 and xetHash |
| HF-14 | Model Cards; Licenses; Hugging Face | https://huggingface.co/docs/hub/model-cards ; https://huggingface.co/docs/hub/repositories-licenses | no date shown | [CHECKED] license, base_model, pipeline_tag, library_name, datasets are machine-read (filters, licence display, widgets, model tree) but author-supplied; license uses a controlled identifier list; pipeline_tag validated by the metadata UI; base_model relation type inferred (adapter/merge/quantized/finetune); NO statement that the relation is verified → [NOT ESTABLISHED] for verification |
| HF-15 | Getting Started with Repositories; Hugging Face | https://huggingface.co/docs/hub/repositories-getting-started | no date shown | [CHECKED] licence field may be left blank; model card is best practice, not required; full commit history with diffs |
| HF-16 | Xet overview; Backward compatibility with LFS; Xet security; Storage backends; Using Xet; Hugging Face | https://huggingface.co/docs/hub/xet/overview ; https://huggingface.co/docs/hub/xet/legacy-git-lfs ; https://huggingface.co/docs/hub/xet/security ; https://huggingface.co/docs/hub/storage-backends ; https://huggingface.co/docs/hub/xet/using-xet-storage | no date shown | [CHECKED] LFS pointer carries SHA-256 of contents; Xet keeps the LFS pointer format and adds a Xet hash; Xet is the storage backend with an LFS bridge for legacy clients; chunk access bound to repository permissions |
| HF-17 | Download files from the Hub (huggingface_hub v2.1.1); Downloading models; Hugging Face | https://huggingface.co/docs/huggingface_hub/guides/download ; https://huggingface.co/docs/hub/models-downloading | library v2.1.1 shown | [CHECKED] huggingface_hub, hf CLI (hf download), git clone with git-xet + git-lfs; pin to full commit hash; file contents served from separate CDN/Xet hostnames |
| HF-18 | Inference Endpoints; About Inference Endpoints; Hugging Face | https://huggingface.co/docs/inference-endpoints ; https://huggingface.co/docs/inference-endpoints/about | no date shown | [CHECKED] managed hosted API; weights pulled from the Hub into a container; user receives an API, not a file |
| KG-01 | Models Documentation; Kaggle | https://www.kaggle.com/docs/models | no date shown | [CHECKED] any user or Organization profile publishes via UI, kagglehub or CLI; Hugging Face model pages auto-created when a notebook uses them; gated models require accepting an agreement (status banner, only "accepted" can download), Kaggle credentials needed for such downloads; handle = owner/model/framework/variation/version, framework enumerated; licence selected in the upload flow; download via kagglehub, kaggle CLI or REST URL returning tar.gz |
| KG-02 | Terms of Use; Kaggle | https://www.kaggle.com/terms | no date in rendered text | [CHECKED] one account per user; minors need parental consent; IP complaints via Google's report-content troubleshooter, repeat infringers may be suspended; content removable without notice; no endorsement, no warranty on content (→ [PARTIAL] for "no pre-publication review") |
| KG-03 | Kaggle Community Guidelines; Kaggle | https://www.kaggle.com/community-guidelines | "Updated March 4, 2026" | [CHECKED] models must not be plagiarised or misrepresent their source licence; NSFW, spam, misinformation, IP-infringing content removed; moderation by people and machine learning; report option on model pages; removal, suspension, ban, law-enforcement referral; appeal path and EU DSA out-of-court option |
| KG-04 | Acceptable Use Policy; Kaggle | https://www.kaggle.com/aup | "Version June 22, 2025" | [PARTIAL] prohibits distributing viruses, Trojan horses, corrupted files; policy only, no scanning statement → scanning, signing, conversion [NOT ESTABLISHED] |
| KG-05 | kaggle-cli docs: models_metadata.md; model_variations_versions.md; Kaggle (GitHub) | https://raw.githubusercontent.com/Kaggle/kaggle-cli/main/docs/models_metadata.md ; https://raw.githubusercontent.com/Kaggle/kaggle-cli/main/docs/model_variations_versions.md | no date shown | [CHECKED] licenseName chosen from a fixed list (Apache 2.0, MIT, GPL 3, CC variants…); modelInstanceType, baseModelInstance, externalBaseModelUrl, provenanceSources self-declared; each upload creates a numbered version, previous versions remain downloadable; files listing has no hash field → file hashes [NOT ESTABLISHED]; licence and parent verification [NOT ESTABLISHED] |
| KG-06 | kagglehub README; Kaggle (GitHub) | https://github.com/Kaggle/kagglehub | no version shown | [CHECKED] kagglehub.model_download; licence optional on upload; authentication only for consent-gated or private resources |
| MS-01 | Terms and Conditions (CN site, served in English); ModelScope (Alibaba, with CCF) | https://modelscope.cn/protocol/Terms-and-Condition | updated 2025-08-20, effective 2025-08-27 | [CHECKED] registration by natural persons or legal entities with full civil capacity, not under sanctions, one account, mobile-phone registration with SMS verification (nationality of the number not stated → [PARTIAL]); PRC-law content prohibitions; downloaders bound by each model's Custom License; platform may review content "through technical or manual methods" and delete; accounts frozen on evidenced complaints; written infringement notice with identity, proof of rights, URLs, truthfulness statement; notice forwarded to uploader, removal "as appropriate", counter-notice route |
| MS-02 | Terms and Conditions (international site); Alibaba Cloud (Singapore) Pte Ltd | https://www.modelscope.ai/protocol/Terms-and-Condition | "Last updated: August 21, 2025" | [CHECKED] under-18s barred; "User Content is not verified or approved by us. We do not assume any obligation to remove, validate, screen, verify or edit any User Content"; removal at discretion with or without notice; Singapore Copyright Act 2021 notice to a dedicated e-mail |
| MS-04 | Models intro; Model card; Overview; Quick Start; ModelScope | https://www.modelscope.ai/docs/models/intro ; https://www.modelscope.ai/docs/models/model-card ; https://www.modelscope.ai/docs/overview ; https://modelscope.ai/docs/intro/quickstart | docs build 2026-09-01 | [CHECKED] account needed to create a model; public models downloadable by all; "application-based" models require accepting a download agreement and sharing e-mail/username, optional extra_gated_* fields, manual or automatic approval; licence is a required form choice, create_model defaults to Apache-2.0 if omitted; README YAML fields license, frameworks, base_model, base_model_relation (adapter/merge/quantized/finetune, may be inferred by the platform), new_version, datasets parsed for filtering and lineage; repos Git-backed; verification of licence or base_model [NOT ESTABLISHED]; launched November 2022 by Alibaba with the CCF Open Source Development Technical Committee; Transformers/Diffusers loading compatibility (no mirroring statement) |
| MS-05 | Model upload; ModelScope | https://modelscope.cn/docs/models/upload | docs build 2026-09-01 | [PARTIAL] files over 5 MB or with weight extensions (.bin, .pt, .pth, .safetensors, .ckpt, .gguf…) auto-routed to Git LFS; upload API hashes files (buffer_size_mb); versions advised; no scanning, signing, conversion or review statement → [NOT ESTABLISHED] |
| MS-06 | Model download (CN and international copies); ModelScope | https://modelscope.cn/docs/models/download ; https://www.modelscope.ai/docs/models/download | docs build 2026-09-01 | [CHECKED] three channels: modelscope download CLI, Python SDK (snapshot_download, model_file_download, from_pretrained), git clone with Git LFS; revision pinning (branch or tag), default = last version before the library release; cache ~/.cache/modelscope/hub; login/token only for private or application-gated models; default endpoint modelscope.cn, MODELSCOPE_DOMAIN=www.modelscope.ai for the international site |
| MS-07 | repo files API; model API (AI-ModelScope/bert-base-uncased; Qwen/Qwen2.5-0.5B-Instruct); AI-ModelScope organisation page; ModelScope | https://www.modelscope.cn/api/v1/models/Qwen/Qwen2.5-0.5B-Instruct/repo/files?Revision=master ; https://www.modelscope.cn/api/v1/models/AI-ModelScope/bert-base-uncased ; https://www.modelscope.cn/organization/AI-ModelScope | 2026-10-06 | [PARTIAL] per-file Sha256, Size, IsLFS, commit message and committer returned by the API; no documentation page promises hashes or client-side verification; AI-ModelScope organisation holds 1,997 models reproducing HF model cards, commits "Upload folder using huggingface_hub" by ai-modelscope, ModelSource "USER_UPLOAD"; no documented mirroring or syncing process → [NOT ESTABLISHED]; hash/metadata preservation across platforms [NOT ESTABLISHED] |
| MS-08 | modelscope/modelscope README; ModelScope (GitHub) | https://github.com/modelscope/modelscope | no date shown | [CHECKED] "Most models on ModelScope are public and can be downloaded directly from the website" |
| OL-01 | Importing a Model; Ollama Inc. | https://docs.ollama.com/import (old github docs/import.md is 404) | no date shown | [CHECKED] any registered user publishes under their own namespace after registering a public key, via ollama push; GGUF taken as-is, no re-quantisation on import; Safetensors import for supported architectures |
| OL-02 | Terms of Service; Ollama Inc. | https://ollama.com/terms | "Last updated: May 2026" | [CHECKED] users 18+; prohibited unlawful, infringing, harmful content; suspension or termination; copyright/trademark notice to hello@ollama.com per 17 U.S.C. §512(c)(3); repeat-infringer policy; no counter-notice procedure or transparency log published |
| OL-03 | docs/api.md (Push a Model; Pull a Model); ollama/ollama repository | https://raw.githubusercontent.com/ollama/ollama/main/docs/api.md | no date shown | [CHECKED] push requires an ollama.com account plus a registered public key; pull streams "pulling manifest", "pulling <digest>", "verifying sha256 digest", "writing manifest"; behaviour on mismatch not stated → [PARTIAL]; consumer-side signature verification not described → [NOT ESTABLISHED] |
| OL-04 | registry manifest, library/llama3.2:latest (primary artefact); Ollama Inc. registry | https://registry.ollama.ai/v2/library/llama3.2/manifests/latest | no date shown | [CHECKED] Docker distribution v2 manifest; layers content-addressed by sha256 with mediaTypes application/vnd.ollama.image.{model,template,license,params} |
| OL-05 | Modelfile Reference; Show model details; Ollama Inc. | https://docs.ollama.com/modelfile ; https://docs.ollama.com/api-reference/show-model-details | no date shown | [CHECKED] Modelfile records FROM, PARAMETER, TEMPLATE, SYSTEM and optional free-text LICENSE; shown Modelfile keeps the parent as a comment and FROM points to a local sha256 blob; show API has details.parent_model, empty for base models → [PARTIAL] for parent recording |
| OL-06 | llama3.2:latest library page; Ollama Inc. | https://ollama.com/library/llama3.2:latest | "Updated 2 years ago" | [CHECKED] tag page lists content-addressed layers with digest prefixes and sizes, arch/parameters/quantisation, licence layer names; no publisher identity beyond the namespace |
| OL-07 | CLI Reference; FAQ; API pull; API push; Ollama Inc. | https://docs.ollama.com/cli ; https://docs.ollama.com/faq ; https://docs.ollama.com/api/pull ; https://docs.ollama.com/api/push | no date shown | [CHECKED] ollama pull over HTTPS only into a local blob store; POST /api/pull and /api/push with an insecure flag for non-TLS registries |
| OL-09 | none; searched: docs.ollama.com (import, cli, faq, api, llms.txt), ollama.com/terms, ollama.com/library, GitHub README | — | — | [NOT ESTABLISHED] no documented malware, content or licence scanning or review of pushed models |
| GH-01 | About releases; GitHub | https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases | no date shown | [CHECKED] only users with write permission manage releases; releases bound to Git tags; automatic zip/tarball of the repository at the tag; each asset under 2 GiB; up to 1000 assets; no total-size or bandwidth cap |
| GH-02 | GitHub Terms of Service; GitHub | https://docs.github.com/en/site-policy/github-terms/github-terms-of-service | "Effective: April 27, 2026" | [CHECKED] human accounts 13+; GitHub may refuse or remove content violating law or policy |
| GH-03 | GitHub Acceptable Use Policies; Active Malware or Exploits; GitHub | https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies ; https://docs.github.com/en/site-policy/acceptable-use-policies/github-active-malware-or-exploits | no date shown | [CHECKED] bans unlawful content and direct support of active attack or malware campaigns; dual-use security research content explicitly allowed; removal as last resort; suspension, termination or removal at GitHub's discretion |
| GH-04 | DMCA Takedown Policy; GitHub | https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy | no date shown | [CHECKED] notice processed by GitHub; about 1 business day to fix; counter-notice; forks not automatically disabled; redacted notices published at github/dmca |
| GH-05 | Releases now expose digests for release assets (changelog); REST API endpoints for release assets; GitHub | https://github.blog/changelog/2025-06-03-releases-now-expose-digests-for-release-assets/ ; https://docs.github.com/en/rest/releases/assets | 2025-06-03 | [CHECKED] SHA-256 digest computed at upload for every release asset, immutable, shown in UI, REST (field digest, string or null), GraphQL and gh CLI |
| GH-06 | Immutable releases (concept); Immutable releases are now generally available (changelog); gh release verify; gh release verify-asset; Managing releases in a repository; GitHub | https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases ; https://github.blog/changelog/2025-10-28-immutable-releases-are-now-generally-available/ ; https://cli.github.com/manual/gh_release_verify ; https://cli.github.com/manual/gh_release_verify-asset ; https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository | GA 2025-10-28 | [CHECKED] opt-in per repository or organisation; assets and tag locked after publication; Sigstore-format release attestation over tag, commit SHA and asset digests; verified with gh release verify / verify-asset |
| GH-07 | Artifact attestations (concept); Using artifact attestations to establish provenance for builds; GitHub | https://docs.github.com/en/actions/concepts/security/artifact-attestations ; https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds | no date shown | [CHECKED] opt-in Sigstore build provenance, SLSA v1.0 Build L2 (L3 with reusable workflows); verified with gh attestation verify; "not a guarantee that an artifact is secure" |
| GH-08 | About large files on GitHub; About Git Large File Storage; Git LFS billing; GitHub | https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github ; https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage ; https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-git-large-file-storage/about-billing-for-git-large-file-storage | no date shown | [CHECKED] git blocks files over 100 MiB; LFS per-file 2 GB Free/Pro, 4 GB Team, 5 GB Enterprise Cloud; 10 GiB free LFS storage and bandwidth; large binaries steered to releases; the asset cap on this page is tied to the LFS plan limit (differs from GH-01's flat 2 GiB) |
| GH-09 | gh release download; GitHub CLI manual | https://cli.github.com/manual/gh_release_download | no date shown | [CHECKED] assets downloaded by direct HTTPS or gh release download with --pattern / --archive |
| GH-10 | none; searched: docs.github.com AUP and malware pages, REST release assets, web search | — | — | [NOT ESTABLISHED] no documented malware or antivirus scanning of release assets; no model-specific metadata (licence, base model) guaranteed for assets |
| GH-11 | GitHub Models (retirement notice); changelog 2026-07-01 "GitHub Models is being fully retired on July 30, 2026"; changelog 2026-07-30 "GitHub Models is now retired"; GitHub | https://docs.github.com/en/github-models ; https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026/ ; https://github.blog/changelog/2026-07-30-github-models-is-now-retired/ | 2026-07-30 | [CHECKED] playground, model catalogue, inference API and BYOK fully retired 2026-07-30; migration path Microsoft Foundry or GitHub Copilot |
| GH-12 | Solving the inference problem for open source AI projects with GitHub Models (blog, 2025-07-23); Deprecation of Azure endpoint for GitHub Models (changelog 2025-07-17); Introducing GitHub Models (blog 2024-08-01); GitHub | https://github.blog/ai-and-ml/llms/solving-the-inference-problem-for-open-source-ai-projects-with-github-models/ ; https://github.blog/changelog/2025-07-17-deprecation-of-azure-endpoint-for-github-models/ ; https://github.blog/news-insights/product-news/introducing-github-models/ | 2025-07-23; 2025-07-17; 2024-08-01 | [CHECKED] while live it exposed a hosted OpenAI-compatible endpoint (models.github.ai) under a GitHub token; models from Meta, Mistral, Azure OpenAI Service, Microsoft and others; "never distributed weights" by absence → [PARTIAL] |
| TA-01 | Deprecations (model deprecation policy and schedule); Together AI | https://docs.together.ai/docs/deprecations | removal dates listed, latest 2026-09-14 | [CHECKED] two to three weeks' notice for serverless and on-demand dedicated endpoints, under 24 hours for preview models after 30 days; email to affected users; removal date and migration target per model; nothing on handing over weights |
| TA-02 | Serverless models (catalogue); Together AI | https://docs.together.ai/docs/serverless-models | no date shown | [CHECKED] serverless catalogue of third-party models from Meta, Qwen, DeepSeek, Minimax, Moonshot, Z.ai, OpenAI, Google, Black Forest Labs, ByteDance, Stability AI; per-token, no provisioning; dedicated inference a separate catalogue; curation and community publishing not stated → [PARTIAL] |
| TA-03 | Terms of Service; Together AI | https://www.together.ai/terms-of-service | updated 2026-05-19 | [CHECKED] 13+; no resale or redistribution; "All Third-Party Models remain the intellectual property of their respective third-party provider"; services subject to modification; zero data retention optional; weight download not addressed |
| TA-04 | Custom models (upload); Together AI | https://docs.together.ai/docs/custom-models | no date shown | [CHECKED] upload from local machine, Hugging Face Hub or S3 presigned URL; "Only safetensors format is supported. Models with only .bin or .pt files fail validation"; validation of config and architecture against a supported base; private by default |
| TA-05 | Fine-tuning overview; Together AI | https://docs.together.ai/docs/fine-tuning-overview | no date shown | [PARTIAL] "Serve your fine-tuned model on a dedicated endpoint or download it for local use"; format of the download not stated on the page |
| DK-01 | Docker Model Runner (overview); Docker | https://docs.docker.com/ai/model-runner/ | no date shown | [CHECKED] pulls models from Docker Hub, any OCI-compliant registry or Hugging Face into a local store; packages GGUF and safetensors files as OCI artefacts; signing, scanning, digests and licence handling not stated |
| DK-02 | Docker Hub, ai namespace; Docker | https://hub.docker.com/u/ai | relative update times only | [CHECKED] 118 repositories published by Docker as Verified Publisher; no licence shown on the listing |
| DK-03 | docker model push (CLI reference); Docker | https://docs.docker.com/reference/cli/docker/model/push/ | no date shown | [PARTIAL] "Push a model to Docker Hub or Hugging Face"; namespaces, packaging, digests and metadata fields not stated |
| DK-04 | Docker Terms of Service; Docker | https://www.docker.com/legal/docker-terms-service/ | effective 2026-08-26 | [CHECKED] 13+ with parental consent under 18; Docker may refuse, remove or disable user content it reasonably believes violates the terms or poses risk; DMCA agent and counter-notification; OCI artefacts not addressed separately |
| CG-01 | Overview of Model Garden; Use Hugging Face Models; Overview of self-deployed models (Model Garden on Gemini Enterprise Agent Platform, the renamed Vertex AI); Google Cloud | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-hugging-face-models ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/self-deployed-models | last updated 2026-10-05 | [CHECKED] Google-curated: models from Google and partners; popular Hugging Face models added automatically by Google; partner proprietary models via Cloud Marketplace; models flagged as malware removed immediately; Google vulnerability-scans its serving containers; partner checkpoints get authenticity scans; HF models scanned by HF and its third-party scanner, "unsafe" blocked from deployment, "suspicious" or remote-code flagged but still deployable; daily HF malware scan; "we don't guarantee the absence of vulnerabilities or malicious code"; "verified by Google" = deployment settings, not weights; licence compliance is the user's; self-deployment runs in the customer's project and VPC |
| CG-02 | Open model deprecations; Control access to Model Garden models; Google Cloud | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/open-models ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/control-model-access | last updated 2026-10-05 | [CHECKED] deprecation then retirement (endpoint deactivated); preview open models available at least 45 days; organisation policy allow-lists models |
| CG-03 | Open models overview (choose serving option); Deploy open models from Model Garden; Deploy models with custom weights (Preview); Google Cloud | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/choose-serving-option ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/deploy-model-garden ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/deploy-models-with-custom-weights | last updated 2026-10-05 | [CHECKED] / [PARTIAL] Google-optimised prebuilt containers (vLLM, Hex-LLM, SGLang, TGI, TensorRT-LLM); provider-prepared variants such as an FP8 Llama 3.3 (who converted not stated → PARTIAL); models addressed as publisher/model@version and containers by dated tag, no digest or immutability guarantee stated (PARTIAL); accept_eula=True at deploy; custom weights in Hugging Face format from Cloud Storage; partner-model weights cannot be exported; no signing, digest or SBOM statement → [NOT ESTABLISHED] |
| CG-04 | Overview - Amazon Bedrock; Amazon Bedrock Marketplace; Subscribe to a model; Deploy a model; Bring your own endpoint; End-to-end workflow; Request access to models; AWS | https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html (the older bedrock-marketplace.html redirects to the guide root) ; …/bedrock-marketplace-subscribe-to-a-model.html ; …/bedrock-marketplace-deploy-a-model.html ; …/bedrock-marketplace-bring-your-own-endpoint.html ; …/bedrock-marketplace-end-to-end-workflow.html ; …/model-access.html | no date shown | [CHECKED] AWS-curated; Marketplace: 100+ third-party models, public or proprietary, subscription accepts provider prices and EULAs; AcceptEula flag; first invocation of a serverless third-party model = EULA agreement; Marketplace models deploy to a SageMaker endpoint in the customer's account (VPC, KMS, IAM) and are called through Bedrock APIs; registration checks compatibility and requires network isolation; "a HuggingFace model" is a public model needing no subscription; no pre-listing scanning statement → [NOT ESTABLISHED] |
| CG-05 | Model lifecycle (and legacy policy) - Amazon Bedrock; AWS | https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html ; …/model-lifecycle-legacy.html | applies to models launched on/after 2026-09-07; legacy: at least 12 months on Bedrock | [CHECKED] Active, Legacy (6 months or 45 days), EOL (removed from all Regions); model card states the EOL policy; modelLifecycle API field |
| CG-06 | SageMaker JumpStart pretrained models; JumpStart Foundation Models; Model sources and license agreements; Deploy a Model; ModelBuilder class; Use your JumpStart models in Bedrock; HubContentDocument schema; JumpStart marketing page; AWS | https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html ; …/jumpstart-foundation-models.html ; …/jumpstart-foundation-models-choose.html ; …/jumpstart-deploy.html ; …/jumpstart-foundation-models-use-python-sdk-model-class.html ; …/jumpstart-foundation-models-use-studio-updated-register-bedrock.html ; …/hub-content-document-schema.html ; https://aws.amazon.com/sagemaker/jumpstart/ | delisting notice dated 2026-03-13 | [CHECKED] JumpStart "onboards and maintains" public models from third-party sources under the source's licence plus proprietary ones; delisted some models 2026-03-13, existing endpoints keep working, licence info for delisted open-weight models "refer to the Hugging Face listing"; accept_eula default False, must be set True; all JumpStart models run in network isolation; artefacts served from the AWS-managed bucket jumpstart-cache-prod-<region>; model_version pinning; semantic version in the hub-content ARN; model IDs prefixed huggingface-; whether catalogue weights may be downloaded not stated → [PARTIAL]; no signing, digest or SBOM statement → [NOT ESTABLISHED] |
| CG-07 | Use Custom model import to import a customized open-source model into Amazon Bedrock; AWS | https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html | no date shown | [CHECKED] import from the customer's S3 in Hugging Face safetensors format; Bedrock detects the architecture, pins transformers 4.51.3, overrides Llama 3 rope_scaling; licence compliance is the customer's |
| CG-08 | Microsoft Foundry Models overview (classic); Foundry Models from partners and community; Deploy models with managed compute (classic); Deploy Hugging Face Hub models in Microsoft Foundry (classic); Microsoft Learn | https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/foundry-models-overview ; https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-from-partners ; https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/deploy-models-managed ; https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/deploy-models-managed-hugging-face | ms.date 2026-07-28; 2026-09-21; 2026-01-22; 2026-05-14 | [CHECKED] two tiers: "sold by Azure" (Microsoft evaluates, internal Responsible AI review) vs "partners and community" (validated by providers themselves); Hugging Face maintains its own collection; customers can only request additions; model card with License tab; partner licences and billing via Azure Marketplace; registry asset IDs with versions (azureml://registries/…/versions/N); versionUpgradeOption; classic: weights download from Hugging Face Hub to the endpoint at deploy time, not hosted on Azure, not usable as job inputs; models needing trust_remote_code "aren't supported for security reasons"; "Non-Microsoft Products that aren't tested or evaluated by Microsoft" |
| CG-09 | Hugging Face models in Microsoft Foundry (preview); Managed compute in Microsoft Foundry (preview); Microsoft Learn | https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/hugging-face-models ; https://learn.microsoft.com/en-us/azure/foundry/concepts/managed-compute-overview | ms.date 2026-06-16 (updated 2026-09-28); 2026-06-01 (updated 2026-09-28) | [CHECKED] new Foundry: mandatory malware scanning, trust_remote_code disallowed unless HF-verified or trusted org, Safetensors-only, runtime validation; runtime containers built, CVE-scanned and signed by Microsoft; deployment templates pin runtime and quantisation; weights "pulled from Hugging Face once, validated, and stored in Microsoft-managed Azure storage"; dedicated Microsoft-owned GPU capacity, no egress needed; gated HF models not available (use classic); upstream licence metadata preserved; no digest or SBOM statement → [NOT ESTABLISHED] |
| CG-10 | Foundry Models lifecycle and support policy; Model retirement schedule; Microsoft Learn | https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements ; https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule | ms.date 2026-07-24; 2026-09-21 | [CHECKED] Preview, GA, Legacy, Deprecated, Retired (410 Gone); GA retirement set at launch (18 months; 12 for Anthropic, DeepSeek, Fireworks, Mistral); emergency retirement for security or compliance issues; GA weights and APIs fixed |
| CG-11 | NGC Catalog User Guide; Join the NGC Software Partner Network; NVIDIA | https://docs.nvidia.com/ngc/latest/ngc-catalog-user-guide.html ; https://www.nvidia.com/en-us/gpu-cloud/ngc-software-partners/ | no date shown (version selector) | [CHECKED] NVIDIA-curated; third-party ISVs via a partner programme with legal agreement, staging push, security scanning, QA and sign-off; every image security-scanned under the NGC Container Security Policy, public images rescanned every 30 days, NVIDIA AI Enterprise and NIM images weekly, Security Scanning tab; all NVIDIA container images signed since July 2023 (cosign); all NVIDIA models signed since April 2025 (OpenSSF Model Signing, model_signing verify); SBOM (CycloneDX), VEX and scan results retrievable by image digest via NGC API or ORAS; governing terms accepted once per NGC org before download; ngc registry model download-version |
| CG-12 | Llama-3.1-8B-Instruct NIM container page (NGC); NVIDIA | https://catalog.ngc.nvidia.com/orgs/nim/teams/meta/containers/llama-3.1-8b-instruct | tags latest, 2.0.13, 2.0.12; updated 2026-09-16 | [CHECKED] Signed badge; Security Scanning tab; source linked to huggingface.co/meta-llama/Llama-3.1-8B-Instruct; "governed by the NVIDIA Open Model Agreement" plus the Llama 3.1 Community License; container under the NVIDIA Software License Agreement and Product-Specific Terms |
| CG-13 | NIM for LLM and VLM: Get Started (1.11.0); Prerequisites; Quickstart; Model Profiles and Selection; Model Download; Model Signature Verification; overview; NVIDIA | https://docs.nvidia.com/nim/large-language-models/1.11.0/getting-started.html ; https://docs.nvidia.com/nim/large-language-models/latest/get-started/prerequisites.html ; …/latest/get-started/quickstart.html ; …/latest/deployment/model-profiles-and-selection.html ; …/latest/deployment/model-download.html ; …/latest/reference/model-signature-verification.html ; …/latest/about-nim-llm/overview.html | 1.11.0 and latest (2.0.x), no date shown | [CHECKED] pull from nvcr.io with an NGC API key (keyless for eligible public NIMs); self-hosting under the NVIDIA AI Enterprise licence; pre-built optimised profiles (vllm, sglang, trtllm at bf16, fp8, mxfp4, nvfp4), "curated weights"; 64-char profile IDs; weights downloaded at startup from ngc://, hf://, s3://, gs://, modelscope://, local://; mirror to S3; NIM_MODEL_PATH for own weights; internal checksum verification; hosted alternative build.nvidia.com |
| CG-14 | NVIDIA AI Enterprise Lifecycle Policy: Application Layer Software; End of Life Notices; NVIDIA | https://docs.nvidia.com/ai-enterprise/lifecycle/latest/application-software.html ; https://docs.nvidia.com/ai-enterprise/lifecycle/latest/eol-notices.html | last updated 2026-08-20; 2026-09-09 | [CHECKED] Feature Branch supported one month, Production Branch 9 months; public EOL notices (e.g. NIM Llama-3.1-70b-instruct end of support July 2026); support lifecycle, not an explicit catalogue takedown policy |

### 3.2 What the platforms carry (LD)

| ID | Source | URL | Date or version on page | Verified |
|---|---|---|---|---|
| LD-13 | Kaggle models index and Hugging Face integration blog; Kaggle | https://www.kaggle.com/models ; https://www.kaggle.com/blog/kaggle-hugging-face-integration | no date shown | [CHECKED] a distinct Hugging Face surface whose entries are links out rather than Kaggle-held files |
| LD-27 | as LD-26; Microsoft | as LD-26 | no date shown | [CHECKED] the catalogue includes a Hugging Face collection served on managed compute |
| LD-28 | Overview of Model Garden, Google Cloud; Google | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models | no date shown | [PARTIAL] three catalogue categories and a four-axis filter pane; task and feature values not published. Also states that Hugging Face models deemed unsafe by that platform's scanners are blocked from deployment while suspicious or remote-code ones are flagged and remain deployable |

### 3.3 Taxonomy evidence (TX)

| ID | Source | URL | Date or version on page | Verified |
|---|---|---|---|---|
| TX-01 | Hub model search with filters (counts above); Hugging Face | https://huggingface.co/models?pipeline_tag=…&library=… | no date shown | [CHECKED] counts as tabulated |
| TX-03 | Serialization semantics; torch.load; PyTorch | https://docs.pytorch.org/docs/2.14/notes/serialization.html ; https://docs.pytorch.org/docs/2.14/generated/torch.load.html | 2.14.0, "Last Updated On: May 08, 2026" | [CHECKED] torch.save/load use pickle by default; .pt/.pth convention; since 2.6 torch.load defaults to weights_only=True; "Never load data from an untrusted source" |
| TX-04 | transformers Models (v4.35.0; v5.17.0); huggingface_hub Serialization (v2.1.1); Hugging Face | https://huggingface.co/docs/transformers/v4.35.0/en/main_classes/model ; https://huggingface.co/docs/transformers/main_classes/model ; https://huggingface.co/docs/huggingface_hub/en/package_reference/serialization | v4.35.0 / v5.17.0 / v2.1.1 | [CHECKED] safe_serialization defaults True since v4.35; v5.17 exposes no pickle save option and from_pretrained defaults weights_only=True; hub library: saving as pickle deprecated, loaders refuse pickle unless opted in |
| TX-05 | Safetensors (index); Hugging Face | https://huggingface.co/docs/safetensors/index | no date shown | [CHECKED] "simple format for storing tensors safely (as opposed to pickle)"; used by transformers, mlx, candle, llama.cpp, diffusers |
| TX-06 | GGUF specification; ggml-org | https://github.com/ggml-org/ggml/blob/master/docs/gguf.md | spec v3 | [CHECKED] single-file inference format for GGML executors; quant tensor types Q2_K…Q8_K, IQ*, TQ*, MXFP4; filename Type "LoRA : GGUF file is a LoRA adapter"; mmproj sidecar; LoRA metadata still "TODO" |
| TX-07 | GGUF (Hub docs); Use Ollama with any GGUF model; GGUF usage with llama.cpp; GGUF in transformers; Hugging Face | https://huggingface.co/docs/hub/gguf ; raw hub-docs ollama.md, gguf-llamacpp.md; raw transformers quantization/gguf.md | no date shown | [CHECKED] Hub has built-in GGUF features and a library=gguf filter; Ollama consumes any Hub GGUF, default Q4_K_M; transformers loads GGUF by dequantising, cannot save GGUF |
| TX-08 | Export to ONNX (transformers); Optimum Task manager; Optimum ONNX overview; Transformers.js README; sentence-transformers Speeding up Inference; Hugging Face / UKPLab | raw transformers serialization.md; raw optimum task_manager.mdx; https://huggingface.co/docs/optimum/exporters/onnx/overview ; raw transformers.js README; https://sbert.net/docs/sentence_transformer/usage/efficiency.html | no date shown | [CHECKED] ONNX exporter tasks include text-generation, text-classification, feature-extraction, sentence-similarity, image-text-to-text; Transformers.js runs ONNX in the browser; sentence-transformers backend="onnx" with onnx/model.onnx and quantised variants; huggingface.co returned 429 in bursts, same source files fetched from GitHub |
| TX-09 | onnxruntime-genai README; Run with LoRA adapters (ORT GenAI tutorial); Microsoft | https://github.com/microsoft/onnxruntime-genai ; https://onnxruntime.ai/docs/genai/tutorials/finetune.html | no version shown | [CHECKED] ORT GenAI runs LLMs (Llama, Mistral, Phi, Qwen, Gemma, DeepSeek, Nemotron…) and vision models; Multi-LoRA with .onnx_adapter files via olive convert-adapters; int4 sample paths |
| TX-11 | Docker Model Runner; Docker | https://docs.docker.com/ai/model-runner/ | no date shown | [CHECKED] packages GGUF and Safetensors as OCI artefacts to any registry; pulls from Hugging Face |
| TX-13 | llama.cpp server README; embedding example README; multimodal.md; convert_lora_to_gguf.py; ggml-org | https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md ; raw examples/embedding/README.md ; https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md ; https://github.com/ggml-org/llama.cpp/blob/master/convert_lora_to_gguf.py | no date shown | [CHECKED] --embedding and /v1/embeddings; --rerank with bge-reranker-v2-m3; multimodal via libmtmd with --mmproj (Gemma 3/4, Qwen 2.5 VL, Pixtral, Llama 4 Scout…); PEFT LoRA converted to GGUF ADAPTER type and loaded with --lora |
| TX-14 | PEFT checkpoint format (v0.21.0); Hugging Face | https://huggingface.co/docs/peft/developer_guides/checkpoint | v0.21.0 | [CHECKED] adapter_model.safetensors by default or adapter_model.bin (pickle); interchangeable |
| TX-15 | Quantization overview; bitsandbytes (transformers docs); Hugging Face | https://huggingface.co/docs/transformers/quantization/overview ; raw transformers quantization/bitsandbytes.md | no version shown | [CHECKED] serialisable methods (AWQ, GPTQ, bitsandbytes, compressed-tensors, FP8…) save through transformers = safetensors; GGUF, HQQ, NVFP4, quanto, Quark not serialisable in transformers |
| TX-16 | Filter Models page by Base Models only (changelog); Hugging Face | https://huggingface.co/changelog/filter-models-by-base-models-only | "May 28, 26" | [PARTIAL] "Base only" toggle and Model Tree filter exist; no URL parameter fetched gives base-only counts, so the generative (base) row inherits the instruct row |

### 3.4 Unreachable, redirected or otherwise noted

The former Bedrock modality page now redirects to a provider-organised catalogue. Google's Model Garden
documentation resolves under a renamed product path, Vertex AI having become Gemini Enterprise Agent
Platform, and Azure AI Foundry having become Microsoft Foundry, with separate classic and current
portals that differ in substance. ModelScope's documented metadata page returns navigation only on both
its domains. Counts from live catalogue pages drift between
readings and are quoted as at the access date.
