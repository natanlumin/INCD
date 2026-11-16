# Model-integrity and inference-time threats

## What this document answers

An organisation that takes an open-source model (SCRUM-281) into use meets its threats in two states.

- **Before adoption: the model as an object.**
    - The organisation that holds the file (SCRUM-281) studies the model's behaviour and its internals.
    - It compares the model with its parent, or with other candidates for the same use.
    - It tries to reveal what was done to the model before the model arrives in service.
    - This is where threats to the model itself are found, if they can be found at all.
    - The state acts as a gate the model must pass.
- **In service: the model through its interface.**
    - The organisation watches the inputs that reach the model, the content it reads, and the outputs and
      actions it returns.
    - This is where threats that act on the model in use appear.
    - They appear as failures of security, harm to the organisation's data and systems, or of safety, the
      model producing what its safeguard (SCRUM-281) should refuse.
- **The two states are not substitutes.**
    - Testing before adoption can search for a trigger, in the model's behaviour, in its internals and
      against its parent, and can find one; it cannot show that none is there, because a search covers only
      the triggers it is able to reach.
    - Watching in service sees only the inputs that arrive.
    - An organisation that reaches a model only through a key, by proxy (SCRUM-281), loses most of the first
      state and relies on the second.

This document sets the threats on that frame and answers four questions, one per row of Table 1.

**Table 1. The questions this document answers, and where**

| Question | What the document gives | Where |
|---|---|---|
| Which of these threats have been shown to work, and which are still argued? | a status for every threat, observed in deployment, demonstrated in research or theoretical, with the part of the threat it applies to, resting on official and research sources only | 1.3; every entry in Parts 2 and 3; Table 3 |
| At which point in the organisation's use of a model does each threat enter? | a lifecycle stage (SCRUM-281) for every threat, with the assessment question at which it first becomes answerable and the party that introduces it | 1.4; every entry; Table 3 |
| Can the threat be judged on the model, or only on the deployed system? | one test that places every threat at model level or system level, and for threats that sit on both sides, which part is which | 1.5; every entry; Part 4 |
| Which threats must the report's threat classification and decision cycle decide on? | one register with a row per threat and an empty column for the decision the cycle records against it (report structure, section 2.3, and Appendix A) | 1.2; Part 5, Table 3 |

The contributions, stated once:

- **One register for the whole threat landscape.** Thirteen threats in two families, six that act on the
  model itself and seven that act on it in use, each described with the same fields. They are numbered T9
  to T21, after the eight supply-chain and artefact-level threats, T1 to T8, defined in the supply-chain
  document (Supply-chain and artefact-level threats on the Hugging Face Hub, Part 2), so that all twenty-one
  can be compared, classified and decided on in one table.
- **A separation of evidence from argument.** The status says what the literature shows; the confidence label
  (SCRUM-281) says how well that is sourced. Neither is inferred from a neighbouring case.
- **Every threat placed on the lifecycle** in the stages and questions of the lifecycle assessment framework
  (SCRUM-284), so that the assessment chapters can attach a method to each threat at the stage where it can
  be answered.
- **An explicit boundary** between what can be required of a model before it is selected and what can be
  required only of a deployment, drawn by a test any reader can apply.
- **A two-state view of adoption**, examination before adoption and observation in service, which the
  boundary makes precise: each threat's model-level part is what the first state can reveal, its
  system-level part what only the second can see.

**Scope.** The threats that act on the model itself, model-integrity threats, and the threats that act on it
in use, inference-time and runtime threats: two of the glossary's three threat families. The third,
supply-chain and artefact-level threats, is treated in its own document, referred to here as the
supply-chain document (Supply-chain and artefact-level threats on the Hugging Face Hub): it describes how a file reaches the
organisation; this one describes what was done to the model's numbers before it arrived, and what can be
done with the model once it answers.

**Structure.** Part 1 sets out the two families and fixes how every threat is described. Part 2 gives the model-integrity threats, T9 to T14. Part 3
gives the inference-time and runtime threats, T15 to T21. Part 4 applies the boundary threat by threat. Part
5 is the register. A closing summary answers the four questions of Table 1, and an annex gives
the text of every lifecycle question and evidence item cited.

**Symbols.** Terms, stage and question numbers, citation prefixes and table references that come from outside
this document are listed, with where each is defined, in "Symbols from outside this document" after the
source log.

## Part 1. The threats and how each is described

### 1.1 What the organisation receives, and what can go wrong with it

An organisation that adopts an open-source model (SCRUM-281) receives a file (SCRUM-281) it did not train, from a producer it does
not control, and then runs that file on its own inputs. Three things can go wrong on that path.

- **The file is not what it seems.** The account, the repository or the file itself carries something other
  than the model the organisation selected: a program hidden in the serialisation, a parser exploit, a
  substituted revision. These are the supply-chain and artefact-level threats (SCRUM-281), T1 to T8 of the
  supply-chain document, Part 2.
- **The file is what it seems, but the model inside it was altered.** Someone with access to its training
  data, its training or its numbers changed what it does, before the organisation received it or while the
  organisation adjusted it. The file loads cleanly and passes every scan for executable content; what
  differs is behaviour. These are the **model-integrity threats**.
- **The model is sound, but it is turned against its use.** Someone who can reach its input, directly or
  through content it reads, makes it produce what neither its producer (SCRUM-281) nor the organisation
  intended, or reads from its outputs what the organisation did not mean to give away. Nothing in the model
  changes. These are the **inference-time and runtime threats**.

This document covers the second and third. The two meet at the safeguard (SCRUM-281): a model-integrity
threat can remove or weaken the safeguard for every input, while an inference-time threat defeats it on one
input at a time.

Part 1 then fixes how every threat is described, so that the entries in Parts 2 and 3 can be compared.
Section 1.2 names the thirteen threats. Sections 1.3 to 1.5 define the three things recorded for each: how far
it has been shown, the stage at which it reaches the organisation, and whether it acts at model level or
system level. Section 1.6 gives the shape of an entry. Each term is defined here once and used unchanged
afterwards.

### 1.2 The thirteen threats

**Where the list comes from.** The thirteen threats are the scope the report's structure assigns to its two
threat-landscape sections on model-integrity threats and on inference-time and runtime threats (report
structure, sections 4.3 and 4.4), named in its words. Three of its paired names are split, because the two
halves differ in evidence, in stage or in level: prompt injection into direct and indirect, extraction into
model and training data, quantisation into drift and triggered backdoors. Model inversion, which the report
structure names beside extraction, is treated with training-data extraction, because what it recovers is
training data. The abliterated model (SCRUM-281), a published copy whose refusal behaviour was removed by an
edit of its numbers, is treated with fine-tune and LoRA tampering, because it is the same threat reached by a
third route.

**Where the frameworks name them.** Each threat is checked against three frameworks: the OWASP Top 10 for
LLM Applications [TH-01]; MITRE ATLAS [TH-02]; and NIST AI 100-2, the adversarial machine learning taxonomy (NIST AI 100-2) [TH-03]. The last column of
Table 2 gives the entries or sections that name each threat, read from their own text. Ten of the thirteen
are named by all three. Quantisation-induced drift and quantisation-triggered backdoors are named by NIST
alone, in a closing discussion of quantised models rather than as attack classes of its taxonomy; no OWASP
entry and no ATLAS technique mentions quantisation. Merge contamination is named by OWASP alone, as an exploit
of collaborative model-merge services; neither ATLAS nor NIST mentions model merging.

**Table 2. The thirteen threats, and the framework entries that name them** (framework editions and their verification as in the source log, TH-01 to TH-03)

| Threat | Family | What it is | Named in: OWASP 2025; MITRE ATLAS 2026.09; NIST AI 100-2 E2025 |
|---|---|---|---|
| T9 training-data poisoning | model-integrity | part of the training data is controlled by an attacker, so that the trained model behaves as the attacker chose | LLM04:2025 Data and Model Poisoning; AML.T0020 Training Data Poisoning; NIST 2.3 Poisoning Attacks; 3.2.1 Data Poisoning Attacks |
| T10 backdoors and trojan triggers | model-integrity | the model behaves normally except when its input contains a trigger chosen by whoever planted the behaviour | LLM04:2025, backdoors and triggers; LLM03:2025 Supply Chain, pre-trained models with hidden backdoors; AML.T0018 Manipulate AI Model, behaviour activated only for selected inputs; AML.T0018.000 Poison AI Model; NIST 2.3.3 Backdoor Poisoning; 3.2.2 Model Poisoning Attacks, backdoors in pre-trained models persisting after fine-tuning |
| T11 fine-tune and LoRA tampering | model-integrity | a published model is changed by further training, by an adapter (SCRUM-281), or by a direct edit of its numbers, so that its behaviour or its safeguard differs from the parent's | LLM03:2025, malicious LoRA adapters; LLM04:2025, fine-tuning data; AML.T0018.000 Poison AI Model, by fine-tuning or direct manipulation of weights; AML.T0054 LLM Jailbreak, by modifying model weights or safety mechanisms; NIST 3.1.3 Attacker Capabilities, model control and fine-tuning circumvention attacks that remove refusal behaviour; 2.3.4 Model Poisoning |
| T12 quantisation-induced drift | model-integrity | a quantised model (SCRUM-281) behaves differently from its parent without anyone intending it | no OWASP entry; no ATLAS technique; NIST 4.2.4 Quantized Models, quantised models inherit the original's weaknesses and add their own |
| T13 quantisation-triggered backdoors | model-integrity | a model is built to behave well at full precision and badly once it is quantised | no OWASP entry; no ATLAS technique; NIST 4.2.4 Quantized Models, a harmful quantised model whose full-precision counterpart appears benign |
| T14 merge contamination | model-integrity | a merged model (SCRUM-281) inherits a backdoor, a behaviour or contaminated content from one of its parents | LLM03:2025, collaborative model merge and model merging used to bypass reviews; no ATLAS technique; no NIST section |
| T15 direct prompt injection | inference-time and runtime | the person writing the input overrides the instructions the deployment gave the model | LLM01:2025 Prompt Injection, direct; AML.T0051.000 LLM Prompt Injection: Direct; NIST 3.3 Direct Prompting Attacks |
| T16 indirect prompt injection | inference-time and runtime | instructions placed in content the model reads, a page, a document, a tool's output, are followed as if they came from the user | LLM01:2025, indirect; AML.T0051.001 LLM Prompt Injection: Indirect; NIST 3.4 Indirect Prompt Injection Attacks |
| T17 jailbreaks | inference-time and runtime | an input that makes the model produce what its safeguard was trained to refuse | LLM01:2025, jailbreaking as a related concept; AML.T0054 LLM Jailbreak; NIST 3.3 Direct Prompting Attacks, 3.3.1 Attack Techniques |
| T18 model extraction | inference-time and runtime | the model's parameters or behaviour are reconstructed from its outputs | LLM10:2025 Unbounded Consumption, model extraction via API and functional model replication; AML.T0024.002 Extract AI Model; NIST 2.4.4 Model Extraction |
| T19 training-data extraction | inference-time and runtime | the model is made to return data it was trained on, or that data is reconstructed from its outputs | LLM02:2025 Sensitive Information Disclosure, training data and inversion; AML.T0024.001 Invert AI Model; AML.T0057 LLM Data Leakage; NIST 2.4.1 Data Reconstruction; 3.3.2 Information Extraction, training data extraction |
| T20 membership inference | inference-time and runtime | the outputs reveal whether a given record was in the training data | LLM02:2025, by reference to the ATLAS technique; AML.T0024.000 Infer Training Data Membership; NIST 2.4.2 Membership Inference |
| T21 agentic and tool-use abuse | inference-time and runtime | a model that calls tools or acts on the organisation's behalf is made to take an action no one authorised | LLM06:2025 Excessive Agency; AML.T0053 AI Agent Tool Invocation; AML.T0086 Exfiltration via AI Agent Tool Invocation; NIST 3.5 Security of Agents |

