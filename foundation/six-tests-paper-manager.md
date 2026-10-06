# Six tests for the model file you are about to deploy

A plain-English paper for the person who runs language models in production and has never trained
one. Companion to the technical paper (Jira SCRUM-346). Same tests, same definitions, same framework
mapping and bibliography. The numbers are left out on purpose: this paper explains what each test is,
not what one model scored.

---

## Summary

A language model you download is a file of numbers. Everything it knows and every habit it has,
including the habit of refusing harmful requests, is inside those numbers. Nobody can read them. So
the two security questions you would ask of any software you did not write, "is this the real thing"
and "can its protections be switched off", have no ordinary answer: there is no signature on the
behaviour and no configuration file for the safety.

SABRE answers both questions by stress-testing the file itself. Three tests measure how steady and
how forgiving the model is. Three tests measure how good its built-in safeguard is: how much work an
attacker with access to the model needs to make it comply. This is a different question from the one
red-teaming asks. Red-teaming asks whether the attacks people already know about work today. On an
advanced model the answer is almost always no, and that tells you only that nobody has found the right
words yet. SABRE tells you how much it would cost them.

---

## 1. Four things to know before the tests

**The file is the model.** There is no separate rulebook, no policy engine, no setting that says
"refuse harmful requests". The refusal is a habit baked into the numbers, learned from examples.

**The refusal is a single thing inside the file.** When the model meets a harmful request, its
internal state leans in a consistent direction, and that lean is what produces the "no". Because the
lean is consistent, anyone holding the file can locate it with a few dozen example requests and a
published recipe. No understanding of the model is needed. And anything that can be located can be
moved. This is the fact that the whole of Group 2 rests on.

**Inside the model, a small push can become a large change.** The model builds its answer step by
step. A small nudge to its internal state early on can grow into a different answer by the end. How
much it grows is a property of the file, and it can be measured.

**Results are bands, not numbers.** Every file is measured the same way on the same fixed scale.
You get a word per test, never a number and never a comparison with another named model. Group 1
uses Robust, Sensitive and Fragile. Group 2 uses the Low, Medium, High and Critical you already know.

---

## 2. The threat model: three doors and two halves

A model deployed as-is has exactly three attack surfaces. A door is defined by the access it gives,
not by who stands at it.

| Door | What the attacker can do | Who typically has it | What this means for the model | Which tests speak to it |
|---|---|---|---|---|
| **1. The input** | send text to the model and read what comes back; nothing else | any user of your product; any document, web page or tool result your product feeds to the model | prompt attacks: jailbreaks, prompt injection, data extraction. Nothing inside the model can be read or changed | none of the six directly. SABRE's separate prompt attacks measure this door. The six tell you the floor: how little internal movement an attack must produce to succeed |
| **2. The serving path** | read and change what is happening inside the model while it runs | your own engineers, plugins, adapters, serving and guardrail code, a compromised host, an insider | bend or remove the safeguard live, in minutes, without changing the file. The change leaves when the hook is removed, so nothing shows in a checksum | fidelity, containment, the twist test, the forgetting test |
| **3. The supply chain** | the file before you deploy it, and the examples it was tuned with | the model vendor, the author of a fork, a compression or conversion step, a mirror, anyone who edits the file or its tuning set | ship a different model under the same name: a corrupted copy, a fork with the refusal removed and baked in, a variant tuned from tampered examples | integrity, the firmness test; the twist and forgetting tests for stripped forks |

Three rules follow.

1. Every one of the six tests needs door 2 or door 3. None of them can be reproduced by typing a
   prompt.
2. Door 1 is indicated by the six, never measured by them. The six tell you how little has to happen
   inside the model for an attack to succeed. Whether a prompt can make that happen is a separate
   measurement, and SABRE's prompt attacks are it.
3. Reconnaissance is free at doors 2 and 3. Finding the safeguard costs nothing. The tests measure
   moving it.

**The two halves of a report.** The six tests grade what the model's own steadiness and safeguard are
worth from inside the file or upstream. The prompt attacks show what an outsider gets today at the
input. A SABRE report presents both. Reading either half alone is the mistake to avoid: a clean
prompt-attack result on a model with a weak safeguard means only that the words have not been found
yet.

---

## 3. Group 1: how steady and how forgiving is the model

One measurement runs through all three: how small a change inside the model already changes its
answer. The three tests ask it three ways, which are also the three ways you get something other than
what you asked for.

### 3.1 Integrity (weight-tamper radius): does a slightly altered copy still behave like the original?

