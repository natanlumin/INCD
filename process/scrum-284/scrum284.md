# SCRUM-284: the lifecycle assessment framework

Version 1, 12 October 2026. Research cut-off and access date 12 October 2026.

Section 1 is the drafted subsection for the skeleton's 6.1, with the figure and the summary tables. The full
stage tables, one question table and one evidence inventory per stage, are in `stage-tables.md` and enter
the report with this subsection; they are numbered Table 4 onward at assembly. Section 2 is what the
blocked items take from here. Section 3 is the source log. Vocabulary and sources follow the report style
guide (SCRUM-281); citations in brackets resolve to rows of section 3 or, with a platform prefix, to the
SCRUM-280 log.

## 1. Lifecycle assessment framework

### 1.1 What the framework is

An organisation that takes an open-source model into use answers questions about it at four points: when
it selects the model, when it adjusts it, when it deploys it, and while it runs. The glossary names these
the lifecycle stages. The framework fixes, for each stage, which questions are answered there, who can
answer them, and what evidence exists at that point to answer them with. Everything the report says later
about assessment methods and acceptance criteria attaches to one of these stages.

The framework rests on one observation about evidence. What can be known about a model at any stage is
one of four kinds, and the kind decides the rest: who can answer, whether the answer exists when the
organisation holds the file and when it holds only a key, and which test family produces it. The kinds are
the glossary's attestable properties split by who vouches for them, and its testable properties:

- guaranteed: the platform enforces or verifies it. Account identity, upload dates, file hashes and commit
  history, scan results, gating [HF-05, HF-06, HF-11, HF-12, HF-15];
- declared: the producer states it about the model, or the serving provider about an endpoint, and nothing
  verifies it. The model card's parent, training data and licence are free-text or optional fields; the
  licence may be left blank and the card itself is best practice, not a requirement [HF-14, HF-15];
- readable: read from the artefact itself, or from the organisation's own deployment of it. Format,
  precision, completeness, and the code and templates that ship with the file;
- testable: established only by running the model. Outputs, measured black-box through a file or a key;
  internals, measured white-box, which needs the file.

**Table 1. The evidence kind decides the rest** (verified against the stage tables, 12 October 2026)

| Evidence kind | Who answers | Exists in possession | Exists by proxy | Test family |
|---|---|---|---|---|
| guaranteed | the platform | yes | no: the guarantee does not travel with the key | provenance |
| declared | the producer, about the model; by proxy also the serving provider, about the endpoint | yes, as a statement | yes, as a statement | none: nothing verifies it, so it is recorded as an assessment gap |
| readable | the organisation, from the file or its own deployment | yes | no | static |
| testable, outputs | the organisation, by running or calling the model | yes | yes, black-box | behavioural |
| testable, internals | the organisation, by running the file | yes | no: white-box needs the file | dynamic |

Two consequences follow at every stage. By proxy, the organisation can establish only declared statements
and black-box behaviour; the static, dynamic and provenance families drop out. And a declared item is a
gap under both access states, so the gaps of the framework are exactly the declared items.

### 1.2 The access line

Whether the organisation holds the file or only a key is the glossary's in possession and by proxy. The
framework treats it as a line, H, decided once, at or before deployment, and in force for every stage
after. Above the line the four stages are the same for everyone; below it, the evidence that exists at
each stage is read off Table 1. A serving provider's endpoint sold beside a repository is the common case
of a key to a model that also exists as a file [HF-18]; the framework does not assume the two are the same
model, which is why the question returns at deployment.

### 1.3 The four stages

**Figure 1. Lifecycle assessment framework** (working figure, 12 October 2026; question texts in the stage tables)

![Lifecycle assessment framework](lifecycle-framework-template.png)

**Table 2. The four stages: questions, answerers, evidence** (derived from the stage tables, 12 October 2026)

| Stage | Questions | Who answers | Evidence added at the stage, by kind | Families that run |
|---|---|---|---|---|
| S1 Selection | Q1.1 Where does the model live and who published it?<br>Q1.2 Is the file what the page says it is?<br>Q1.3 Can loading it harm us?<br>Q1.4 May we use it?<br>Q1.5 Which row and column of the segmentation is it, and so which threats apply?<br>Q1.6 Does it behave as described, and is the safeguard present? | platform, producer, organisation | 10 items: guaranteed, declared, readable, testable, outputs, testable, internals | static, dynamic, behavioural, provenance |
| S2 Adjustment | Q2.1 What was changed, and from which base?<br>Q2.2 Did the change carry in anything we did not intend?<br>Q2.3 Is the safeguard still present after the change?<br>Q2.4 Is the adjusted artefact still what the segmentation says, and does it still do what the base was selected for? | organisation; the party that made the change | 5 items: declared, readable, testable, outputs, testable, internals | static, dynamic, behavioural |
| S3 Deployment | Q3.1 Is the model in service the model we assessed?<br>Q3.2 What surrounds the model, and does it change what the model does?<br>Q3.3 Does the deployed system give the outputs the assessed model gave on the same inputs?<br>Q3.4 Who can reach the model and its file? | organisation; serving provider by proxy | 7 items: declared, readable, testable, outputs | static, behavioural |
| S4 Runtime detection | Q4.1 Has what deployment fixed been changed since, the model, its serving software or its configuration?<br>Q4.2 Are the inputs arriving in service turning the model against its use, and does it comply?<br>Q4.3 Does the model still give the outputs it gave at deployment?<br>Q4.4 Who is reaching the model and its file, and how much? | organisation; serving provider by proxy | 6 items: declared, readable, testable, outputs | static, behavioural |