Every threat in Table 2 has an entry in Part 2 or 3 and a row in the register, and every one enters the
report's threat classification and decision cycle, which decides the depth of treatment each threat receives
and records the decision against it (report structure, section 2.3, and Appendix A, threat disposition
table).

### 1.3 Demonstrated or theoretical

Every threat carries a status that says what the evidence shows. The status is separate from the confidence
label, which says how well a claim is sourced: a peer-reviewed laboratory result is established and
demonstrated in research, not observed in deployment.

- **Observed in deployment.** An official record, a security advisory or a party's statement about its own
  service, or a research measurement, reports the threat against a deployed system, a production service or
  a public model repository (SCRUM-281).
- **Demonstrated in research.** The threat has been carried out on real models in a research setting, with
  the researchers playing both attacker and victim, and no record of it in deployment was found.
- **Theoretical.** The threat is argued, or shown only on a constructed case that does not reach the model
  types in scope, or not shown at all.

The literature is the official and research sources the citation policy admits (SCRUM-281). Each result is
cited where it is used, by its authors, venue and year, or as a preprint, and resolves to a row of the source
log that records what was checked in it. A status rests on what the literature shows, not on a measurement
taken for this report or on the date it was read, so it holds for any model and any period the cited work
covers, and changes only when the literature does. Press and blogs
are not evidence for a status. The techniques executed for this report, the demonstration set (SCRUM-281),
are not evidence here either; they are reported beside their own evidence.

A threat may hold different statuses in different parts, for example demonstrated in research for its
mechanism and not established for its occurrence in published models; each entry says which part holds
which. Each entry gives the demonstrated part and the theoretical part under their own headings, so the line
between them is never left to the reader. "Not established" is written wherever no admissible source was
found, and is never inferred from a neighbouring case.

### 1.4 The lifecycle stage a threat enters at

Each threat is tagged with the lifecycle stage (SCRUM-281) at which it enters the organisation's hands. The stages are
the four the glossary defines as the points at which a question about a model is answered (SCRUM-281,
section 1.4, lifecycle stage), and the report structure assesses at (report structure, section 6.1). The
lifecycle assessment framework numbers them and fixes the questions answered at each (SCRUM-284, section 1.3,
Table 2):

- **S1 selection**: the organisation chooses a model from where it is published and checks it before taking
  it in;
- **S2 adjustment**: the organisation changes the model, by fine-tuning, an adapter, a merge, quantisation or
  conversion, or has another party change it;
- **S3 deployment**: the model is put into service with what surrounds it: serving software, configuration,
  retrieval, tools, guards and access;
- **S4 runtime detection**: the model runs, and what deployment fixed and what arrives at its input are
  watched.

Every threat carries exactly one entry stage for each route by which it can reach the organisation, and the
entry says which route it is. The tag gives four things:

- **enters at**: the stage at which the threat enters;
- **first answerable at**: the framework question at which it can first be answered, Qn.k (SCRUM-284), and
  the evidence item that answers it, en.k (SCRUM-284); every question and item used is given in full in the
  annex, Table 5;
- **introduced by**: the producer, a third party that published a derivative, the organisation's own
  adjustment, or whoever reaches the model's input;
- **exposure fixed at**, where it differs from the entry stage: the earlier stage whose decisions decide
  whether the threat can reach the model at all.

A threat introduced before the organisation selects the model, in the producer's training or in a derivative
another party published, enters at S1, because selection is where the organisation first holds it. The two
families therefore enter at different points:

- **Model-integrity threats enter at S1 or S2.** At S1 when they arrive with the model; at S2 when the
  organisation's own adjustment, or one made on its behalf, introduces them. A threat with both routes,
  training-data poisoning for one, carries both tags, one per route.
- **Inference-time and runtime threats enter at S4.** They arrive with the inputs the model receives in
  service, and are first answerable at Q4.2, on the inputs arriving and the outputs returned, e4.3
  (SCRUM-284). Their exposure is fixed at S3, where deployment decides what surrounds the model and who can
  reach it (SCRUM-284, Q3.2 and Q3.4). The model's susceptibility to them, the model-level part of 1.5, can
  be tested earlier, at S1 on the model's behaviour, Q1.6 on e1.9, but the threat itself enters only when
  the model is in service.

Whether the organisation holds the file or only a key, in possession (SCRUM-281) or by proxy (SCRUM-281), decides which
evidence exists to answer the question (SCRUM-284, Table 1); by proxy only declared statements and black-box
behaviour exist. Each entry states both cases.

### 1.5 The boundary between model level and system level

The glossary marks every threat as acting at model level or system level (SCRUM-281). The boundary is drawn
here by one test.

> Move the same model file to a deployment with nothing around it: no system prompt, no retrieval, no tools,
> no guard (SCRUM-281), default serving settings. If the threat goes with the file, it is model level. If it
> stays behind, it is system level.

A model-level threat is a property of the numbers. It is present in every deployment of that file, and a
test of the model alone can, in principle, find it. A system-level threat exists because of what surrounds
the model: the serving software, the configuration, retrieval, tools and permissions that deployment fixes
(SCRUM-284, Q3.2). It is assessed per deployment, not per model.

Many threats have a part on each side. The model's inability to tell an instruction from the data it reads
is a property of the model; what an injected instruction can then do depends on the tools it can call. Each
entry names the part on each side, and Part 4 sets them side by side.

The boundary is also the line between the two states of adoption. The model-level part of a threat is what
examination before adoption can reveal, at S1 and S2, by testing the model and comparing it with its parent
or with other candidates (SCRUM-284, e2.4 and e2.5). The system-level part exists only once the model is
deployed, and is seen at S3 and S4, through the interface.

The boundary decides three things the later chapters depend on:

- **What an acceptance criterion can require, and when.** A model-level property can be required of the
  model before it is selected; a system-level one can be required only of a deployment, and is re-assessed
  whenever what surrounds the model changes.
- **Who answers.** In possession, the organisation answers for both sides. By proxy, the producer answers for
  the model and the serving provider (SCRUM-281) for the endpoint, never for the model itself, so a
  model-level threat cannot be passed to the serving provider.
- **Which control can meet it.** A guard placed around the model is a system-level control; it can contain a
  model-level threat on the inputs it sees, and it does not remove it from the file.

### 1.6 The shape of an entry

Every entry has the same shape, so that the threats can be compared:

- what the threat is and how it works;
- **Enters at**, in the terms of 1.4: entry stage, first answerable at, introduced by, and exposure fixed at
  where it applies, in italics under the heading;
- **Demonstrated**, the part the literature shows, with its sources;
- **Theoretical or not established**, the part it does not;
- a closing line with the organisation exposed, the level, the status, the confidence label (SCRUM-281), what the threat
  applies to, and the framework entries that name it.

"Applies to" uses the row and column labels of the segmentation (SCRUM-280, Table 4): classification,
embedding and generative model, with the image-and-text qualifier, against pickle checkpoint, safetensors,
GGUF and ONNX, and the file kinds quantised model, adapter and merged model (SCRUM-281). The framework
entries are those of the OWASP Top 10 for LLM Applications, MITRE ATLAS and NIST AI 100-2, in the editions
recorded in the source log (NIST AI 100-2) [TH-01, TH-02, TH-03].

## Part 2. Model-integrity threats

Six threats alter the model before the organisation runs it. Each leaves the file (SCRUM-281) in a valid format,
loadable without error, so none is visible to the scans that look for executable content in a file; those
belong to the supply-chain document, whose artefact layer is the route by which an altered file arrives
(supply-chain document, Part 2.2, T3 to T7). What changes is behaviour.

Four of the six act through a derivative model (SCRUM-281), and on the primary model repository (SCRUM-281)
derivatives are a large and growing share of what is published: fine-tunes, adapters, quantised copies and
merged models, each declaring its parent on its model card (SCRUM-286, section 1.1). The relation is a field
the uploader fills in and the platform does not verify, so the parent an assessment starts from is the one
the uploader named.

The six are defined in Table 2 (section 1.2) and treated below in that order, T9 to T14.

### T9. Training-data poisoning

*Enters at: S1, through the training of the producer (SCRUM-281), first answerable at Q1.6 on e1.9 and e1.10; or S2, through
data the organisation trains on itself, at Q2.2 on e2.2 and e2.5 (SCRUM-284). Introduced by whoever controls
part of the training data.*

A model learns what its training data shows it. Poisoning is the placement of examples in that data so that
the trained model learns a behaviour the attacker chose. It can enter at each phase of training: the
web-scale text of pre-training, the instruction examples that teach the model to follow requests, and the
preference data that teaches it which answers are better. The goal may be to degrade the model, to bias
it on a topic, or to attach a behaviour to a trigger; the last is T10, and the data is one of its routes.

The organisation cannot inspect the data. What the producer used is a declared (SCRUM-284) statement on the
model card, e1.2, and nothing verifies it; among widely used models, only a minority fill the training-data
field at all (SCRUM-286, section 2.3).

**Demonstrated.** Four results, each in a research setting: the first on public training datasets, the other
three on models the researchers trained themselves.

- Web-scale datasets can be poisoned in practice. Two routes, buying expired domains whose content a dataset
  index still points to, and editing pages shortly before a dataset takes its periodic snapshot, could have
  poisoned 0.01 per cent of two large image-and-text datasets for about 60 US dollars, and ten public datasets
  were found open to them (Carlini et al., IEEE S&P 2024) [TH-04].
- Instruction tuning is sensitive to a few examples. About a hundred poisoned examples made a chosen phrase
  produce negative or degenerate output across tasks held out from training, and larger models were more
  affected, not less (Wan et al., ICML 2023) [TH-05].
- Pre-training poisoning persists. Researchers pre-trained models from 600 million to 7 billion parameters
  from scratch with poisoned data, then applied the post-training that makes a chat model. Poisoning 0.1 per
  cent of the pre-training data was enough for three of four attack goals, belief manipulation, jailbreaking
  and prompt stealing among them, to persist; denial of service persisted from 0.001 per cent (Zhang et al., ICLR 2025) [TH-06].
- The number of poisoned documents needed may not grow with the model. Two hundred and fifty documents were
  enough for models from 600 million to 13 billion parameters, whatever the size of the clean data; success
  followed the count of poisoned documents, not their share (Souly et al. 2025, preprint) [TH-07].

**Theoretical or not established.**

- That any published open-source model (SCRUM-281) was poisoned through its training data is not established: no
  official record and no research measurement was found.
- Whether the near-constant count holds above 13 billion parameters is not established; the largest models
  in the cited study are below that size (Souly et al. 2025, preprint) [TH-07].
- The organisation's own S2 data being poisoned is the instruction-tuning case above in mechanism (Wan et al., ICML 2023) [TH-05]; no
  record of it in an organisation's adjustment was found.