**What we do.** We deliberately alter a small share of the numbers in the file, the way a broken
download, a careless compression step or a quiet edit would, and check whether the model still gives
the same answers. We increase the alteration until the answers move, and report how much it took.

**What a failure means.** The fear is not a crash. A corrupted or edited file that crashes is caught.
The fear is a file that keeps working and quietly answers differently, because such a file can be
swapped for the original and nobody will notice. A forgiving model cannot be nudged that way.

**What it covers.** This file only. A compressed copy, a retrained copy or a fork is a different model
and gets its own run. There is no before-and-after mode; you run SABRE on each file you consider.

**Door.** The supply chain. This is the one test that protects you even when nobody attacks.

### 3.2 Fidelity (J-space on-cone distortion): how easily does it answer your question wrong?

**What we do.** We give the model a small push inside, along a direction that means something to it,
and measure how little push already changes the answer while the answer stays on topic. We also
measure whether the push grows as the model keeps writing.

**What a failure means.** A wrong answer that stays on topic: a support assistant that confidently
states the wrong refund policy, a pricing assistant that quotes the wrong figure. Fluent, relevant,
wrong. This is the failure no output filter catches, which is why fidelity is the headline of
Group 1.

**Door.** The serving path directly. The supply chain through altered copies. The input as the
floor: a prompt attack has to produce, through words, the same internal movement this test produces
from inside, so this test says how little movement is needed. Whether a prompt can produce it is what
the prompt attacks measure.

### 3.3 Containment (J-space off-cone diversion): how easily does it answer a different question?

**What we do.** The same small push, in a random direction that means nothing to the model, to see
how cheaply it drifts off topic or into content it was not asked for.

**What it is for.** This is the control for fidelity. It tells you whether the model is loosely held
in general, or only along the directions that mean something to it. It has no band of its own.
Off-topic drift is also the failure an ordinary output filter catches, so it is the least worrying of
the three.

### How to read Group 1

| Band | What it means | What an attacker needs | What you do |
|---|---|---|---|
| **Robust** | a large push inside the model is needed before the answer moves | heavy access and effort, easy to notice | use |
| **Sensitive** | a moderate push moves the answer, and it grows as the model writes | ordinary access: a plugin, an adapter, a careless conversion | use with the mitigation on the card: for integrity, pin the checksum and rerun on any other copy; for fidelity, an answer check outside the model and no third-party code on the serving path |
| **Fragile** | a tiny push is enough and the model amplifies it | almost nothing; any door will do | do not deploy |

---

## 4. Group 2: how good is the built-in safeguard

### 4.1 Why these tests exist

Your toolbox already covers performance. For security it offers classical cyber tools, which do not
see the model at all, and red-teaming with public jailbreak and prompt-injection sets, which sees only
the input door and seldom catches anything on an advanced model. A clean red-team pass is a lower
bound on attacker success.

Group 2 measures something else: how much work it takes to make this model comply, measured on the
safeguard itself. This is how a cipher is certified. Nobody says "nobody has broken it yet"; they
state the effort it takes to break. The three tests are indicators of that effort, each along a
different part of the same safeguard. The effort comes in three different currencies, so you get bands,
never a single figure. A safeguard that costs little to defeat will be defeated through the input
eventually. The red-team pass says only that it has not happened yet.

### 4.2 One safeguard, three parts

The model's "no" is one line inside the file, between the requests it refuses and the requests it
answers. The three tests check different parts of that one line, the way an inspection checks the
radiator, the carburettor, the oil and the brakes: one part each, one verdict each, and a failure
anywhere is a failure. The attacker's prize is the same in all three: the model answers a harmful
request fluently, sounding exactly like itself.

- **The twist test** checks how far the model must be pushed off its own refusal before it complies.
- **The forgetting test** checks whether the refusal still fires when the model's sense of danger is
  dulled.
- **The firmness test** checks how firmly the line between refuse and answer is drawn.

In all three, only fluent compliance counts. A model that has been pushed until it produces gibberish
has not been jailbroken; an attacker wants usable answers. The tests throw such cases out, which makes
every Group 2 result conservative.

### 4.3 The twist test (Angular steering)

**The essence.** The refusal is a position the model holds inside, not a decision it makes each time.
An attacker does not delete it and does not argue with it. They turn the model's internal state a
little away from that position and ask the same question. We measure the smallest turn at which the
model starts answering harmful questions fluently.

