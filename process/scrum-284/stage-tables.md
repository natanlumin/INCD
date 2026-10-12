# SCRUM-284 working file: lifecycle stage tables

Status 11 October 2026: selection agreed, adjustment drafted and pending the user's review; deployment and
runtime detection to follow in the same shape. Vocabulary is the glossary's (SCRUM-281): lifecycle stage, test
family, acceptance criterion, gap, in possession, by proxy, attestable and testable properties. Within
attestable, evidence is marked guaranteed (the platform enforces or verifies it), declared (the publisher
states it) or readable (read from the file); testable evidence is measured. No sources yet; sources are
added when the subsection is drafted.

## Notation

Every symbol in the figure and the tables is defined here before it is used. Terms in the right-hand column are the glossary's (SCRUM-281).

| Symbol | Reads as | Definition |
|---|---|---|
| S1, S2, S3, S4 | stage | The four lifecycle stages in order: S1 selection, S2 adjustment, S3 deployment, S4 runtime detection. Each is a point at which a question about the model is answered |
| Q, Qn.k | question | A question about the model answered at stage Sn; k numbers the questions of that stage (Q1.1 is the first question of selection) |
| en.k | evidence item | One item of the evidence that exists at stage Sn, numbered k, listed in that stage's inventory table with its kind, what it is and where it comes from; a question cites the items it draws on, and the kind alone decides who answers it, where it exists and which family establishes it (the rule table) |
| A | answerer | Who answers the question: the platform, the publisher, the provider, or the organisation that selects, adjusts, deploys or runs the model |
| E, En | evidence | The set of items that exist at stage Sn and can answer a question, listed in the stage's inventory table. Evidence accumulates: En includes everything in En-1 plus what the stage adds, written En = En-1 ∪ {additions} |
| guaranteed, declared, readable | attestable evidence | The glossary's attestable properties, split by who vouches for them: guaranteed, the platform enforces or verifies it; declared, the publisher or provider states it and nothing verifies it; readable, read from the file itself |
| testable | testable evidence | The glossary's testable properties: a property no metadata reveals, established only by running the model; split into outputs, measured black-box, and internals, measured white-box |
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
| declared | the publisher; by proxy, the provider | yes, as a statement | yes, as a statement | none: nothing verifies it, so it is recorded as an assessment gap |
| readable | the organisation, from the file | yes | no: there is no file | static |
| testable, outputs | the organisation, by running or calling the model | yes | yes, black-box | behavioural |
| testable, internals | the organisation, by running the file | yes | no: white-box needs the file | dynamic |

Two consequences for every stage. By proxy, the organisation can establish only declared statements and black-box behaviour; the static and dynamic families drop out, and every question that rested on guaranteed or readable items passes to the provider. A declared item is a gap at every stage and under both access states, so the gaps of the framework are exactly the declared items.

## S1 Selection

### The selection questions

Six questions about the model. The evidence column cites the items of E1, listed in full at the end of the stage; the four columns after it apply the rule to the cited items and nothing else.

| # | Question | Evidence from E1 | Who answers | In possession | By proxy | Test family |
|---|---|---|---|---|---|---|
| Q1.1 | Where does the model live and who published it? | e1.1 account, date, hashes<br>e1.2 parent, training data, organisation | e1.1: platform<br>e1.2: publisher; by proxy, provider | e1.1, e1.2 | e1.2 | e1.1: provenance<br>e1.2: none, gap |
| Q1.2 | Is the file what the page says it is? | e1.3 hash or signature matches<br>e1.4 format, completeness, precision, configuration agree with the page<br>e1.2 derivation and training claims, which the file cannot confirm | e1.3: platform<br>e1.4: organisation<br>e1.2: publisher; by proxy, provider | e1.3, e1.4, e1.2 | e1.2 | e1.3: provenance<br>e1.4: static<br>e1.2: none, gap |
| Q1.3 | Can loading it harm us? | e1.4 format, pickle or not<br>e1.5 platform scan results<br>e1.6 own scan | e1.4, e1.6: organisation<br>e1.5: platform | e1.4, e1.5, e1.6 | none; the question passes to the provider | e1.4, e1.6: static<br>e1.5: provenance |
| Q1.4 | May we use it? | e1.7 licence and terms<br>e1.8 gating | e1.7: publisher; by proxy, provider<br>e1.8: platform | e1.7, e1.8 | e1.7 | e1.7: none, gap<br>e1.8: provenance |
| Q1.5 | Which row and column of the segmentation is it, and so which threats apply? | e1.4 column: format, precision, completeness<br>e1.2 row: what it produces, modality | e1.4: organisation<br>e1.2: publisher; by proxy, provider | e1.4, e1.2 | e1.2 | e1.4: static<br>e1.2: none, gap |
| Q1.6 | Does it behave as described, and is the safeguard present? | e1.9 measured behaviour<br>e1.10 internals while it runs | e1.9, e1.10: organisation | e1.9, e1.10 | e1.9 | e1.9: behavioural<br>e1.10: dynamic |