Organisation exposed: both; by proxy (SCRUM-281) the served model carries whatever its training put in it,
and the organisation holds only black-box behaviour, e1.9. Level: model level; the result is in the numbers
and goes with the file. Status: demonstrated in research; observed in deployment not established. Label:
established (Carlini et al., IEEE S&P 2024; Wan et al., ICML 2023; Zhang et al., ICLR 2025) [TH-04, TH-05, TH-06]; the near-constant count emerging (Souly et al. 2025, preprint) [TH-07]. Applies to: the generative model
row (Wan et al., ICML 2023; Zhang et al., ICLR 2025; Souly et al. 2025, preprint) [TH-05, TH-06, TH-07] and the image-and-text qualifier through its training sets (Carlini et al., IEEE S&P 2024) [TH-04]; the
classification model row, where poisoning is demonstrated in research across spam, malware, sentiment and
toxic-comment classifiers, as the NIST taxonomy's survey records (NIST AI 100-2, section 2.3) [TH-03]; the
embedding row not established, since no cited source demonstrates poisoning of an embedding model; every
artefact format column, since the change is in the numbers whatever the container. Framework: OWASP LLM04:2025 Data and Model Poisoning
[TH-01]; MITRE ATLAS AML.T0020 Training Data Poisoning [TH-02].

### T10. Backdoors and trojan triggers

*Enters at: S1, through the producer or a third party that published the model, first answerable at Q1.6 on
e1.9 and e1.10; or S2, through an adjustment made by another party on the organisation's behalf, at Q2.2 on
e2.3, e2.4 and e2.5 (SCRUM-284). Introduced by whoever trained or changed the model.*

A backdoor is behaviour that appears only when the input contains a trigger: a word, a phrase, a date, a
pattern. On every other input the model behaves as expected, which is what makes it hard to find. "Trojan"
names the same thing in older literature; this document says backdoor and trigger. Three routes plant one:
poisoned training data, T9 with a trigger attached; training carried out by another party, who returns a
model with the backdoor in it; and the numbers of a pre-trained model, edited so that the backdoor survives
the fine-tuning that follows. Adapters, quantisation and merging are further routes, treated as T11, T13 and
T14.

The organisation meets T10 in the form the framework anticipates: at Q2.2 it asks for probes for triggers and
planted content, e2.5, and for where the weights and activations moved, e2.4 (SCRUM-284). A probe can find
only what it sends, and a trigger is chosen so that ordinary inputs do not contain it.

**Demonstrated.**

- Training handed to another party can return a backdoored model. A network trained by an outside party was
  accurate on the owner's validation data and misbehaved on the trigger: a street-sign detector read a stop
  sign carrying a small sticker as a speed-limit sign, and the backdoor survived transfer to a new task
  (Gu et al., IEEE Access 2019) [TH-09].
- A backdoor can be planted in pre-trained numbers and survive the victim's fine-tuning. Edited pre-trained
  language models kept the attacker's behaviour after the downstream training that turns them into
  classifiers (Kurita et al., ACL 2020) [TH-10]. This is the case of an organisation that downloads a pre-trained model and adapts it.
- A backdoor can be planted through preference data. Poisoned human feedback planted a trigger word that made
  any prompt a jailbreak of the safeguard (SCRUM-281) the model was trained with (Rando and Tramèr, ICLR
  2024) [TH-08].
- A backdoor can persist through safety training. Models built to write secure code when the prompt says the
  year is 2023 and exploitable code when it says 2024 kept the behaviour through supervised fine-tuning,
  reinforcement learning and adversarial training; adversarial training taught the models to recognise their
  trigger better, and persistence was strongest in the largest models (Hubinger et al. 2024, preprint)
  (Hubinger et al. 2024, preprint) [TH-11].
- A search can find a trigger in a classifier. A scanner that inverts the words most likely to form a trigger,
  given only the model and a few benign samples, detected backdoors in 3,839 language classifiers of seven
  transformer structures, BERT and GPT among them, across 17 attack types, with over 0.9 detection accuracy
  in most settings (Liu et al., IEEE S&P 2022) [TH-13].
- Detection is fragile. Backdoor detectors evaluated for language models failed when the strength with which
  the backdoor was trained was varied, so a detector's published success does not carry to backdoors trained
  differently (Yan et al., EMNLP 2025) [TH-12].
- A scan can find a backdoor in a generative model without knowing its trigger. Inverting the backdoor's
  target rather than its trigger, a scanner with only black-box access outperformed five baselines across 153
  generative models of eight architectures and six attack types, and ranked first in the generative-model
  round of a public trojan-detection competition (Shen et al., IEEE S&P 2025) [TH-53].
- Recovering the planted trigger itself is far harder. In a trigger-detection competition on generative
  language models, the best methods recovered the planted triggers with a recall of about 0.16, comparable to
  sampling sentences at random from inputs like the training prefixes (Maloyan et al. 2024, preprint)
  [TH-14].

**Theoretical or not established.**

- A trigger backdoor in a published open-source model is not established. The malicious models found on the
  Hugging Face Hub carried code that runs when the file is loaded, not behaviour planted in the numbers
  (Zhao et al., ASE 2024) [SC-17]; that is malicious serialisation, T3 of the supply-chain document (Part 2.2), and not this threat.
- A backdoor that arises without anyone planting it is theoretical. The persistent backdoors above were built
  deliberately, as studies of what such behaviour would do (Hubinger et al. 2024, preprint) [TH-11].
- A method that shows a model carries no backdoor is not established. Scanners give statistical evidence: a
  scan that finds nothing lowers the likelihood of a backdoor of the kinds and within the search it covers,
  with the error rates its evaluation reports (Liu et al., IEEE S&P 2022; Shen et al., IEEE S&P 2025) [TH-13,
  TH-53]; it is not a proof, a planted trigger may not be recoverable (Maloyan et al. 2024, preprint) [TH-14],
  and a detector's success does not carry to backdoors trained differently (Yan et al., EMNLP 2025)
  [TH-12].

Organisation exposed: both; by proxy the organisation holds only black-box behaviour, e1.9, and a trigger it
does not know is absent from its inputs by construction. Level: model level; the backdoor is in the numbers
and survives the organisation's own fine-tuning (Kurita et al., ACL 2020; Hubinger et al. 2024, preprint) [TH-10, TH-11]. Status: demonstrated in research; observed in
deployment not established. Label: established (Rando and Tramèr, ICLR 2024; Gu et al., IEEE Access 2019; Kurita et al., ACL 2020; Yan et al., EMNLP 2025; Liu et al., IEEE S&P 2022) [TH-08, TH-09, TH-10, TH-12, TH-13];
persistence through safety training and the difficulty of trigger recovery in generative models emerging
(Hubinger et al. 2024, preprint; Maloyan et al. 2024, preprint) [TH-11, TH-14]. Applies to: the classification model row (Gu et al., IEEE Access 2019; Kurita et al., ACL 2020) [TH-09, TH-10] and the generative model row
(Wan et al., ICML 2023; Rando and Tramèr, ICLR 2024; Hubinger et al. 2024, preprint) [TH-05, TH-08, TH-11]; the embedding row not established,
since no cited source demonstrates a backdoor in an embedding model; every artefact format column. The NIST
taxonomy records backdoors in transformer classifiers for sentiment and toxic-comment detection (NIST AI
100-2, section 2.3) [TH-03].
Framework: OWASP LLM04:2025 Data and Model Poisoning [TH-01]; MITRE ATLAS AML.T0018.000 Poison AI Model, under
AML.T0018 Manipulate AI Model, and AML.T0020 Training Data Poisoning for the data route [TH-02].

### T11. Fine-tune and LoRA tampering

*Enters at: S1, through a third party that published a fine-tuned, adapted or abliterated copy, first
answerable at Q1.6 on e1.9 and e1.10; or S2, through the organisation's own fine-tune or adapter, at Q2.3 on
e2.5 against e1.9 and on e2.4 (SCRUM-284). Introduced by whoever changed the model after its producer
(SCRUM-281).*

A published model can be changed by anyone who holds its file. Three routes change it: further training on
new examples, a fine-tune; a small adapter (SCRUM-281) loaded beside the model, of which LoRA is the common
kind; and a direct edit of the numbers. The change can remove the safeguard (SCRUM-281), plant a behaviour,
or both. The abliterated model (SCRUM-281) is the direct-edit route made public: a copy whose refusal was
located and removed, then published. The adapter is also a file kind with its own delivery threat, the
malicious adapter of the supply-chain document (Part 2.2, T6); this entry concerns what the adapter does to
behaviour, not the code it may carry.

**Demonstrated.**

- Fine-tuning removes the safeguard cheaply, and can do so without intent. Ten harmful examples, submitted
  through a production fine-tuning service, removed the safety alignment of the served model, and fine-tuning
  on benign data also degraded it (Qi et al., ICLR 2024) [TH-15].
- An adapter removes it on the largest open models. A LoRA adapter brought the refusal rate of a 70-billion
  parameter chat model to about one per cent on two refusal benchmarks, on one GPU, keeping its other
  capabilities (Lermen et al. 2023, preprint) [TH-16].
- A direct edit removes it without training. Refusal in thirteen open chat models up to 72 billion parameters
  is carried by a single direction inside the model, and a rank-one edit of the numbers that removes the
  direction removes refusal (Arditi et al., NeurIPS 2024) [TH-17].
- Abliterated copies are published. The primary model repository (SCRUM-281) lists repositories that name
  themselves abliterated, under the platform's own search (Hugging Face Hub search) [TH-20].
- Adapters can carry a backdoor that survives sharing. A backdoored LoRA adapter kept its behaviour when
  combined with other adapters (Liu et al. 2024, preprint) [TH-18]; trojaned adapters made a model emit the
  attacker's content or misuse its tools, running malware and writing spear-phishing, and none of three
  defences tested removed the threat fully (Dong et al., NDSS 2025) [TH-19].

**Theoretical or not established.**

- How often published fine-tunes and adapters carry a planted behaviour, as opposed to a removed safeguard,
  is not established: no measurement was found.
- Whether a parent's assessment says anything about a derivative is not established in either direction; the
  glossary therefore treats every derivative as a model of its own (SCRUM-281).

Organisation exposed: both; by proxy the serving provider (SCRUM-281) may serve a fine-tune or adapter the
organisation cannot inspect, and the organisation holds only behaviour, e1.9. Level: model level; the change
is in the numbers or in the adapter loaded with them. Status: observed in deployment, for safeguard removal
through a production fine-tuning service (Qi et al., ICLR 2024) [TH-15] and for published abliterated copies (Hugging Face Hub search) [TH-20]; demonstrated in
research for planted adapter behaviour (Liu et al. 2024, preprint; Dong et al., NDSS 2025) [TH-18, TH-19]. Label: established (Qi et al., ICLR 2024; Arditi et al., NeurIPS 2024; Dong et al., NDSS 2025; Hugging Face Hub search) [TH-15, TH-17, TH-19, TH-20]; the
adapter results on the largest models and on combined adapters emerging (Lermen et al. 2023, preprint; Liu et al. 2024, preprint) [TH-16, TH-18]. Applies to: the
generative model row, instruct and chat models chiefly, since they carry the safeguard (SCRUM-281); the
adapter file kind; every artefact format column; the classification and embedding rows not established in the
cited sources. Framework: as Table 2.

### T12. Quantisation-induced drift

