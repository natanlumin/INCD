# Assessment tooling for open-source models: a desk survey and comparison

## What this document answers

An organisation that takes an open-source model (SCRUM-281) into use meets it in two states, and in each it
needs tools.

- **Before adoption: the file (SCRUM-281) is in hand.**
    - The organisation can read the file without running it: scan its format for code that runs on load,
      and check that it is the file the producer (SCRUM-281) published.
    - It can run the file and test it: send it inputs and judge the outputs, or read its internals while it
      runs, looking for what no metadata shows.
- **In service: the model answers requests.**
    - Guards sit in front of and behind the model and decide what reaches it and what leaves it.
    - Monitors read what arrives and what is returned, and the same tests are run again to see whether the
      model in service still gives the outputs it gave when it was assessed.
- **Many tools exist, and they are not alike.**
    - They differ in what they cover, in the access they need, in how far their maintainers stand behind
      them, and in what their licences allow.
    - Some that are still cited are no longer maintained. Some that are cited in research
      have no licence at all.

This document surveys the tools in each state and compares them on one table. It is a desk survey: every
statement about a tool comes from the tool's own documentation or release record, and no tool was run.

**Table 1. The questions this document answers, and where**

| Question | What the document gives | Where |
|---|---|---|
| Which kinds of tool exist, and where in the lifecycle does each work? | six categories, each placed on the lifecycle stages by the rule of the lifecycle assessment framework | Part 1, Table 2 |
| What does each tool cover, and what does it need? | a table per category, Tables 3 to 8: for each tool what it reads, its method and the access it needs; for each category what it cannot do | Part 2 |
| How do the tools compare? | one table on coverage, lifecycle stage, maturity, licensing and operational fit, with the evaluation date and each version | Part 3, Table 9 |
| Which threats and properties does no tool cover? | the threats of the taxonomy and the testable properties, each with the tools that read for it, or none | Part 4, Table 10 |
| Which tools should the demonstration set use, and why? | proposals, each justified from its row of Table 9 | Part 5, Table 11 |

The contributions, stated once:

- **One placement rule for every tool.** Each tool is placed on the lifecycle stages by the evidence it
  reads, the rule the lifecycle assessment framework fixes, so a reader can see when a tool can be used and
  when it cannot.
- **One comparison table**, on five comparison dimensions: coverage, lifecycle stage, maturity, licensing
  and operational fit, the five the survey is asked for, each defined with its scale in 1.3. The word
  "axis" is not used for them, because the glossary (SCRUM-281, section 1.2) keeps it for the two
  axes of the segmentation, model type and artefact format. The table gives the version of every tool and the date the
  versions were read, so the comparison can be repeated and its age is visible.
- **A coverage map against named threats**: every threat of the taxonomy and every testable property,
  with the tools that read for it. Where no tool does, the map says so.
- **Proposals for the demonstration set**, each traced to a row of the table, and the reasons the other
  tools are not proposed.

**Scope.** Open-source tools that assess an open-source model, the code shipped with it or the software
that loads it, or that stand around it as a control, with a
published version and a stated licence or a stated absence of one. Commercial services are named only where
a platform documents its use of them, because they publish neither a version nor their method, and a row
without a version cannot be compared. The threats are numbered as in two earlier documents: T1 to T8 are defined in the supply-chain
document, "Supply-chain and artefact-level threats on the Hugging Face Hub", Part 2; T9 to T21 in the
threats document, "Model-integrity and inference-time threats" (SCRUM-288), Parts 2 and 3. The properties
are those of the attestable-and-testable document, "Attestable and testable properties of an open-source
model" (SCRUM-289): P1 to P6 in its Part 2, D1 to D5 in its Part 3. Every number used here is listed with
its name in the annex, Table 13. The lifecycle stages (SCRUM-281), test families (SCRUM-281) and evidence items are those of the
lifecycle assessment framework (SCRUM-284).

**Structure.** Part 1 fixes the categories, the placement rule and the five comparison
dimensions. Part 2 surveys the tools,
one category per subsection, each with its own table. Part 3 is the comparison table. Part 4 maps coverage against the threats and
properties. Part 5 proposes the tools for the demonstration set. A closing summary answers the five
questions of Table 1, and an annex gives the text of every lifecycle question and evidence item cited.

**Symbols.** Terms, stage and question numbers, threat and property numbers, and citation prefixes that come
from outside this document are listed, with where each is defined, in "Symbols from outside this document"
after the source log.

## Part 1. Categories, placement and the five comparison dimensions

### 1.1 The categories

The survey covers six categories of tool.

- **Artefact and format scanners** read statically, without loading or running anything, for code that
  would run when the model is loaded. Three objects are read, at different stages: the file alone, the
  code shipped with it, and the packages that code brings in; 2.1 takes them in turn.
- **Red-team and adversarial frameworks** send inputs to the model and judge what comes back, or perturb
  inputs to change a prediction.
- **Guardrail layers** are guards (SCRUM-281): controls (SCRUM-281) placed in front of or behind the model
  in service. They are not the model's safeguard (SCRUM-281), the refusal behaviour its publisher trained
  into the file: the safeguard is not a category of tool but a property the tools assess, set out in 2.3.
- **Runtime monitors** read the inputs that arrive and the outputs returned while the model is in service.
- **Provenance verifiers** check a signature, an attestation or a hash, so that the file in use can be
  shown to be the one published, by the one who published it.
- **White-box analysis**: tools that read the model's internals, its weights and activations while
  it runs, rather than its file format or its outputs. Their ground is mechanistic interpretability,
  "reverse engineering the computational mechanisms and representations learned by neural networks into
  human-understandable algorithms and concepts" (Bereska and Gavves, TMLR 2024) [TL-48]. Two uses matter
  here: looking for a hidden trigger, by inverting the model's behaviour (T10; D2), and finding the
  mechanism that carries the safeguard, such as the refusal direction (Arditi et al., NeurIPS 2024)
  [TH-17]. White-box analysis holds the only tools that read for
  backdoors and trojan triggers, and the only way to check the safeguard from inside the model; without it
  T10 would have no row, and Q2.3 only half of one.

### 1.2 Where each category works

The lifecycle stages (SCRUM-281) are four: S1 selection, S2 adjustment, S3 deployment and S4 runtime
detection, labelled as in the lifecycle assessment framework (SCRUM-284, stage tables, notation). Each
holds evidence items, written en.k for the k-th item of stage n, and questions, written Qn.k.

The test families are four, named in the glossary (SCRUM-281, section 1.4) and each defined by the evidence kind it reads (SCRUM-284, section 1.1, Table 1):

- **static** reads what is readable in the file or the deployment, without running the model;
- **dynamic** reads the model's internals while it runs, white-box, so it needs the file;
- **behavioural** reads the model's outputs on chosen inputs, black-box, so it works in possession and by
  proxy;
- **provenance** reads what the platform guarantees: account, upload date, hashes, gating.

A tool reads one evidence kind, and it can be used at every lifecycle stage whose evidence includes that
kind, where its access need is met (SCRUM-284, section 1.4). The lifecycle assessment framework placed the
tooling kinds by this rule before any tool was named (SCRUM-284, stage tables, section M); Table 2 repeats
that placement, and Part 3 places each tool by it. The text of every question and evidence item is in the
annex, Table 12.

**Table 2. Category to test family and stage** (placement as in SCRUM-284, stage tables, section M)

| Category | Test family (SCRUM-281) | Evidence it reads | Stages |
|---|---|---|---|
| Artefact and format scanners | static | e1.4, e1.6; e2.1; e3.3 | S1, S2, S3 |
| Red-team and adversarial frameworks | behavioural | e1.9, e2.5, e3.5, e4.4 | S1, S2, S3, S4 |
| Guardrail layers | none: a control, not a method | set as configuration in e3.3; their effect measured through e3.5 and e4.3 | S3 as a thing assessed; S4 as a thing watched |
| Runtime monitors | behavioural | e4.3, e4.4 | S4 |
| Provenance verifiers | provenance; static for the re-reads | e1.1, e1.3, e1.8; e2.1, e3.1, e4.1 against e1.3 | S1; the re-reads at S2, S3, S4 |
| White-box analysis | dynamic | e1.10, e2.4 | S1, S2 |

Two readings follow from Table 2.

- **Only the behavioural family works at every stage, and only it works by proxy (SCRUM-281).** An
  organisation that reaches the model through a serving provider (SCRUM-281) and never holds the file can
  use a red-team framework and a monitor, and nothing else in this survey (SCRUM-284, section 1.4).
- **Static and white-box tools are front-loaded.** They need the file, so they are used before the model is
  put behind serving software; after that, only the re-read of a hash ties the model in service to the one
  assessed (SCRUM-284, section 1.4).

### 1.3 The five comparison dimensions

Each tool is compared on the five comparison dimensions the survey is asked for. Each dimension has a fixed meaning and, where it
is graded, a fixed scale.

- **Coverage.** The threats the tool reads for, by number, T1 to T21; the testable properties, D1 to D5,
  and the attestable ones, P1 to P6, where it reads one; and the rows of the segmentation it addresses,
  classification, embedding or generative, the model-type axis (SCRUM-281, section 1.2, Axis A) as
  segmented in SCRUM-280, Table 4. A tool covers a threat where its own
  documentation names the threat or the technique; a claim of the maintainer that has not been tested
  independently is marked emerging (SCRUM-281).
- **Lifecycle stage.** The stages S1 to S4 at which the tool can be used, by the rule of 1.2 and the access
  the tool needs.
- **Maturity.** How far the maintainers stand behind the tool, read from published markers only, not from
  any judgement of quality. Five grades:
    - *stable*: a release at version 1.0 or above, or a stated "Production/Stable" status, and maintained;
    - *pre-release*: a stated alpha or beta status, or a version below 1.0, and maintained;
    - *research code*: code published with a paper, with no release process;
    - *dormant*: no change in the year before the evaluation date, and not archived;
    - *retired*: archived, or stated by its maintainers to be no longer maintained.
    A stated status takes precedence over a version number: a tool at 1.2 that states "Alpha" is graded
    pre-release.
- **Licensing.** The licence of the code, by its SPDX identifier, read from the licence file; the licence
  of any model the tool ships, where it differs; or the absence of a licence. Without a licence, the
  default copyright laws apply and "no one may reproduce, distribute, or create derivative works" from the
  code (GitHub, licensing a repository) [TL-34].
- **Operational fit.** What the tool needs to run: the file alone, the weights loaded with their hardware,
  a running endpoint, keys or an identity; its interface, command line, library or continuous-integration
  step; and any dependency on a third-party service.

### 1.4 What a desk survey can and cannot say

- **It can say what the maintainers state**: what the tool reads, how, with what access, under what
  licence, at what version and with what status. Each statement here is cited to the tool's documentation
  or release record, an Official source in the citation policy (SCRUM-281).