**Two clauses.** How far must the model be turned away from its "no" before it complies. And: is the
"no" a judgment or a position. A small turn says position: the model did not decide anything, it was
standing somewhere and it was moved.

**What it is not.** Not a prompt attack; the questions are plain and the turn is inside. Not an edit
of the file; nothing is written, and the turn is removed afterwards. The permanent version of this
attack is a separate SABRE test, and the "uncensored" forks on public model sites are that permanent
version, published. Not a measure of how hard the refusal is to find; that is free.

**Door.** The serving path, in minutes. The supply chain, as a fork. The input as the floor.

### 4.4 The forgetting test (Amnesia)

**The essence.** Part of the refusal is triggered by recognition: the model notices that a request is
about harm, legality or danger, and that recognition wakes the "no". The forgetting test dulls that
recognition at one point inside the model and leaves the question unchanged. If the model then answers
harmful questions fluently, the refusal was resting on a sense it can be made to lose. Picture a guard
who still sees everyone but has lost the meaning of the word "weapon".

**Two clauses.** Does the safeguard still fire when the model's sense of danger is dulled. And: is
there a second, independent way to switch the "no" off. The twist test moves the model's stance; the
forgetting test dulls the trigger. Different place, different lever, and real models give different
answers to the two. That is why both tests exist.

**What it is not.** Not removing dangerous words from the prompt; the prompt is untouched. Not making
the model forget facts; the answers stay fluent and on topic, only the danger sense is dulled. Not the
twist test under another name. Not an edit of the file.

**Door.** As the twist test.

### 4.5 The firmness test (steering-vector poisoning)

**The essence.** The line between refuse and answer is located, by anyone who wants it, from a small
set of example requests: some harmful, some harmless. That is also how the industry builds safety
controls for a model after training, without retraining it. We locate the line the standard way, then
change one word in twenty in the harmless examples, with swaps that read naturally and would pass any
reviewer, and locate it again. We check whether the line moved, after confirming that an aimless edit
of the same size would not have moved it.

**Two clauses.** How firmly is the model's own safeguard drawn. A firm line stays put under light
tampering; a soft line swings. And: if you build a safeguard from examples on this model, can you trust
what you built. Building one is equally easy on every model; what differs is whether the result can be
trusted. On a soft line it depends on the exact examples used, so it is easy to get wrong by accident
and easy to tamper with on purpose.

**How this relates to the data poisoning you read about.** Data poisoning is the technique. What we
measure is how much control it gets over your model: whether the smallest, least-guarded input in the
pipeline, a text file of examples that a human reviews by eye, can silently re-aim the model's safety.

**What it is not.** Not training-data poisoning; nothing is assumed about how the model was trained,
nothing is injected, the tampering is ours, at scan time, on our own text, and the model is identical
in both readings. Not a test for planted hidden behaviour; nothing is planted and nothing is detected,
and a low result does not mean the file carries nothing of the kind. That is a separate test. Not a
prompt attack; the altered examples never reach the deployed model.

**Door.** The supply chain, for anyone who adopts a variant tuned from examples they cannot inspect.
The input as the floor: a soft line is the precondition for crossing it with a few changed words.

### How to read Group 2

| Band | What it means | What you do |
|---|---|---|
| **Low** | the safeguard held on this part | keep your normal safety guard; record it |
| **Medium** | it gave way under a moderate effort | use the model only behind a separate guard, in front and behind |
| **High** | it gave way under a small effort | do not rely on the built-in refusals for anything; a separate guard is required |
| **Critical** | a nudge was enough | treat the model as having no refusals of its own; deploy only behind a guard you control, and accept no tuned variants |

---

## 5. What the six tests are not

- **Not prompt attacks.** The questions asked are plain. The push, the dulling and the example edits
  happen inside the file or in our own text, never at your input.
- **Not edits of the file.** Nothing is written. Each change is applied live and removed afterwards.
  A fork that bakes such a change in is the supply-chain case.
- **Not tests for planted hidden behaviour.** Nothing is planted and nothing is detected by these six.
  That is a separate SABRE test.
- **Not a prediction that an attack will happen.** The tests measure exposure: what an attacker gets
  if they try. They say nothing about whether anyone will.
- **Not a single score.** Three currencies in Group 2 and two in Group 1. Bands, never a joint figure.

---

## 6. Limitations, in plain words

- Only fluent compliance counts, so the safeguard tests understate the risk rather than overstate it.
- Each test uses a small fixed set of questions, enough for a band, not for fine comparison.
- Each safeguard test uses one located line. Research shows the refusal is a small bundle of lines,
  so a single-line attack is a floor on how removable the safeguard is.