*Enters at: S1, through a third party that published a quantised copy, first answerable at Q1.6 on e1.9; or
S2, through the organisation's own quantisation, at Q2.3 and Q2.4 on e2.5 against e1.9 (SCRUM-284).
Introduced by whoever quantised the model, without intent.*

A quantised model (SCRUM-281) stores the same model with less precise numbers, so that it runs on less
memory. Its behaviour is close to its parent's and not identical, and nothing guarantees that the safeguard
moves with the rest. Drift is the unintended difference: no one planted it, and no one checked it.

**Demonstrated.**

- The official taxonomy records the effect: quantised models inherit the weaknesses of the original and add
  their own, since the loss of precision amplifies errors and weakens robustness to adversarial inputs, and
  the effect on generative models has been studied less than on predictive ones (NIST AI 100-2, section 4.2.4)
  (NIST AI 100-2) [TH-03].
- On open generative models, fine-tuning raised jailbreak success while quantisation had mixed effects, in
  either direction depending on the model and the method (Kumar et al. 2024, preprint) [TH-21].

**Theoretical or not established.**

- The direction and size of the drift for a given model and quantisation method cannot be predicted from the
  parent: not established. It is measured per copy or not known.
- That drift has caused harm in a deployment is not established.

Organisation exposed: both; by proxy the serving provider chooses the precision it serves, and the
organisation may not know it. Level: model level. Status: demonstrated in research. Label: established for
the effect stated by the taxonomy (NIST AI 100-2) [TH-03]; its direction on generative models emerging (Kumar et al. 2024, preprint) [TH-21]. Applies to:
the quantised model file kind, in every model type row; the GGUF column chiefly, where quantisation is the
normal state of the file (SCRUM-280, Table 6). Framework: as Table 2.

### T13. Quantisation-triggered backdoors

*Enters at: S1, through the producer or a third party that published the full-precision model, first
answerable once a quantised copy exists: at Q2.3 and Q2.4 on e2.5 against e1.9 when the organisation
quantises at S2, or at Q1.6 when it selects a quantised copy (SCRUM-284). Introduced by whoever built the
model.*

A model can be built to behave well at full precision and badly once it is quantised. The behaviour is
planted in the rounding: the full-precision numbers pass every test, and the quantised copy, which is what is
deployed on smaller hardware, does what the attacker chose. This is T10 with quantisation as its trigger, and
T12 made deliberate.

**Demonstrated.**

- On generative models, a full-precision model that appeared benign became malicious once quantised with
  widely used methods, producing insecure code, injecting content or over-refusing (Egashira et al., NeurIPS
  2024) [TH-22]; the official taxonomy records the result (NIST AI 100-2, section 4.2.4) [TH-03].
- The same holds for the quantisation types of the GGUF format: across three generative models and nine GGUF
  types, the quantised copies produced insecure code in 88.7 per cent and injected content in 85.0 per cent of
  cases (Egashira et al., ICML 2025) [TH-23].
- On classifiers, standard post-training quantisation in commercial deployment frameworks activated a dormant
  backdoor with close to complete success (Ma et al. 2021, preprint) [TH-24], and training aware of
  quantisation made quantisation cause accuracy loss, targeted errors or a backdoor (Hong et al., NeurIPS
  2021) [TH-25].

**Theoretical or not established.**

- A published model carrying a quantisation-triggered backdoor is not established.
- A test of the full-precision model alone cannot find it; it is found, if at all, by testing the quantised
  copy against its parent, the comparison of 1.5.

Organisation exposed: both; by proxy only behaviour exists, and the precision served is the serving
provider's choice. Level: model level. Status: demonstrated in research. Label: established (NIST AI 100-2; Egashira et al., NeurIPS 2024;
Egashira et al., ICML 2025; Hong et al., NeurIPS 2021) [TH-03, TH-22, TH-23, TH-25]; the commercial-framework result emerging (Ma et al. 2021, preprint) [TH-24]. Applies to: the quantised model file kind;
the generative model row (Egashira et al., NeurIPS 2024; Egashira et al., ICML 2025) [TH-22, TH-23] and the classification row (Ma et al. 2021, preprint; Hong et al., NeurIPS 2021) [TH-24, TH-25]; the GGUF column
demonstrated (Egashira et al., ICML 2025) [TH-23], other columns through the quantisation method rather than the container. Framework: as
Table 2.

### T14. Merge contamination

*Enters at: S1, through a third party that published a merged model, first answerable at Q1.6 on e1.9; or
S2, when the organisation merges models itself, at Q2.2 and Q2.3 on e2.5 against each parent's e1.9
(SCRUM-284). Introduced by whoever published one of the parents.*

A merged model (SCRUM-281) combines the numbers of two or more models. Each parent contributes what it
carries, so a parent with a backdoor or an unwanted behaviour can pass it into the merge, and the merged model
has no parent's assessment.

**Demonstrated.**

- One backdoored contributing model compromised the whole merged model, whatever the merging coefficients
  (Zhang et al., ACM CCS 2024) [TH-26].
- On generative models, a malicious model uploaded for others to merge passed its backdoor to the merged
  model, which kept its usefulness, and the backdoor survived paraphrasing defences and fine-pruning (Yuan et
  al., ACL 2025) [TH-27].
- A model built to be merged raised the leakage of personal data and of training-set membership in the merged
  result (Guo et al. 2025, preprint) [TH-28].
- The industry framework records merging as a route around review, merged models being common and highly
  ranked on public leaderboards (OWASP LLM03:2025) [TH-01].

**Theoretical or not established.**

- That a merged model inherits a parent's contamination of evaluation data, so that its benchmark scores
  overstate it, is theoretical: no research or official source establishes it.
- A published merged model carrying a planted backdoor is not established.

Organisation exposed: both. Level: model level. Status: demonstrated in research for inherited backdoors and
leakage; theoretical for inherited evaluation contamination. Label: established (Zhang et al., ACM CCS 2024; Yuan et al., ACL 2025) [TH-01, TH-26, TH-27];
leakage emerging (Guo et al. 2025, preprint) [TH-28]. Applies to: the merged model file kind; the generative model row (Yuan et al., ACL 2025; Guo et al. 2025, preprint) [TH-27, TH-28];
other rows not established in the cited sources; every artefact format column. Framework: as Table 2.

## Part 3. Inference-time and runtime threats

Seven threats act on a model in service through what reaches its input or what leaves its output. Each is
defined in Table 2 (section 1.2) and treated below in that order, T15 to T21. All seven enter at S4, with
their exposure fixed at S3 (1.4). Each has a part that goes with the file (SCRUM-281), the model's susceptibility, and a
part that stays with the deployment, what the deployment lets the attacker reach; each entry names both.

### T15. Direct prompt injection

*Enters at: S4, through the person writing the input, first answerable at Q4.2 on e4.3; exposure fixed at S3,
Q3.2, by the instructions and data the deployment places in front of the model (SCRUM-284).*

A deployment gives the model instructions the user does not see: a system prompt, a role, rules. Direct
injection is an input that overrides them, so that the model follows the user instead of the deployment, or
reveals what the deployment put in front of it.

**Demonstrated.**

- Inputs that hijack the task and leak the hidden instructions worked against a production model's interface
  (Perez and Ribeiro, NeurIPS ML Safety Workshop 2022) [TH-29].
- Five attack kinds and ten defences evaluated on ten models showed the attacks succeed across models and no
  defence stopped them fully (Liu et al., USENIX Security 2024) [TH-30].
- Records of deployment: a service's prompt injection let a user take over its logic and leak its hard-coded
  system prompt (CVE-2024-5184) [TH-31]; in an application framework, a prompt injection executed arbitrary
  code through the component that ran the model's output (CVE-2023-29374) [TH-32].
- Training the model to rank the deployment's instructions above the user's made it more robust, with some
  over-refusal (Wallace et al. 2024, preprint) [TH-33]: the susceptibility is a property of the model.

**Theoretical or not established.**

- A model that cannot be directly injected is not established; the cited defences reduce the rate only.

Organisation exposed: both. Level: model level for the susceptibility (Wallace et al. 2024, preprint) [TH-33]; system level for the
consequence, which is whatever the deployment's instructions protect and its output can reach (CVE-2024-5184; CVE-2023-29374) [TH-31, TH-32].
Status: observed in deployment. Label: established. Applies to: the generative model row, instruct and chat
models; every artefact format column. Framework: as Table 2.

### T16. Indirect prompt injection

*Enters at: S4, through content the model reads, a page, a document, an e-mail, a tool's output, first
answerable at Q4.2 on e4.3; exposure fixed at S3, Q3.2, by the retrieval and tools that bring content to the
model (SCRUM-284).*

When the model reads content the attacker wrote, instructions inside that content are followed as if they
came from the user. The attacker never talks to the model; they place text where the model will read it.

**Demonstrated.**

- Instructions planted in content read by production assistants, a search-integrated chat and code
  completion, led to data theft and to injections that spread themselves (Greshake et al., ACM AISec 2023)
  (Greshake et al., ACM AISec 2023) [TH-34].
- Records of deployment: an injection in an office assistant disclosed information over a network
  (CVE-2025-32711) [TH-35]; in a coding agent, an indirect injection wrote the agent's tool configuration and
  ran code without the user's approval (CVE-2025-54135) [TH-36]; in another coding assistant, a web-fetching
  tool reached files outside the workspace, so that an indirect injection could exfiltrate them
  (CVE-2025-66389) [TH-37].
- The official taxonomy states that current mitigations do not fully protect against indirect injection, and
  advises designing the system on the assumption that it will happen (NIST AI 100-2, section 3.4) [TH-03].

**Theoretical or not established.**

- A model that reliably separates instructions from the data it reads is not established.

Organisation exposed: both. Level: model level for the susceptibility, which no cited model is free of;
system level for the exposure and the consequence, which retrieval, tools and permissions decide. Status:
observed in deployment. Label: established; that the deployment records, on hosted assistants, describe a
susceptibility shared by open-source models (SCRUM-281) is an extension, emerging. Applies to: the generative
model row, with the image-and-text qualifier where content arrives as images; every artefact format column.
Framework: as Table 2.

### T17. Jailbreaks

*Enters at: S4, through the person writing the input, first answerable at Q4.2 on e4.3; exposure fixed at S3,
Q3.2, by the serving settings and guards (SCRUM-284). For an open-source model the attacker can also hold the
file, and prepare the jailbreak offline.*

A jailbreak is an input that makes the model produce what its safeguard (SCRUM-281) was trained to refuse. It differs
from T11 in that nothing in the model changes: the same file, given another input, refuses again.

**Demonstrated.**

- Safety training fails in two systematic ways, a request that sets the model's goals against each other and
  one phrased where the training did not reach, and attacks built on them succeeded on production models
  (Wei et al., NeurIPS 2023) [TH-38].
- Suffixes optimised on open models transferred to production services (Zou et al. 2023, preprint) [TH-39];
  hundreds of examples placed in a long input jailbroke widely used models, with success growing as a power
  law of their number (Anil et al., NeurIPS 2024) [TH-40]; a template with random search reached complete
  success on open and production models (Andriushchenko et al., ICLR 2025) [TH-41].
- On open models, changing only the generation settings raised the success rate from near zero to over 95 per
  cent on eleven models (Huang et al., ICLR 2024) [TH-42]; with the file, the refusal direction itself can be
  removed at inference (Arditi et al., NeurIPS 2024) [TH-17].