Selection closes with the first answer to the access question, file or key, which the figure carries as the access line H. It is a decision about the organisation, not a question about the model, so it is not a row; it is settled no later than deployment and governs which items exist from S2 onward.

**Links to the other stages.**

- Q1.6 recurs after adjustment as Q2.3 and at runtime as drift; each time it is answered on new measured evidence against e1.9.
- Q1.2 and Q1.3 recur at deployment when the access state is by proxy, with the provider as answerer, because by proxy nothing of them is left to the organisation at selection.
- e1.2, the model card, is cited by four of the six questions; its parent relation is the gap that adjustment can close, e2.1 with e2.2, and that no other stage can.

### E1: the evidence that exists at selection

The full list of what the selection questions above cite. Each item has one kind, which the rule turns into answerer, access and family.

| Id | Kind | What it is | Where it comes from | In possession | By proxy |
|---|---|---|---|---|---|
| e1.1 | guaranteed | publisher account, upload date, file hashes | the platform page | yes | no |
| e1.2 | declared | the model card: parent model, training data, organisation behind the account, what the model produces, modality | the publisher; by proxy the provider's catalogue entry | yes | yes |
| e1.3 | guaranteed | the downloaded file's hash or signature against the page | the platform and the file | yes | no |
| e1.4 | readable | format, whole model or adapter, precision, configuration | the file | yes | no |
| e1.5 | guaranteed | malware and pickle scan results, advisory | the platform page | yes | no |
| e1.6 | readable | the organisation's own scan of the file | the file, through the organisation's scanner | yes | no |
| e1.7 | declared | licence and usage terms | the card; by proxy the provider's terms | yes | yes |
| e1.8 | guaranteed | gating, where the platform enforces it | the platform | yes | no |
| e1.9 | testable, outputs | behaviour on the organisation's inputs | running or calling the model | yes | yes |
| e1.10 | testable, internals | the file's internals while it runs | running the file | yes | no |

## S2 Adjustment

**Definition.** Adjustment is a change to the selected model that the organisation makes itself, or has a platform or redistributor make at its request, between selection and serving. It is one of five kinds:

- fine-tuning, which changes the weights;
- an adapter, which adds weights beside the base;
- a merge, which combines the weights of two or more models;
- quantisation, which changes the precision of the weights;
- conversion, which changes the artefact format.

**Scope.** Three rules fix what the stage covers.

- The organisation's alone. An adjusted model exists only for the organisation that asked for it. It has no public page and no public identifier, and the selected model's public existence is untouched: its page, hash and declarations stay what they were at S1. This holds when a third party does the work: a hosted provider fine-tuning on the organisation's data, or the Hub converting a checkpoint on request, acts on the organisation's instruction and hands the result to the organisation only. What is declared about the adjusted copy, by the organisation or by the party that made the change, is a statement inside the organisation, not a publication.
- Not configuration. A system prompt, retrieval, guardrails or serving settings around an unchanged model are deployment and belong to S3.
- Not another party's change. A fine-tune, adapter or quantised copy another party published, or a variant a redistributor customised for its own catalogue, is a different model with its own public identifier. The organisation meets it at S1 as a candidate in its own right, with its own page, hash and declared parent. The lifecycle starts at S1 for whichever model is picked, base or someone else's derivative; S2 covers only what the organisation does, or has done, to it afterwards.

