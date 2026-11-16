# Attestable and testable properties of an open-source model

## What this document answers

An organisation that takes an open-source model (SCRUM-281) into use wants to know things about it: who
published it, what it was trained on, what it may be used for, whether the file (SCRUM-281) is the one
published, and how it behaves. Some of these it can establish without running the model, from what the
producer (SCRUM-281) and the platform expose. The rest it can establish only by running the model. A few it
cannot establish at all.

- **Attestable properties: read, not run.**
    - They come from the platform, the producer, a signature or a record that travels with the file.
    - Each rests on someone's word or on a cryptographic check, and their strength differs widely.
- **Properties discoverable only by testing: run, not read.**
    - They are behaviour, hidden triggers, capability boundaries, robustness and latent contamination.
    - No metadata reveals them, because no one who writes metadata knows them, or because the one who does
      has a reason not to say.
- **The split is the reason testing is necessary.**
    - Everything the organisation needs to know about how the model behaves lies on the second side.
    - What lies on the first side is, at its strongest, a statement of who published the file and that it
      has not changed since.

This document answers four questions, one per row of Table 1.

**Table 1. The questions this document answers, and where**

| Question | What the document gives | Where |
|---|---|---|
| What can be established about a model without running it, and how strongly? | an evidence-strength rating for each attestable property, with the reason and its sources | 1.3; Part 2; Table 2 |
| What can be established only by running it? | an entry for each property no metadata reveals, with how it is tested and where the test stops | Part 3 |
| Which side of the line is each property on? | one table placing every property on the public or the discoverable side, with who answers and what exists by proxy | Part 4, Table 3 |
| What can be established neither way today? | a short statement, each item cited | Part 5 |

The contributions, stated once:

- **A rating for every attestable property**, on one scale, so that a reader can see which signals carry
  weight and which carry only the publisher's word.
- **The complement, property by property**, tied to the threats each property would reveal, so that the
  testing methodology answers named threats rather than a general concern.
- **One split table** that a reader can use at selection to see what to ask for and what to test.
- **A plain statement of the limit**: what no one can currently establish about an open-source model, by
  reading or by testing.

**Scope.** The properties of an open-source model that an organisation may want established before or during
its use. The threats those properties bear on are treated in the model-integrity and inference-time threats
document, referred to here as the threats document; its threats are numbered T9 to T21 and cited here as
such. The evidence kinds and lifecycle stages (SCRUM-281) are those of the lifecycle assessment framework (SCRUM-284).

**Structure.** Part 1 fixes the split and the rating scale. Part 2 gives the six attestable properties.
Part 3 gives the five properties discoverable only by testing. Part 4 is the split table. Part 5 states what
is neither attestable nor practically testable. A closing summary answers the four questions of Table 1, and
an annex gives the text of every lifecycle question and evidence item cited.

**Symbols.** Terms, stage and question numbers, citation prefixes and table references that come from outside
this document are listed, with where each is defined, in "Symbols from outside this document" after the
source log.

## Part 1. The split and how strength is rated

### 1.1 Where the line falls

The glossary distinguishes attestable properties, established from what publisher and platform expose, from
testable properties, which no metadata reveals (SCRUM-281, section 1.4). The lifecycle assessment framework
splits the attestable side by who vouches for it, and the testable side by what is measured (SCRUM-284,
section 1.1, Table 1):

- **guaranteed**: the platform enforces or verifies it;
- **declared**: the producer (SCRUM-281) states it about the model, or the serving provider (SCRUM-281) about the
  endpoint, and nothing verifies it;
- **readable**: read from the artefact itself, or from the organisation's own deployment of it, with no one's
  word in between;
- **testable**: established only by running the model, on its outputs or on its internals.

A cryptographic signature is a fifth case that the organisation can check itself: whoever holds the key
vouches for the file (SCRUM-281), and the check of the signature against the key is the organisation's own. It is
treated here as attestable and rated on its own terms.

### 1.2 What the line depends on

Two things move a property across the line or remove it.

- **Access.** By proxy (SCRUM-281), only declared statements and black-box behaviour exist; the platform's
  guarantees, the file and its signatures do not travel with the key (SCRUM-284, Table 1). A property that is
  readable in possession (SCRUM-281) becomes, by proxy (SCRUM-281), the serving provider's statement.
- **Derivation.** A derivative model (SCRUM-281) declares its parent on its card, and the platform does not
  verify the relation (SCRUM-286, section 1.1). Every attestable property of the parent, its licence, its
  training-data statement, its signature, says nothing about the derivative unless the derivative carries its
  own.

### 1.3 The evidence-strength rating

Each attestable property is rated on four levels. The rating is of the evidence the property can offer at
best, with the reason stated; where the property is often absent, the entry says so.