**Theoretical or not established.**

- A safeguard that resists all jailbreaks is not established; every cited defence is broken by a later
  attack in the cited work.

Organisation exposed: both; in possession (SCRUM-281) the organisation also sets the generation settings that one route
exploits (Huang et al., ICLR 2024) [TH-42]. Level: model level, since the safeguard is in the numbers; the generation-settings route
is system level, set by the serving configuration. Status: observed in deployment, through research on
production services (Wei et al., NeurIPS 2023; Andriushchenko et al., ICLR 2025) [TH-38, TH-41]. Label: established; transfer emerging (Zou et al. 2023, preprint) [TH-39]. Applies to: the generative
model row, instruct and chat models; every artefact format column. Framework: as Table 2.

### T18. Model extraction

*Enters at: S4, through whoever can query the endpoint, first answerable at Q4.4 on e4.5, the access record;
exposure fixed at S3, Q3.4, by who can reach the model and what its outputs expose (SCRUM-284).*

Extraction reconstructs a model's parameters or behaviour from its outputs. An open-source model is already
public, so extraction matters for what the organisation adds: a model it fine-tuned, adapted or merged at S2,
served to others, is its own, and its outputs can rebuild it.

**Demonstrated.**

- Logistic regressions, neural networks and decision trees were extracted almost exactly through the
  prediction interfaces of production machine-learning services (Tramèr et al., USENIX Security 2016)
  (Tramèr et al., USENIX Security 2016) [TH-43].
- Part of production language models, the final projection layer and the hidden size, was recovered through
  their public interface at low cost (Carlini et al., ICML 2024) [TH-44].

**Theoretical or not established.**

- Full extraction of a large generative model's parameters through its interface is not established; the
  cited work recovers one layer.

Organisation exposed: by proxy (SCRUM-281) the serving provider (SCRUM-281) answers for the endpoint, never for the model, and the
organisation that serves its own adjusted model is the party exposed. Level: system level; what can be
extracted is decided by what the endpoint returns and to whom. Status: observed in deployment, through
research on production services. Label: established. Applies to: every model type row, classification first
(Tramèr et al., USENIX Security 2016) [TH-43], generative (Carlini et al., ICML 2024) [TH-44]; artefact formats do not apply, since the attack needs only outputs. Framework: as
Table 2.

### T19. Training-data extraction

*Enters at: S4, through whoever can query the model, first answerable at Q4.2 on e4.3; exposure fixed at S2,
when the organisation trains or fine-tunes on its own data, and at S3, Q3.4 (SCRUM-284).*

A model can return data it was trained on, verbatim, or that data can be reconstructed from its outputs;
inversion is the reconstruction case. For an open-source model the producer's data is at stake; for the
organisation's own fine-tune, its own data is.

**Demonstrated.**

- Hundreds of verbatim training sequences, personal data among them, were extracted from a public generative
  model (Carlini et al., USENIX Security 2021) [TH-45].
- A production chat model was made to emit training data at about 150 times its normal rate, and thousands of
  examples were recovered (Nasr et al., ICLR 2025) [TH-46].
- Inversion reconstructed recognisable faces from a name and access to a face classifier's confidence values
  (Fredrikson et al., ACM CCS 2015) [TH-47]; from text embeddings, 92 per cent of 32-token inputs were
  recovered exactly, full names from clinical notes among them (Morris et al., EMNLP 2023) [TH-48].

**Theoretical or not established.**

- Which records of a given model can be extracted cannot be predicted from the data alone: not established.

Organisation exposed: both. Level: model level for memorisation, which is in the numbers; system level for
exposure, which the outputs returned and the access granted decide, embeddings stored and served included.
Status: observed in deployment, through research on a production service (Nasr et al., ICLR 2025) [TH-46]. Label: established.
Applies to: the generative model row (Carlini et al., USENIX Security 2021; Nasr et al., ICLR 2025) [TH-45, TH-46], the classification row (Fredrikson et al., ACM CCS 2015) [TH-47] and the embedding row
(Morris et al., EMNLP 2023) [TH-48]; every artefact format column. Framework: as Table 2.

### T20. Membership inference

*Enters at: S4, through whoever can query the model, first answerable at Q4.2 on e4.3; exposure fixed at S2,
by the data trained on, and at S3, Q3.4 and the outputs the endpoint returns (SCRUM-284).*

Membership inference decides from a model's outputs whether a given record was in its training data. It
reveals the fact of inclusion, a patient in a clinical dataset for example, without extracting the record.

**Demonstrated.**

- Shadow models trained to imitate the target inferred membership against classifiers built on production
  machine-learning services, a hospital dataset among them (Shokri et al., IEEE S&P 2017) [TH-49].
- On generative models trained on large public corpora, membership inference barely beat random guessing,
  and apparent successes came from differences between the member and non-member data rather than from
  membership (Duan et al., COLM 2024) [TH-50].

**Theoretical or not established.**

- Reliable membership inference against a large pre-trained generative model is not established (Duan et al., COLM 2024) [TH-50].
  Whether it holds for a model fine-tuned on a small dataset is not established in the cited sources.

Organisation exposed: both. Level: model level for what the numbers retain; system level for what the
outputs expose, such as confidence values. Status: observed in deployment on classifiers, through research
on production services (Shokri et al., IEEE S&P 2017) [TH-49]; not established on large generative models (Duan et al., COLM 2024) [TH-50]. Label: established.
Applies to: the classification row (Shokri et al., IEEE S&P 2017) [TH-49]; the generative row with the limit above (Duan et al., COLM 2024) [TH-50]; every artefact
format column. Framework: as Table 2.

### T21. Agentic and tool-use abuse

*Enters at: S4, through an input or content that reaches an agent, first answerable at Q4.2 on e4.3, the
inputs and the actions returned; exposure fixed at S3, Q3.2 and Q3.4, by the tools, permissions and autonomy
the deployment grants (SCRUM-284).*

An agent is a deployment in which the model calls tools, browses, runs code or acts on the organisation's
behalf. Agentic abuse makes it take an action no one authorised. It is usually reached through T15 or T16,
and its consequence is whatever the tools allow.

**Demonstrated.**

- In a benchmark of 97 tasks and 629 security cases, injected content made agents take attacker-chosen
  actions in a share of cases even against the best agents tested (Debenedetti et al., NeurIPS 2024) [TH-51];
  across 30 agents, a tool-integrated agent built on a leading model was attacked successfully in about a
  quarter of cases, and in about half with a reinforcing prompt (Zhan et al., Findings of ACL 2024) [TH-52].
- Trojaned adapters made an agent run malware and send spear-phishing (Dong et al., NDSS 2025) [TH-19]: the
  susceptibility can be planted in the model.
- Records of deployment: an indirect injection made a coding agent change its own tool configuration and run
  code without approval (CVE-2025-54135) [TH-36]; a web-fetching tool exposed files to exfiltration
  (CVE-2025-66389) [TH-37].

**Theoretical or not established.**

- An agent design that prevents unauthorised actions without limiting its tools is not established; the
  official taxonomy treats agents as exposed to every attack on the model plus those on their tools (NIST AI
  100-2, section 3.5) [TH-03].

Organisation exposed: both; by proxy the serving provider answers for its endpoint, and the organisation for
the tools it connects. Level: system level, decided by the tools, permissions and autonomy granted; model
level where the behaviour is planted (Dong et al., NDSS 2025) [TH-19]. Status: observed in deployment. Label: established. Applies to:
the generative model row, instruct and chat models; every artefact format column. Framework: as Table 2.

## Part 4. The boundary, applied

Table 4 applies the test of 1.5 to each threat: the part that goes with the file (SCRUM-281), which examination before
adoption can reveal and an acceptance criterion can require of the model, and the part that stays with the
deployment, which only observation in service sees and only a deployment can be required to meet. The
serving-side routes of the supply-chain document, plugins, custom operators and the compile cache
(Part 2.3, T8), sit wholly on the system side and are not repeated here.

**Table 4. Each threat on the boundary**

| Threat | Model level: goes with the file | System level: stays with the deployment | Revealed before adoption by | Seen in service by |
|---|---|---|---|---|
| T9 training-data poisoning | the learned behaviour | none | behaviour and internals, Q1.6, Q2.2 | outputs, Q4.2 |
| T10 backdoors and trojan triggers | the backdoor | none | trigger search, against the parent where one exists, Q1.6, Q2.2 | the trigger arriving, Q4.2 |
| T11 fine-tune and LoRA tampering | the change, and the adapter loaded with it | which fine-tune or adapter the server loads | comparison with the parent, Q1.6, Q2.3 | outputs against deployment, Q4.3 |
| T12 quantisation-induced drift | the drift | which precision is served | comparison with the parent, Q2.3, Q2.4 | outputs against deployment, Q4.3 |
| T13 quantisation-triggered backdoors | the planted rounding behaviour | which precision is served | comparison of the quantised copy with full precision, Q2.3 | outputs, Q4.2 |
| T14 merge contamination | the inherited behaviour | none | comparison with each parent, Q2.2, Q2.3 | outputs, Q4.2 |
| T15 direct prompt injection | the susceptibility | what the deployment's instructions protect and its output reaches | behaviour, Q1.6 | inputs and outputs, Q4.2 |
| T16 indirect prompt injection | the susceptibility | retrieval, tools and permissions | behaviour, Q1.6 | content arriving, Q4.2 |
| T17 jailbreaks | the safeguard's resistance | generation settings and guards | behaviour and internals, Q1.6 | inputs and outputs, Q4.2 |
| T18 model extraction | none | what the endpoint returns and to whom | none | access record, Q4.4 |
| T19 training-data extraction | memorisation | outputs returned, access granted | behaviour, Q1.6, Q2.3 | outputs, Q4.2 |
| T20 membership inference | what the numbers retain | outputs and confidence values exposed | behaviour, Q2.3 | outputs, Q4.2 |
| T21 agentic and tool-use abuse | the susceptibility, and a planted behaviour | tools, permissions, autonomy | behaviour, Q1.6 | actions returned, Q4.2 |

Three readings follow. Six threats are wholly or mainly model level, T9 to T14, and can be required of the
model before it is selected or after it is adjusted. One, model extraction, is wholly system level. The other
six are split: the model's susceptibility can be tested before adoption, and what it leads to is decided by
the deployment, so for them a criterion on the model and a criterion on the deployment are both needed.


## Part 5. Register

One row per threat, in the column order of the supply-chain document's register (Part 5, Table 6), with the stage tag and the status
added. The last column, Disposition, is left empty for the threat classification and decision cycle, which
decides the depth of treatment each threat receives and records that decision against it (report structure,
section 2.3); the completed rows form the threat disposition table (report structure, Appendix A).

**Table 3. Register of model-integrity and inference-time threats** (framework entries as in Table 2;
framework editions and their verification as in the source log, TH-01 to TH-03)