Selection is the only stage at which the platform is present, so it is the only stage with guaranteed
evidence and the only one at which the provenance family runs. It is also where the two code-execution
paths of a file are met: a pickle-serialised artefact, which the platforms scan but do not block [HF-06],
and custom modelling code that the file asks the loading library to run, which the library refuses unless
the organisation opts in [LC-01].

Adjustment is the organisation's own change, or one it has a platform or redistributor make at its
request: fine-tuning, an adapter, a merge, quantisation, conversion, or a change to the code and templates
that execute the weights. The adjusted copy exists only for the organisation, with no public page or
identifier, so the producer's declared statements are replaced by the organisation's own readable record,
the one place in the framework where that replacement happens. A fine-tune or quantised copy another party
has published is a different model, met at selection.

Deployment fixes what surrounds weights that no longer change: the serving software, the configuration,
often called the harness or scaffolding, and who may reach the model. The model is assessed with these in
place, because they change what the deployed system does without changing the model. Deployment is also
where the access line is settled at the latest, and where, by proxy, the selection questions about the file
return with the serving provider answering in the producer's place: the served hash cannot be read, and the
serving provider's model identifier and version is all that stands for it.

Runtime detection has no entry event and no end. It watches two things: whether what deployment fixed is
still in place, and what the model does on inputs the organisation did not write. Nothing is set here; a
change it finds returns the model to the stage that owns it. By proxy the freeze on the model and its
configuration is a serving provider's statement, and providers retire and replace versions on published
schedules [CG-10], so the first job of the stage by proxy is to find a change that was not announced, and
the only evidence that can do so is behaviour on the same inputs as before. The inference-time and runtime
threats of the taxonomy are seen here, and only here, as inputs given and outputs returned.

### 1.4 Methods to stages

A method reads one evidence kind. It maps to every stage whose inventory holds an item of that kind, at
which its access need is met, and the mapping is never empty, because every kind occurs at selection.

**Table 3. Test family to stage** (derived from the stage inventories, 12 October 2026)

| Family | Reads | In possession | By proxy |
|---|---|---|---|
| static | readable | S1, S2, S3, S4 | none |
| dynamic | testable, internals | S1, S2 | none |
| behavioural | testable, outputs | S1, S2, S3, S4 | S1, S2, S3, S4 |
| provenance | guaranteed | S1 | none |

By proxy the whole framework rests on the behavioural family and on declared statements. The dynamic and
provenance families are front-loaded: internals are measured only while the organisation holds a file it
has not yet put behind serving software, and guarantees exist only where the platform is. The tooling
kinds the report compares later, scanners, provenance verifiers, red-team frameworks, runtime monitors,
are placed by the same rule in `stage-tables.md`, section M; a guard is not among them, because it is a
control assessed with the model, not a method that assesses it.

## 2. What the blocked items take from here

- The stage labels S1 to S4 and the question numbers Qn.k, used as the row keys of the method coverage by
  stage and of the acceptance criteria per stage.
- The mapping rule of 1.4: a method is placed by the evidence kind it reads, and a method whose access
  need is not met at a stage does not map to that stage.
- The gap rule: every declared item is a gap, listed per stage in the evidence inventories.
- The measurement chain e1.9, e2.5, e3.5, e4.4: the same inputs at every stage, which is what makes the
  acceptance criteria comparable from selection to runtime.

## 3. Source log

Platform-prefixed citations (HF-, CG-) resolve to the SCRUM-280 log, section 3 of `../scrum-280/scrum280.md`,
research cut-off 6 October 2026. Entries added by this item:

| ID | Source | URL | Date or version on page | Verified |
|---|---|---|---|---|
| LC-01 | Customizing models (custom code on the Hub); Transformers documentation; Hugging Face | https://huggingface.co/docs/transformers/custom_models | v5.19.0 | [CHECKED] a model whose modelling code is not in the library loads only with trust_remote_code=True in from_pretrained(); the code in the repository then runs on load |

Uncited: the stage definitions, the four evidence kinds and the mapping rule are the authors' own
construction on the glossary's rows and carry no source; the glossary rows used are lifecycle stage,
attestable and testable properties, guaranteed metadata, in possession, by proxy, producer, redistributor,
test family, acceptance criterion, gap, safeguard and guard, threat.