| Rating | Meaning |
|---|---|
| strong | the organisation can verify it itself: a cryptographic check against a known key, or a fact the platform guarantees |
| moderate | the record's presence and form can be checked, a structured field or a standard format, but its content is the publisher's statement |
| weak | free text or optional fields, unverified, and in the literature often absent, incomplete or wrong |
| none | nothing exists to check |

Each entry also tags the lifecycle stage (SCRUM-281) at which the property is read, and the framework
question and evidence item it answers, Qn.k and en.k (SCRUM-284), given in full in the annex, Table 4.

## Part 2. Attestable properties

Six properties can be established, to a degree, without running the model. They are treated in the order the
assessment of a model meets them.

### P1. Publisher identity

*Read at: S1, Q1.1, on e1.1 and e1.2 (SCRUM-284).*

The repository guarantees which account uploaded a file (SCRUM-281) and when (SCRUM-284, section 1.1). It does not
guarantee that the account is the producer (SCRUM-281) whose name appears in the repository's title: organisations group
accounts with no identity-proof step on the documentation page (Hugging Face, Organizations) [SC-29]. The one
verification the platform documents is a badge for organisations on its paid plans that verify a domain name
and require admin approval for members with matching e-mail addresses (Hugging Face, Advanced Security)
[AT-05]. Signed commits bind a commit to a key on the account, treated under P5. A publisher can also plant an
identifying response that only it can trigger, a fingerprint, but a third party can test for it only if the
publisher planted one (Xu et al., NAACL 2024) [AT-25].

**Rating: strong for the uploading account; moderate for an organisation with a verified domain; weak for the
producer behind any other account.**

### P2. Training-data disclosure

*Read at: S1, Q1.1 and Q1.2, on e1.2 (SCRUM-284).*

What a model was trained on is documented, where it is documented at all, by its producer: the practice of a
datasheet records a dataset's motivation, composition and collection process (Gebru et al., Communications of
the ACM 2021) [AT-17], and on the primary repository it is declared on the card, in a datasets field the uploader fills in or leaves
empty (Hugging Face, Model Cards) [AT-04]; among widely used models only a minority fill it (SCRUM-286,
section 2.3). Where card sections are filled, the training section is the most consistently filled and
limitations and evaluation the least (Liang et al., Nature Machine Intelligence 2024) [AT-18], but a filled
section is a statement, not the data. Among major developers, data access, data labour and copyright status
remain systemically opaque (Bommasani et al., TMLR 2025) [AT-19]. Regulation now requires the providers of
general-purpose models, open-source ones included, to publish a sufficiently detailed summary of the content
used for training, on a template that sets a common minimal baseline (EU AI Act, Article 53(1)(d) and 53(2);
European Commission template) [AT-01, AT-02]. The obligation raises how often a statement exists; it does not
make the statement verifiable, and a summary is not the data.

**Rating: weak.** The statement cannot be checked against the file, and whether a given record was in the
training data cannot be tested reliably either (Part 5).

### P3. Model card

*Read at: S1, Q1.5 and Q1.6, on e1.2 (SCRUM-284).*

A model card reports a model's intended use and its evaluation across conditions (Mitchell et al., FAT*
2019) [AT-16]. On the primary model repository (SCRUM-281) it is a README with machine-read metadata, licence,
datasets, base model, which the platform uses for filters and to infer the relation to a parent (Hugging
Face, Model Cards) [AT-04]. The card is best practice, not a requirement (Hugging Face, Getting Started with Repositories) [HF-15]. The structured fields can be
checked for presence and form; their content, the base model included, is the uploader's statement
(SCRUM-286, section 1.1). Whether a declared parent is the real one can be tested in part: black-box
provenance testing identified derived models with high precision where the derivation preserves output
similarity (Nikolic et al. 2025, preprint) [AT-26].

**Rating: moderate for the structured fields; weak for the free text.**

### P4. AI bill of materials

*Read at: S1, Q1.2, on e1.4 where it ships with the file, and S3, Q3.2, on e3.3 for what is deployed
(SCRUM-284).*

**What it is.** A software bill of materials, SBOM, is "a formal record containing the details and supply chain
relationships of various components used in building software"; its minimum data fields name each component,
its supplier, its version, its other identifiers and its relationships, and it is meant to be generated and
read by machine (NTIA, The Minimum Elements for a Software Bill of Materials, 2021) [AT-27]. An AI bill of
materials, AIBOM, applies the same record to a model. The model becomes a component of its own, and the record adds
what software has no equivalent for: the datasets the model was trained and evaluated on, its training
parameters, its intended use and limitations, and its provenance (CycloneDX ML-BOM; SPDX 3.0.1 AI and
Dataset profiles) [AT-06, AT-07].

**The two formats.** A bill of materials is written in a standard format so that tools can produce and check
it; the minimum-elements report names SPDX and CycloneDX among them [AT-27].

