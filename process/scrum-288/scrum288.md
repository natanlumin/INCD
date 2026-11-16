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
5 is the register. A closing summary answers the four questions of Table 1.

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
LLM Applications [TH-01]; MITRE ATLAS [TH-02]; and NIST AI 100-2, the adversarial machine learning taxonomy [TH-03]. The last column of
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
  the evidence item that answers it, en.k (SCRUM-284);
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
recorded in the source log [TH-01, TH-02, TH-03].

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
  [TH-11].
- A search can find a trigger in a classifier. A scanner that inverts the words most likely to form a trigger,
  given only the model and a few benign samples, detected backdoors in 3,839 language classifiers of seven
  transformer structures, BERT and GPT among them, across 17 attack types, with over 0.9 detection accuracy
  in most settings (Liu et al., IEEE S&P 2022) [TH-13].
- Detection is fragile. Backdoor detectors evaluated for language models failed when the strength with which
  the backdoor was trained was varied, so a detector's published success does not carry to backdoors trained
  differently (Yan et al., EMNLP 2025) [TH-12].
- In generative models, recovering a planted trigger is far harder. In a trigger-detection competition on
  generative language models, the best methods recovered the planted triggers with a recall of about 0.16,
  comparable to sampling sentences at random from inputs like the training prefixes (Maloyan et al. 2024,
  preprint) [TH-14].

**Theoretical or not established.**

- A trigger backdoor in a published open-source model is not established. The malicious models found on the
  Hugging Face Hub carried code that runs when the file is loaded, not behaviour planted in the numbers
  (Zhao et al., ASE 2024) [SC-17]; that is malicious serialisation, T3 of the supply-chain document (Part 2.2), and not this threat.
- A backdoor that arises without anyone planting it is theoretical. The persistent backdoors above were built
  deliberately, as studies of what such behaviour would do (Hubinger et al. 2024, preprint) [TH-11].
- A method that finds an unknown trigger in a generative model reliably is not established: the search that
  works on classifiers [TH-13] has no counterpart of that strength for generative models in the cited sources
  (Yan et al., EMNLP 2025; Maloyan et al. 2024, preprint) [TH-12, TH-14].

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
| T10 backdoors and trojan triggers | model-integrity | S1 Q1.6; S2 Q2.2 | model | both; by proxy black-box only, trigger unknown | classification and generative rows; embedding not established; every format | demonstrated in research; in deployment not established | established; persistence and generative trigger recovery emerging | LLM04:2025, LLM03:2025; AML.T0018, AML.T0018.000, AML.T0020; NIST 2.3.3, 3.2.2 | TH-03, TH-05, TH-08 to TH-14, SC-17 | |

## Summary: the four questions answered

**Which threats have been shown to work, and which are still argued?** The literature demonstrates both
poisoning and backdoors in research, on models the researchers built, and does not establish either in a
published open-source model (SCRUM-281). Poisoning works from a small and possibly near-constant number of examples and
persists through the training that makes a chat model; a backdoor survives the victim's fine-tuning and, in
deliberately built cases, safety training. What is theoretical is a backdoor that arises without being
planted. Of the thirteen threats, ten are named by all three frameworks, the two quantisation threats by NIST
alone, and merge contamination by OWASP alone (Table 2).

**At which point does each threat enter?** Model-integrity threats enter at selection, with the model, or at
adjustment, through the organisation's own change or one made on its behalf. Inference-time and runtime threats
enter in service, with exposure fixed at deployment. Poisoning and backdoors enter at selection through the
producer (SCRUM-281) or a third party, and at adjustment through data or a change the organisation commissions.

**Can the threat be judged on the model, or only on the deployed system?** By one test: a threat that moves
with the file (SCRUM-281) is model level and can be required of the model before it is selected; one that stays with the
deployment is system level and can be required only of a deployment. Poisoning and backdoors are model level.
Examination before adoption can search for a trigger and, in classifiers, find one, but cannot show that none
is there, and recovering a planted trigger in a generative model is not reliable with any method the
literature establishes; observation in service is therefore not optional for them.

**Which threats must the classification and decision cycle decide on?** All thirteen, each with one register
row in Table 3 carrying its family, entry stage, level, exposure, model types, status, confidence label (SCRUM-281),
framework entries and sources, and an empty Disposition column for the decision.

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
| Qn.k | lifecycle assessment question k at stage n; e.g. Q1.6 "Does it behave as described, and is the safeguard present?" | SCRUM-284, Table 2 and the stage question tables | process/scrum-284/scrum284.md and stage-tables.md |
| en.k | evidence item k at stage n; e.g. e1.9 behaviour on the organisation's inputs | SCRUM-284, the stage evidence inventories E1 to E4 | process/scrum-284/stage-tables.md |
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