- **It cannot say how well a tool works.** Detection rates, false-positive rates and resistance to evasion
  are stated here only where a research paper measured them, and cited to that paper.
- **Its versions have a date.** The versions, licences and statuses in Table 9 are those published on the
  evaluation date stated in the table's caption. Tools change; the table is a record of that date, and the
  method of 1.3 is what lets it be repeated.

## Part 2. The tools

The earlier documents ask the questions this part answers with tools. The supply-chain document names the
threats that ride on the file and the platform, T1 to T8. The threats document names the threats to the
model itself and at use, T9 to T21, and states which are demonstrated in research and which are
theoretical. The attestable-and-testable document separates what can be read about a model, P1 to P6, from
what can only be tested, D1 to D5. The lifecycle assessment framework (SCRUM-284) fixes the stages S1 to S4
and the evidence each stage holds. Part 1 placed each category of tool on those stages (Table 2) and fixed
the five comparison dimensions on which tools are compared.

This part takes each category in turn and asks, of every tool in it, which of those threats and properties
it reads for, with what access, and what its maintainers say it does not do. Each section opens with a
table of the category's tools, on the columns that matter for that category, then gives each tool with its
sources, and closes with what the category cannot do. Part 3 brings every tool onto the five common comparison dimensions in
one table, Table 9.

### 2.1 Artefact and format scanners

What a scanner reads has to be stated, because three different objects can be called "the model", and they
enter at different stages and carry different threats.

- **The file alone.** The weights container, the serialised objects inside it, its metadata and the
  templates stored with it. Reading it is file analysis: nothing outside the file is involved. It is
  readable at selection and after adjustment (e1.4, e2.1), and an own scan of it is e1.6. Malicious
  serialisation (T3), malicious adapters (T6) and the template part of T5 live here.
- **The code shipped with the file.** Custom modelling code, Python files uploaded with the weights, which
  the loader runs only when the user allows it with trust_remote_code [SC-08]: "the second path to code
  execution beside pickle" (SCRUM-284, stage tables, Q1.3). It is readable at selection (e1.4), but reading
  it is code analysis, not format analysis: the code part of T5.
- **What that code brings in.** The third-party packages the shipped code imports, and the loader and
  serving software that run it: software during loading (T8). It is first in hand when the organisation
  builds the environment or container that will run the model, read at deployment (e3.3), where "the
  object scanned is the container or engine contents, not the file alone" (SCRUM-284, stage tables,
  section M), and re-read in service (e4.1).

The category is surveyed in the same three groups. The first group is made for model files. The second and
third are general software tools: they read Python code, packages and containers wherever these come from,
and none of their READMEs mentions model files [TL-35 to TL-42]. They are included because the
lifecycle assessment framework places code and container scanning in this category (SCRUM-284, stage
tables, section M), and because without them the code part of T5 and all of T8 would have no tool.

**Table 3. Artefact and format scanners, by the object they read** (each fact from the tool's
documentation; source log)

| Tool | Object read | What it reads | Method | Limits stated by its maintainers | Covers | Source |
|---|---|---|---|---|---|---|
| picklescan | the file | pickle; PyTorch archives (.bin, .pt, .pth, .ckpt); NumPy; zip | lists the globals a pickle imports and checks them against safe and unsafe lists | none stated; bypasses published [SC-15, SC-16] | T3, T6 | TL-01 |
| ModelScan | the file | H5, pickle, SavedModel | byte search for unsafe code signatures | none stated; GGUF, ONNX and safetensors not listed | T3, T6 | TL-02 |
| fickling | the file | pickle; PyTorch and TorchScript variants | symbolic execution of the pickle; a load-time hook with an import allow-list | imports added to the allow-list are trusted | T3, T6 | TL-03 |
| ModelAudit | the file | pickle, PyTorch, safetensors, GGUF, ONNX, Keras, SavedModel, chat templates, archives | static analysis without loading; weight-anomaly indicators | a clean scan is not "risk is zero"; runtime-only backdoors may not be visible | T3, T5 templates, T6; P4 | TL-04, TL-05 |
| The Hub's scans (platform side) | the file, every upload | every file; pickle imports | ClamAV; listing of pickle imports | "not 100% foolproof"; lists kept "in a best-effort manner" | T3 in part | HF-05 to HF-08 |
| Bandit | shipped code | Python source files | builds a syntax tree of each file and runs security plugins against it | not stated | T5 code | TL-35 |
| Semgrep Community Edition | shipped code | source in 30 or more languages | pattern-based static analysis | "will miss many true positives as it can only analyze code within the boundaries of a single function or file"; registry rules report pseudonymous metrics | T5 code | TL-36 |
| GuardDog | shipped code; packages | packages from PyPI, npm and other registries; a local archive or directory; a requirements file | YARA rules on package source; capabilities and threat indicators correlated into a risk score | threat indicators alone "might be false positives" | T5 code; T8 malicious packages | TL-37 |
| pip-audit | packages | a Python environment or a requirements file | matches packages against the Python Packaging Advisory Database | "not a static code analyzer"; "If you wouldn't pip install it, you should not pip audit it" | T8 known vulnerabilities | TL-38 |
| OSV-Scanner | packages; container | lockfiles and manifests in 11 or more ecosystems; container images | matches dependencies against the OSV database | version 2 described as beta | T8 known vulnerabilities | TL-39 |
| Syft | packages; container | container images, filesystems, archives | generates a software bill of materials, CycloneDX or SPDX; signed in-toto attestations | not stated | T8 inventory; P4 for software | TL-40 |
| Grype | packages; container | container images, filesystems, bills of materials | matches packages against vulnerability data | not stated | T8 known vulnerabilities | TL-41 |
| Trivy | packages; container | container images, filesystems, repositories, virtual machine images, Kubernetes | vulnerabilities, misconfigurations, secrets, licences, bill of materials | its own release channel was compromised [TL-43] | T8 known vulnerabilities | TL-42, TL-43 |

**The file alone.**

- **picklescan** lists the globals a pickle imports and checks them against lists of safe and unsafe
  imports; it reads pickle files, PyTorch archives and NumPy files, from local paths, URLs or Hugging Face
  repositories, and returns an exit code for use in a pipeline (picklescan, README and source) [TL-01]. It
  is the scanner the Hugging Face Hub's pickle scan builds on, and it has had published bypasses: an
  installer call missing from its unsafe list [SC-15], and a parsing flaw that its maintainer states "also
  affects the online hugging face pickle scanners" [SC-16].
- **ModelScan** "currently supports: H5, Pickle, and SavedModel formats" and "reads the content of the file
  one byte at a time just like a string, looking for code signatures that are unsafe"; it ranks findings in
  four severities and is designed for continuous-integration use (Protect AI, ModelScan README) [TL-02;
  SC-26]. It does not list GGUF, ONNX or safetensors.
- **fickling** is a "decompiler, static analyzer, and bytecode rewriter for Python pickle" that executes
  the pickle symbolically rather than running it, and can hook the loader at run time with an allow-list of
  imports from machine-learning libraries; imports the user adds to the list are trusted (Trail of Bits,
  fickling README) [TL-03].
- **ModelAudit** registers scanners across model, archive and configuration formats, among them pickle,
  PyTorch, safetensors, GGUF, ONNX, Keras, SavedModel and chat templates, without loading or executing the
  model, and can emit a CycloneDX bill of materials (Promptfoo, ModelAudit README) [TL-04]. It also reports
  "potential backdoor indicators" from suspicious weight patterns and anomalous tensors [TL-04]; that is a
  claim of the maintainer, not independently tested: emerging. Its security model states the limit plainly: a
  clean scan means "no known indicators were found," not "risk is zero," and "runtime-only backdoors and
  environment-triggered logic may not be visible" [TL-05]. Packaged installs enable telemetry by default
  [TL-04]. Of the shipped files it reads the chat templates; its documentation does not state that it
  analyses shipped Python modelling code [TL-04].
- **The Hub's own scans** are platform-side controls (SCRUM-281), not tools an organisation adopts: ClamAV
  on every file and a pickle-import scan on every pickled upload [HF-05, HF-06], and the Protect AI and
  JFrog scanners on public repositories [HF-07, HF-08]. The Hub states that its lists are kept "in a
  best-effort manner" and that the scan "is not 100% foolproof" [HF-06]. Shipped code is reached only by
  the antivirus signatures; to the Hub it is an ordinary file (supply-chain document, Table 4, row T5).

**The code shipped with the file.**

- **Bandit** "is a tool designed to find common security issues in Python code": it "processes each file,
  builds an AST from it, and runs appropriate plugins against the AST nodes" (PyCQA, Bandit README)
  [TL-35]. It reads the shipped modelling code as it reads any Python file, statically and file by file.
- **Semgrep Community Edition** is a static analysis tool for 30 or more languages, driven by rules from a
  registry; its maintainers state that "in security contexts, Semgrep Community Edition will miss many true
  positives as it can only analyze code within the boundaries of a single function or file", and that
  using registry rules "reports pseudonymous rule metrics to semgrep.dev" unless switched off (Semgrep,
  README) [TL-36]. Its licence is LGPL-2.1 [TL-36].
- **GuardDog** "identifies malicious PyPI and npm packages" and packages of other registries; it "runs
  static analysis on package source code (through YARA rules)" and correlates what code can do with
  threat indicators, because indicators alone "might be false positives"; it scans a registry package, a
  local archive or directory, or every package in a requirements file (Datadog, GuardDog README) [TL-37].
  It is the one tool here that reads for intent, malicious code, rather than for flaws.

**What that code brings in.**

- **pip-audit** scans "Python environments for packages with known vulnerabilities" from the Python
  Packaging Advisory Database, an environment or a requirements file; its security model states that it
  "is not a static code analyzer. It analyzes dependency trees, not code", and "If you wouldn't pip install
  it, you should not pip audit it" (PyPA, pip-audit README) [TL-38].
- **OSV-Scanner** finds "existing vulnerabilities affecting your project's dependencies" from lockfiles and
  manifests and in container images, against the OSV database; its README describes its current version
  as beta (Google, OSV-Scanner README) [TL-39].
- **Syft** generates "a Software Bill of Materials (SBOM) from container images and filesystems" in
  CycloneDX or SPDX, and can sign it as an in-toto attestation; **Grype** scans "container images,
  filesystems, and SBOMs for known vulnerabilities" (Anchore, READMEs) [TL-40, TL-41]. Together they
  inventory the container in which a model is served and match it against known vulnerabilities.
- **Trivy** scans container images, filesystems, repositories and clusters for vulnerabilities,
  misconfigurations, secrets and licences, and produces a bill of materials (Aqua Security, README)
  [TL-42]. Its maintainers' advisory records that a threat actor "used compromised credentials to publish
  a malicious Trivy v0.69.4 release" and malicious images (Aqua Security, GHSA-69fq-xp46-6x23) [TL-43]:
  an assessment tool is itself software in the supply chain, and the same provenance checks apply to it.