- **CycloneDX**, published as an international standard by Ecma International (ECMA-424) [AT-28].
  Machine-learning models have been a component type since its version 1.5, with a model card section recording
  datasets, training parameters and provenance (CycloneDX ML-BOM) [SC-25, AT-06].
- **SPDX**, published as an international standard by ISO and IEC (ISO/IEC 5962:2021, as its maintainers
  state) [AT-29]. Its version 3.0.1 has an AI profile and a dataset profile recording training information,
  limitations, known bias and data collection (SPDX 3.0.1) [AT-07].

**Who asks for one, and who ships one.** The secure development profile for generative and foundation models asks producers to track the
provenance of a model, its components and derivatives, and to consider disclosing the provenance of training
data (NIST SP 800-218A, PS.3.2) [AT-09]. A vendor channel ships one with each image it publishes (NVIDIA NGC)
[CG-11]. How many open-source models (SCRUM-281) ship one is not established.

**Rating: moderate.** The format can be validated; the content is declared by whoever wrote it.

### P5. Cryptographic signing and attestation

*Read at: S1, Q1.2, on e1.3; again at S3, Q3.1, on e3.1 (SCRUM-284).*

A model signature covers a manifest listing every file by its hash, so that a recipient can verify that the
model was published by the expected source and has not been changed since (OpenSSF Model Signing) [AT-10,
AT-11]. A commit on the primary repository is marked verified when it is signed with a key on the uploading
account; unsigned commits carry no status, and git itself does not authenticate commit authors (Hugging Face,
Signing commits with GPG) [AT-03, HF-11]. One vendor signs every model it publishes on its catalogue with the
OpenSSF format (NVIDIA NGC and NIM) [AT-12]; a code platform signs build attestations with Sigstore and
states that they are not a guarantee that an artefact is secure (GitHub artifact attestations) [AT-13]. The
build-provenance standard does not address models or training data (SLSA v1.1) [AT-14]. On the primary model
repository, signatures were close to absent in the year measured, about 0.1 per cent of artefacts, and fewer
than a quarter of those were valid (Schorlemmer et al., IEEE S&P 2024) [AT-23].

**Rating: strong where present, for origin and integrity only.** A valid signature establishes who published
the files and that they are unchanged; it establishes nothing about what the model does, and it is rarely
present.

### P6. Licence lineage

*Read at: S1, Q1.4, on e1.7 (SCRUM-284).*

A licence field can be added to any repository, and `unknown` and `other` are valid values (Hugging Face,
Licenses) [AT-08]; the field may be left blank (Hugging Face, Getting Started with Repositories) [HF-15]. Lineage is the chain of licences from a base model
through its derivatives, and it runs along the declared parent relation, which nothing verifies (P3). On
dataset hosting sites, licences were omitted for more than 70 per cent of datasets and wrong for more than
half (Longpre et al., Nature Machine Intelligence 2024) [AT-20]; licences were found inconsistent between
models and the projects that use them (Jiang et al., MSR 2024) [AT-21], and in about a third of transitions
from a model to an application a restrictive clause was dropped by relicensing (Jewitt et al. 2025, preprint)
[AT-22].

**Rating: weak.**

## Part 3. Properties discoverable only by testing

Five properties no metadata reveals. For each: what it is, why no record carries it, how it is tested, and
where the test stops. Each is tied to the threats of the threats document it would reveal.

### D1. Behavioural properties

*Tested at: S1, Q1.6, on e1.9; S2, Q2.3, on e2.5; S3, Q3.3, on e3.5; S4, Q4.3, on e4.4 (SCRUM-284).*

What the model does on the inputs the organisation will give it: whether it follows instructions, refuses
what its safeguard (SCRUM-281) should refuse, and gives the outputs it gave when assessed. A card states an
intended use (Mitchell et al., FAT* 2019) [AT-16]; it cannot state behaviour on inputs its writer never saw. Behaviour is measured
black-box, through a file (SCRUM-281) or a key, on the same inputs at every stage, which is what makes stages comparable
(SCRUM-284, section 2). It reveals quantisation drift and fine-tune tampering against the parent (T11, T12)
and the susceptibility half of direct injection and jailbreaks (T15, T17). The test covers the inputs sent.

### D2. Hidden triggers

*Tested at: S1, Q1.6, on e1.9 and e1.10; S2, Q2.2, on e2.4 and e2.5 (SCRUM-284).*

Behaviour that appears only on a trigger the planter chose (T10), including one that appears only once the
model is quantised (T13). No record carries it, since the only party who knows it is the one who planted it.
A search can find a trigger in a classifier (Liu et al., IEEE S&P 2022) [TH-13]; in generative models,
recovering a planted trigger is close to random (Maloyan et al. 2024, preprint) [TH-14], and detectors fail
when the backdoor is trained differently (Yan et al., EMNLP 2025) [TH-12]. A quantisation trigger is found, if
at all, by testing the quantised copy against full precision. The test can find a trigger; it cannot show
that none is there.

