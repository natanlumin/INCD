# SABRE lay explainer package (2026-10-05)

The six SABRE J-space and safeguard tests explained for a non-technical, security-aware reader who
downloads an LLM from Hugging Face and runs it as-is (SageMaker, NIM, Rafay). Content agreed and
wording done. Nothing here needs a run.

## What is in the package

| File | What it is | For whom | Status |
|---|---|---|---|
| `01-explainer-and-cards.md` | The customer text: one-page explainer, six result cards, five verdict lines, shared "what the Group 2 tests are not" section, review notes | the customer; the product (cards) | **final wording** (app polish pass + three post-polish decisions applied) |
| `02-six-tests-map.md` | The reference under the story: lay name ↔ technical name ↔ scanner ↔ paper ↔ OWASP / ATLAS / NIST ↔ two clauses ↔ door ↔ verdicts, plus the shared story and the open decisions | us; a security reader who wants to file it; the technical appendix | reference, numbers and IDs verified |
| `03-twist-test-concept.md` | Angular steering, the deep version (work factor, two clauses, risk, as built, what it is not, doors, result table, lines to say) | us; technical appendix | agreed |
| `04-forgetting-test-concept.md` | Amnesia, same shape | us; technical appendix | agreed |
| `05-firmness-test-concept.md` | Steering-vector poisoning, same shape | us; technical appendix | agreed |
| `06-writing-brief.md` | The brief the wording was produced from: audience, framing, three doors, two halves, work factor, vocabulary and honesty rules, deliverables, open items | the writer (Claude app) if wording is redone | source of truth for content |

## The six, in one line each

| # | Lay name | Checks | Group |
|---|---|---|---|
| 1 | Integrity | does a slightly altered copy still behave like the original | 1, steadiness |
| 2 | Fidelity (headline) | how easily it answers the question wrong, on topic | 1 |
| 3 | Containment (control) | how easily it answers a different question | 1 |
| 4 | The twist test | how far it must be pushed off its own refusal before it complies | 2, safeguard |
| 5 | The forgetting test | whether it still refuses when its sense of danger is dulled | 2 |
| 6 | The firmness test | how firmly the line between refuse and answer is drawn | 2 |

## Rules the package follows

- Customer text: no numbers, no framework IDs, no technical names, no "backdoor"; every card names
  its door; the two-halves statement (these tests vs the black-box prompt attacks) appears once.
- Car-inspection depth: name the part each test checks, never walk through the mechanism.
- Input-door claims are literature-backed inference only; nothing in the six can be verified by
  typing a prompt.
- Numbers, IDs and file paths live only in `02` to `05`.

## Decisions (closed 2026-10-05)

1. Band map: Robust = low, Sensitive = medium, Fragile = high + critical (the scan's own bands).
2. Containment: a note under the fidelity card.
3. Coverage sentence: added under fidelity and the twist test.
4. Six cards: the customer deck is the six; push test and random-push probe in the appendix.

Two fact corrections applied in this version: the 122B's fidelity verdict is **Robust** (the
production J-space score is the leverage, 1.35×, which sits in the low band), and Nemotron's
forgetting-test verdict is **High** (0.69 at its first attention block on the finer grid), not
low/medium.

## What to do with it

1. **Read `01`** once more as the customer. If a sentence makes you reach for `02`, it is too
   technical and should be cut from `01`, not explained.
2. **The four decisions are closed.** Decision 1 needs one wiring item: surface q_isnr and q_jspace separately so integrity and fidelity can show two words.
3. **Repo:** `01` and `02` go into `sabre/docs/` on the working branch and into PR #134; `03` to `05`
   go in as the technical appendix; `06` stays as the writing record (repo or Downloads).
4. **Product:** the card texts in `01` become the "what this means for you" lines; the band word
   per card needs decision 1 wired in code and a text table the UI reads. Spec next.
5. **Claude app:** only if a technical appendix in prose or a slide deck is wanted. Attach `02` to
   `05` read-only, tell it facts, names and IDs are fixed, and let it write prose around them. Do not
   send `02` for a polish pass.
6. **Later, on your go:** a real run on the VM so the cards show real bands; the firmness symptom
   test (cheap); wiring the random-push probe only if decision 4 is "full set".
