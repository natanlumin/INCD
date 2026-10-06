# Style guide, glossary and citation policy for the open-source AI model security report

Governs the INCD report (`nk_dans_incd_report.docx` skeleton, "Securing Open-Source AI Models:
Threat Landscape, Assessment Methodology and Acceptance Criteria") and every document that feeds it.
Built from the report's base, the landscape and the single segmentation, outward: platforms and
distribution first, the taxonomy second, artefacts and derivatives third, the threat model and
assessment vocabulary fourth, and the test families, including the six SABRE tests, last.

Satisfies two Jira items. (a) The style-guide item: "terminology glossary agreed once and used
everywhere, citation policy and source-quality bar, figure and table style, English-language QA
approach"; acceptance = published to the shared workspace before drafting starts, with the citation
policy stating the minimum source standard for a government deliverable. (b) The landscape item's
taxonomy half: "a reusable taxonomy table agreed with Dan as the single segmentation used consistently
across Parts I–IV; every later matrix keys off this taxonomy, so it must be stable before S2". The
landscape item's other half, the platform comparison with every claim carrying a dated source, is a
drafted subsection; §6 here gives its skeleton and the source classes it must meet. Version 1.1,
2026-10-05.

---

## 1. Terminology glossary (agreed once, used everywhere)

Rules: one canonical term per concept; the canonical term is used in all prose; the technical anchor
may appear once per section as a tag in parentheses; "avoid" words are not used in customer-facing or
executive text and may appear in technical appendices only when the anchor is being defined. A term
not in this glossary is not introduced by any chapter on its own; it is added here first.

### 1.1 Where models live and move (platforms and distribution)

| Canonical term | Definition | Technical anchor | Avoid |
|---|---|---|---|
| model repository | a public platform that hosts model files and their metadata for download | Hugging Face Hub, Kaggle Models, ModelScope | "marketplace" |
| model hub | synonym used by platforms; in this report "repository" is canonical | Hub | mixing "hub" and "repository" in one chapter |
| model garden | a cloud provider's curated catalogue of models deployable on that provider | Vertex AI Model Garden, Amazon Bedrock and SageMaker JumpStart, Azure AI model catalog, NVIDIA NGC / NIM | treating a garden as an independent source of the file; it redistributes |
| package registry | a distribution channel that ships models as installable packages with their runtime | Ollama library (GGUF), GitHub releases, PyPI-hosted weights | "repository" for Ollama or GitHub releases |
| distribution mechanism | how the file moves from the publisher to the operator: direct download, git-LFS clone, API pull, container image, package manager | `huggingface_hub`, git LFS, `ollama pull`, OCI image | implying one mechanism for all platforms |
| platform-side control | a protection the platform applies to hosted files before or at download: malware and pickle scanning, format conversion, signing, gating, licence acceptance | Hugging Face pickle scanning and safetensors conversion bot; gated repos; Kaggle moderation | assuming a control exists on a platform without a dated source |
| guaranteed metadata | fields the platform enforces or verifies, as opposed to fields the publisher fills in freely | model card YAML (`base_model`, `license`, `pipeline_tag`), file hashes, commit history | treating free-text model-card claims as guaranteed |
| provenance | the recorded chain from a base model to the file in hand: base model, derivation kind, author, commit, hash | model tree, `base_model` relations, SHA-256 of each file | "provenance" for a licence statement alone |
| governance | who may publish, what is removed, how disputes and takedowns work on the platform | terms of service, content policy, DMCA process | "governance" for the operator's own policy (say "organisational practice") |
| gated model | a file the platform releases only after the downloader accepts terms or is approved | gated repository | "private" |
| mirror | a copy of a repository on another platform or host; provenance must be re-established | ModelScope mirrors of Hugging Face repos; internal mirrors | assuming a mirror preserves hashes or metadata |

### 1.2 The single segmentation: model type × artefact format (the taxonomy)

Every later matrix (threat × model type, control × model type, test family × model type) keys off
this segmentation. It has two axes and is used exactly as defined here (see §6.1 for the table).

**Axis A, model type** (by task and by relation to a parent):

| Canonical term | Definition | Technical anchor | Avoid |
|---|---|---|---|
| generative model | produces text (or other media) token by token from a prompt; the class the six tests address | decoder-only LLM, causal LM | "LLM" for non-text generators |
| classification model | maps an input to one of a fixed set of labels; no free-form output | encoder classifier, sequence classification head | "generative" for a classifier with a text label |
| embedding model | maps an input to a vector used for search, clustering or retrieval; no readable output | sentence embedding, bi-encoder | "generative" |
| multimodal model | takes or produces more than one modality, typically image and text | VLM, image-text-to-text, audio-text | "LLM" when the image path is in scope |
| adapter | a small file that changes a base model's behaviour when loaded with it; not runnable alone | LoRA, QLoRA adapters, PEFT | assessing an adapter without its base |
| quantised model | a compressed copy of a model at lower numeric precision; a derivation kind, orthogonal to task | INT8 / FP8 / 4-bit, GGUF quant levels, GPTQ, AWQ | "the same model" as its parent |
| base model | a file with no recorded parent, from which derivatives are made | foundation model, pretrained checkpoint | "base" for an instruct-tuned release without saying so |
| instruct / chat model | a base model retrained to follow instructions and, usually, to refuse; the file whose safeguard the six tests measure | instruction-tuned, chat-tuned, aligned | "aligned" as a guarantee |

Note: the Jira list names quantised, classification, generative, embedding, multimodal and adapters.
Quantised and adapter are derivation kinds, the other four are task kinds. The taxonomy keeps both on
one axis because the report's later matrices need each as a row, and marks which is which.

**Axis B, artefact format** (how the numbers are stored):

| Canonical term | Definition | Technical anchor | Avoid |
|---|---|---|---|
| pickle checkpoint | a file serialised with Python's pickle; loading it can execute arbitrary code, so the format itself is a threat surface | `.bin`, `.pt`, `.pth`, `.ckpt` (PyTorch pickle) | loading one from an unverified source; "legacy" without saying it still exists |
| safetensors | a format that stores tensors only, with no executable content; loading cannot run code | `.safetensors` | treating it as a guarantee about behaviour (it guarantees only the container) |
| GGUF | a single-file format for quantised models used by llama.cpp-family runtimes, with metadata inside the file | `.gguf` (successor of GGML) | "GGML" for current files |
| ONNX | a graph-based interchange format for running models outside their training framework | `.onnx`, ONNX Runtime | assuming the ONNX export behaves identically to the source |
| container or image | a runnable bundle of model, runtime and serving code | OCI image, NIM container | assessing the model without the serving code inside |

### 1.3 Artefacts and derivatives (what is in hand)

| Canonical term | Definition | Technical anchor | Avoid in prose |
|---|---|---|---|
| model file, the file | the downloaded artefact; all knowledge and behaviour are its numbers | weights, checkpoint, safetensors | "weights" as the subject of a sentence |
| open-source model | a model whose file is publicly downloadable, whatever its licence | open-weights model | "open source" for a hosted API |
| derivative model | any file produced from another model file. Four kinds: a compressed copy (quantised), a retrained copy (fine-tuned, or with adapters), a merged model (two or more files combined), and a stripped fork (abliterated, "uncensored"). Every derivative is a different model and gets its own assessment. Synonyms met in the field: derivative work or derivative model (Llama and OpenRAIL licences), downstream or derived model (policy texts), the model tree with its base-model relations finetune / adapter / merge / quantized (Hugging Face metadata) | quantization, fine-tuning / LoRA adapters, model merging, abliteration | treating a derivative as the same model as its parent; assuming a parent's result carries to a derivative |
| merged model | a derivative made by combining the numbers of two or more model files | model merging (weight averaging, SLERP, TIES) | "merge" without saying which parents |
| weight averaging | the simplest merge: each number in the result is the average of the parents' numbers; works only for parents trained from the same base | linear merge, model soups | treating the average as a tested model |
| SLERP | a merge that blends two parents along the shortest arc between them rather than a straight average, so the result keeps the parents' overall size; pronounced "slurp", from spherical linear interpolation | spherical linear interpolation of weight tensors | expanding it as a method in executive text; say "a merge" |
| TIES | a merge for more than two parents: keep only each parent's largest changes from the base, resolve sign conflicts by majority, then combine; pronounced as a word, from Trim, Elect Sign, and Merge | TIES-Merging (Yadav et al., 2023) | implying it preserves any parent's safeguard |
| compressed copy | a derivative with reduced numeric precision | quantization (INT8/FP8/4-bit) | "quantised" in executive text |
| retrained copy | a derivative whose behaviour was changed by further training or adapters | fine-tune, LoRA, adapter | "fine-tune" in executive text |
| stripped fork | a published derivative with the refusal removed | abliterated, "uncensored" model | "uncensored" without quotation marks |
| fine-tuned model | the technical name for a retrained copy: a derivative whose numbers were changed by further training on new examples, or extended with adapters; its safeguard may differ from the parent's in either direction | fine-tuning, SFT, RLHF/DPO, LoRA / adapters | assuming the parent's assessment covers it |
| quantised model | the technical name for a compressed copy: the same model stored at lower numeric precision; behaviour is close to the parent but not identical, and the safeguard can shift | quantization (INT8, FP8, 4-bit, GGUF) | "the same model" |
| abliterated model | the technical name for a stripped fork: a copy in which the refusal direction was located and removed from the numbers, permanently, then published; the weight-surgery attack done once | abliteration, refusal-direction ablation; "uncensored" | calling it a jailbreak (it needs no prompt) |
| refusal vector | the technical name for the model's "no": the direction in internal state along which harmful and harmless requests differ on average; it is what the twist, forgetting and firmness tests act on, and what abliteration removes | refusal direction r = mean(h | harmful) − mean(h | harmless); per-expert r_e on a committee model | "vector" in executive text; implying it is a single switch (it is a small bundle; one direction is a floor) |
| internal state | what is happening inside the model while it answers | activations, hidden state, residual stream h_ℓ | "activations" in executive text |
| the model's "no", the line | the consistent internal lean that produces refusal, located from examples; the line between what it refuses and what it answers | refusal direction r, difference of means over harmful and harmless prompts | "vector" |
| a push inside | a small change to the internal state along a direction | ε·v on h_ℓ; steering | "perturbation" in executive text |
| meaning direction, random direction | a direction the model itself uses; one it does not | on-cone, off-cone | "cone" in executive text |
| how big a push it takes | the smallest push that already changes the answer | radius, KL ≥ τ | "KL", "radius" in executive text |
| whether the push grows as it writes | amplification of a push along generation | leverage | "leverage" in executive text |
| fluent compliance | a harmful request answered, and the answer is not gibberish | coherent jailbreak: degeneracy gate + rule-based refusal detector | "ASR" in executive text |
| committee of specialists | a model in which only a few parts answer each token | mixture of experts (MoE), router, per-expert direction | "MoE", "expert", "router" in executive text |
| safeguard, built-in safeguard | the model's own refusal behaviour, inside the file | safety alignment, refusal | "guardrail" for the model's own refusal |
| guard | a control placed around the model, in front of or behind it | guardrail, input/output filter, classifier | "safeguard" for an external control |


### 1.4 Threat model and assessment

| Canonical term | Definition | Technical anchor | Avoid |
|---|---|---|---|
| door | an attack surface defined by the access it grants, not by who stands at it; exactly three | attack surface | "vector" for an attack path |
| the input (door 1) | send text, read the answer, nothing else | black-box, prompt-level | — |
| the serving path (door 2) | read and change the internal state while the model runs | white-box at inference: hooks, adapters, serving code, insiders | — |
| the supply chain (door 3) | the file before deployment and the examples it was tuned with | artefact provenance, dataset provenance | — |
| indicated vs measured | a test indicates a door when it fixes a floor for attacks through it; measures it when the attack is run through it | — | "measured" for door 1 by the six tests |
| two halves | what the model's own steadiness and safeguard are worth (doors 2, 3) vs what an outsider gets today (door 1) | white-box scores vs black-box prompt attacks | reporting one half as the whole |
| work factor | the effort an attacker with model access needs to force compliance; reported per test in its own currency | angle, coefficient, geometric shift | a single joint figure |
| band | the word a test returns on a fixed global scale | low / medium / high / critical (attack metrics ≥ 0.70 / 0.40 / 0.20); quality > 0.80 / 0.60 / 0.30 | numbers in executive text |
| Robust / Sensitive / Fragile | the Group 1 band words = low / medium / high + critical | q_stability bands | mixing the two vocabularies in one table |
| test family | a group of tests sharing a construct: Group 1 (J-space stability), Group 2 (intrinsic-safeguard robustness), prompt attacks (door 1) | — | "scanner" in executive text |
| acceptance criterion | the band at which a model is used, used with a named control, or not deployed | threshold policy | criteria without the named control |
| trust tier | the protection level a deployment requires; the bands are its input | — | tiers defined without the band mapping |
| reconnaissance | locating the safeguard; free at doors 2 and 3 | diff-of-means estimation | implying obscurity protects |
| backdoor | a planted trigger that changes behaviour on specific inputs; detected by a separate test family | T0043.004 | "backdoor" or "soft backdoor" for any of the six tests |
| data poisoning | the technique of corrupting what a system learns from; what the firmness test measures is the control it gains on the model | LLM04, T0020 | presenting the firmness test as "merely data poisoning" |

### 1.5 Test families and the six SABRE tests (names fixed)

Test families in the report: (i) artefact and supply-chain checks (format, hash, signature, scan);
(ii) Group 1, J-space stability; (iii) Group 2, intrinsic-safeguard robustness; (iv) black-box prompt
attacks (door 1); (v) backdoor and trojan detection (separate family). Families (ii) and (iii) are the
six SABRE tests:

| # | Canonical name | Question | Technical tag (once per section) |
|---|---|---|---|
| 1 | Integrity | does a slightly altered copy still behave like the original | weight-tamper radius |
| 2 | Fidelity | how easily does it answer the question wrong, on topic | J-space on-cone distortion |
| 3 | Containment | how easily does it answer a different question (control, no band) | J-space off-cone diversion |
| 4 | The twist test | how far must it be pushed off its own refusal before it complies | Angular steering |
| 5 | The forgetting test | does it still refuse when its sense of danger is dulled | Amnesia |
| 6 | The firmness test | how firmly is the line between refuse and answer drawn | steering-vector poisoning |

Group names (ii) and (iii): Group 1 "how steady and how forgiving is the model"; Group 2 "how good is the built-in
safeguard". The three parts of Group 2 are introduced together with the car-inspection sentence
(radiator, carburettor, oil, brakes), one line each, before any analogy.

---

## 2. Citation policy and source-quality bar

**Minimum standard for this deliverable.** Every factual claim in the report is traceable to a dated
source of one of the classes below, and the class is visible to the reader. No claim is cited from
memory. A claim that cannot be sourced to the standard is either dropped or marked as the authors'
assessment.

### 2.1 Source classes, in order of weight

| Class | Examples | Admitted as | Required fields |
|---|---|---|---|
| S1 Standards and frameworks | OWASP Top 10 for LLM Applications 2025; MITRE ATLAS (ATLAS.yaml); NIST AI RMF 1.0, NIST AI 100-2e2025; ISO/IEC 42001 | authoritative for taxonomy and IDs | name, version or release date, ID verified against the live artefact, access date |
| S2 Peer-reviewed or accepted venue | NeurIPS, ICML, ICLR, ACL (incl. Findings), IEEE S&P, USENIX Security, CCS | authoritative for a result | authors, title, venue, year, identifier |
| S3 Preprint, verified | arXiv papers whose claim was read in full and checked | admissible, labelled "preprint" | arXiv ID, version, date; the [CHECKED] tag in the source log with what was verified |
| S4 Vendor and platform documentation | model cards, Hugging Face docs, NVIDIA, AWS, SageMaker, NIM documentation | admissible for facts about the artefact or platform | URL, access date, version |
| S5 Our own measurement | SABRE runs | admissible with provenance | model and precision, scanner and commit, run identifier, date, settings, where the raw callback lives |
| S6 Practitioner interview | primary-source statements | admissible as attributed opinion | interview record and attribution log entry; consent for attribution level |
| S7 Secondary and press | blogs, news, talks | not admissible for a technical claim; may motivate a question | — |

### 2.2 Rules

1. **Frameworks IDs are verified, never recalled.** Every OWASP, ATLAS and NIST ID is checked against
   the current artefact before it appears; the check date goes in the source log. Known trap recorded:
   ATLAS T0018 is "Manipulate AI Model", not "Backdoor"; a backdoor trigger is T0043.004.
2. **Preprints are labelled and verified.** An arXiv source is cited only after the claim used has
   been read in the paper itself; the source log records what was checked. A preprint that later
   appears at an S2 venue is upgraded in the log, not re-cited.
3. **Our own results carry provenance or do not appear.** Numbers appear only in technical sections
   and appendices, with model, commit, run identifier and date. Executive and customer text uses band
   words only. Earlier results superseded by a rerun are cited only as history, labelled as such.
4. **Inference is labelled as inference.** Where a claim bridges our measurement to a threat the test
   does not run (door 1 via Arditi 2406.11717), the sentence says "literature-backed inference".
5. **Research cut-off.** A single cut-off date is fixed at drafting start and stated in §2.4 of the
   report; sources after it are not admitted except by an explicit addendum.
6. **One source log** (Appendix E) lists every source with class, date, access date, verification
   tag and the sections that cite it. No citation exists outside the log.
7. **Attribution of people** follows the interview record: role, never name, unless the attribution
   level recorded permits it.
8. **Citation form.** In text: (Author year) or (Standard, version). In the bibliography: authors,
   title, venue or repository, identifier, year; for S5: SABRE, scanner, commit, run id, date.

---

## 3. Figure and table style

### 3.1 Tables

- Header row always; first column is the thing being described; units or scale in the header, not
  the cells.
- Bands appear as words. Numbers appear only in technical tables, with a "higher = worse" or "higher =
  safer" note in the caption.
- Every table that reports a measurement has a provenance footnote: model, run identifier, date.
- One vocabulary per table: either Robust / Sensitive / Fragile or low / medium / high / critical,
  never both.
- Framework tables carry the verification date in the caption.
- Column order for test tables, where applicable: test, question, door, scored by, band, action,
  framework. The master's one-row-per-test table is the reference layout.

### 3.2 Figures

- One message per figure; the caption states what is shown, on which model, from which run.
- Diagrams of the model use the glossary words (door, push inside, the line); technical labels go in
  a legend, not on the drawing.
- Colour: colour-blind-safe palette; bands use the same colours throughout (one colour per band,
  fixed in the shared workspace).
- No vendor logos; model names as in their model cards.
- Numbering: Figure n and Table n per chapter; cross-references by number, never "below".

### 3.3 Boxes

- Three box types only: Definition (glossary term introduced), Example (a demonstration result),
  Caution (a limitation or an honesty rule). Each box has a one-line title.

---

## 4. English-language QA approach

### 4.1 Register and spelling

- British English spelling (artefact, prioritisation, organisational), matching the skeleton.
- Two registers, never mixed in one section: executive and customer text (glossary words only, no
  numbers, no IDs); technical text (anchors, numbers, IDs, provenance).
- Technical names appear once per section as a tag in parentheses after the canonical name.

### 4.2 Sentence rules

- One idea per sentence; aim for about twenty words; a verb in every sentence.
- No em-dashes, no parentheses for asides, no arrows in prose.
- Acronyms expanded at first use in each chapter; the glossary lists the expansion.
- No "simply", "just", "obviously"; no exclamation marks.
- At most one analogy per test, and never one that implies crashing; the fear is quiet wrong answers.
- Headings are questions or noun phrases, never claims.

### 4.3 QA passes, in order

1. **Glossary lint.** A search for every "avoid" word in §1 across the draft; each hit is replaced
   or moved to a technical appendix. The banned list from the writing brief (weights, activations,
   layer, vector, cone, radius, KL, leverage, MoE, expert, router, quantised, fine-tune, backdoor,
   soft backdoor, reference point, interpret the safeguard) is the seed.
2. **Numbers lint.** Any digit in an executive or customer section is a defect unless it is a date,
   a section number or a count of items.
3. **Door lint.** Every statement about the input door says "indicated" or "floor", never
   "measured", unless it is about the prompt-attack family.
4. **Citation lint.** Every claim sentence has a source in the log; every source in the log is
   cited; every framework ID has a verification date.
5. **Two-reader read.** One technical reader checks that nothing in the plain-English text is false
   to the code; one non-technical reader checks that nothing needs the appendix to be understood. A
   sentence that sends the lay reader to the appendix is cut from the executive text, not explained.
6. **Consistency read.** The six names, the three doors, the two halves and the band words are
   identical in every chapter, table and figure.
7. **Final pass.** Spelling to British English; headings numbered; cross-references resolved;
   provenance footnotes present on every measurement table.

### 4.4 Ownership

The glossary and this guide live in the shared workspace. A change to a canonical term is a change
to this file first, then to every document that uses it; no document introduces a term on its own.

---

## 5. Mapping to the Jira acceptance criteria

| Required | Where satisfied |
|---|---|
| Terminology glossary agreed once, used everywhere | §1, with the six names fixed in §1.3 |
| Citation policy and source-quality bar | §2, minimum standard stated at the top of §2, classes S1–S7, rules 1–8 |
| Figure and table style | §3 |
| English-language QA approach | §4, seven passes |
| Published to the shared workspace before drafting starts | this file, plus the master organization and the six-tests papers, in the package and in `sabre/docs/` |
| Reusable taxonomy table, single segmentation across Parts I–IV (landscape item) | §1.2 definitions and §6.1 table; to be agreed with Dan and frozen before S2 |
| Platform comparison table, every claim with a dated source (landscape item) | §6.2 skeleton: rows, columns and the source class each cell must meet; the cells themselves are the drafted subsection's work |

---

## 6. Tables that the rest of the report keys off

### 6.1 The taxonomy table (single segmentation; freeze before S2)

Rows are model types (Axis A), columns are artefact formats (Axis B). Cell values: **C** common,
**P** possible but uncommon, **–** not applicable. Values below are the working proposal; each is to
be confirmed with a dated source (class S4, platform documentation) before the table is frozen.

| Model type \ format | pickle checkpoint | safetensors | GGUF | ONNX | container / image |
|---|---|---|---|---|---|
| generative (instruct / chat) | C | C | C | P | C |
| generative (base) | C | C | C | P | P |
| classification | C | C | – | C | P |
| embedding | C | C | P | C | P |
| multimodal | C | C | P | P | C |
| adapter | C | C | – | – | – |
| quantised (any task) | P | C | C | C | C |

Reading rules: a derivation kind (quantised, adapter) is a row of its own because later matrices need
it; a quantised multimodal model is counted once, in the row that the chapter is about. Each later
matrix (threat × type, control × type, test family × type) uses these row labels verbatim.

### 6.2 The platform comparison table (skeleton; every cell needs a dated source)

| Platform | Kind (§1.1) | Governance (who may publish; takedown) | Platform-side controls (scanning, conversion, signing, gating) | Guaranteed metadata (enforced fields, hashes, history) | Distribution mechanism | Source (class, date) |
|---|---|---|---|---|---|---|
| Hugging Face Hub | model repository | | | | | |
| Kaggle Models | model repository | | | | | |
| ModelScope | model repository (mirror of many HF repos) | | | | | |
| Ollama library | package registry (GGUF) | | | | | |
| GitHub releases | package registry | | | | | |
| Cloud model gardens (Vertex, Bedrock / JumpStart, Azure, NGC / NIM) | model garden | | | | | |

Rules for filling it: one row per platform, one dated source per cell (class S4 or S1), access date
in the source log; a cell with no source stays empty and is marked "not established", never inferred
from another platform. Columns are the four the Jira names; no column is added without a reason
recorded in the source log.