### D3. Capability boundaries

*Tested at: S1, Q1.6, on e1.9 and e1.10; S2, Q2.3, on e2.5 (SCRUM-284).*

What the model can do when pushed, harmful capabilities included, as opposed to what it does when asked
plainly. The producer (SCRUM-281) may state a boundary; the statement is declared. A test elicits the capability and
gives a lower bound: models can be made to underperform on capability evaluations on purpose, and models
trained to hide a capability behind a password kept it hidden on a hazardous-knowledge benchmark, so that
capability evaluations are vulnerable to this underperformance (van der Weij et al., ICLR 2025) [AT-24]. The
safeguard's boundary moves under jailbreaks (T17) and is removed by tampering (T11).

### D4. Robustness

*Tested at: S1, Q1.6, on e1.9 and e1.10; S2, Q2.3 and Q2.4, on e2.5 (SCRUM-284).*

Whether the model's behaviour holds under adversarial inputs, changed generation settings and reduced
precision. No record carries it, because it depends on inputs and settings the producer did not try. The
official taxonomy records that quantised models inherit the original's weaknesses and add their own (NIST AI
100-2, section 4.2.4) [TH-03], and that changing generation settings alone can break a safeguard (Huang et
al., ICLR 2024) [TH-42]. Robustness is tested against the attacks the tester knows (T16, T17) and holds only
for them; every defence in the cited jailbreak literature was broken by a later attack (threats document,
T17).

### D5. Latent contamination

*Tested at: S1, Q1.6, on e1.9 and e1.10; S2, Q2.2 and Q2.3, on e2.4 and e2.5 (SCRUM-284).*

What the training put into the model without saying so: poisoned behaviour (T9), a behaviour inherited from a
merged parent (T14), and evaluation data seen in training, which inflates the model's published scores. No
record carries it, because the training data is declared at best (P2). Poisoning and inherited behaviour are
tested as behaviour, D1 and D2. Evaluation contamination is tested by comparing performance across benchmarks,
and existing detection methods for it can be evaded and fail to quantify it (Dekoninck et al., NeurIPS 2024)
[AT-15]; whether a given record was in the training data cannot be established reliably on large generative
models (Duan et al., COLM 2024) [TH-50].

## Part 4. The split table

Table 3 places the eleven properties on the line. "In possession" and "by proxy (SCRUM-281)" say whether the evidence
exists for an organisation that holds the file (SCRUM-281) and for one that holds only a key (SCRUM-284, Table 1).

**Table 3. Attestable and discoverable properties**

| Property | Side | Evidence kind | Who answers | In possession | By proxy | Test family | Strength |
|---|---|---|---|---|---|---|---|
| P1 publisher identity | attestable | guaranteed for the account; declared for the producer behind it | platform; producer | yes | the serving provider's statement | provenance | strong for the account; moderate with a verified domain; weak otherwise |
| P2 training-data disclosure | attestable | declared | producer; by regulation, a summary from the provider of a general-purpose model | yes, as a statement | yes, as a statement | none | weak |
| P3 model card | attestable | declared, structured fields readable for form | producer | yes | the serving provider's catalogue entry | static for form; none for content | moderate structured; weak free text |
| P4 AI bill of materials | attestable | declared, format readable | producer or redistributor | where shipped | the serving provider's statement | static for form | moderate |
| P5 signing and attestation | attestable | checked by the organisation against a key | key holder; organisation verifies | where signed | no: the signature does not travel with the key | provenance | strong where present, origin and integrity only |
| P6 licence lineage | attestable | declared | producer, along a declared parent | yes, as a statement | yes, as a statement | none | weak |
| D1 behavioural properties | discoverable | testable, outputs | organisation | yes | yes, black-box | behavioural | not rated: tested |
| D2 hidden triggers | discoverable | testable, outputs and internals | organisation | yes | outputs only | behavioural; dynamic | not rated: tested |
| D3 capability boundaries | discoverable | testable, outputs and internals | organisation | yes | outputs only | behavioural; dynamic | not rated: tested |
| D4 robustness | discoverable | testable, outputs and internals | organisation | yes | outputs only | behavioural; dynamic | not rated: tested |
| D5 latent contamination | discoverable | testable, outputs and internals | organisation | yes | outputs only | behavioural; dynamic | not rated: tested |

Read down the strength column: the only strong evidence on the attestable side is the account that uploaded
and a valid signature, and both say who published and that the files are unchanged. Nothing on the attestable
side says what the model does. Read across the by-proxy column: an organisation that holds only a key keeps
the declared statements and black-box behaviour, and loses every guarantee, every signature and every test of
internals.

## Part 5. What is neither attestable nor practically testable