| Threat | Family | Enters at | Level | Organisation exposed | Applies to | Status | Label | Framework | Sources | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|
| T9 training-data poisoning | model-integrity | S1 Q1.6; S2 Q2.2 | model | both; by proxy black-box only | classification and generative rows, image-and-text qualifier; embedding not established; every format | demonstrated in research; in deployment not established | established; constant count emerging | LLM04:2025; AML.T0020; NIST 2.3, 3.2.1 | TH-03 to TH-07 | |
| T10 backdoors and trojan triggers | model-integrity | S1 Q1.6; S2 Q2.2 | model | both; by proxy black-box only, trigger unknown | classification and generative rows; embedding not established; every format | demonstrated in research; in deployment not established | established; persistence and generative trigger recovery emerging | LLM04:2025, LLM03:2025; AML.T0018, AML.T0018.000, AML.T0020; NIST 2.3.3, 3.2.2 | TH-03, TH-05, TH-08 to TH-14, TH-53, SC-17 | |
| T11 fine-tune and LoRA tampering | model-integrity | S1 Q1.6; S2 Q2.3 | model | both; by proxy black-box only | generative row, instruct and chat; adapter file kind; every format | observed in deployment for safeguard removal; demonstrated in research for planted adapter behaviour | established; largest-model and combined-adapter results emerging | LLM03:2025, LLM04:2025; AML.T0018.000, AML.T0054; NIST 3.1.3, 2.3.4 | TH-15 to TH-20 | |
| T12 quantisation-induced drift | model-integrity | S1 Q1.6; S2 Q2.3, Q2.4 | model | both; by proxy precision unknown | quantised model file kind, every row; GGUF chiefly | demonstrated in research | established for the effect; direction emerging | none; none; NIST 4.2.4 | TH-03, TH-21 | |
| T13 quantisation-triggered backdoors | model-integrity | S1, answerable at S2 Q2.3 or S1 Q1.6 on a quantised copy | model | both; by proxy black-box only | quantised model file kind; generative and classification rows; GGUF demonstrated | demonstrated in research | established; commercial-framework result emerging | none; none; NIST 4.2.4 | TH-03, TH-22 to TH-25 | |
| T14 merge contamination | model-integrity | S1 Q1.6; S2 Q2.2, Q2.3 | model | both | merged model file kind; generative row; every format | demonstrated in research; inherited evaluation contamination theoretical | established; leakage emerging | LLM03:2025; none; none | TH-01, TH-26 to TH-28 | |
| T15 direct prompt injection | inference-time and runtime | S4 Q4.2; exposure S3 Q3.2 | model susceptibility; system consequence | both | generative row, instruct and chat; every format | observed in deployment | established | LLM01:2025; AML.T0051.000; NIST 3.3 | TH-29 to TH-33 | |
| T16 indirect prompt injection | inference-time and runtime | S4 Q4.2; exposure S3 Q3.2 | model susceptibility; system exposure and consequence | both | generative row, image-and-text qualifier; every format | observed in deployment | established; transfer to open-source models emerging | LLM01:2025; AML.T0051.001; NIST 3.4 | TH-03, TH-34 to TH-37 | |
| T17 jailbreaks | inference-time and runtime | S4 Q4.2; exposure S3 Q3.2 | model; generation-settings route system | both; in possession the settings too | generative row, instruct and chat; every format | observed in deployment | established; transfer emerging | LLM01:2025; AML.T0054; NIST 3.3, 3.3.1 | TH-17, TH-38 to TH-42 | |
| T18 model extraction | inference-time and runtime | S4 Q4.4; exposure S3 Q3.4 | system | the party serving an adjusted model | every model type row; formats not applicable | observed in deployment | established | LLM10:2025; AML.T0024.002; NIST 2.4.4 | TH-43, TH-44 | |
| T19 training-data extraction | inference-time and runtime | S4 Q4.2; exposure S2 and S3 Q3.4 | model memorisation; system exposure | both | generative, classification and embedding rows; every format | observed in deployment | established | LLM02:2025; AML.T0024.001, AML.T0057; NIST 2.4.1, 3.3.2 | TH-45 to TH-48 | |
| T20 membership inference | inference-time and runtime | S4 Q4.2; exposure S2 and S3 Q3.4 | model retention; system exposure | both | classification row; generative row not established as reliable; every format | observed in deployment on classifiers; not established on large generative models | established | LLM02:2025; AML.T0024.000; NIST 2.4.2 | TH-49, TH-50 | |
| T21 agentic and tool-use abuse | inference-time and runtime | S4 Q4.2; exposure S3 Q3.2, Q3.4 | system; model where planted | both | generative row, instruct and chat; every format | observed in deployment | established | LLM06:2025; AML.T0053, AML.T0086; NIST 3.5 | TH-03, TH-19, TH-36, TH-37, TH-51, TH-52 | |

## Summary: the four questions answered

**Which threats have been shown to work, and which are still argued?** Six of the thirteen are observed in
deployment: safeguard (SCRUM-281) removal by fine-tuning, through a production service and in published abliterated
copies (T11); direct and indirect prompt injection, recorded in security advisories (T15, T16); jailbreaks,
model extraction and training-data extraction, shown against production services (T17 to T19); and agentic
abuse, recorded in advisories (T21). Membership inference is observed on classifiers and not established as
reliable on large generative models (T20). Five are demonstrated in research and not established in any
published model: poisoning, backdoors, quantisation drift, quantisation-triggered backdoors and merged
backdoors (T9, T10, T12 to T14). What is theoretical is narrower: a backdoor that arises without being planted
(T10) and evaluation contamination inherited through a merge (T14). Ten threats are named by all three
frameworks, the two quantisation threats by NIST alone, and merge contamination by OWASP alone (Table 2).

**At which point does each threat enter?** The six model-integrity threats enter at selection, with the model,
or at adjustment, through the organisation's own change or one made on its behalf; the quantisation-triggered
backdoor enters at selection and can be answered only once a quantised copy exists. The seven inference-time
and runtime threats enter in service, with their exposure fixed at deployment, and for training-data
extraction and membership inference also at adjustment, by the data the organisation trains on (Table 3).

**Can the threat be judged on the model, or only on the deployed system?** By one test: what goes with the
file is model level, what stays with the deployment is system level (1.5). T9 to T14 are model level and can
be required of the model before it is selected or after it is adjusted. Model extraction is system level and
can be required only of a deployment. The other six are split: the model's susceptibility can be tested before
adoption, and what it leads to is decided by the deployment, so both a criterion on the model and a criterion
on the deployment are needed (Table 4). Examination before adoption can search for a trigger and, in
classifiers and generative models, find one with the error rates its evaluation reports; a scan that finds
nothing is statistical evidence within the kinds of backdoor it covers, not a proof that none is there, so
observation in service is not optional.

**Which threats must the threat classification and decision cycle decide on?** All thirteen, each with one
row in Table 3 carrying its family, entry stage, level, exposure, model types, status, confidence label,
framework entries and sources, and an empty Disposition column for the decision.

## Annex. The lifecycle questions and evidence items this document uses

The stage tags of every entry name a question, Qn.k, and an evidence item, en.k, of the lifecycle assessment
framework (SCRUM-284). Table 5 gives the text of each one used here, in the framework's own words, so that a tag
can be read without the framework at hand. n is the stage, S1 to S4; k numbers the questions or items of that
stage. The evidence kind says who can produce the item and whether it exists by proxy (1.4).

**Table 5. Questions and evidence items cited in the stage tags** (text as in SCRUM-284, stage tables)

| Symbol | Stage | Question, or evidence item and its kind |
|---|---|---|
| Q1.6 | S1 selection | Does it behave as described, and is the safeguard present? |
| Q2.2 | S2 adjustment | Did the change carry in anything we did not intend? |
| Q2.3 | S2 adjustment | Is the safeguard still present after the change? |
| Q2.4 | S2 adjustment | Is the adjusted artefact still what the segmentation says, and does it still do what the base was selected for? |
| Q3.2 | S3 deployment | What surrounds the model, and does it change what the model does? |
| Q3.4 | S3 deployment | Who can reach the model and its file? |
| Q4.2 | S4 runtime detection | Are the inputs arriving in service turning the model against its use, and does it comply? |
| Q4.3 | S4 runtime detection | Does the model still give the outputs it gave at deployment? |
| Q4.4 | S4 runtime detection | Who is reaching the model and its file, and how much? |
| e1.2 | S1 selection | declared: the model card: parent model, training data, organisation behind the account, what the model produces, modality |
| e1.9 | S1 selection | testable, outputs: behaviour on the organisation's inputs |
| e1.10 | S1 selection | testable, internals: the file's internals while it runs |
| e2.2 | S2 adjustment | readable: the organisation's record of the change: training data, recipe, adapter or changed tensors |
| e2.3 | S2 adjustment | declared: the account of the change, its base and the served format, from the party that made it |
| e2.4 | S2 adjustment | testable, internals: the adjusted weights and activations against the base |
| e2.5 | S2 adjustment | testable, outputs: behaviour on the adjusted model, same inputs as e1.9 |
| e4.3 | S4 runtime detection | testable, outputs: the inputs arriving at the endpoint in service, user, retrieved content and tool outputs, and the outputs returned |
| e4.5 | S4 runtime detection | readable: the organisation's access record for the endpoint, the file at rest and the container, against e3.6 |

## Source log

The sources this document adds. Each row gives:

- **ID**: the citation key used in the text.
- **Class** (SCRUM-281): *Official*, a standards or framework body, or a party writing about its own artefact
  or service; or *Research*, a paper at an accepted venue, or a preprint labelled as such.
- **Source** and **URL**: what was read and where.
- **Verified**: what was checked in it, and the statement the citation rests on.

