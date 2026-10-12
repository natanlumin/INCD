# SCRUM-284 working file: lifecycle stage tables

Status 12 October 2026: all four stages drafted and reviewed, selection, adjustment and deployment agreed, runtime
detection under review. Vocabulary is the glossary's (SCRUM-281, v1.3): lifecycle stage, test
family, acceptance criterion, gap, in possession, by proxy, producer, serving provider, attestable and testable properties, outputs and internals. Within
attestable, evidence is marked guaranteed (the platform enforces or verifies it), declared (the producer
states it) or readable (read from the artefact, or from the organisation's own deployment of it); testable evidence is measured. No sources yet; sources are
added when the subsection is drafted.

## Notation

Every symbol in the figure and the tables is defined here before it is used. Terms in the right-hand column are the glossary's (SCRUM-281).

| Symbol | Reads as | Definition |
|---|---|---|
| S1, S2, S3, S4 | stage | The four lifecycle stages in order: S1 selection, S2 adjustment, S3 deployment, S4 runtime detection. Each is a point at which a question about the model is answered |
| Q, Qn.k | question | A question answered at stage Sn about the model, or about what that stage puts around it (its serving software, configuration and access); k numbers the questions of that stage (Q1.1 is the first question of selection) |
| en.k | evidence item | One item of the evidence that exists at stage Sn, numbered k, listed in that stage's inventory table with its kind, what it is and where it comes from; a question cites the items it draws on, and the kind alone decides who answers it, where it exists and which family establishes it (the rule table) |
| A | answerer | Who answers the question: the platform, the producer, the serving provider, or the organisation that selects, adjusts, deploys or runs the model |
| producer | the model's producer | The glossary's producer: the organisation that trains a model and first publishes its file. Its statements are about the model: parent, training data, licence, what it produces. They are made once, at S1, and do not change later |
| serving provider | the party that serves the endpoint | The glossary's serving provider: the platform or redistributor that runs the copy a key opens; it answers for the endpoint, never for the model. The only party besides the organisation that answers at S3 and S4, and only by proxy |
| E, En | evidence | The set of items that exist at stage Sn and can answer a question, listed in the stage's inventory table. Evidence accumulates: En includes everything in En-1 plus what the stage adds, written En = En-1 ∪ {additions} |
| guaranteed, declared, readable | attestable evidence | The glossary's attestable properties, split by who vouches for them: guaranteed, the platform enforces or verifies it; declared, the producer states it about the model, or the serving provider about the endpoint, and nothing verifies it; readable, read from the artefact itself or from the organisation's own deployment of it, with no one's word in between |
| testable | testable evidence | The glossary's testable properties: a property no metadata reveals, established only by running the model; split into outputs, measured black-box, and internals, measured white-box |
| testable, outputs; testable, internals | the two testable kinds | The glossary's outputs and internals: outputs are measured black-box through a file or a key, so under both access states; internals white-box, so in possession only |
| H | access line | What the organisation holds, decided once, at or before S3, and in force for every stage after: H = file, in possession; H = key, by proxy |
| E(S) under H | evidence available | In possession: guaranteed, declared, readable and testable evidence can all exist. By proxy: only declared and testable, because there is no file and the platform's guarantees do not travel with the key |
| M, Mi | method | One assessment method; i numbers the methods once the later chapters name them |
| F1, F2, F3, F4 | test family | The glossary's four test families: F1 static, F2 dynamic, F3 behavioural, F4 provenance. Every method belongs to one family and carries what it detects, what it cannot, and the access it needs, black-box or white-box |
| map(Mi) | mapping | The set of stages a method runs at. It is never empty, which is the item's acceptance criterion, and it excludes any stage where the method's access need is not met: a white-box method does not map to a stage under H = key |
| M→Sn | methods at a stage | The methods whose mapping includes Sn |
| ∪, ∈, ⊆, ∅ | set signs | Union, member of, subset of, empty set |

## Figure: the framework

![Lifecycle assessment framework, template with symbolic names](lifecycle-framework-template.png)

Template with the symbols above; the stage boxes are filled from the stage tables below once each is agreed, and the figure then carries question numbers in place of symbols.

## The rule: the evidence kind decides the rest

Every evidence item has one kind. The kind fixes who answers it, whether it exists under each access state, and which test family establishes it. Each stage first lists its evidence, En, one item per row with its kind; the question table then cites those items. The question table keeps the Jira's three columns, question, who answers, evidence, and adds in possession, by proxy and test family; the four columns after the evidence are read off this table, item by item, and never filled by hand.

| Evidence kind | Who answers | Exists in possession | Exists by proxy | Test family that establishes it |
|---|---|---|---|---|
| guaranteed | the platform, which enforces or verifies it | yes | no: the platform's guarantee does not travel with the key | provenance |
| declared | the producer, about the model; by proxy also the serving provider, about the endpoint | yes, as a statement | yes, as a statement | none: nothing verifies it, so it is recorded as an assessment gap |
| readable | the organisation, from the file or from its own deployment | yes | no: there is no file and no deployment of its own | static |
| testable, outputs | the organisation, by running or calling the model | yes | yes, black-box | behavioural |
| testable, internals | the organisation, by running the file | yes | no: white-box needs the file | dynamic |

Two consequences for every stage. By proxy, the organisation can establish only declared statements and black-box behaviour; the static and dynamic families drop out, and every question that rested on guaranteed or readable items passes to the serving provider. A declared item is a gap at every stage and under both access states, so the gaps of the framework are exactly the declared items.

## S1 Selection

### The selection questions

Six questions about the model. The evidence column cites the items of E1, listed in full at the end of the stage; the four columns after it apply the rule to the cited items and nothing else.

| # | Question | Evidence from E1 | Who answers | In possession | By proxy | Test family |
|---|---|---|---|---|---|---|
| Q1.1 | Where does the model live and who published it? | e1.1 account, date, hashes<br>e1.2 parent, training data, organisation | e1.1: platform<br>e1.2: producer; by proxy, serving provider | e1.1, e1.2 | e1.2 | e1.1: provenance<br>e1.2: none, gap |
| Q1.2 | Is the file what the page says it is? | e1.3 hash or signature matches<br>e1.4 format, completeness, precision, configuration agree with the page<br>e1.2 derivation and training claims, which the file cannot confirm | e1.3: platform<br>e1.4: organisation<br>e1.2: producer; by proxy, serving provider | e1.3, e1.4, e1.2 | e1.2 | e1.3: provenance<br>e1.4: static<br>e1.2: none, gap |
| Q1.3 | Can loading it harm us? | e1.4 format, pickle or not, and custom modelling code the file asks to run on load, the second path to code execution beside pickle<br>e1.5 platform scan results<br>e1.6 own scan | e1.4, e1.6: organisation<br>e1.5: platform | e1.4, e1.5, e1.6 | none; the question passes to the serving provider | e1.4, e1.6: static<br>e1.5: provenance |
| Q1.4 | May we use it? | e1.7 licence and terms<br>e1.8 gating | e1.7: producer; by proxy, serving provider<br>e1.8: platform | e1.7, e1.8 | e1.7 | e1.7: none, gap<br>e1.8: provenance |
| Q1.5 | Which row and column of the segmentation is it, and so which threats apply? | e1.4 column: format, precision, completeness<br>e1.2 row: what it produces, modality | e1.4: organisation<br>e1.2: producer; by proxy, serving provider | e1.4, e1.2 | e1.2 | e1.4: static<br>e1.2: none, gap |
| Q1.6 | Does it behave as described, and is the safeguard present? | e1.9 measured behaviour<br>e1.10 internals while it runs | e1.9, e1.10: organisation | e1.9, e1.10 | e1.9 | e1.9: behavioural<br>e1.10: dynamic |

Selection closes with the first answer to the access question, file or key, which the figure carries as the access line H. It is a decision about the organisation, not a question about the model, so it is not a row; it is settled no later than deployment and governs which items exist from S2 onward.

**Links to the other stages.**

- Q1.6 recurs after adjustment as Q2.3 and at runtime as drift; each time it is answered on new measured evidence against e1.9.
- Q1.2 and Q1.3 recur at deployment when the access state is by proxy, with the serving provider as answerer, because by proxy nothing of them is left to the organisation at selection.
- e1.2, the model card, is cited by four of the six questions; its parent relation is the gap that adjustment can close, e2.2 with e2.1, and that no other stage can.

### E1: the evidence that exists at selection

The full list of what the selection questions above cite. Each item has one kind, which the rule turns into answerer, access and family.

| Id | Kind | What it is | Where it comes from | In possession | By proxy |
|---|---|---|---|---|---|
| e1.1 | guaranteed | producer account, upload date, file hashes | the platform page | yes | no |
| e1.2 | declared | the model card: parent model, training data, organisation behind the account, what the model produces, modality | the producer; by proxy the serving provider's catalogue entry | yes | yes |
| e1.3 | guaranteed | the downloaded file's hash or signature against the page | the platform and the file | yes | no |
| e1.4 | readable | format, whole model or adapter, precision, configuration, and the code and templates that ship with the file: custom modelling code, tokenizer, chat template, generation defaults | the file | yes | no |
| e1.5 | guaranteed | malware and pickle scan results, advisory | the platform page | yes | no |
| e1.6 | readable | the organisation's own scan of the file | the file, through the organisation's scanner | yes | no |
| e1.7 | declared | licence and usage terms | the card; by proxy the serving provider's terms | yes | yes |
| e1.8 | guaranteed | gating, where the platform enforces it | the platform | yes | no |
| e1.9 | testable, outputs | behaviour on the organisation's inputs | running or calling the model | yes | yes |
| e1.10 | testable, internals | the file's internals while it runs | running the file | yes | no |

## S2 Adjustment

**Definition.** Adjustment is a change to the selected model that the organisation makes itself, or has a platform or redistributor make at its request, between selection and serving. It is one of six kinds:

- fine-tuning, which changes the weights;
- an adapter, which adds weights beside the base;
- a merge, which combines the weights of two or more models;
- quantisation, which changes the precision of the weights;
- conversion, which changes the artefact format;
- a change to the code or templates that execute the weights: the forward function, the chat template, the generation defaults, whether they shipped with the artefact or came from the library. The weights are untouched, but what the model does is not.

**Scope.** Three rules fix what the stage covers.

- The organisation's alone. An adjusted model exists only for the organisation that asked for it. It has no public page and no public identifier, and the selected model's public existence is untouched: its page, hash and declarations stay what they were at S1. This holds when a third party does the work: a hosted inference provider fine-tuning on the organisation's data, or a model repository converting a checkpoint on request, acts on the organisation's instruction and hands the result to the organisation only. What is declared about the adjusted copy, by the organisation or by the party that made the change, is a statement inside the organisation, not a publication.
- Not configuration. A system prompt, retrieval, guards or serving settings around an unchanged model are deployment and belong to S3.
- Not another party's change. A fine-tune, adapter or quantised copy another party published, or a variant a redistributor customised for its own catalogue, is a different model with its own public identifier. The organisation meets it at S1 as a candidate in its own right, with its own page, hash and declared parent. The lifecycle starts at S1 for whichever model is picked, base or someone else's derivative; S2 covers only what the organisation does, or has done, to it afterwards.

**Two facts that set the evidence.** Who made the change and what came back are independent, and E2 follows from both.

- Who made it decides the record. The organisation's own change leaves its own record, e2.2, readable. A change made at its request leaves that party's account, e2.3, declared: the party is never the producer, so its statement of the base rests on the same declared parent relation as e1.2.
- What came back decides the access state. A file, as from a model repository's conversion, or a container received instead of a file, as from a packaged inference microservice, is in possession. A key to a changed copy, as from a hosted serving provider's customisation service, is by proxy: the organisation never holds the adjusted copy, and what remains of the evidence is read off E2 by the rule.

**Who answers.** Because the adjusted copy is the organisation's own, the who-answers column names the organisation where selection named the producer. The organisation answers every item it produced, e2.1, e2.2 and e2.4, and always the behaviour, e2.5; the party that made the change answers the account, e2.3, whenever that party is not the organisation.

### The adjustment questions

The evidence column cites the items of E2, listed in full at the end of the stage. Where an E1 item is named as the baseline of a comparison, e1.3, e1.4 and e1.9, it keeps the columns it has in S1 and is not repeated here.

| # | Question | Evidence from E2 | Who answers | In possession | By proxy | Test family |
|---|---|---|---|---|---|---|
| Q2.1 | What was changed, and from which base? | e2.1 base hash matches e1.3<br>e2.2 the change itself, when the organisation made it<br>e2.3 the account of the party that made it, otherwise | e2.2, e2.1: organisation<br>e2.3: the party that made the change | e2.1, and e2.2 or e2.3 | e2.3 | e2.2, e2.1: static<br>e2.3: none, gap |
| Q2.2 | Did the change carry in anything we did not intend? | e2.2 data and recipe inspected<br>e2.4 where weights and activations moved<br>e2.5 probes for triggers and planted content | e2.2, e2.5, e2.4: organisation | e2.2, e2.5, e2.4 | e2.5 | e2.2: static<br>e2.4: dynamic<br>e2.5: behavioural |
| Q2.3 | Is the safeguard still present after the change? | e2.5 against e1.9<br>e2.4 the safeguard's mechanism against the base | e2.5, e2.4: organisation | e2.5, e2.4 | e2.5 | e2.5: behavioural<br>e2.4: dynamic |
| Q2.4 | Is the adjusted artefact still what the segmentation says, and does it still do what the base was selected for? | e2.1 against e1.4<br>e2.5 task behaviour against e1.9<br>e2.3 the format and precision as the party that made the change states them | e2.1, e2.5: organisation<br>e2.3: the party that made the change | e2.1, e2.5, and e2.3 when another party made the change | e2.5, e2.3 | e2.1: static<br>e2.5: behavioural<br>e2.3: none, gap |

**Links to the other stages.**

- Q2.3 is Q1.6 asked again on new evidence, e2.5 against e1.9; that pair is what the acceptance criterion for adjustment will compare.
- Q2.1 ties the stage to selection: an adjusted copy whose base hash, e2.1, does not match e1.3 is not the selected model, and the lifecycle restarts at S1.
- e2.2 with e2.1 is the one place in the framework where a readable record replaces a declared claim, the parent relation that S1 could not verify; it exists only when the organisation made the change itself.

### E2: the evidence that exists at adjustment

The full list of what the adjustment questions above cite. E2 is all of E1, which stays available, plus these five items.

| Id | Kind | What it is | Where it comes from | In possession | By proxy |
|---|---|---|---|---|---|
| e2.1 | readable | the adjusted artefact: format, completeness, precision, and its base hash against e1.3 | the adjusted file | yes | no |
| e2.2 | readable | the organisation's record of the change: training data, recipe, adapter or changed tensors | the organisation, when it made the change itself | yes | no |
| e2.3 | declared | the account of the change, its base and the served format, from the party that made it | the platform or redistributor that made the change, when it was not the organisation | yes, as a statement | yes, as a statement |
| e2.4 | testable, internals | the adjusted weights and activations against the base | running both files | yes | no |
| e2.5 | testable, outputs | behaviour on the adjusted model, same inputs as e1.9 | running or calling the adjusted model | yes | yes |

## S3 Deployment

**Definition.** Deployment is putting the assessed model, selected and, where S2 applied, adjusted, into service. It fixes three things around weights that no longer change: the serving software and hardware the model runs on, the configuration that surrounds it, and who may reach it. In possession, the organisation runs the file, or a container or engine received instead of a file, on software it chooses. By proxy, the organisation configures a serving provider's endpoint, model identifier, version and settings, and the serving provider runs it.

**Scope.** Four rules fix what the stage covers.

- The weights are fixed. Any change to them is adjustment and sends the model back to S2; deployment changes only what is around the model.
- Configuration is deployment. System prompt, retrieval, tools, guards and serving settings such as sampling, together what is often called the harness or scaffolding around the model, are set here, and the model is assessed with them in place, because they change what the deployed system does without changing the model.
- The access line is settled here at the latest. Whether the organisation holds the file or a key is fixed by what it deploys, and from this stage on the by-proxy column is not a possibility but a fact.
- The surroundings are frozen on exit. Serving software, configuration and access are set here and do not change in service; any change to them is a redeployment and returns the model to this stage. By proxy the freeze is a serving provider's statement, e3.2 and e3.4, and finding that it was broken is the first job of runtime detection.

**What the stage adds.** Two kinds of evidence that did not exist before.

- The served thing itself: which artefact is actually in service and under what software and configuration, readable in possession, declared by the serving provider by proxy.
- Behaviour through the whole stack: the deployed system measured on the organisation's inputs, with its configuration in place, against the measurements of S1 and S2.

**Who answers.** The organisation answers what it configured and what it measured. By proxy the serving provider answers for the endpoint, which model and version it serves, what surrounds it, and who can reach it, and those answers are declared.

### The deployment questions

The evidence column cites the items of E3, listed in full at the end of the stage. Where an earlier item is named as the baseline of a comparison, e1.3, e1.9, e2.1 and e2.5, it keeps the columns it has in its own stage and is not repeated here.

| # | Question | Evidence from E3 | Who answers | In possession | By proxy | Test family |
|---|---|---|---|---|---|---|
| Q3.1 | Is the model in service the model we assessed? | e3.1 the served artefact's hash against e1.3, or e2.1 after adjustment<br>e3.2 the serving provider's model identifier and version for the endpoint | e3.1: organisation<br>e3.2: serving provider | e3.1 | e3.2 | e3.1: static<br>e3.2: none, gap |
| Q3.2 | What surrounds the model, and does it change what the model does? | e3.3 the serving software and its version, the container or engine contents, and the configuration: system prompt, retrieval, tools, guards, serving settings<br>e3.4 the serving provider's statement of the endpoint's configuration and filters | e3.3: organisation<br>e3.4: serving provider | e3.3 | e3.4 | e3.3: static<br>e3.4: none, gap |
| Q3.3 | Does the deployed system give the outputs the assessed model gave on the same inputs? | e3.5 outputs through the deployed endpoint against e1.9, or e2.5 after adjustment | e3.5: organisation | e3.5 | e3.5 | e3.5: behavioural |
| Q3.4 | Who can reach the model and its file? | e3.6 the organisation's access configuration for the endpoint, the file at rest and the container<br>e3.7 the serving provider's statements of access control and isolation | e3.6: organisation<br>e3.7: serving provider | e3.6 | e3.7 | e3.6: static<br>e3.7: none, gap |

**Links to the other stages.**

- Q3.1 is where Q1.2 returns by proxy: the organisation could not read the file at selection, and at deployment the serving provider's identifier and version, e3.2, is all it has in place of the hash. Q1.3 returns the same way, inside e3.4, as the serving provider's word that what it loaded was safe.
- Q3.3 is the third measurement of the same behaviour, after e1.9 and e2.5, and the first with the configuration in place; it is the baseline that runtime detection compares against.
- Q3.2 is the one place where the glossary's warning against assessing the model without the software around it is acted on: the container or engine contents, e3.3, are read here and nowhere else.

### E3: the evidence that exists at deployment

The full list of what the deployment questions above cite. E3 is all of E2, which stays available, plus these seven items.

| Id | Kind | What it is | Where it comes from | In possession | By proxy |
|---|---|---|---|---|---|
| e3.1 | readable | the served artefact's hash, against the file assessed at S1 or S2 | the file, container or engine in service | yes | no |
| e3.2 | declared | the model identifier and version the endpoint serves | the serving provider | not applicable | yes, as a statement |
| e3.3 | readable | the serving software and its version: inference engine and its own forward implementation, kernels and numerics, serving layer (batching, caching, speculative decoding); the container base image and drivers, or the compiled engine and its hardware target; and the configuration around the model: system prompt, retrieval, tools, guards, serving settings | the organisation's deployment | yes | no |
| e3.4 | declared | the endpoint's configuration, filters and loading, as the serving provider states them | the serving provider | not applicable | yes, as a statement |
| e3.5 | testable, outputs | behaviour through the deployed endpoint on the organisation's inputs, configuration in place | calling the deployed endpoint | yes | yes |
| e3.6 | readable | the organisation's access configuration for the endpoint, the file at rest and the container | the organisation's deployment | yes | no |
| e3.7 | declared | access control and isolation, as the serving provider states them | the serving provider | not applicable | yes, as a statement |

## S4 Runtime detection

**Definition.** Runtime detection is watching the deployed system while it is in service. It is the only stage with no entry event and no end: nothing new is selected, changed or set, and the stage runs for as long as the deployment does. It watches two things. Whether what deployment fixed, the model and its configuration, is still in place; and what the model does on inputs the organisation did not write, the live traffic of users, retrieved content and tool outputs.

**Scope.** Four rules fix what the stage covers.

- Nothing is set here. A change the stage finds belongs to the stage that owns it: changed weights send the model to S2, a changed configuration to S3. Runtime detection detects; what is done about a finding is response, outside the framework.
- Inputs are not configuration. What users send, what retrieval returns and what tools return change by nature and are the stage's material, not a change to the deployment. Only the model, its serving software and its configuration are expected to stay fixed.
- By proxy, the freeze is a statement. The serving provider can change the model or the endpoint's configuration, and the organisation learns of it only if the serving provider says so, e4.2. The first job of the stage by proxy is therefore to find such a change without being told, and the only evidence that can do that is behaviour, e4.4.
- Model level, not system level. The questions ask what the model is given and what it returns. The inference-time and runtime threats the taxonomy places at system level are seen here only through those two things.

**What the stage adds.** Evidence over time, which no earlier stage has.

- The same measurement repeated: the inputs of e3.5 sent again and compared, so that a change in the model or its surroundings shows as a change in outputs.
- Outputs on inputs the organisation did not choose: what the model is given in service and what it returns, recorded at the organisation's side of the endpoint under either access state.

**Who answers.** The organisation answers everything it records and measures, e4.1, e4.3, e4.4 and e4.5. The producer answers nothing at this stage: its statements about the model were made at S1 and do not change. By proxy the serving provider answers for the endpoint it runs, whether the model or the endpoint's configuration changed, e4.2, and who used the key, e4.6, and those answers are declared, so both are gaps.

### The runtime detection questions

The evidence column cites the items of E4, listed in full at the end of the stage. Where an earlier item is named as the baseline of a comparison, e3.1 to e3.7, it keeps the columns it has in its own stage and is not repeated here.

| # | Question | Evidence from E4 | Who answers | In possession | By proxy | Test family |
|---|---|---|---|---|---|---|
| Q4.1 | Has what deployment fixed been changed since, the model, its serving software or its configuration? | e4.1 the served artefact's hash, the serving software and the configuration re-read against e3.1 and e3.3<br>e4.2 the serving provider's version and change notices against e3.2 and e3.4 | e4.1: organisation<br>e4.2: serving provider | e4.1 | e4.2 | e4.1: static<br>e4.2: none, gap |
| Q4.2 | Are the inputs arriving in service turning the model against its use, and does it comply? | e4.3 the inputs arriving at the endpoint, user, retrieved content and tool outputs, and the outputs returned | e4.3: organisation | e4.3 | e4.3 | e4.3: behavioural |
| Q4.3 | Does the model still give the outputs it gave at deployment? | e4.4 the inputs of e3.5 sent again, against e3.5 | e4.4: organisation | e4.4 | e4.4 | e4.4: behavioural |
| Q4.4 | Who is reaching the model and its file, and how much? | e4.5 the organisation's access record for the endpoint, the file at rest and the container against e3.6<br>e4.6 the serving provider's access and usage records | e4.5: organisation<br>e4.6: serving provider | e4.5 | e4.6 | e4.5: static<br>e4.6: none, gap |

**Links to the other stages.**

- The four questions are the four deployment questions asked again, continuously: Q3.1 and Q3.2 become Q4.1, Q3.3 becomes Q4.3, Q3.4 becomes Q4.4, and Q3.2's second half, what surrounds the model, becomes Q4.2 for the part of the surroundings that changes by nature, the inputs.
- Q4.3 is the fourth measurement of the behaviour first measured at e1.9, after e2.5 and e3.5. It is the only question that can be answered the same way under both access states, and by proxy it is the only evidence of a change the serving provider did not announce.
- Q4.2 is where the glossary's inference-time and runtime threat family lands: prompt injection, jailbreaks, extraction and tool-use abuse are all seen as inputs given and outputs returned, e4.3, and nowhere else in the framework.
- Q4.1 conditions the other two measurements. A change it finds restarts the lifecycle at the stage that owns it, S2 for the weights, S3 for the serving software or configuration, and until then the baselines of S3 are void: a Q4.3 comparison against e3.5 is a comparison with a different system, and the record of e4.3 must be split at the change, because a changed system prompt, retrieval, tool set or guard changes what the model is given and so what it returns. When Q4.1 finds no change and Q4.3 still drifts, the drift is inside the stack, sampling, numerics or hardware, or, by proxy, the one case in which Q4.1 is answered without the serving provider's word: a change it did not announce.

### E4: the evidence that exists at runtime

The full list of what the runtime detection questions above cite. E4 is all of E3, which stays available, plus these six items.

| Id | Kind | What it is | Where it comes from | In possession | By proxy |
|---|---|---|---|---|---|
| e4.1 | readable | the served artefact's hash, the serving software and the configuration, re-read in service, against e3.1 and e3.3 | the deployment, read again | yes | no |
| e4.2 | declared | version changes and change notices for the endpoint, against e3.2 and e3.4 | the serving provider | not applicable | yes, as a statement |
| e4.3 | testable, outputs | the inputs arriving at the endpoint in service, user, retrieved content and tool outputs, and the outputs returned | the organisation's side of the endpoint, recorded | yes | yes |
| e4.4 | testable, outputs | behaviour on the inputs of e3.5, measured again, against e3.5 | calling the deployed endpoint again | yes | yes |
| e4.5 | readable | the organisation's access record for the endpoint, the file at rest and the container, against e3.6 | the organisation's deployment | yes | no |
| e4.6 | declared | access and usage to the endpoint, as the serving provider records them | the serving provider | not applicable | yes, as a statement |

## M: methods to stages

The mapping rule is in the notation: map(Mi) is the set of stages whose inventory En holds an item of the kind the method reads, at which the method's access need is met. It is never empty. The mapping is derived from the inventories above and nothing else, so it changes only when an inventory does. The test families are defined where the skeleton defines them; here they are labels.

### Family to stage

The family column follows the rule table: a family reads one evidence kind.

| Family | Reads | Items by stage | In possession | By proxy |
|---|---|---|---|---|
| F1 static | readable | S1: e1.4, e1.6; S2: e2.1, e2.2; S3: e3.1, e3.3, e3.6; S4: e4.1, e4.5 | S1, S2, S3, S4 | none: no readable item exists |
| F2 dynamic | testable, internals | S1: e1.10; S2: e2.4 | S1, S2 | none: white-box needs the file |
| F3 behavioural | testable, outputs | S1: e1.9; S2: e2.5; S3: e3.5; S4: e4.3, e4.4 | S1, S2, S3, S4 | S1, S2, S3, S4 |
| F4 provenance | guaranteed | S1: e1.1, e1.3, e1.5, e1.8 | S1 | none: the guarantee does not travel with the key |

Two readings. By proxy the whole framework rests on F3 and on declared statements; every other family drops out at every stage. F2 and F4 are front-loaded: internals are measured only while the organisation holds a file it has not yet put behind serving software, and guarantees exist only where the platform is, at selection.

### Tooling kind to stage

The kinds the skeleton names for the tooling comparison, placed by the same rule. Each method the report describes later is added here as a row under its kind, with the items it reads, when it is drafted.

| Tooling kind | Family | Items it reads | Stages | Note |
|---|---|---|---|---|
| scanners (file, format, code) | F1 static | e1.4, e1.6; e2.1; e3.3 | S1, S2, S3 | at S3 the object scanned is the container or engine contents, not the file alone |
| provenance verifiers (hash, signature, account, gating) | F4 provenance; F1 static for the re-reads | e1.1, e1.3, e1.8; e2.1, e3.1, e4.1 against e1.3 | S1; the re-reads at S2, S3, S4 | the guarantee is established once, at S1; later stages compare a readable hash against it |
| red-team frameworks | F3 behavioural | e1.9, e2.5, e3.5, e4.4 | S1, S2, S3, S4 | the same inputs at every stage are what make the four measurements comparable |
| runtime monitors | F3 behavioural | e4.3, e4.4 | S4 | the only kind that reads live inputs; where the inference-time and runtime threats are detected |
| guards | none: not an assessment method | set as configuration, e3.3; their effect is measured through e3.5 and e4.3 | S3 as a thing assessed; S4 as a thing watched | a guard is a control, assessed with the model, not a method that assesses it |
| white-box analysis (internals) | F2 dynamic | e1.10, e2.4 | S1, S2 | in possession only; not available once the model is behind serving software, see the cut of internals from S3 |

Acceptance for the Jira item, "every assessment method described later maps to at least one lifecycle stage", is met by construction: a method that reads some evidence kind maps to every stage holding that kind, and every kind occurs at S1.