> **Caution. What no one can currently establish about an open-source model (SCRUM-281).**
>
> - **The training data actually used.** It is declared at best, in a summary if the law requires one
>   (EU AI Act, Article 53; European Commission template) [AT-01, AT-02]; it cannot be read from the file (SCRUM-281); and testing whether a given record was used is not
>   reliable on large generative models (Duan et al., COLM 2024) [TH-50].
> - **That a generative model carries no trigger.** A search can find a trigger; no method reliably recovers
>   one in a generative model, and none can show absence (Maloyan et al. 2024, preprint; Yan et al., EMNLP
>   2025) [TH-14, TH-12].
> - **The full extent of what a model can do.** A capability test gives a lower bound, and a model can be made
>   to hide what it can do (van der Weij et al., ICLR 2025) [AT-24].
> - **That benchmark scores were not inflated by contamination.** Detection methods can be evaded (Dekoninck
>   et al., NeurIPS 2024) [AT-15].
> - **That a signed model is safe.** A signature establishes origin and integrity only (Sigstore model-transparency; GitHub artifact attestations) [AT-11, AT-13].
> - **The real parent of a derivative that does not declare one,** or declares a false one, beyond the
>   statistical evidence of provenance testing where the derivation preserves output similarity (Nikolic et al.
>   2025, preprint) [AT-26].
> - **For a model held only by proxy (SCRUM-281): anything beyond the serving provider's statements and the model's
>   black-box behaviour.** The file, its hash, its signature and its internals are out of reach, and which
>   model and version is served is the provider's word (SCRUM-284, Table 1).

The list is the reason the testing methodology is necessary rather than optional. Every declared item of the
lifecycle framework is an assessment gap (SCRUM-284, section 2); Part 2 shows that most attestable properties
are declared; and Part 3 shows that the properties an organisation most needs, how the model behaves and
whether something was planted in it, are on the side no metadata reaches.

## Summary: the four questions answered

**What can be established without running the model, and how strongly?** Two things strongly: which account
uploaded the files, which the platform guarantees, and, where the files are signed, that they come from the
key holder and are unchanged. The structured fields of a card and a bill of materials moderately, in form but
not in content. Training-data disclosure, free-text card claims and licence lineage weakly: they are the
producer's word, often absent, and in the cited audits often wrong.

**What can be established only by running it?** Behaviour, hidden triggers, capability boundaries, robustness
and latent contamination. Each is tested against named threats, and each test is bounded: by the inputs sent,
by the triggers a search can reach, by the capability a test can elicit, and by the attacks the tester knows.

**Which side of the line is each property on?** Six attestable, five discoverable (Table 3). By proxy the
attestable side shrinks to statements and the discoverable side to outputs.

**What can be established neither way today?** The training data used, the absence of a trigger in a
generative model, the full extent of a capability, freedom from benchmark contamination, the safety of a signed
model, the real parent of an undeclared derivative, and, by proxy (SCRUM-281), anything beyond statements and outputs
(Part 5).

## Annex. The lifecycle questions and evidence items this document uses

The tags of every entry name a question, Qn.k, and an evidence item, en.k, of the lifecycle assessment
framework (SCRUM-284). Table 4 gives the text of each one used here, in the framework's own words. n is the
stage, S1 to S4; k numbers the questions or items of that stage.

**Table 4. Questions and evidence items cited in the tags** (text as in SCRUM-284, stage tables)

| Symbol | Stage | Question, or evidence item and its kind |
|---|---|---|
| Q1.1 | S1 selection | Where does the model live and who published it? |
| Q1.2 | S1 selection | Is the file what the page says it is? |
| Q1.4 | S1 selection | May we use it? |
| Q1.5 | S1 selection | Which row and column of the segmentation is it, and so which threats apply? |
| Q1.6 | S1 selection | Does it behave as described, and is the safeguard present? |
| Q2.2 | S2 adjustment | Did the change carry in anything we did not intend? |
| Q2.3 | S2 adjustment | Is the safeguard still present after the change? |
| Q2.4 | S2 adjustment | Is the adjusted artefact still what the segmentation says, and does it still do what the base was selected for? |
| Q3.1 | S3 deployment | Is the model in service the model we assessed? |
| Q3.2 | S3 deployment | What surrounds the model, and does it change what the model does? |
| Q3.3 | S3 deployment | Does the deployed system give the outputs the assessed model gave on the same inputs? |
| Q4.3 | S4 runtime detection | Does the model still give the outputs it gave at deployment? |
| e1.1 | S1 selection | guaranteed: producer account, upload date, file hashes |
| e1.2 | S1 selection | declared: the model card: parent model, training data, organisation behind the account, what the model produces, modality |
| e1.3 | S1 selection | guaranteed: the downloaded file's hash or signature against the page |
| e1.4 | S1 selection | readable: format, whole model or adapter, precision, configuration, and the code and templates that ship with the file |
| e1.7 | S1 selection | declared: licence and usage terms |
| e1.9 | S1 selection | testable, outputs: behaviour on the organisation's inputs |
| e1.10 | S1 selection | testable, internals: the file's internals while it runs |
| e2.1 | S2 adjustment | readable: the adjusted artefact: format, completeness, precision, and its base hash against e1.3 |
| e2.4 | S2 adjustment | testable, internals: the adjusted weights and activations against the base |
| e2.5 | S2 adjustment | testable, outputs: behaviour on the adjusted model, same inputs as e1.9 |
| e3.1 | S3 deployment | readable: the served artefact's hash against e1.3, or e2.1 after adjustment |
| e3.3 | S3 deployment | readable: the serving software and its version, the container or engine contents, and the configuration |
| e3.5 | S3 deployment | testable, outputs: outputs through the deployed endpoint against e1.9, or e2.5 after adjustment |
| e4.4 | S4 runtime detection | testable, outputs: the inputs of e3.5 sent again, against e3.5 |