| ID | Class (SCRUM-281) | Source | URL | Verified |
|---|---|---|---|---|
| TH-01 | Official | OWASP Top 10 for LLM Applications, 2025 edition; OWASP GenAI Security Project; entry pages LLM01 to LLM10 | https://genai.owasp.org/llm-top-10/ ; entry pages under https://genai.owasp.org/llmrisk/ | [CHECKED] all ten entry pages read 16 November 2026. LLM01: direct and indirect prompt injections; jailbreaking a related concept. LLM02: training data, inversion attacks; references AML.T0024.000 to .002. LLM03: malicious LoRA adapters; pre-trained models with hidden backdoors; collaborative model merge, "model merging ... can be exploited to bypass reviews". LLM04: pre-training, fine-tuning or embedding data manipulated to introduce backdoors; behaviour untouched until a trigger. LLM06: excessive functionality, permissions, autonomy. LLM10: model extraction via API; functional model replication. No entry mentions quantisation. No release date on the English page; cited as the 2025 edition, which predates the cut-off |
| TH-02 | Official | MITRE ATLAS, release 2026.09 of 15 September 2026, current at the research cut-off; data at github.com/mitre-atlas/atlas-data | https://atlas.mitre.org/ | [CHECKED] read from the release's data file, 224 techniques. AML.T0020 Training Data Poisoning; AML.T0018 Manipulate AI Model ("may retain expected behavior under ordinary conditions while activating malicious behavior only for selected inputs"), AML.T0018.000 Poison AI Model (weights, poisoned data, further fine-tuning); AML.T0051.000 and .001 LLM Prompt Injection, Direct and Indirect; AML.T0054 LLM Jailbreak ("via adversarial prompting, or by modifying model weights or safety mechanisms"); AML.T0024.000 Infer Training Data Membership, .001 Invert AI Model, .002 Extract AI Model; AML.T0057 LLM Data Leakage; AML.T0053 AI Agent Tool Invocation; AML.T0086 Exfiltration via AI Agent Tool Invocation. No technique's text mentions quantisation or model merging. Release 2026.10 of 28 October 2026, after the cut-off, restructures the inference techniques; this document keeps 2026.09 |
| TH-03 | Official | Vassilev, Oprea, Fordyce, Anderson, Davies, Hamin. "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations". NIST AI 100-2 E2025, March 2025; DOI 10.6028/NIST.AI.100-2e2025 | https://csrc.nist.gov/pubs/ai/100/2/e2025/final | [CHECKED] full text read 16 November 2026. Sections used: 2.3 Poisoning (poisoning studied in spam detection, malware classification, computer vision and NLP; NLP backdoors for sentiment analysis and toxic comment detection against transformer models), 2.3.3 Backdoor Poisoning, 2.3.4 Model Poisoning; 2.4.1 Data Reconstruction, 2.4.2 Membership Inference, 2.4.4 Model Extraction; 3.1.3 Attacker Capabilities ("fine-tuning circumvention attacks which remove refusal behavior"); 3.2.1 Data Poisoning, 3.2.2 Model Poisoning; 3.3 Direct Prompting, 3.3.2 Information Extraction; 3.4 Indirect Prompt Injection; 3.5 Security of Agents; 4.2.4 Quantized Models ("quantized models inherit the vulnerabilities of the original models and introduce additional weaknesses"; "widely used quantization methods can be exploited to produce a harmful quantized LLM, even though the full-precision counterpart appears benign"). No passage on model merging |
| TH-04 | Research | Carlini, Jagielski, Choquette-Choo, Paleka, Pearce, Anderson, Terzis, Thomas, Tramèr. "Poisoning Web-Scale Training Datasets is Practical". IEEE S&P 2024, pp. 407-425; DOI 10.1109/SP54263.2024.00179 | https://arxiv.org/abs/2302.10149 | [CHECKED] split-view and frontrunning poisoning; 0.01 per cent of LAION-400M or COYO-700M poisonable for about 60 US dollars; ten datasets vulnerable |
| TH-05 | Research | Wan, Wallace, Shen, Klein. "Poisoning Language Models During Instruction Tuning". ICML 2023, PMLR 202 | https://arxiv.org/abs/2305.00944 | [CHECKED] about 100 poisoned examples make a trigger phrase cause negative polarity or degenerate output on held-out tasks; larger models more vulnerable |
| TH-06 | Research | Zhang, Rando, Evtimov, Chi, Smith, Carlini, Tramèr, Ippolito. "Persistent Pre-Training Poisoning of LLMs". ICLR 2025 | https://arxiv.org/abs/2410.13722 | [CHECKED] 0.1 per cent of pre-training data; three of four attacks persist through post-training; denial of service persists at 0.001 per cent; models 600M to 7B trained from scratch |
| TH-07 | Research, preprint | Souly, Rando, Chapman, Davies, Hasircioglu, Shereen, Mougan, Mavroudis, Jones, Hicks, Carlini, Gal, Kirk. "Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples". arXiv:2510.07192 | https://arxiv.org/abs/2510.07192 | [CHECKED] 250 poisoned documents backdoor models from 600M to 13B regardless of clean-data size; success depends on the absolute count. A later conference listing exists; cited as the preprint, which predates the cut-off: emerging |
| TH-08 | Research | Rando, Tramèr. "Universal Jailbreak Backdoors from Poisoned Human Feedback". ICLR 2024 | https://arxiv.org/abs/2311.14455 | [CHECKED] poisoned RLHF data plants a universal trigger word that turns any prompt into a jailbreak |
| TH-09 | Research | Gu, Liu, Dolan-Gavitt, Garg. "BadNets: Evaluating Backdooring Attacks on Deep Neural Networks". IEEE Access 7, 2019, pp. 47230-47244; DOI 10.1109/ACCESS.2019.2909068 | https://doi.org/10.1109/ACCESS.2019.2909068 | [CHECKED] outsourced training yields a network clean on validation and misbehaving on a trigger; stop sign with a sticker read as a speed limit; backdoor survives transfer learning |
| TH-10 | Research | Kurita, Michel, Neubig. "Weight Poisoning Attacks on Pretrained Models". ACL 2020, pp. 2793-2806 | https://arxiv.org/abs/2004.06660 | [CHECKED] backdoors planted in pre-trained weights survive downstream fine-tuning; BERT-class classifiers |
| TH-11 | Research, preprint | Hubinger et al. "Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training". arXiv:2401.05566 | https://arxiv.org/abs/2401.05566 | [CHECKED] deliberately backdoored models, secure code for 2023 and exploitable code for 2024, persist through SFT, RL and adversarial training; adversarial training improves trigger recognition; persistence strongest in larger models and with chain of thought. No peer-reviewed venue found: emerging |
| TH-12 | Research | Yan, Mo, Ren, Jia. "Rethinking Backdoor Detection Evaluation for Language Models". EMNLP 2025 | https://arxiv.org/abs/2409.00399 | [CHECKED] backdoor detectors fail when the training intensity of the poisoned model varies |
| TH-13 | Research | Liu, Shen, Tao, An, Ma, Zhang. "Piccolo: Exposing Complex Backdoors in NLP Transformer Models". IEEE S&P 2022, pp. 2025-2042; DOI 10.1109/SP46214.2022.9833579 | https://par.nsf.gov/biblio/10335908 (accepted manuscript) | [CHECKED] abstract of the accepted manuscript: trigger-word inversion with word discriminativity analysis, given the subject model and a few benign samples; 3,839 NLP models from TrojAI and earlier work, 7 structures including BERT and GPT, 17 attack types; over 0.9 detection accuracy in most scenarios; top in 2 of 3 TrojAI NLP rounds. Venue and pages from the DOI record |
| TH-14 | Research, preprint | Maloyan, Verma, Nutfullin, Ashinov. "Trojan Detection in Large Language Models: Insights from The Trojan Detection Challenge". arXiv:2404.13660 | https://arxiv.org/abs/2404.13660 | [CHECKED] abstract: Trojan Detection Competition 2023 on LLMs; top methods reach recall about 0.16, comparable to randomly sampling sentences similar to the training prefixes; difficulty separating intended from unintended triggers. Preprint: emerging |
| TH-15 | Research | Qi, Zeng, Xie, Chen, Jia, Mittal, Henderson. "Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!". ICLR 2024 | https://arxiv.org/abs/2310.03693 | [CHECKED] ten harmful examples through a production fine-tuning API remove safety alignment; benign fine-tuning also degrades it; production service and an open chat model |
| TH-16 | Research, preprint | Lermen, Rogers-Smith, Ladish. "LoRA Fine-tuning Efficiently Undoes Safety Training in Llama 2-Chat 70B". arXiv:2310.20624 | https://arxiv.org/abs/2310.20624 | [CHECKED] LoRA reduces the 70B model's refusal rate to about 1 per cent on two benchmarks, one GPU, capabilities kept. No venue found: emerging |
| TH-17 | Research | Arditi, Obeso, Syed, Paleka, Panickssery, Gurnee, Nanda. "Refusal in Language Models Is Mediated by a Single Direction". NeurIPS 2024 | https://arxiv.org/abs/2406.11717 | [CHECKED] refusal mediated by one direction in 13 open chat models up to 72B; rank-one weight edit as a white-box jailbreak |
| TH-18 | Research, preprint | Liu et al. "LoRATK: LoRA Once, Backdoor Everywhere in the Share-and-Play Ecosystem" (v1: "LoRA-as-an-Attack! Piercing LLM Safety Under The Share-and-Play Scenario"). arXiv:2403.00108 | https://arxiv.org/abs/2403.00108 | [CHECKED] backdoored shared LoRA modules; the backdoor persists when adapters are combined. No venue found: emerging |
| TH-19 | Research | Dong, Xue, Chen, Holland, Meng, Li, Liu, Zhu. "The Philosopher's Stone: Trojaning Plugins of Large Language Models". NDSS 2025 | https://www.ndss-symposium.org/ndss-paper/the-philosophers-stone-trojaning-plugins-of-large-language-models/ | [CHECKED] trojaned LoRA adapters make a model emit attacker content or misuse tools, an agent running malware and spear-phishing; three defences tested, none fully effective |
| TH-20 | Official | Hugging Face Hub model search, query "abliterated"; Hugging Face | https://huggingface.co/models?search=abliterated | [CHECKED] the platform's own listing returns repositories that name themselves abliterated; no count is used in the text |
| TH-21 | Research, preprint | Kumar, Kumar, Agarwal, Harshangi. "Fine-Tuning, Quantization, and LLMs: Navigating Unintended Outcomes" (v1: "Increased LLM Vulnerabilities from Fine-tuning and Quantization"). arXiv:2404.04392 | https://arxiv.org/abs/2404.04392 | [CHECKED] fine-tuning raises jailbreak success; quantisation has mixed effects; open models. Industry preprint: emerging |
| TH-22 | Research | Egashira, Vero, Staab, He, Vechev. "Exploiting LLM Quantization". NeurIPS 2024 | https://arxiv.org/abs/2405.18137 | [CHECKED] a full-precision model appears benign and is malicious once quantised: vulnerable code, content injection, over-refusal |
| TH-23 | Research | Egashira, Staab, Vero, He, Vechev. "Mind the Gap: A Practical Attack on GGUF Quantization". ICML 2025, PMLR 267 | https://arxiv.org/abs/2505.23786 | [CHECKED] first attack on GGUF k-quants: 3 models, 9 GGUF types; 88.7 per cent insecure code, 85.0 per cent content injection |
| TH-24 | Research, preprint | Ma, Qiu, Gao, Zhang, Abuadbba, Xue, Fu, Zhang, Al-Sarawi, Abbott. "Quantization Backdoors to Deep Learning Commercial Frameworks". arXiv:2108.09187 | https://arxiv.org/abs/2108.09187 | [CHECKED] a dormant backdoor activated by standard int8 post-training quantisation in TFLite and PyTorch Mobile, close to complete success. Journal publication stated by the authors, record not retrieved: cited as the preprint, emerging |
| TH-25 | Research | Hong, Panaitescu-Liess, Kaya, Dumitraş. "Qu-ANTI-zation: Exploiting Quantization Artifacts for Achieving Adversarial Outcomes". NeurIPS 2021 | https://arxiv.org/abs/2110.13541 | [CHECKED] training makes quantisation cause accuracy loss, targeted misclassification or a backdoor; convolutional classifiers |
| TH-26 | Research | Zhang, Chi, Li, Cai, Zhang, Tian. "BadMerging: Backdoor Attacks Against Model Merging". ACM CCS 2024; DOI 10.1145/3658644.3690284 | https://arxiv.org/abs/2408.07362 | [CHECKED] one backdoored task model compromises the merged model despite merging coefficients |
| TH-27 | Research | Yuan, Xu, Shi, Zhou, Sun. "Merge Hijacking: Backdoor Attacks to Model Merging of Large Language Models". ACL 2025; DOI 10.18653/v1/2025.acl-long.1571 | https://arxiv.org/abs/2505.23561 | [CHECKED] an uploaded malicious model passes its backdoor to the merged LLM, which keeps utility; survives paraphrasing, CLEANGEN and fine-pruning; LLaMA-2, Qwen, Phi-3 |
| TH-28 | Research, preprint | Guo et al. "Be Cautious When Merging Unfamiliar LLMs: A Phishing Model Capable of Stealing Privacy". arXiv:2502.11533 | https://arxiv.org/abs/2502.11533 | [CHECKED] a phishing model merged in raises personal-data and membership leakage of the merged model: emerging |
| TH-29 | Research | Perez, Ribeiro. "Ignore Previous Prompt: Attack Techniques For Language Models". NeurIPS 2022 ML Safety Workshop | https://arxiv.org/abs/2211.09527 | [CHECKED] goal hijacking and prompt leaking against a production model's API |
| TH-30 | Research | Liu, Jia, Geng, Jia, Gong. "Formalizing and Benchmarking Prompt Injection Attacks and Defenses". USENIX Security 2024 | https://arxiv.org/abs/2310.12815 | [CHECKED] 5 attacks, 10 defences, 10 models, 7 tasks |
| TH-31 | Official | CVE-2024-5184, EmailGPT; NVD record | https://nvd.nist.gov/vuln/detail/CVE-2024-5184 | [CHECKED] prompt injection lets a user take over service logic and leak hard-coded system prompts; a direct injection |
| TH-32 | Official | CVE-2023-29374, LangChain LLMMathChain; NVD record | https://nvd.nist.gov/vuln/detail/CVE-2023-29374 | [CHECKED] through 0.0.131, prompt injection executes arbitrary code via Python exec |
| TH-33 | Research, preprint | Wallace, Xiao, Leike, Weng, Heidecke, Beutel. "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions". arXiv:2404.13208 | https://arxiv.org/abs/2404.13208 | [CHECKED] training a priority of system over user over tool output improves robustness, with some over-refusal: emerging |
| TH-34 | Research | Greshake, Abdelnabi, Mishra, Endres, Holz, Fritz. "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection". ACM AISec 2023 | https://arxiv.org/abs/2302.12173 | [CHECKED] indirect injection against production search-integrated chat and code completion; data theft, self-spreading injection |
| TH-35 | Official | CVE-2025-32711, Microsoft 365 Copilot; NVD and Microsoft records | https://nvd.nist.gov/vuln/detail/CVE-2025-32711 | [CHECKED] "AI command injection in M365 Copilot allows an unauthorized attacker to disclose information over a network" |
| TH-36 | Official | CVE-2025-54135, Cursor (advisory GHSA-4cxx-hrm3-49rm); NVD record | https://nvd.nist.gov/vuln/detail/CVE-2025-54135 | [CHECKED] below 1.3.9, an indirect prompt injection creates the agent's MCP configuration and runs code without user approval |
| TH-37 | Official | CVE-2025-66389, GitHub Copilot; NVD record | https://nvd.nist.gov/vuln/detail/CVE-2025-66389 | [CHECKED] a fetch tool reaches files outside the workspace without approval, so that exfiltration could occur through indirect prompt injection |
| TH-38 | Research | Wei, Haghtalab, Steinhardt. "Jailbroken: How Does LLM Safety Training Fail?". NeurIPS 2023 | https://arxiv.org/abs/2307.02483 | [CHECKED] competing objectives and mismatched generalisation; attacks succeed on production models |
| TH-39 | Research, preprint | Zou, Wang, Carlini, Nasr, Kolter, Fredrikson. "Universal and Transferable Adversarial Attacks on Aligned Language Models". arXiv:2307.15043 | https://arxiv.org/abs/2307.15043 | [CHECKED] suffixes optimised on open models transfer to production services. No venue found: emerging |
| TH-40 | Research | Anil et al. "Many-shot Jailbreaking". NeurIPS 2024; DOI 10.52202/079017-4121 | https://doi.org/10.52202/079017-4121 | [CHECKED] hundreds of in-context examples jailbreak widely used models; success follows a power law in their number |
| TH-41 | Research | Andriushchenko, Croce, Flammarion. "Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks". ICLR 2025 | https://arxiv.org/abs/2404.02151 | [CHECKED] template plus random search: complete success on open and production models |
| TH-42 | Research | Huang, Gupta, Xia, Li, Chen. "Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation". ICLR 2024 | https://arxiv.org/abs/2310.06987 | [CHECKED] changing decoding settings alone raises success from near 0 to over 95 per cent on 11 open models |
| TH-43 | Research | Tramèr, Zhang, Juels, Reiter, Ristenpart. "Stealing Machine Learning Models via Prediction APIs". USENIX Security 2016 | https://arxiv.org/abs/1609.02943 | [CHECKED] near-exact extraction of logistic regression, neural networks and decision trees through production prediction APIs |
| TH-44 | Research | Carlini et al. "Stealing Part of a Production Language Model". ICML 2024, PMLR 235 | https://arxiv.org/abs/2403.06634 | [CHECKED] final projection layer and hidden dimension of production models recovered through the public API at low cost |
| TH-45 | Research | Carlini et al. "Extracting Training Data from Large Language Models". USENIX Security 2021 | https://arxiv.org/abs/2012.07805 | [CHECKED] hundreds of verbatim training sequences, personal data among them, from a public model |
| TH-46 | Research | Nasr et al. "Scalable Extraction of Training Data from Aligned, Production Language Models". ICLR 2025 | https://arxiv.org/abs/2311.17035 | [CHECKED] a divergence attack makes a production chat model emit training data at about 150 times the normal rate; thousands of examples |
| TH-47 | Research | Fredrikson, Jha, Ristenpart. "Model Inversion Attacks that Exploit Confidence Information and Basic Countermeasures". ACM CCS 2015; DOI 10.1145/2810103.2813677 | https://doi.org/10.1145/2810103.2813677 | [CHECKED] recognisable faces reconstructed from a name and confidence values |
| TH-48 | Research | Morris, Kuleshov, Shmatikov, Rush. "Text Embeddings Reveal (Almost) As Much As Text". EMNLP 2023 | https://arxiv.org/abs/2310.06816 | [CHECKED] 92 per cent of 32-token inputs recovered exactly from embeddings; full names from clinical notes |
| TH-49 | Research | Shokri, Stronati, Song, Shmatikov. "Membership Inference Attacks against Machine Learning Models". IEEE S&P 2017 | https://arxiv.org/abs/1610.05820 | [CHECKED] shadow-model membership inference against classifiers trained on production ML services, a hospital dataset among them |
| TH-50 | Research | Duan et al. "Do Membership Inference Attacks Work on Large Language Models?". COLM 2024 | https://arxiv.org/abs/2402.07841 | [CHECKED] membership inference barely beats random on models trained on a large public corpus, 160M to 12B; apparent success from distribution shift |
| TH-51 | Research | Debenedetti, Zhang, Balunović, Beurer-Kellner, Fischer, Tramèr. "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents". NeurIPS 2024 Datasets and Benchmarks | https://arxiv.org/abs/2406.13352 | [CHECKED] 97 tasks, 629 security cases; attacks succeed in a share of cases against the best agents |
| TH-52 | Research | Zhan, Liang, Ying, Kang. "InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents". Findings of ACL 2024 | https://arxiv.org/abs/2403.02691 | [CHECKED] 1,054 cases, 30 agents; a ReAct agent on a leading model attacked in 24 per cent of cases, 47 per cent with a reinforcing prompt |
| TH-53 | Research | Shen, Cheng, Zhang, Tao, Zhang, Guo, Yan, Jin, An, Ma, Zhang. "BAIT: Large Language Model Backdoor Scanning by Inverting Attack Target". IEEE S&P 2025, pp. 1676-1694 | https://www.cs.purdue.edu/homes/cheng535/static/papers/sp25_bait.pdf (authors' copy) | [CHECKED] abstract: scans by inverting backdoor targets instead of triggers, without prior knowledge of trigger or target, with black-box access; evaluated on 153 LLMs, 8 architectures, 6 attack types; outperforms 5 baselines; top of the TrojAI LLM-round leaderboard. An independent preprint reports lower scores on code models, a different setting |