**Two facts that set the evidence.** Who made the change and what came back are independent, and E2 follows from both.

- Who made it decides the record. The organisation's own change leaves its own record, e2.1, readable. A change made at its request leaves that party's account, e2.5, declared: the party is never the producer, so its statement of the base rests on the same declared parent relation as e1.2.
- What came back decides the access state. A file, as from the Hub's conversion, or a container received instead of a file, as from a packaged inference microservice, is in possession. A key to a changed copy, as from a hosted provider's customisation service, is by proxy: the organisation never holds the adjusted copy, and what remains of the evidence is read off E2 by the rule.

**Who answers.** Because the adjusted copy is the organisation's own, the who-answers column names the organisation where selection named the publisher. The organisation answers every item it produced, e2.1 to e2.4, and always the behaviour, e2.3; the party that made the change answers the record, e2.5, whenever that party is not the organisation.

### The adjustment questions

The evidence column cites the items of E2, listed in full at the end of the stage. Where an E1 item is named as the baseline of a comparison, e1.3, e1.4 and e1.9, it keeps the columns it has in S1 and is not repeated here.

| # | Question | Evidence from E2 | Who answers | In possession | By proxy | Test family |
|---|---|---|---|---|---|---|
| Q2.1 | What was changed, and from which base? | e2.2 base hash matches e1.3<br>e2.1 the change itself, when the organisation made it<br>e2.5 the account of the party that made it, otherwise | e2.1, e2.2: organisation<br>e2.5: the party that made the change | e2.2, and e2.1 or e2.5 | e2.5 | e2.1, e2.2: static<br>e2.5: none, gap |
| Q2.2 | Did the change carry in anything we did not intend? | e2.1 data and recipe inspected<br>e2.4 where weights and activations moved<br>e2.3 probes for triggers and planted content | e2.1, e2.3, e2.4: organisation | e2.1, e2.3, e2.4 | e2.3 | e2.1: static<br>e2.4: dynamic<br>e2.3: behavioural |
| Q2.3 | Is the safeguard still present after the change? | e2.3 against e1.9<br>e2.4 the safeguard's mechanism against the base | e2.3, e2.4: organisation | e2.3, e2.4 | e2.3 | e2.3: behavioural<br>e2.4: dynamic |
| Q2.4 | Is the adjusted artefact still what the segmentation says, and does it still do what the base was selected for? | e2.2 against e1.4<br>e2.3 task behaviour against e1.9<br>e2.5 the format and precision as the party that made the change states them | e2.2, e2.3: organisation<br>e2.5: the party that made the change | e2.2, e2.3, and e2.5 when another party made the change | e2.3, e2.5 | e2.2: static<br>e2.3: behavioural<br>e2.5: none, gap |

**Links to the other stages.**

- Q2.3 is Q1.6 asked again on new evidence, e2.3 against e1.9; that pair is what the acceptance criterion for adjustment will compare.
- Q2.1 ties the stage to selection: an adjusted copy whose base hash, e2.2, does not match e1.3 is not the selected model, and the lifecycle restarts at S1.
- e2.1 with e2.2 is the one place in the framework where a readable record replaces a declared claim, the parent relation that S1 could not verify; it exists only when the organisation made the change itself.

### E2: the evidence that exists at adjustment

The full list of what the adjustment questions above cite. E2 is all of E1, which stays available, plus these five items.

| Id | Kind | What it is | Where it comes from | In possession | By proxy |
|---|---|---|---|---|---|
| e2.1 | readable | the organisation's record of the change: training data, recipe, adapter or changed tensors | the organisation, when it made the change itself | yes | no |
| e2.2 | readable | the adjusted artefact: format, completeness, precision, and its base hash against e1.3 | the adjusted file | yes | no |
| e2.3 | testable, outputs | behaviour on the adjusted model, same inputs as e1.9 | running or calling the adjusted model | yes | yes |
| e2.4 | testable, internals | the adjusted weights and activations against the base | running both files | yes | no |
| e2.5 | declared | the account of the change, its base and the served format, from the party that made it | the platform or redistributor that made the change, when it was not the organisation | yes, as a statement | yes, as a statement |

## S3 Deployment

To do.

## S4 Runtime detection

To do.