## Source log

The sources this document adds. Each row gives:

- **ID**: the citation key used in the text.
- **Class** (SCRUM-281): *Official*, a standards or framework body, a regulator, or a party writing about its
  own artefact or service; or *Research*, a paper at an accepted venue, or a preprint labelled as such.
- **Source** and **URL**: what was read and where.
- **Verified**: what was checked in it, and the statement the citation rests on.

| ID | Class (SCRUM-281) | Source | URL | Verified |
|---|---|---|---|---|
| AT-01 | Official | Regulation (EU) 2024/1689 (AI Act), Article 53 | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | [CHECKED] text read from a mirror of the Official Journal text and to be quoted from EUR-Lex at assembly. 53(1)(d): providers of general-purpose AI models "draw up and make publicly available a sufficiently detailed summary about the content used for training", on the AI Office template; 53(2): the free and open-source exception covers points (a) and (b) only, so (d) applies to open-source models; no exception for models with systemic risk |
| AT-02 | Official | Explanatory Notice and Template for the Public Summary of Training Content for general-purpose AI models; European Commission, AI Office | https://digital-strategy.ec.europa.eu/en/library/explanatory-notice-and-template-public-summary-training-content-general-purpose-ai-models | [CHECKED] template "to provide a common minimal baseline for the information to be made publicly available"; the Commission's questions and answers list only 53(1)(a) and (b) as exempt for open-source models |
| AT-03 | Official | Signing commits with GPG; Hugging Face Hub documentation | https://huggingface.co/docs/hub/security-gpg | [CHECKED] git "does not authenticate the actual commit authors"; verified when signed and the key is on the account. Live page, read after the research cut-off; the feature is recorded before it in HF-11 |
| AT-04 | Official | Model Cards; Hugging Face Hub documentation | https://huggingface.co/docs/hub/model-cards | [CHECKED] README with YAML metadata: license, datasets, base_model; the Hub infers the relation (adapter, merge, quantized, finetune); metadata entered by the author. Recorded before the cut-off in HF-14 and EC-02 |
| AT-05 | Official | Advanced Security (Team and Enterprise); Hugging Face Hub documentation | https://huggingface.co/docs/hub/en/enterprise-advanced-security | [CHECKED] organisations with a verified domain name may require admin approval for members with matching e-mail, which "adds a verified badge to your organization page"; paid plans. No other criteria page found. Live page, read after the cut-off |
| AT-06 | Official | CycloneDX 1.6 JSON reference, modelCard; ML-BOM capability; OWASP CycloneDX | https://cyclonedx.org/docs/1.6/json/ ; https://cyclonedx.org/capabilities/mlbom/ | [CHECKED] model card section "typically contain[s] the training parameters, which datasets were used to train the model"; datasets "used to train and evaluate the model"; documents provenance of datasets. ML-BOM introduced in 1.5 (SC-25) |
| AT-07 | Official | SPDX 3.0.1, AI profile and Dataset profile; SPDX project, Linux Foundation | https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/ ; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Dataset/ | [CHECKED] AI profile: informationAboutTraining, limitation, metric, safetyRiskAssessment, typeOfModel; Dataset profile: dataCollectionProcess, dataPreprocessing, knownBias, hasSensitivePersonalInformation, intendedUse |
| AT-08 | Official | Licenses; Hugging Face Hub documentation | https://huggingface.co/docs/hub/repositories-licenses | [CHECKED] a licence can be added to any repository; identifiers include unknown and other. Recorded before the cut-off in HF-14 |
| AT-09 | Official | NIST SP 800-218A, Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile; July 2024; DOI 10.6028/NIST.SP.800-218A | https://csrc.nist.gov/pubs/sp/800/218/a/final | [CHECKED] PS.2.1: hashes or signatures for a model, components, artefacts and documentation; PS.3.2: "Track the provenance of an AI model and its components and derivatives"; consider disclosing training-data provenance; "Provenance verification is not possible in all cases" |
| AT-10 | Official | An Introduction to the OpenSSF Model Signing (OMS) Specification; OpenSSF | https://openssf.org/blog/2025/06/25/an-introduction-to-the-openssf-model-signing-oms-specification/ | [CHECKED] detached signature over a manifest of file hashes; "Recipients can verify that a model was published by the expected source, and has not subsequently been tampered with". The specification owner writing about its own specification |
| AT-11 | Official | model-transparency (model_signing); Sigstore and OpenSSF | https://github.com/sigstore/model-transparency | [CHECKED] signs (path, digest) pairs in an in-toto statement; aims to show the model "hasn't been tampered with after training"; no claim about behaviour. See also SC-24 |
| AT-12 | Official | NGC Catalog User Guide; NIM Model Signature Verification; NVIDIA | https://docs.nvidia.com/ngc/latest/ngc-catalog-user-guide.html ; https://docs.nvidia.com/nim/large-language-models/latest/reference/model-signature-verification.html | [CHECKED] all NVIDIA models published on the catalogue are signed, to verify origin and that files are unaltered, using the OpenSSF Model Signing standard. See also CG-12, CG-13 |
| AT-13 | Official | Artifact attestations; GitHub documentation | https://docs.github.com/en/actions/concepts/security/artifact-attestations | [CHECKED] uses Sigstore; consumers verify where and how software was built; "artifact attestations are not a guarantee that an artifact is secure" |
| AT-14 | Official | SLSA specification v1.1; OpenSSF | https://slsa.dev/spec/v1.1/ | [CHECKED] provenance identifies the output by digest and how it was produced; build track on the build process; no text on models or training data |
| AT-15 | Research | Dekoninck, Müller, Vechev. "ConStat: Performance-Based Contamination Detection in Large Language Models". NeurIPS 2024 | https://arxiv.org/abs/2405.16281 | [CHECKED] "existing detection methods can be easily evaded and fail to quantify contamination" |
| AT-16 | Research | Mitchell, Wu, Zaldivar, Barnes, Vasserman, Hutchinson, Spitzer, Raji, Gebru. "Model Cards for Model Reporting". FAT* 2019; DOI 10.1145/3287560.3287596 | https://arxiv.org/abs/1810.03993 | [CHECKED] short documents accompanying trained models, reporting evaluation across conditions and intended use |
| AT-17 | Research | Gebru, Morgenstern, Vecchione, Wortman Vaughan, Wallach, Daumé III, Crawford. "Datasheets for Datasets". Communications of the ACM 64(12), 2021; DOI 10.1145/3458723 | https://arxiv.org/abs/1803.09010 | [CHECKED] documents a dataset's motivation, composition, collection process and recommended uses |
| AT-18 | Research | Liang, Rajani, Yang, Ozoani, Wu, Chen, Smith, Zou. "Systematic analysis of 32,111 AI model cards characterizes documentation practice in AI". Nature Machine Intelligence 6, 2024; DOI 10.1038/s42256-024-00857-z | https://arxiv.org/abs/2402.05160 | [CHECKED] training section the most consistently filled; environmental impact, limitations and evaluation the lowest |
| AT-19 | Research | Bommasani et al. "The Foundation Model Transparency Index v1.1". TMLR 2025 | https://arxiv.org/abs/2407.12929 | [CHECKED] sustained and systemic opacity on copyright status, data access, data labour and downstream impact |
| AT-20 | Research | Longpre, Mahari, Chen et al. "A large-scale audit of dataset licensing and attribution in AI". Nature Machine Intelligence 6, 2024; DOI 10.1038/s42256-024-00878-8 | https://doi.org/10.1038/s42256-024-00878-8 | [CHECKED] licence omission rates above 70 per cent and error rates above 50 per cent on popular dataset hosting sites |
| AT-21 | Research | Jiang et al. "PeaTMOSS: A Dataset and Initial Analysis of Pre-Trained Models in Open-Source Software". MSR 2024 | https://arxiv.org/abs/2310.03620 | [CHECKED] reveals inconsistencies in software licences across pre-trained models and their dependent projects |
| AT-22 | Research, preprint | Jewitt, Li, Adams, Rajbahadur, Hassan. "From Hugging Face to GitHub: Tracing License Drift in the Open-Source AI Ecosystem". arXiv:2509.09873 | https://arxiv.org/abs/2509.09873 | [CHECKED] 35.5 per cent of model-to-application transitions drop restrictive clauses by relicensing under permissive terms: emerging |
| AT-23 | Research | Schorlemmer, Kalu, Chigges, Ko, Abu Isghair, Bagchi, Torres-Arias, Davis. "Signing in Four Public Software Package Registries: Quantity, Quality, and Influencing Factors". IEEE S&P 2024 | https://arxiv.org/abs/2401.14635 | [CHECKED] Hugging Face 0.1 per cent of artefacts signed in the year measured; of the signed artefacts, under a quarter valid; Hugging Face uses git commit signing |
| AT-24 | Research | van der Weij, Hofstätter, Jaffe, Brown, Ward. "AI Sandbagging: Language Models can Strategically Underperform on Evaluations". ICLR 2025 | https://proceedings.iclr.cc/paper_files/paper/2025/hash/b5e5753b0a0e440a6d8dc7e143617cec-Abstract-Conference.html | [CHECKED] capability evaluations are vulnerable to sandbagging; password-locked models hide capability, generalising to a hazardous-knowledge benchmark |
| AT-25 | Research | Xu, Wang, Ma, Koh, Xiao, Chen. "Instructional Fingerprinting of Large Language Models". NAACL 2024; DOI 10.18653/v1/2024.naacl-long.180 | https://aclanthology.org/2024.naacl-long.180 | [CHECKED] the publisher implants a private key as an instruction backdoor; testable only where planted |
| AT-26 | Research, preprint | Nikolic, Baluta, Saxena. "Model Provenance Testing for Large Language Models". arXiv:2502.00706 | https://arxiv.org/abs/2502.00706 | [CHECKED] black-box provenance testing; derivations preserve output similarity; 90 to 95 per cent precision and 80 to 90 per cent recall over more than 600 models. Conference proceedings appeared after the cut-off; cited as the preprint, which predates it: emerging |
| AT-27 | Official | The Minimum Elements For a Software Bill of Materials (SBOM), pursuant to Executive Order 14028; United States Department of Commerce and NTIA, 12 July 2021 | https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf | [CHECKED] "An SBOM is a formal record containing the details and supply chain relationships of various components used in building software"; data fields: supplier name, component name, version, other unique identifiers, dependency relationship and others; automation support: "Data formats used to generate and consume SBOMs include SPDX, CycloneDX, and SWID tags" |
| AT-28 | Official | ECMA-424, CycloneDX Bill of materials specification, 1st edition, June 2024; Ecma International, TC54 | https://ecma-international.org/publications-and-standards/standards/ecma-424/ | [CHECKED] the standard defines the CycloneDX bill of materials specification, "a structured format for representing detailed inventory information"; 1st edition June 2024 in the archive. A 2nd edition, December 2025, postdates the research cut-off and is not cited |
| AT-29 | Official | SPDX overview; SPDX project, Linux Foundation; with the Linux Foundation announcement of 9 September 2021 | https://spdx.dev/about/overview/ ; https://www.linuxfoundation.org/press/featured/spdx-becomes-internationally-recognized-standard-for-software-bill-of-materials | [CHECKED] "The SPDX specification is recognized as the international open standard for security, license compliance, and other software supply chain artifacts as ISO/IEC 5962:2021"; published as ISO/IEC 5962:2021 in 2021. The ISO catalogue page refused automated access; the maintainers' statement is cited |