Sources read after
the research cut-off are read for records that predate it: the ATLAS release in force at the cut-off, and
papers published before it.

Searched and not found, recorded for the log: any official record or research measurement of a published
open-source model poisoned through its training data, or carrying a trigger backdoor in its numbers. Press
coverage motivated no claim here.

## Symbols from outside this document

| Symbol | Meaning | Defined in | File |
|---|---|---|---|
| (SCRUM-281) after a term | the term is a glossary term; shown at its first use in each part | SCRUM-281, report style guide and glossary, version 1.3, section 1 | governing/report-style-guide-and-glossary.md |
| established, emerging, forecast | confidence labels | SCRUM-281, section 2.3 | governing/report-style-guide-and-glossary.md |
| Official, Research | citation classes | SCRUM-281, section 2.2, Table 2.1 | governing/report-style-guide-and-glossary.md |
| model level, system level | the level a threat acts at | SCRUM-281, section 1.4, threat | governing/report-style-guide-and-glossary.md |
| S1 to S4 | lifecycle stages: selection, adjustment, deployment, runtime detection | glossary term: SCRUM-281, section 1.4; numbering and questions: SCRUM-284, section 1.3, Table 2, and Notation | governing/report-style-guide-and-glossary.md; process/scrum-284/scrum284.md; process/scrum-284/stage-tables.md |
| Qn.k | lifecycle assessment question k at stage n, those used given in full in Table 5; e.g. Q1.6 "Does it behave as described, and is the safeguard present?" | SCRUM-284, Table 2 and the stage question tables | process/scrum-284/scrum284.md and stage-tables.md |
| en.k | evidence item k at stage n, those used given in full in Table 5; e.g. e1.9 behaviour on the organisation's inputs | SCRUM-284, the stage evidence inventories E1 to E4 | process/scrum-284/stage-tables.md |
| declared | evidence a party states and nothing verifies | SCRUM-284, Table 1 | process/scrum-284/scrum284.md |
| (SCRUM-284) Table 1 | the evidence kind decides who answers and what exists by proxy | SCRUM-284 | process/scrum-284/scrum284.md |
| (SCRUM-280) Table 4 | the segmentation: model type against artefact format | SCRUM-280 | process/scrum-280/scrum280.md |
| report structure, section 2.3, and Appendix A | the threat classification and decision cycle, how the depth of treatment for each threat is decided and by whom; and the threat disposition table, the full threat inventory with the classification decision recorded against every entry | report skeleton, version 0.2 | skeleton/nk_dans_incd_report.docx |
| report structure, section 6.1 | the report's lifecycle assessment framework section: what question is answered at selection, adjustment, deployment and runtime detection | report skeleton, version 0.2 | skeleton/nk_dans_incd_report.docx |
| report structure, sections 4.3 and 4.4 | the report's sections on model-integrity threats and on inference-time and runtime threats, whose named scope is the thirteen threats | report skeleton, version 0.2 | skeleton/nk_dans_incd_report.docx |
| (SCRUM-286) section 1.1 | derivative and quantised variants on the primary model repository, by declared derivative kind | SCRUM-286 | process/scrum-286/scrum286.md |
| (SCRUM-286) section 2.3 | provenance metadata among widely used models: declared fields present | SCRUM-286 | process/scrum-286/scrum286.md |
| T1 to T8; "the supply-chain document" | supply-chain and artefact-level threats, defined in Part 2 of "Supply-chain and artefact-level threats on the Hugging Face Hub"; T3 malicious serialisation, T6 malicious adapters; register in Part 5, Table 6 | supply-chain document, Parts 2 and 5 | process/huggingface/hub-supply-chain-threats.md |
| [SC-nn] | supply-chain sources | supply-chain document, source log | process/huggingface/hub-supply-chain-threats.md |