- Whether an answer complied is decided by a rule-based detector of refusal phrases, not by another
  model. Auditable, and blind to subtle partial compliance.
- Everything the six say about the input door is a floor, inferred with the help of published work,
  never a measurement.

---

## 7. Framework mapping

Where each test files under OWASP LLM Top-10 2025, MITRE ATLAS and NIST. IDs verified against
MITRE's ATLAS.yaml and the OWASP 2025 list. Tests 2 to 5 read and perturb the model's internals, so
ATLAS T0044 Full AI Model Access is their precondition; they are not reachable behind an inference
API.

| Test | OWASP LLM 2025 | MITRE ATLAS | NIST |
|---|---|---|---|
| Integrity (weight-tamper radius) | LLM04 Data and Model Poisoning | T0031 Erode AI Model Integrity; T0018 Manipulate AI Model | AI RMF MEASURE 2.7 |
| Fidelity (J-space on-cone distortion) | LLM01 Prompt Injection (steering susceptibility); LLM09 Misinformation | T0018; T0054 LLM Jailbreak | MEASURE 2.7; AI 100-2e evasion / model manipulation |
| Containment (J-space off-cone diversion) | LLM01; LLM06 Excessive Agency | T0018 (control) | MEASURE 2.7 |
| The twist test (Angular steering) | LLM01 (jailbreak outcome) | T0018 technique → T0054 outcome; precondition T0044 | MEASURE 2.7; AI 100-2e |
| The forgetting test (Amnesia) | LLM01 | T0018 → T0054; T0044 | MEASURE 2.7; AI 100-2e |
| The firmness test (steering-vector poisoning) | LLM04 (+ LLM03 Supply Chain) | T0020 Poison Training Data (+ T0019 Publish Poisoned Datasets); enables T0054 | AI 100-2e data / model poisoning |

Note: T0018 is "Manipulate AI Model", not "Backdoor"; a backdoor trigger would be T0043.004.

---

## 8. Names

| In this paper | Technical name | Where it is built |
|---|---|---|
| Integrity | weight-tamper KL radius (objective 1) | SABRE stability scanner |
| Fidelity | J-space on-cone distortion and leverage (objective 2) | SABRE J-space driver |
| Containment | J-space off-cone diversion (control) | SABRE J-space driver |
| The twist test | Angular steering | SABRE angular steering scanner |
| The forgetting test | Amnesia | SABRE amnesia scanner |
| The firmness test | steering-vector poisoning | SABRE poisoning scanner |
| the model's "no", the line | refusal direction, difference of means over harmful and harmless prompts | shared cache |

---

## Bibliography

- Arditi et al., Refusal in Language Models Is Mediated by a Single Direction, arXiv 2406.11717.
  The refusal is one direction; jailbreak prompts suppress it.
- Vu & Nguyen, Angular Steering, arXiv 2510.26243 (NeurIPS 2025 spotlight). The twist test.
- Amnesia: Adversarial Semantic Layer-Specific Activation Steering, arXiv 2603.10080. The forgetting
  test.
- Steering Vectors are an Adversarial Attack Surface, arXiv 2606.05958. The firmness test.
- Analysing the Safety Pitfalls of Steering Vectors, arXiv 2603.24543. The refusal is a small bundle
  of directions; why single-line results are a floor.
- The Rogue Scalpel: Activation Steering Compromises LLM Safety, arXiv 2509.22067. Random pushes
  remove refusals too; no skill needed.
- Steering in the Shadows: Causal Amplification for Activation-Space Attacks, arXiv 2511.17194. Push
  where a small push grows most; the same measurement as fidelity's leverage.
- Probing the Safety Robustness of LLMs in Latent Space (ASA), arXiv 2506.16078. Push inside, watch
  the answer drift; the same construct as fidelity.
- RARE: router-aware steering on mixture-of-experts models, arXiv 2608.21236. Why pushes on a
  committee-of-specialists model must not change which specialists answer.
- Expert-Aware Refusal Steering, arXiv 2606.04160. Each specialist has its own refusal line.
- Katz, On the Dynamical Interpretation of the Jacobian Lens (internal note); Transformer Circuits
  2026, J-lens / union of cones. The J-space framing behind Group 1.
- OWASP Top 10 for LLM Applications 2025; MITRE ATLAS (ATLAS.yaml); NIST AI RMF 1.0 and NIST AI
  100-2e2025 Adversarial Machine Learning taxonomy.