What the category cannot do.

- **File scanners read code paths, not behaviour.** They read what runs on load, not what the weights do.
  A research evaluation found the scanners it tested missed known malicious models (Kellas et al., ACM CCS
  2025) [SC-18]. No scanner in this survey reads for a parser exploit in a weight format (T4) by name.
- **Code scanners do not know they are reading model code.** They find patterns and known flaws in Python
  files; none states a rule for what modelling code should or should not do [TL-35 to TL-37].
- **Dependency scanners report known vulnerabilities, not intent.** A package without a published advisory
  passes pip-audit, OSV-Scanner, Grype and Trivy; only GuardDog reads package code for malicious
  behaviour [TL-37, TL-38].
- **The import chain is not resolved from the file.** No tool here starts from a model repository and
  follows what its shipped code imports. The packages are known only once an environment or container is
  built, which is why the third object is read at deployment (e3.3), not at selection.

### 2.2 Red-team and adversarial frameworks

These tools send inputs and judge outputs, so they read behaviour (D1) and work at every stage, by proxy as
well as in possession (Table 2). The generative frameworks address prompt injection (T15, T16),
jailbreaks (T17) and agentic abuse (T21); the adversarial libraries address the classification row.

**Table 4. Red-team and adversarial frameworks** (each fact from the tool's documentation; source log)

| Tool | Attacks and tests | Model rows | Access | How outputs are judged | Covers | Source |
|---|---|---|---|---|---|---|
| garak | probes for prompt injection, jailbreaks, data leakage, training-data replay, toxicity | generative | endpoint over REST, or a local model | the detectors each probe recommends; a failure rate per probe | T15, T17, T19; D1, D4 | TL-11 |
| PyRIT | single- and multi-turn attacks (Crescendo, TAP); content harms, data leakage | generative | provider API, application endpoint, browser | scorers: true or false, Likert, classification; by a model, a content-safety service or custom logic | T15, T17; D1 | TL-12 |
| promptfoo | indirect prompt injection, personal data leaked from context, misuse of connected APIs | generative; retrieval pipelines; agents | HTTP API, browser or direct model access | deterministic and model-graded metrics | T15, T16, T17, T21; D1 | TL-13 |
| Inspect, inspect_evals | agent security (AgentDojo, AgentHarm); jailbreak (StrongREJECT); capability (Cybench, CyberSecEval, WMDP) | generative | provider API or local engine | model-graded and task-defined | T16, T17, T21; D1, D3 | TL-14, TL-15 |
| DeepTeam | jailbreak, prompt injection, multi-turn, excessive agency, tool-metadata poisoning | generative; agents; retrieval pipelines | callback to the system under test | a model as judge | T15, T16, T17, T21; D1 | TL-16 |
| AgentDojo | indirect prompt injection against tool-using agents, with defences | generative, agents | model API | the benchmark's task and security cases [TH-51] | T16, T21 | TL-21 |
| ART | evasion, poisoning, extraction, inference | classification; large language models not named | the model object (white-box) or its predictions | the attack's effect on predictions | T9, T18, T20; D4 | TL-17 |
| TextAttack | attack recipes on text, including gradient-based search | classification, sequence-to-sequence | local model | the attack's effect on predictions | D4 | TL-18 |
| HarmBench | red-team methods against standard, contextual and multimodal behaviours | generative; image and text | local model or API | its own judge classifiers | T17; D1 | TL-19 |
| Counterfit | wraps existing adversarial frameworks | classification | archived | not applicable | T18, T20 | TL-20 |

- **garak** "probes for hallucination, data leakage, prompt injection, misinformation, toxicity
  generation, jailbreaks, and many other weaknesses", against "pretty much anything accessible via REST" or
  a local Hugging Face model, and writes a report of every probe and hit (NVIDIA, garak README) [TL-11].
  Among its probes is a replay probe for training data, which reads for training-data extraction (T19)
  [TL-11]. Its package states "Alpha" status [TL-11].
- **PyRIT** finds "security and safety weaknesses in generative AI systems through automated scans,
  adaptive multi-turn attacks, and human-led testing", including multi-turn strategies such as Crescendo
  and TAP, against provider APIs or application endpoints over HTTP, WebSockets or a browser (Microsoft AI
  Red Team, PyRIT documentation) [TL-12]. Its former repository is archived with the notice "PyRIT has
  moved!" [TL-12]. Its package states "Alpha" status despite a version above 1.0 [TL-12].
- **promptfoo** in red-team mode tests applications, retrieval pipelines and agents for indirect prompt
  injection, leaks of personal data from context and "misuse of connected APIs or databases (in agents)",
  through an HTTP API, a browser or direct model access, configured in YAML (promptfoo, red-team
  documentation) [TL-13]. Its README states "Promptfoo is now part of OpenAI. Promptfoo remains open source
  and MIT licensed." [TL-13].
- **Inspect** is "a framework for large language model evaluations created by the UK AI Security
  Institute" (Inspect README) [TL-14]. Its companion collection, inspect_evals, includes agent-security
  tasks (AgentDojo, AgentHarm), jailbreak tasks (StrongREJECT) and capability tasks for offensive cyber and
  hazardous knowledge (Cybench, CyberSecEval, WMDP) [TL-15], so it is the one framework here that reads for
  capability boundaries (D3) as well as behaviour.
- **DeepTeam** simulates "jailbreaking, prompt injection, multi-turn exploitation" against agents,
  retrieval pipelines and chat applications through a callback, judging outputs with an LLM, and names
  excessive agency and tool-metadata poisoning among its vulnerability types (Confident AI, DeepTeam
  README) [TL-16]. It also offers a guard mode [TL-16].
- **AgentDojo** is "a dynamic environment to evaluate prompt injection attacks and defenses for LLM
  agents" (ETH Zurich and Invariant Labs, AgentDojo README) [TL-21]; its benchmark is the research result
  cited for indirect injection against agents (Debenedetti et al., NeurIPS 2024) [TH-51]. Its maintainers
  state that "the API of the package is still under development and might change" [TL-21].
- **Adversarial Robustness Toolbox (ART)** implements "Evasion, Poisoning, Extraction, and Inference"
  attacks for classification, object detection, speech recognition and generation, across TensorFlow,
  PyTorch, scikit-learn and others, under the Linux Foundation AI & Data Foundation (ART README) [TL-17].
  It is the only maintained tool here that reads for model extraction (T18) and membership inference (T20),
  and for poisoning (T9) on the classification row. Its documentation does not name large language
  models [TL-17]. Some of its attacks need the model object, white-box, and so the file [TL-17].
- **TextAttack** runs "adversarial attacks, data augmentation, and model training in NLP" on
  classification and sequence-to-sequence models loaded in process, including gradient-based search
  (TextAttack README and documentation) [TL-18]: robustness (D4) on the classification row.
- **HarmBench** is a benchmark "for evaluating automated red teaming methods and LLM attacks/defenses",
  with behaviours, attack methods and judge classifiers (Center for AI Safety, HarmBench README) [TL-19].
  It has no release, and no change in the year before the evaluation date [TL-19].
- **Counterfit** brought "several existing adversarial frameworks under one tool" for classical models;
  its repository is archived and names no successor (Microsoft, Counterfit) [TL-20].

What the category cannot do. A red-team result is a judgement of outputs on chosen inputs; it finds a
trigger only if an input happens to contain it, and its verdicts are as good as the judge that scores
them, which several of these frameworks delegate to another model [TL-16, TL-19]. No framework here reads
for quantisation drift (T12), quantisation-triggered backdoors (T13) or merge contamination (T14) by name;
each can be pointed at the changed file and compared with the base, which is the measurement chain of the
lifecycle assessment framework (e1.9, e2.5), not a feature of any tool.

### 2.3 Guardrail layers

A guard (SCRUM-281) is a control (SCRUM-281) assessed with the model, not a method that assesses it
(SCRUM-284, section 1.4). The
survey compares guards because the organisation chooses one, and the choice is set at S3 (e3.3) and
measured through the behaviour of the deployed system (e3.5, e4.3).

A guard is not the safeguard (SCRUM-281). The glossary separates the two: the safeguard is "the model's own
refusal behaviour, trained in by its publisher, inside the file"; a guard is "a control placed around the
model, in front of or behind it", and the word "guardrail" is not used for the model's own refusal
(SCRUM-281, section 1.3). The safeguard is therefore not surveyed here as a category. It is a property the
tools assess, at two questions of the lifecycle assessment framework: whether it is present at selection
(Q1.6) and whether it is still present after an adjustment (Q2.3), where fine-tuning, adapters,
quantisation and merging can weaken it (T11, T12, T14) and an abliterated model (SCRUM-281) has had it
removed on purpose. Two kinds of tool read it:

- **From outputs**, the red-team frameworks of 2.2, which measure whether the model refuses (e1.9, e2.5).
- **From internals**, the white-box tools of 2.6, which look for the refusal mechanism itself, the
  direction in the model's activations that mediates refusal (Arditi et al., NeurIPS 2024) [TH-17]
  (e1.10, e2.4).

A guard can stand in for a weak safeguard in service; it cannot show that the safeguard is there.

**Table 5. Guardrail layers** (each fact from the tool's documentation; source log)

| Tool | Where it sits | What it checks | Model inside it, and its licence | Covers | Source |
|---|---|---|---|---|---|
| NeMo Guardrails | at the points the application chooses; library or server | jailbreaks, injected instructions, unsafe tool calls | models the user configures | T15, T16, T17, T21 | TL-22 |
| LlamaFirewall | user input, agent reasoning, generated code; conversation traces | direct injection (Prompt Guard 2); goal hijacking and indirect injection (AlignmentCheck); insecure code (CodeShield) | Prompt Guard 2, Llama 4 Community Licence; code MIT | T15, T16, T21 | TL-23, TL-24 |
| Llama Prompt Guard 2 | a classifier in the path | prompt injection and jailbreaks, without a separate injection label | itself, 86M or 22M; Llama 4 Community Licence | T15, T17 | TL-24 |
| Llama Guard 4 | a classifier in the path | content safety, image and text | itself, 12B; Llama 4 Community Licence | harmful content | TL-25 |
| Guardrails AI | input and output | validators, one per risk | validators, moving from hosted inference to packages | per validator | TL-26 |
| LLM Guard | input and output | injection, secrets, personal data, toxicity | its own models, no longer maintained | T15 | TL-27 |

- **NeMo Guardrails** adds "model-backed checks for jailbreaks, injected instructions, and unsafe tool
  calls", configured in YAML, as a library or a server in the request path (NVIDIA, NeMo Guardrails README)
  [TL-22]. Its package states "Beta" status [TL-22].
- **LlamaFirewall** is "a flexible, real-time guardrail framework" with three components: Prompt Guard 2,
  which "detects direct prompt injection attempts"; AlignmentCheck, which looks for "goal hijacking,
  indirect prompt injections, and signs of agent misalignment"; and CodeShield, static analysis of generated
  code (Meta, LlamaFirewall README) [TL-23]. Its code is MIT; the models it uses carry their own licences
  [TL-23].
- **Llama Prompt Guard 2 and Llama Guard 4** are the classifier models behind such guards: Prompt Guard 2
  to "detect both prompt injection and jailbreaking attacks", whose model card names its "vulnerability to
  adaptive attacks" (Meta, model card) [TL-24]; Llama Guard 4 a "natively multimodal safety classifier with
  12 billion parameters" (Meta, model card) [TL-25]. Both are under the Llama 4 Community Licence [TL-24,
  TL-25].
- **Guardrails AI** runs input and output guards "that detect, quantify and mitigate the presence of
  specific types of risks", built from validators, as a library or a server (Guardrails AI README) [TL-26].
  Its maintainers have announced the end of their hosted inference for validators [TL-26].
- **LLM Guard** scanned prompts and outputs for injection, secrets, personal data and toxicity; its README
  states "THIS PROJECT HAS BEEN ARCHIVED" and that it and its models "are no longer under active
  development or maintained" (Protect AI, LLM Guard README) [TL-27].

What the category cannot do. A guard reads text at the boundary of the model; it does not change what is in
the file, so it does not remove a trigger, and a classifier guard is itself a model that an adaptive input
can evade, as its own card states [TL-24].

### 2.4 Runtime monitors

A monitor reads e4.3, the inputs that arrive and the outputs returned, at S4. It is where indirect
injection (T16) and agentic abuse (T21) are seen in service (SCRUM-284, stage tables, section M).

**Table 6. Runtime monitors** (each fact from the tool's documentation; source log)

| Tool | What it reads | Method | Status | Covers | Source |
|---|---|---|---|---|---|
| LangKit | prompts and responses, as metrics in logs | similarity to known jailbreaks and injections; patterns; refusal and toxicity metrics | dormant; its maintaining company is discontinuing operations | T15, T17 | TL-30, TL-31 |
| Vigil | prompts and responses | vector similarity, YARA rules, a classifier, canary tokens | alpha; dormant | T15, T17 | TL-29 |
| Rebuff | prompts | heuristics, a model, a vector store, canary tokens | retired | T15 | TL-28 |
| LlamaFirewall, as a monitor | conversation traces | as in Table 5 | maintained | T16, T21 | TL-23 |

- **LangKit** is an "open-source text metrics toolkit for monitoring language models", with similarity
  scores for jailbreak and injection, refusal and toxicity metrics, logged through whylogs (WhyLabs,
  LangKit README) [TL-30]. Its maintaining company states that it "is discontinuing operations" and has
  open-sourced its platform [TL-31]; the toolkit itself has had no change in the year before the
  evaluation date [TL-30].
- **Vigil** assesses "Large Language Model prompts and responses against a set of scanners", by vector
  similarity, YARA rules, a classifier and canary tokens, and states that it is "currently in an alpha
  state and should be considered experimental / for research purposes" (Vigil README) [TL-29].
- **Rebuff** detected prompt injection by heuristics, a model, a vector store and canary tokens, and
  depended on third-party model and vector-store services; its repository is archived and its README calls
  it "still a prototype" (Protect AI, Rebuff README) [TL-28].
- **Guards that log** also serve as monitors: LlamaFirewall can "scan entire conversation traces" [TL-23],
  and NeMo Guardrails and DeepTeam's guard mode sit in the same path [TL-22, TL-16].

What the category cannot do. Among the open-source tools surveyed, no dedicated monitor is maintained:
each is dormant, alpha or retired, and the maintained candidates are guards used for monitoring. A monitor
sees the system, not the file; a hidden trigger is visible to it only when an input carries it.

### 2.5 Provenance verifiers

These tools establish who published the file and that it has not changed since: cryptographic signing and
attestation (P5), and the re-reads that tie the model in service to the one assessed (Q3.1, Q4.1). They
address revision drift (T7) wherever the producer signs.

**Table 7. Provenance verifiers** (each fact from the tool's documentation; source log)

| Tool | What it signs or verifies | Identity | Where it re-reads | Covers | Source |
|---|---|---|---|---|---|
| model-signing | a model directory, file by file, as (path, digest) pairs | keyless identity, keys, certificates, hardware tokens | S1; S2 to S4 by recomputing the hashes | T7; P5 | TL-06 |
| cosign | containers and other artefacts; in-toto attestations | keyless identity, key management service, key pair | S3, S4: the container in service | T7 for containers; P5 | TL-07 |
| in-toto | the steps of a supply chain, against a signed layout | keys per step | each recorded step | T7, T8 in part; P5 | TL-09 |
| slsa-verifier | the build provenance of an artefact | the expected builder | none: no longer maintained | P5 | TL-08 |
| cyclonedx-python | an inventory of a Python environment; no model | none | S2, S3 | T8 as inventory; P4 for software only | TL-10 |

- **model-signing** signs a model directory as "a list of (file path, digest) pairs" in an in-toto
  statement inside a Sigstore bundle, keyless through an identity provider or with keys, certificates or
  hardware tokens, and verifies by checking the signature and computing "the model's file hashes again"
  (Sigstore, model-transparency README) [TL-06; SC-24]. It claims "integrity and provenance" only [TL-06].
  Its package states "Alpha" status [TL-06].
- **cosign** signs "OCI containers (and other artifacts)" with built-in support for in-toto attestations
  (Sigstore, cosign README) [TL-07]: the container in which a model is served (e3.1, e4.1). Its README notes
  that signatures keep "only a weak reference back to the object they sign" [TL-07].
- **in-toto** verifies "that each task in the chain is carried out as planned, by authorized personnel
  only", from a signed layout and signed records of each step; by default it allows artefacts not
  explicitly disallowed (in-toto README) [TL-09].
- **slsa-verifier** checks the signature on build provenance; its README states "This project is no
  longer actively maintained" (SLSA, slsa-verifier README) [TL-08].
- **cyclonedx-python** generates a bill of materials from a Python environment or its manifests
  (CycloneDX, README) [TL-10]: the software around the model, not the model. Its documentation does not
  mention machine-learning models [TL-10], so it records the inventory against software during loading (T8)
  and does not produce the AI bill of materials (P4). Among the tools surveyed, ModelAudit is the one that
  emits a bill of materials from a model file [TL-04].

What the category cannot do. A verifier shows origin and integrity, not safety: the Hub's own documentation
says a signed commit "does not guarantee that your file is safe, but it does guarantee the origin of the
file" [HF-06]. Signing works only where the producer signed; where nothing is signed, the hash at S1 is
the strongest anchor the later re-reads have (SCRUM-284, section 1.4).

### 2.6 White-box analysis

These tools read the model's internals. They need the file and its hardware, so they work in possession
at S1 and S2 (Table 2). Two things are read for: a hidden trigger (T10; D2), and the refusal mechanism that
carries the safeguard (Q1.6, Q2.3; 2.3).

**Table 8. White-box analysis** (each fact from the tool's repository and paper; source log)

| Tool | Method | Model rows | Access and hardware | Licence | Covers | Source |
|---|---|---|---|---|---|---|
| BAIT | inverts the attack target; a second model judges the inverted sequence | generative | local model, several GPUs, a key for a third-party model service | none | T10; D2 | TL-32, TH-53 |
| PICCOLO | inverts trigger words | classification, transformer text models | local model | none | T10; D2 | TL-33, TH-13 |
| refusal_direction | computes the refusal direction of its paper and reproduces its results | generative | local model and GPU | Apache-2.0 | the safeguard's mechanism, Q1.6, Q2.3; T11 | TL-44, TH-17 |
| TransformerLens | a library for reading and changing a model's internals; no safeguard check of its own | generative | local model and GPU | MIT | none by itself | TL-45 |

- **BAIT** decides whether a large language model is backdoored "by inverting backdoor targets" rather than
  triggers, and uses "a secondary LLM to evaluate whether inverted target sequences contain potentially
  malicious content" (BAIT repository) [TL-32]. Its paper reports top results on the TrojAI model round with
  black-box access (Shen et al., IEEE S&P 2025) [TH-53]; its code runs on local model directories with
  several GPUs and a key for a third-party model service [TL-32]. The repository has no licence [TL-32].
- **PICCOLO** inverts trigger words in transformer classifiers (Liu et al., IEEE S&P 2022) [TH-13]; its
  public code is the authors' competition submission, with no licence and no change since its publication
  (PurduePAML, PICCOLO repository) [TL-33].

- **refusal_direction** is the code that accompanies the paper showing that refusal is mediated by a
  single direction, provided "to reproduce the main results from the paper" (Arditi et al., repository)
  [TL-44; TH-17]. Applied to a selected file and to its adjusted copy, it reads whether the refusal
  mechanism is still there, the internals half of Q2.3. It is research code with no change in the year
  before the evaluation date [TL-44].
- **TransformerLens** is "a library for mechanistic interpretability of generative language models",
  maintained (TransformerLens README) [TL-45]. It gives access to activations; a safeguard check has to be
  written on it.
- **Removal tools are not assessment tools.** The maintained open-source tools that locate refusal
  directions do so to remove them: OBLITERATUS describes itself as a toolkit "for understanding and
  removing refusal behaviors" and Heretic's default action is to "suppress refusals" (READMEs) [TL-46,
  TL-47]. Both are AGPL-3.0. They are how an abliterated model is made, the threat side of Q2.3, and are
  not rows of Table 9.

What the category cannot do. Detection results vary with how the poisoned model was trained (Yan et al.,
EMNLP 2025) [TH-12], and on large language models the best entries of a detection competition were close
to random sampling (Maloyan et al., 2024, preprint) [TH-14]. A scanner gives a statistical verdict with an
error rate, not proof that no trigger is present (threats document, T10).

## Part 3. The comparison table

Table 9 gives every tool surveyed on the five comparison dimensions of 1.3. The versions, licences and statuses are those
published on the evaluation date; each is cited to its source in the source log.

**Table 9. Assessment tooling compared** (evaluation date 18 November 2026; versions as published on that
date, from the package index or the release record named in the source log)

| Tool | Category | Version | Licence | Maturity | Coverage: threats | Coverage: properties and rows | Stages | Operational fit | Source |
|---|---|---|---|---|---|---|---|---|---|
| picklescan | scanner | 1.0.5 | MIT | stable | T3, T6 (pickle); bypasses published [SC-15, SC-16] | every row; pickle and PyTorch archives | S1, S2, S3 | file only; CLI, library, exit codes | TL-01 |
| ModelScan | scanner | 0.8.8 | Apache-2.0 | pre-release | T3, T6 (pickle, H5, SavedModel) | every row; no GGUF, ONNX, safetensors | S1, S2, S3 | file only; CLI, library, CI | TL-02 |
| fickling | scanner | 0.1.13 | LGPL-3.0 | pre-release (beta) | T3, T6 (pickle) | every row; pickle and PyTorch variants | S1, S2, S3; load-time hook | file only; CLI, library | TL-03 |
| ModelAudit | scanner | 0.2.56 | MIT | pre-release (beta) | T3, T5, T6; backdoor indicators claimed, emerging | P4 (emits CycloneDX); every row; pickle, safetensors, GGUF, ONNX, Keras, SavedModel, templates | S1, S2, S3 | file only, credentials for remote stores; CLI, CI; telemetry on by default | TL-04, TL-05 |
| Bandit | scanner (shipped code) | 1.9.4 | Apache-2.0 | stable | T5 code | Python files; every row | S1 | the shipped code only; CLI | TL-35 |
| Semgrep Community Edition | scanner (shipped code) | 1.186.0 | LGPL-2.1 | stable | T5 code | 30 or more languages; every row | S1 | the shipped code only; CLI; registry rules report metrics unless switched off | TL-36 |
| GuardDog | scanner (shipped code, packages) | 3.2.0 | Apache-2.0 | stable | T5 code; T8 malicious packages | every row | S1; S3 | package, directory or requirements file; registry access; CLI | TL-37 |
| pip-audit | scanner (packages) | 2.10.1 | Apache-2.0 | stable | T8 known vulnerabilities | Python environment; every row | S3; re-read S4 | environment or requirements file; advisory database; CLI, CI | TL-38 |
| OSV-Scanner | scanner (packages, container) | 2.7.1 | Apache-2.0 | pre-release (beta) | T8 known vulnerabilities | 11 or more ecosystems; every row | S3; re-read S4 | lockfiles, manifests or image; OSV database; CLI | TL-39 |
| Syft | scanner (packages, container) | 1.57.2 | Apache-2.0 | stable | T8 inventory | P4 for software; every row | S3; re-read S4 | image or filesystem; CLI, library | TL-40 |
| Grype | scanner (packages, container) | 0.122.1 | Apache-2.0 | pre-release | T8 known vulnerabilities | every row | S3; re-read S4 | image, filesystem or bill of materials; vulnerability database; CLI | TL-41 |
| Trivy | scanner (packages, container) | 0.76.2 | Apache-2.0 | pre-release | T8 known vulnerabilities | every row | S3; re-read S4 | image, filesystem or cluster; vulnerability database; CLI; its release channel was compromised once [TL-43] | TL-42, TL-43 |
| garak | red-team | 0.17.1 | Apache-2.0 | pre-release (alpha) | T15, T17, T19 | D1, D4; generative row | S1 to S4; by proxy | endpoint or local model; CLI | TL-11 |
| PyRIT | red-team | 1.2.1 | MIT | pre-release (alpha) | T15, T17; multi-turn | D1; generative row | S1 to S4; by proxy | endpoint, application or browser; CLI, library, GUI | TL-12 |
| promptfoo | red-team | 0.125.1 | MIT | pre-release | T15, T16, T17, T21 | D1; generative row | S1 to S4; by proxy | endpoint, browser or model; CLI, YAML | TL-13 |
| Inspect, inspect_evals | red-team | 0.3.291; 0.29.0 | MIT | pre-release (beta) | T16, T17, T21 | D1, D3; generative row | S1 to S4; by proxy | provider API or local engine; CLI, library | TL-14, TL-15 |
| DeepTeam | red-team | 1.0.10 | Apache-2.0 | stable | T15, T16, T17, T21 | D1; generative row | S1 to S4; by proxy | callback to the system; LLM judge; CLI, YAML, library | TL-16 |
| AgentDojo | red-team | 0.1.35 | MIT | pre-release (beta) | T16, T21 | D1; generative row, agents | S1 to S4; by proxy | model API; CLI, library | TL-21 |
| ART | adversarial | 1.20.1 | MIT | pre-release (alpha) | T9, T18, T20 on the classification row; evasion | D4; classification row; large language models not named | S1, S2 white-box; S1 to S4 black-box | model object or endpoint; library | TL-17 |
| TextAttack | adversarial | 0.3.11 | MIT | pre-release | evasion of text classifiers | D4; classification row | S1, S2 | local model; CLI, library | TL-18 |
| HarmBench | red-team benchmark | no release | MIT | dormant | T17 | D1; generative row, image and text | S1 to S4 | local model or API; scripts, YAML | TL-19 |
| Counterfit | adversarial | 1.1.0 | MIT | retired | T18, T20; evasion | classification row | none: archived | CLI | TL-20 |
| NeMo Guardrails | guard | 0.24.1 | Apache-2.0 | pre-release (beta) | T15, T16, T17, T21 | generative row | S3 assessed; S4 watched | request path; library, server, YAML | TL-22 |
| LlamaFirewall | guard | 1.0.3 | MIT (code); Llama 4 Community (models) | stable | T15, T16, T21; generated code | generative row | S3 assessed; S4 watched | request and agent path; library | TL-23 |
| Llama Prompt Guard 2; Llama Guard 4 | guard (models) | 86M, 22M; 12B | Llama 4 Community | model release: grade not applicable | T15, T17; harmful content | generative row; Guard 4 image and text | S3 assessed; S4 watched | classifier in the path; GPU for 12B | TL-24, TL-25 |
| Guardrails AI | guard | 0.11.0 | Apache-2.0 | pre-release | validators per risk | generative row | S3 assessed; S4 watched | request path; library, server | TL-26 |
| LLM Guard | guard | 0.3.16 | MIT | retired | T15; data leakage | generative row | none: archived | library, API | TL-27 |
| LangKit | monitor | 0.0.35 | Apache-2.0 | dormant | T15, T17 by similarity | generative row | S4 | logging through whylogs | TL-30, TL-31 |
| Vigil | monitor | 0.10.3-alpha | Apache-2.0 | dormant (alpha) | T15, T17 | generative row | S4 | library, REST API | TL-29 |
| Rebuff | monitor | 0.1.1 | Apache-2.0 | retired | T15 | generative row | none: archived | third-party model and vector-store services | TL-28 |
| model-signing | provenance | 1.1.1 | Apache-2.0 | pre-release (alpha) | T7 | P5; every row, every format | S1; re-reads S2 to S4 | files and an identity or key; CLI, library | TL-06 |
| cosign | provenance | 3.1.4 | Apache-2.0 | stable | T7 for containers | P5; the container in service | S3, S4 | identity or key; CLI | TL-07 |
| in-toto | provenance | 3.1.0 | Apache-2.0 | stable | T7, T8 in part (steps of the chain) | P5 | S1 to S4, where each step is recorded | keys per step; CLI, library | TL-09 |
| slsa-verifier | provenance | 2.7.1 | Apache-2.0 | retired | T7 for build outputs | P5 | none: unmaintained | CLI | TL-08 |
| cyclonedx-python | provenance (inventory) | 8.0.1 | Apache-2.0 | stable | T8 inventory only | P4 for software, not the model | S2, S3 | Python environment; CLI | TL-10 |
| BAIT | white-box | no release | none | research code | T10; T13 in principle | D2; generative row | S1, S2 | local model, several GPUs, third-party model key | TL-32, TH-53 |
| PICCOLO | white-box | no release | none | research code, dormant | T10 | D2; classification row | S1, S2 | local model; competition code | TL-33, TH-13 |
| refusal_direction | white-box | no release | Apache-2.0 | research code, dormant | T11, the safeguard removed or weakened | Q1.6, Q2.3 internals; generative row | S1, S2 | local model and GPU; paper code | TL-44, TH-17 |
| TransformerLens | white-box (library) | 4.4.0 | MIT | stable | none by itself | generative row | S1, S2 | local model and GPU; library | TL-45 |

Three readings of Table 9 follow.

- **Maturity is low across the board.** Most maintained tools state an alpha or beta status or sit below
  version 1.0. The stable ones are the general-purpose signing and inventory tools (cosign, in-toto,
  cyclonedx-python), the general code and dependency scanners except OSV-Scanner, Grype and Trivy,
  picklescan, DeepTeam and LlamaFirewall; none of the model-specific provenance or
  white-box tools is stable.
- **Licensing is permissive where code is maintained.** MIT and Apache-2.0 dominate; fickling is LGPL-3.0;
  guard models carry the Llama licence; two of the four white-box tools, BAIT and PICCOLO, carry none, so no organisation may adopt
  them as published [TL-34]; refusal_direction is Apache-2.0 and TransformerLens MIT.
- **Operational fit divides by access.** File scanners and verifiers need only the file; code scanners need only
  the shipped code; dependency scanners need the built environment or container, and an advisory database; red-team frameworks need
  only an endpoint; white-box tools need the file, the hardware to run it and, for BAIT, a third-party
  service. Several red-team frameworks and the white-box scanner rely on another model as a judge.

## Part 4. What the tools cover, and what they do not

Table 10 reads Table 9 the other way: for each threat and testable property, the tools that read for it.
"None" means no tool surveyed names it; "by the chain" means it can be measured only by running a
behavioural tool on the changed file and on its base, and comparing.

**Table 10. Coverage by threat and property**

| Threat or property | Tools that read for it (maintained) | State |
|---|---|---|
| T1 name confusion; T2 account takeover | none | none: platform side, outside these tools |
| T3 malicious serialisation | picklescan, ModelScan, fickling, ModelAudit | covered, evadable [SC-15, SC-16, SC-18] |
| T4 parser exploits | none by name | none |
| T5 code and templates | ModelAudit, for chat templates; Bandit, Semgrep, GuardDog, for shipped code as ordinary Python | in part: general code tools, none specific to model code |
| T6 malicious adapters | the T3 scanners, for pickle adapters | in part |
| T7 revision drift | model-signing, cosign, in-toto | covered where the producer signs |
| T8 software during loading | pip-audit, OSV-Scanner, Grype, Trivy, for known vulnerabilities; GuardDog, for malicious packages; Syft, cyclonedx-python, in-toto, for inventory | covered for known vulnerabilities; in part for malicious packages; only once the environment is built (S3) |
| T9 training-data poisoning | ART, on the classification row | none for generative models |
| T10 backdoors and trojan triggers | BAIT, PICCOLO, unlicensed research code; ModelAudit indicators, emerging | no adoptable tool |
| T11 fine-tune and LoRA tampering | any red-team framework, by the chain | by the chain |
| T12 quantisation-induced drift | any red-team framework, by the chain | by the chain |
| T13 quantisation-triggered backdoors | BAIT in principle | no adoptable tool |
| T14 merge contamination | any red-team framework, by the chain | by the chain |
| T15 direct prompt injection | garak, PyRIT, promptfoo, DeepTeam; guards | covered |
| T16 indirect prompt injection | promptfoo, DeepTeam, AgentDojo, Inspect; LlamaFirewall | covered |
| T17 jailbreaks | garak, PyRIT, promptfoo, DeepTeam, Inspect | covered |
| T18 model extraction | ART | classification row only |
| T19 training-data extraction | garak replay probe | in part |
| T20 membership inference | ART | classification row only; unreliable on large generative models [TH-50] |
| T21 agentic and tool-use abuse | promptfoo, DeepTeam, AgentDojo, Inspect; LlamaFirewall | covered |
| D1 behavioural properties | every red-team framework | covered |
| D2 hidden triggers | as T10 | no adoptable tool |
| D3 capability boundaries | Inspect, through inspect_evals | in part |
| D4 robustness | ART, TextAttack, garak | covered for classifiers; in part for generative |
| D5 latent contamination | none | none |
| The safeguard: present (Q1.6), still present after a change (Q2.3) | outputs: every red-team framework; internals: refusal_direction, research code; TransformerLens, a library without a check | outputs covered; internals: no maintained tool |
| P4 AI bill of materials | ModelAudit | in part |
| P5 signing and attestation | model-signing, cosign, in-toto | covered where adopted |
| Runtime monitoring at S4 | guards used as monitors | no maintained dedicated monitor |

Four gaps stand out, and each is a gap (SCRUM-281) in the sense of the lifecycle assessment framework, a question no
available evidence answers (SCRUM-284, section 2):

- **The model-integrity threats have no adoptable tool.** For backdoors and quantisation-triggered
  backdoors the tools that exist are research code without a licence; for poisoning, tampering and merging
  the only measurement is the chain of behavioural tests across the change.
- **The embedding row has no tool.** No tool surveyed names embedding models.
- **Runtime monitoring has no maintained dedicated tool.** What an organisation can deploy at S4 is a guard
  that logs.
- **The safeguard can be checked from outputs only.** Whether the refusal mechanism is still in the
  weights after an adjustment has no maintained tool; the open tools that find it are made to remove it.

## Part 5. Tools proposed for the demonstration set

The demonstration set (SCRUM-281) is the techniques executed for the report. A tool is proposed for it only
if its row in Table 9 meets four conditions:

1. it is maintained: graded stable or pre-release, not dormant, retired or research code;
2. its licence allows an organisation to run it;
3. it covers a threat or property of Table 10 at a stage where the demonstration can meet its access need;
4. no other maintained tool in its category covers the same threats with fewer dependencies.

**Table 11. Proposals, justified from Table 9**

| Proposed tool | Category | Why, from its Table 9 row | Threats and properties it demonstrates | Stage |
|---|---|---|---|---|
| ModelAudit | scanner | widest format coverage, including GGUF, safetensors, ONNX and templates; MIT; maintained | T3, T5, T6; P4 | S1, S2 |
| picklescan | scanner | the scanner the Hub builds on, so its result is the platform's baseline; MIT; stable | T3, T6 | S1 |
| Bandit | scanner (shipped code) | reads the shipped modelling code, which is Python [SC-08]; stable; Apache-2.0; no external service | T5 code | S1 |
| GuardDog | scanner (shipped code, packages) | the only tool that reads package code for malicious behaviour rather than known flaws; stable; Apache-2.0 | T8 malicious packages; T5 code | S1, S3 |
| pip-audit | scanner (packages) | known vulnerabilities in the Python environment that loads the model; stable; Apache-2.0; maintained under the Python Packaging Authority | T8 known vulnerabilities | S3, re-read S4 |
| model-signing | provenance | the only tool that signs and verifies a model directory file by file; Apache-2.0; maintained | T7; P5; Q1.2, Q3.1 | S1, re-read S3 |
| garak | red-team | endpoint or local model, single-turn probes including training-data replay; Apache-2.0; maintained | T15, T17, T19; D1, D4 | S1 to S4 |
| PyRIT | red-team | the multi-turn strategies no other framework here offers; MIT; maintained | T15, T17; D1 | S1 to S4 |
| AgentDojo | red-team | the agent benchmark behind the research result for indirect injection [TH-51]; MIT; maintained | T16, T21 | S3, S4 |
| ART | adversarial | the only maintained tool for extraction and membership inference, on the classification row; MIT | T9, T18, T20; D4 | S1, S2 |
| LlamaFirewall | guard | code under MIT, components for direct and indirect injection and agent alignment; stable | T15, T16, T21 as a control assessed at S3 | S3, S4 |

Not proposed, with the condition each fails:

- **Retired**: Counterfit, LLM Guard, Rebuff, slsa-verifier (condition 1).
- **Dormant**: HarmBench, LangKit, Vigil (condition 1). HarmBench's behaviours remain citable as a research
  dataset, not as a maintained tool.
- **Dormant research code**: refusal_direction (condition 1); the internals half of Q2.3 is therefore
  demonstrated with a technique reimplemented from its paper [TH-17]. TransformerLens is a library on
  which such a check can be built, not a check (condition 3).
- **Unlicensed research code**: BAIT, PICCOLO (conditions 1 and 2). The demonstration of T10 therefore
  rests on a technique reimplemented from the published paper, or on a licence obtained from the authors,
  not on these repositories as published.
- **Covered by a proposed tool with fewer dependencies**: ModelScan and fickling (by ModelAudit and
  picklescan); Semgrep (by Bandit, for Python, without registry metrics); OSV-Scanner, Grype and Trivy (by
  pip-audit for the Python environment); Syft (inventory without detection); promptfoo, DeepTeam and Inspect (by garak, PyRIT and AgentDojo for the same threats);
  NeMo Guardrails and Guardrails AI (by LlamaFirewall); TextAttack (by ART); cosign, in-toto and
  cyclonedx-python (they sign or inventory the software around the model, not the model) (conditions 3
  and 4).

## Summary: the five questions answered

The survey is desk-based: every statement about a tool is taken from the tool's own documentation or
release record, and no tool was run (1.4).

- **Which kinds of tool exist, and where does each work?** Six categories: the five the survey is asked
  for, artefact and format scanners, red-team and adversarial frameworks, guardrail layers, runtime
  monitors and provenance verifiers, and white-box analysis, which holds the only tools that read a
  model's internals for hidden triggers. Each is placed on the lifecycle stages by the evidence it reads
  (Table 2).
    - Red-team frameworks are the only category that works at every stage, S1 to S4, and by proxy.
    - Runtime monitors work at S4.
    - Scanners work at S1 to S3, on the file, the shipped code, or the packages and container; the package
      scanners re-read at S4.
    - White-box tools need the file and the hardware to run it, and work at S1 and S2.
    - Provenance verifiers anchor at S1 and re-read at S2 to S4.
    - Guardrail layers are controls, assessed with the model at S3 and watched at S4, not methods.
- **What does each tool cover, and what does it need?** Part 2, one table per category, Tables 3 to 8:
  for each tool what it reads, its method and the access it needs, each cited to the tool's own
  documentation. Each category closes with what it cannot do.
- **How do the tools compare?** Table 9 compares every tool surveyed on the five comparison dimensions,
  coverage, lifecycle stage, maturity, licensing and operational fit, with the version of each tool as
  published on the evaluation date, 18 November 2026.
    - Maturity is low: most maintained tools state an alpha or beta status or sit below version 1.0.
    - Licences are permissive, mostly MIT and Apache-2.0, where code is maintained. Two of the four
      white-box tools, BAIT and PICCOLO, carry no licence and cannot be adopted as published.
    - Operational fit divides by access: the file, the shipped code, the built environment, or an
      endpoint.
- **What does no tool cover?** Four gaps (Table 10): the model-integrity threats have no adoptable tool;
  the embedding row has no tool; runtime monitoring has no maintained dedicated tool; and the safeguard
  can be checked from outputs only.
- **Which tools should the demonstration set use?** Eleven: ModelAudit, picklescan, Bandit, GuardDog,
  pip-audit, model-signing, garak, PyRIT, AgentDojo, ART and LlamaFirewall. Each is justified from its row
  of Table 9 against four stated conditions (Table 11), and every tool not proposed is listed with the
  condition it fails. Two demonstrations have no adoptable tool:
    - hidden triggers (T10): BAIT and PICCOLO are unlicensed research code, so the demonstration rests on
      a technique reimplemented from the published paper, or on a licence obtained from the authors;
    - the safeguard read from internals (Q2.3): refusal_direction is dormant research code, so the check
      is reimplemented from its paper [TH-17].

## Annex. The lifecycle questions and evidence items this document uses

The placement of every tool names evidence items, en.k, and some proposals name questions, Qn.k, of the
lifecycle assessment framework (SCRUM-284). Table 12 gives the text of each one used here, in the
framework's own words. n is the stage, S1 to S4; k numbers the questions or items of that stage.

**Table 12. Questions and evidence items cited** (text as in SCRUM-284, stage tables)

| Symbol | Stage | Question, or evidence item and its kind |
|---|---|---|
| Q1.2 | S1 selection | Is the file what the page says it is? |
| Q1.3 | S1 selection | Can loading it harm us? |
| Q1.6 | S1 selection | Does it behave as described, and is the safeguard present? |
| Q2.3 | S2 adjustment | Is the safeguard still present after the change? |
| Q3.1 | S3 deployment | Is the model in service the model we assessed? |
| Q4.1 | S4 runtime detection | Has what deployment fixed been changed since, the model, its serving software or its configuration? |
| e1.1 | S1 selection | guaranteed: producer account, upload date, file hashes |
| e1.3 | S1 selection | guaranteed: the downloaded file's hash or signature against the page |
| e1.4 | S1 selection | readable: format, whole model or adapter, precision, configuration, and the code and templates that ship with the file: custom modelling code, tokenizer, chat template, generation defaults |
| e1.6 | S1 selection | readable: the organisation's own scan of the file |
| e1.8 | S1 selection | guaranteed: gating, where the platform enforces it |
| e1.9 | S1 selection | testable, outputs: behaviour on the organisation's inputs |
| e1.10 | S1 selection | testable, internals: the file's internals while it runs |
| e2.1 | S2 adjustment | readable: the adjusted artefact: format, completeness, precision, and its base hash against e1.3 |
| e2.4 | S2 adjustment | testable, internals: the adjusted weights and activations against the base |
| e2.5 | S2 adjustment | testable, outputs: behaviour on the adjusted model, same inputs as e1.9 |
| e3.1 | S3 deployment | readable: the served artefact's hash, against the file assessed at S1 or S2 |
| e3.3 | S3 deployment | readable: the serving software and its version; the container base image and drivers, or the compiled engine and its hardware target; and the configuration around the model: system prompt, retrieval, tools, guards, serving settings |
| e3.5 | S3 deployment | testable, outputs: behaviour through the deployed endpoint on the organisation's inputs, configuration in place |
| e4.1 | S4 runtime detection | readable: the served artefact's hash, the serving software and the configuration, re-read in service, against e3.1 and e3.3 |
| e4.3 | S4 runtime detection | testable, outputs: the inputs arriving at the endpoint in service, user, retrieved content and tool outputs, and the outputs returned |
| e4.4 | S4 runtime detection | testable, outputs: behaviour on the inputs of e3.5, measured again, against e3.5 |

**Table 13. Threats and properties cited, with where each is defined**

| Symbol | Name | Defined in |
|---|---|---|
| T1 | name confusion and typosquatting | supply-chain document, Part 2, 2.1 |
| T2 | account and name takeover | supply-chain document, Part 2, 2.1 |
| T3 | malicious serialisation | supply-chain document, Part 2, 2.2 |
| T4 | format and parser exploits | supply-chain document, Part 2, 2.2 |
| T5 | code and templates that ship with the model | supply-chain document, Part 2, 2.2 |
| T6 | malicious adapters | supply-chain document, Part 2, 2.2 |
| T7 | revision drift | supply-chain document, Part 2, 2.2 |
| T8 | software installed or executed during loading | supply-chain document, Part 2, 2.3 |
| T9 | training-data poisoning | threats document (SCRUM-288), Part 2 |
| T10 | backdoors and trojan triggers | threats document (SCRUM-288), Part 2 |
| T11 | fine-tune and LoRA tampering | threats document (SCRUM-288), Part 2 |
| T12 | quantisation-induced drift | threats document (SCRUM-288), Part 2 |
| T13 | quantisation-triggered backdoors | threats document (SCRUM-288), Part 2 |
| T14 | merge contamination | threats document (SCRUM-288), Part 2 |
| T15 | direct prompt injection | threats document (SCRUM-288), Part 3 |
| T16 | indirect prompt injection | threats document (SCRUM-288), Part 3 |
| T17 | jailbreaks | threats document (SCRUM-288), Part 3 |
| T18 | model extraction | threats document (SCRUM-288), Part 3 |
| T19 | training-data extraction | threats document (SCRUM-288), Part 3 |
| T20 | membership inference | threats document (SCRUM-288), Part 3 |
| T21 | agentic and tool-use abuse | threats document (SCRUM-288), Part 3 |
| P1 | publisher identity | attestable-and-testable document (SCRUM-289), Part 2 |
| P2 | training-data disclosure | attestable-and-testable document (SCRUM-289), Part 2 |
| P3 | model card | attestable-and-testable document (SCRUM-289), Part 2 |
| P4 | AI bill of materials | attestable-and-testable document (SCRUM-289), Part 2 |
| P5 | cryptographic signing and attestation | attestable-and-testable document (SCRUM-289), Part 2 |
| P6 | licence lineage | attestable-and-testable document (SCRUM-289), Part 2 |
| D1 | behavioural properties | attestable-and-testable document (SCRUM-289), Part 3 |
| D2 | hidden triggers | attestable-and-testable document (SCRUM-289), Part 3 |
| D3 | capability boundaries | attestable-and-testable document (SCRUM-289), Part 3 |
| D4 | robustness | attestable-and-testable document (SCRUM-289), Part 3 |
| D5 | latent contamination | attestable-and-testable document (SCRUM-289), Part 3 |

## Source log

The sources this document adds. Each row gives:

- **ID**: the citation key used in the text.
- **Class** (SCRUM-281): *Official*, a standards or framework body, a regulator, or a party writing about its
  own artefact or service; or *Research*, a paper at an accepted venue, or a preprint labelled as such.
- **Source** and **URL**: what was read and where.
- **Verified**: what was checked in it, and the statement the citation rests on. Every tool row was read on
  the evaluation date, 18 November 2026; its version is the one on the package index or release record named.

| ID | Class (SCRUM-281) | Source | URL | Verified |
|---|---|---|---|---|
| TL-01 | Official | picklescan, README and src/picklescan/scanner.py | https://github.com/mmaitre314/picklescan | [CHECKED] scans "Pickles from local files, directories, URLs, and zip archives"; safe and unsafe globals lists in the source; CLI exit codes; licence MIT; version 1.0.5 on PyPI; no status classifier |
| TL-02 | Official | ModelScan, Protect AI, README | https://github.com/protectai/modelscan | [CHECKED] "ModelScan currently supports: H5, Pickle, and SavedModel formats"; reads the file "one byte at a time"; four severities; CI use; Apache-2.0; version 0.8.8 on PyPI |
| TL-03 | Official | fickling, Trail of Bits, README and pyproject.toml | https://github.com/trailofbits/fickling | [CHECKED] "decompiler, static analyzer, and bytecode rewriter for Python pickle"; symbolic execution; load-time hook with an allow-list; manually added imports trusted; LGPL-3.0; version 0.1.13; "Development Status :: 4 - Beta" |
| TL-04 | Official | ModelAudit, Promptfoo, README and pyproject.toml | https://github.com/promptfoo/modelaudit | [CHECKED] scanners across model, archive and configuration formats incl. pickle, PyTorch, safetensors, GGUF, ONNX, Keras, SavedModel, Jinja2 templates; "No model is ever loaded, unpickled, or executed"; "Potential backdoor indicators"; `--sbom` CycloneDX; "Packaged installs enable telemetry by default"; MIT; version 0.2.56 on PyPI; "4 - Beta" |
| TL-05 | Official | ModelAudit security model, Promptfoo | https://github.com/promptfoo/modelaudit/blob/main/docs/user/security-model.md | [CHECKED] "A clean scan means "no known indicators were found," not "risk is zero.""; "runtime-only backdoors and environment-triggered logic may not be visible" |
| TL-06 | Official | model-transparency (model-signing), Sigstore, README and pyproject.toml | https://github.com/sigstore/model-transparency | [CHECKED] "a list of (file path, digest) pairs"; verification recomputes "the model's file hashes again"; OIDC, keys, certificates, PKCS #11; "integrity and provenance"; Apache-2.0; version 1.1.1 on PyPI; "3 - Alpha" |
| TL-07 | Official | cosign, Sigstore, README | https://github.com/sigstore/cosign | [CHECKED] "Signing OCI containers (and other artifacts)"; in-toto attestations; keyless by default; "only a weak reference back to the object they "sign""; Apache-2.0; release v3.1.4 |
| TL-08 | Official | slsa-verifier, SLSA, README | https://github.com/slsa-framework/slsa-verifier | [CHECKED] verifies "the cryptographic signatures on provenance"; "This project is no longer actively maintained."; Apache-2.0; release v2.7.1 |
| TL-09 | Official | in-toto (Python reference implementation), README, LICENSE and pyproject.toml | https://github.com/in-toto/in-toto | [CHECKED] "verifying that each task in the chain is carried out as planned, by authorized personnel only"; artefacts allowed unless disallowed; licence file Apache-2.0 (the GitHub API reports NOASSERTION); release v3.1.0; "5 - Production/Stable" |
| TL-10 | Official | cyclonedx-python, OWASP CycloneDX, README | https://github.com/CycloneDX/cyclonedx-python | [CHECKED] data sources: Python environment, Poetry, Pipenv, requirements.txt; no mention of machine-learning models; Apache-2.0; release v8.0.1; "5 - Production/Stable" |
| TL-11 | Official | garak, NVIDIA, README and PyPI | https://github.com/NVIDIA/garak | [CHECKED] "probes for hallucination, data leakage, prompt injection, misinformation, toxicity generation, jailbreaks"; REST or local Hugging Face model; leakreplay probe; "using the vulnerability detectors recommended by each probe", a failure rate per probe; report and hit log; Apache-2.0; version 0.17.1; "3 - Alpha" |
| TL-12 | Official | PyRIT, Microsoft AI Red Team, README, documentation and the archived former repository | https://github.com/microsoft/PyRIT ; https://microsoft.github.io/PyRIT/latest/ ; https://github.com/Azure/PyRIT | [CHECKED] "security and safety weaknesses in generative AI systems through automated scans, adaptive multi-turn attacks, and human-led testing"; Crescendo, TAP; HTTP, WebSockets, Playwright; scorers "true/false, Likert scale, classification, and custom scorers, powered by LLMs, Azure AI Content Safety, or your own logic"; former repository archived, "PyRIT has moved!"; MIT; version 1.2.1 on PyPI; "3 - Alpha" |
| TL-13 | Official | promptfoo, red-team documentation and README | https://www.promptfoo.dev/docs/red-team/ ; https://github.com/promptfoo/promptfoo | [CHECKED] indirect prompt injections; PII leaks from context; "misuse of connected APIs or databases (in agents)"; HTTP API, browser or direct model access; YAML configuration; outputs evaluated "using deterministic and model-graded metrics"; "Promptfoo is now part of OpenAI. Promptfoo remains open source and MIT licensed."; version 0.125.1 on npm |
| TL-14 | Official | Inspect, UK AI Security Institute, README | https://github.com/UKGovernmentBEIS/inspect_ai | [CHECKED] "a framework for large language model evaluations created by the UK AI Security Institute"; tool use, multi-turn, model-graded evaluations; MIT; version 0.3.291 on PyPI; "4 - Beta" |
| TL-15 | Official | inspect_evals, README and task directory | https://github.com/UKGovernmentBEIS/inspect_evals | [CHECKED] tasks incl. agentdojo, agentharm, strong_reject, cyberseceval_2 to 4, cybench, wmdp; MIT; version 0.29.0 on PyPI; "4 - Beta" |
| TL-16 | Official | DeepTeam, Confident AI, README | https://github.com/confident-ai/deepteam | [CHECKED] "jailbreaking, prompt injection, multi-turn exploitation … in your AI agents, RAG pipelines, and chatbots"; excessive agency, tool metadata poisoning; `model_callback`; "LLM-as-a-Judge metrics"; guardrails mode; Apache-2.0; version 1.0.10 on PyPI |
| TL-17 | Official | Adversarial Robustness Toolbox, LF AI & Data, README and attacks documentation | https://github.com/Trusted-AI/adversarial-robustness-toolbox ; https://adversarial-robustness-toolbox.readthedocs.io/en/latest/modules/attacks.html | [CHECKED] "Evasion, Poisoning, Extraction, and Inference … (classification, object detection, speech recognition, generation, certification, etc.)"; large language models not named; white-box and no-access attacks distinguished; MIT; version 1.20.1; "3 - Alpha" |
| TL-18 | Official | TextAttack, QData, README and documentation | https://github.com/QData/TextAttack | [CHECKED] "adversarial attacks, data augmentation, and model training in NLP"; classification and sequence-to-sequence; gradient-based search among recipes; MIT; release v0.3.11 |
| TL-19 | Official | HarmBench, Center for AI Safety, README | https://github.com/centerforaisafety/HarmBench | [CHECKED] "evaluating automated red teaming methods and LLM attacks/defenses"; transformers models, closed APIs, multimodal models; judge classifiers; no release; last change August 2024; MIT |
| TL-20 | Official | Counterfit, Microsoft, README | https://github.com/Azure/counterfit | [CHECKED] "brings several existing adversarial frameworks under one tool"; repository archived; no successor named; MIT; release v1.1.0 |
| TL-21 | Official | AgentDojo, ETH Zurich and Invariant Labs, README | https://github.com/ethz-spylab/agentdojo | [CHECKED] "A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents"; "the API of the package is still under development and might change in the future"; MIT; release v0.1.35; "4 - Beta" |
| TL-22 | Official | NeMo Guardrails, NVIDIA, README and LICENSE | https://github.com/NVIDIA-NeMo/Guardrails | [CHECKED] "model-backed checks for jailbreaks, injected instructions, and unsafe tool calls"; YAML rails, Python actions; library or server; licence file Apache-2.0 (the GitHub API reports NOASSERTION); version 0.24.1; "4 - Beta" |
| TL-23 | Official | LlamaFirewall, Meta, README and LICENSE in PurpleLlama | https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall | [CHECKED] "flexible, real-time guardrail framework"; Prompt Guard 2 "detects direct prompt injection attempts"; AlignmentCheck "goal hijacking, indirect prompt injections, and signs of agent misalignment"; CodeShield; can "scan entire conversation traces"; code MIT, models under their Llama licences; version 1.0.3 on PyPI |
| TL-24 | Official | Llama Prompt Guard 2, Meta, model card and LICENSE | https://github.com/meta-llama/PurpleLlama/tree/main/Llama-Prompt-Guard-2 | [CHECKED] 86M and 22M classifiers to "detect both prompt injection and jailbreaking attacks"; "Vulnerability to Adaptive Attacks"; Llama 4 Community Licence |
| TL-25 | Official | Llama Guard 4, Meta, model card and LICENSE | https://github.com/meta-llama/PurpleLlama/tree/main/Llama-Guard4 | [CHECKED] "natively multimodal safety classifier with 12 billion parameters"; Llama 4 Community Licence |
| TL-26 | Official | Guardrails AI, README | https://github.com/guardrails-ai/guardrails | [CHECKED] "Input/Output Guards in your application that detect, quantify and mitigate the presence of specific types of risks"; library or server; notice discontinuing hosted remote inference; Apache-2.0; release v0.11.0 |
| TL-27 | Official | LLM Guard, Protect AI, README | https://github.com/protectai/llm-guard | [CHECKED] "THIS PROJECT HAS BEEN ARCHIVED"; "no longer under active development or maintained"; repository archived; MIT; version 0.3.16 on PyPI |
| TL-28 | Official | Rebuff, Protect AI, README | https://github.com/protectai/rebuff | [CHECKED] heuristics, model-based detection, vector store, canary tokens; OpenAI and Pinecone keys; "still a prototype"; repository archived; Apache-2.0; release v0.1.1 |
| TL-29 | Official | Vigil, README | https://github.com/deadbits/vigil-llm | [CHECKED] "assessing Large Language Model prompts and responses against a set of scanners"; "currently in an alpha state and should be considered experimental / for research purposes"; last change January 2024; Apache-2.0; release v0.10.3-alpha |
| TL-30 | Official | LangKit, WhyLabs, README | https://github.com/whylabs/langkit | [CHECKED] "open-source text metrics toolkit for monitoring language models"; whylogs; last change November 2024; not archived; Apache-2.0; version 0.0.35 |
| TL-31 | Official | WhyLabs, company website | https://whylabs.ai | [CHECKED] "WhyLabs, Inc. is discontinuing operations"; platform open-sourced |
| TL-32 | Official | BAIT, authors' repository, README and doc/UPDATE.md | https://github.com/SolidShen/BAIT | [CHECKED] "by inverting backdoor targets"; "a secondary LLM to evaluate whether inverted target sequences contain potentially malicious content"; local model directories, GPUs, OpenAI API key; no licence file; no release; setup.py version 2.0.0 |
| TL-33 | Official | PICCOLO, PurduePAML, README | https://github.com/PurduePAML/PICCOLO | [CHECKED] "the code of PICCOLO submission to TrojAI rounds 5 to 7"; no licence; last change December 2022 |
| TL-34 | Official | Licensing a repository, GitHub Docs | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository | [CHECKED] "without a license, the default copyright laws apply, meaning that you retain all rights to your source code and no one may reproduce, distribute, or create derivative works from your work" |
| TL-35 | Official | Bandit, PyCQA, README and PyPI | https://github.com/PyCQA/bandit | [CHECKED] "a tool designed to find common security issues in Python code"; "processes each file, builds an AST from it, and runs appropriate plugins against the AST nodes"; Apache-2.0; version 1.9.4 on PyPI; "5 - Production/Stable"; no mention of model files |
| TL-36 | Official | Semgrep, README and PyPI | https://github.com/semgrep/semgrep | [CHECKED] 30 or more languages; "Semgrep Community Edition will miss many true positives as it can only analyze code within the boundaries of a single function or file"; registry configuration "reports pseudonymous rule metrics to semgrep.dev", `--metrics=off`; LGPL-2.1; version 1.186.0 on PyPI; no mention of model files |
| TL-37 | Official | GuardDog, Datadog, README | https://github.com/DataDog/guarddog | [CHECKED] "identifies malicious PyPI and npm packages, Go modules, Rust crates, RubyGems, GitHub actions, or VSCode extensions"; "static analysis on package source code (through YARA rules)"; threat indicators alone "might be false positives"; local archive, directory and requirements-file scans; Apache-2.0; version 3.2.0 on PyPI; no mention of model files |
| TL-38 | Official | pip-audit, Python Packaging Authority, README | https://github.com/pypa/pip-audit | [CHECKED] "scanning Python environments for packages with known vulnerabilities"; Python Packaging Advisory Database; environments and requirements files; security model: "not a static code analyzer. It analyzes dependency trees, not code"; "If you wouldn't `pip install` it, you should not `pip audit` it"; Apache-2.0; version 2.10.1 on PyPI; "5 - Production/Stable" |
| TL-39 | Official | OSV-Scanner, Google, README | https://github.com/google/osv-scanner | [CHECKED] "find existing vulnerabilities affecting your project's dependencies"; lockfiles, manifests, container images; OSV database; "the latest OSV-Scanner V2 beta"; Apache-2.0; release v2.7.1 |
| TL-40 | Official | Syft, Anchore, README | https://github.com/anchore/syft | [CHECKED] "generating a Software Bill of Materials (SBOM) from container images and filesystems"; CycloneDX, SPDX; "signed SBOM attestations using the in-toto specification"; Apache-2.0; release v1.57.2 |
| TL-41 | Official | Grype, Anchore, README | https://github.com/anchore/grype | [CHECKED] "Scan container images, filesystems, and SBOMs for known vulnerabilities"; Apache-2.0; release v0.122.1 |
| TL-42 | Official | Trivy, Aqua Security, README | https://github.com/aquasecurity/trivy | [CHECKED] targets: container image, filesystem, Git repository, virtual machine image, Kubernetes; finds packages (SBOM), vulnerabilities, misconfigurations, secrets, licences; Apache-2.0; release v0.76.2 |
| TL-43 | Official | GHSA-69fq-xp46-6x23, "Trivy ecosystem supply chain temporarily compromised"; Aqua Security | https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23 | [CHECKED] "a threat actor used compromised credentials to publish a malicious Trivy v0.69.4 release", force-pushed version tags of trivy-action to credential-stealing malware, and published malicious container images; malicious components removed |
| TL-44 | Official | refusal_direction, authors' repository (Arditi et al.), README | https://github.com/andyrdt/refusal_direction | [CHECKED] "code and results accompanying the paper "Refusal in Language Models Is Mediated by a Single Direction""; "we provide code to reproduce the main results from the paper"; Apache-2.0; no release; last change June 2025 |
| TL-45 | Official | TransformerLens, README and PyPI | https://github.com/TransformerLensOrg/TransformerLens | [CHECKED] "A Library for Mechanistic Interpretability of Generative Language Models"; MIT; version 4.4.0 on PyPI; no status classifier |
| TL-46 | Official | OBLITERATUS, README | https://github.com/elder-plinius/OBLITERATUS | [CHECKED] "toolkit for understanding and removing refusal behaviors from large language models"; probes hidden states "to locate refusal directions"; AGPL-3.0; release v0.1.4 |
| TL-47 | Official | Heretic, README | https://github.com/p-e-w/heretic | [CHECKED] "Remove censorship"; "Suppress refusals/remove censorship" as the default action; AGPL-3.0; release v2.1.0 |
| TL-48 | Research | Bereska, Gavves. "Mechanistic Interpretability for AI Safety: A Review". Transactions on Machine Learning Research (TMLR) 2024; arXiv:2404.14082 | https://arxiv.org/abs/2404.14082 | [CHECKED] abstract: mechanistic interpretability is "reverse engineering the computational mechanisms and representations learned by neural networks into human-understandable algorithms and concepts"; reviews its relevance to AI safety, and its challenges of scalability and automation; accepted to TMLR per the arXiv record |

## Symbols from outside this document

| Symbol | Meaning | Defined in | File |
|---|---|---|---|
| (SCRUM-281) after a term | the term is a glossary term; shown at its first use in each part | SCRUM-281, report style guide and glossary, version 1.3, section 1 | governing/report-style-guide-and-glossary.md |
| established, emerging, forecast; Official, Research | confidence labels; citation classes | SCRUM-281, sections 2.2 and 2.3 | governing/report-style-guide-and-glossary.md |
| static, dynamic, behavioural, provenance | test families | SCRUM-281, section 1.4; placed on stages in SCRUM-284, section 1.4, Table 3 | process/scrum-284/scrum284.md |
| S1 to S4; Qn.k; en.k | lifecycle stages, questions and evidence items; those used given in full in Table 12 | SCRUM-284, Notation and stage tables | process/scrum-284/stage-tables.md |
| (SCRUM-284) section 1.4; stage tables, section M | the mapping rule; the tooling kinds placed on stages | SCRUM-284 | process/scrum-284/scrum284.md; process/scrum-284/stage-tables.md |
| (SCRUM-284) section 2 | the gap rule | SCRUM-284 | process/scrum-284/scrum284.md |
| classification, embedding, generative rows | segmentation of model types | SCRUM-280, Table 4 | process/scrum-280/scrum280.md |
| T1 to T8; "the supply-chain document"; [SC-nn] | supply-chain threats and their sources | supply-chain document | process/huggingface/hub-supply-chain-threats.md |
| T9 to T21; "the threats document"; [TH-nn] | model-integrity and inference-time threats and their sources | SCRUM-288 | process/scrum-288/scrum288.md |
| P1 to P6; D1 to D5; "the attestable-and-testable document" | attestable properties; properties discoverable only by testing | SCRUM-289 | process/scrum-289/scrum289.md |
| [HF-nn] | Hugging Face sources | SCRUM-280 | process/scrum-280/scrum280.md |
