# Demonstration vocabulary

The terms used by the demonstration set, the techniques executed for this report with LuminAI's
advisor code. They are not part of the report glossary (`governing/report-style-guide-and-glossary.md`
§1) and appear in the report only in the demonstration-evidence appendix and the platform-alignment
chapter, as technical tags; the body of the report uses the glossary's words. Moved here from the
style guide v1.1 §1.3 (lay words), §1.4 and §1.5 on 2026-10-07, unchanged.

## The threat model the demonstration was run under

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
| reconnaissance | locating the safeguard; free at doors 2 and 3 | diff-of-means estimation | implying obscurity protects |

Two rows of the old table, *backdoor* and *data poisoning*, are threat terms and stayed in the
glossary (§1.4) with neutral definitions; their old "avoid" clauses, which referred to the six tests,
are: "backdoor" or "soft backdoor" for any of the six tests; presenting the firmness test as "merely
data poisoning". *Test family*, *acceptance criterion* and *trust tier* also stayed, redefined in the
skeleton's words.

## The six tests

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

## The lay words for the six tests

| Canonical term | Definition | Technical anchor | Avoid in prose |
|---|---|---|---|
| refusal vector | the technical name for the model's "no": the direction in internal state along which harmful and harmless requests differ on average; it is what the twist, forgetting and firmness tests act on, and what abliteration removes | refusal direction r = mean(h | harmful) − mean(h | harmless); per-expert r_e on a committee model | "vector" in executive text; implying it is a single switch (it is a small bundle; one direction is a floor) |
| internal state | what is happening inside the model while it answers | activations, hidden state, residual stream h_ℓ | "activations" in executive text |
| the model's "no", the line | the consistent internal lean that produces refusal, located from examples; the line between what it refuses and what it answers | refusal direction r, difference of means over harmful and harmless prompts | "vector" |
| a push inside | a small change to the internal state along a direction | ε·v on h_ℓ; steering | "perturbation" in executive text |
| meaning direction, random direction | a direction the model itself uses; one it does not | on-cone, off-cone | "cone" in executive text |
| how big a push it takes | the smallest push that already changes the answer | radius, KL ≥ τ | "KL", "radius" in executive text |
| whether the push grows as it writes | amplification of a push along generation | leverage | "leverage" in executive text |
| fluent compliance | a harmful request answered, and the answer is not gibberish | coherent jailbreak: degeneracy gate + rule-based refusal detector | "ASR" in executive text |
| committee of specialists | a model in which only a few parts answer each token | mixture of experts (MoE), router, per-expert direction | "MoE", "expert", "router" in executive text |