Pages of platform documentation read after the research cut-off are cited for features the earlier logs record
before it, as noted per row. Searched and not found, recorded for the log: a versioned OpenSSF Model Signing
specification document; any criteria page for a verified organisation beyond AT-05; any text of SLSA on models;
a peer-reviewed count of models on a public repository carrying an OpenSSF or Sigstore model signature.

## Symbols from outside this document

| Symbol | Meaning | Defined in | File |
|---|---|---|---|
| (SCRUM-281) after a term | the term is a glossary term; shown at its first use in each part | SCRUM-281, report style guide and glossary, version 1.3, section 1 | governing/report-style-guide-and-glossary.md |
| attestable, testable properties | the two sides of the split | SCRUM-281, section 1.4 | governing/report-style-guide-and-glossary.md |
| established, emerging, forecast; Official, Research | confidence labels; citation classes | SCRUM-281, sections 2.2 and 2.3 | governing/report-style-guide-and-glossary.md |
| guaranteed, declared, readable, testable | evidence kinds | SCRUM-284, section 1.1, Table 1 | process/scrum-284/scrum284.md |
| S1 to S4; Qn.k; en.k | lifecycle stages, questions and evidence items; those used given in full in Table 4 | SCRUM-284, Notation and stage tables | process/scrum-284/stage-tables.md |
| (SCRUM-284) section 2 | the gap rule: every declared item is a gap | SCRUM-284 | process/scrum-284/scrum284.md |
| (SCRUM-286) sections 1.1 and 2.3 | derivative kinds declared on cards; provenance metadata among widely used models | SCRUM-286 | process/scrum-286/scrum286.md |
| T9 to T21; "the threats document"; [TH-nn] | model-integrity and inference-time threats and their sources | SCRUM-288 | process/scrum-288/scrum288.md |
| [SC-nn] | supply-chain sources | supply-chain document, source log | process/huggingface/hub-supply-chain-threats.md |
| [HF-nn], [CG-nn] | Hugging Face and NVIDIA sources | SCRUM-280 | process/scrum-280/scrum280.md |
