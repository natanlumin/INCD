# SCRUM-289 (ASM-2): attestable versus testable model properties, strategy

Item folder for SCRUM-289, ASM-2 in the plan (epic SCRUM-266). Per the item convention this README is the
strategy and `scrum289.md` will be the task; the PDF and HTML are built from the task only. Natan drafts
(1.5d), Dan reviews (0.25d). Skeleton sections: 6.2 publicly attestable properties and 6.3 properties
discoverable only by testing.

## What the Jira asks

What can be verified without running the model: publisher identity, training-data disclosure, model cards,
AIBOM/SBOM, cryptographic signing and attestation, licence lineage. The complement: behavioural properties,
hidden triggers, capability boundaries, robustness and latent contamination that no metadata will reveal. The
split is what makes the testing methodology necessary rather than optional.

## Definition of done (acceptance criteria), state on 16 November

| Criterion | Where in `scrum289.md` | State |
|---|---|---|
| Attestable properties named by the Jira: publisher identity, training-data disclosure, model cards, AIBOM/SBOM, cryptographic signing and attestation, licence lineage | Part 2, P1 to P6, one entry each in the Jira's order | met (6 of 6) |
| The complement: behavioural properties, hidden triggers, capability boundaries, robustness, latent contamination | Part 3, D1 to D5, one entry each | met (5 of 5) |
| Drafted subsections | Part 2 (skeleton 6.2), Part 3 (6.3), with Part 1, Part 4, Part 5, summary, annex | met |
| An evidence-strength rating per attestable property | scale in 1.3 (strong, moderate, weak, none); a rating with its reason and sources closing each of P1 to P6; Strength column of Table 3 | met (6 of 6) |
| A clear public-versus-discoverable split table | Part 4, Table 3, 11 rows: side, evidence kind, who answers, in possession, by proxy, test family, strength | met |
| A blunt statement of what is currently neither attestable nor practically testable | Part 5, Caution box, seven items, each cited | met |
| The split makes the testing methodology necessary rather than optional | opening bullets; closing paragraph of Part 5, from SCRUM-284's gap rule | met |
| Blocked by ASM-1, LAND-2 | SCRUM-284 and SCRUM-286, both drafted | met |
| Dan reviews (0.25d) | subtask pending. Points for Dan: P1 rating split; P5 "strong where present, origin and integrity only"; AT-26 provenance testing labelled emerging | pending |

Completion check run 16 Nov: 6 P entries, 5 D entries, 11 rows in Table 3; every AT id cited has a row and every
row is cited; external ids SC-25, SC-29, HF-11, HF-15, CG-11, TH-03, TH-12, TH-13, TH-14, TH-42, TH-50 resolve
in their logs; every Qn.k and en.k used exists in SCRUM-284 and is given in the annex, Table 4; glossary terms
tagged at first use per part; inline citations at every use; no counts or dates from our own runs; no em or en
dashes. Sources AT-01 to AT-29 verified 16 Nov (EU AI Act text read from a mirror; quote from EUR-Lex at
assembly).

## Inputs, bound to the existing files

| From | What this item takes |
|---|---|
| ASM-1, `process/scrum-284/` | the evidence kinds guaranteed, declared, readable, testable (Table 1); S1 to S4, Qn.k, en.k; the E1 inventory (e1.1 account, dates, hashes; e1.2 card; e1.3 hash or signature; e1.5 scans; e1.7 licence; e1.8 gating); the gap rule |
| LAND-2, `process/scrum-286/` | section 2: licence families, model-card completeness, provenance metadata among widely used models (cited by section, numbers stay there) |
| LAND-1, `process/scrum-280/` | platform-side controls and guaranteed metadata per platform; Table 4 segmentation labels |
| 4.2 item, `process/huggingface/` | Hub elements guaranteed versus declared (Table 1), commit signing, model-signing manifests, CycloneDX ML-BOM (SC-24, SC-25), the Hub controls C1 to C18 |
| SCRUM-288, `process/scrum-288/` | the testable side: hidden triggers (T10, with TH-12 to TH-14), latent contamination (T9, T13, T14), behaviour and robustness (T17 and the model-level part of each threat); the demonstrated-versus-theoretical statuses |
| Glossary, SCRUM-281 | attestable and testable properties, outputs and internals, provenance, guaranteed metadata, test family |

## Rules this item runs under (same as SCRUM-288)

- Symbols and notation of the earlier items, unchanged: S1 to S4, Qn.k, en.k, evidence kinds (SCRUM-284);
  T1 to T21 (4.2 item and SCRUM-288); glossary terms tagged (SCRUM-281) at first use per part; source log
  `ID | Class (SCRUM-281) | Source | URL | Verified`; closing symbols table `Symbol | Meaning | Defined in | File`.
- New source ids continue with a new prefix (proposed AT-nn); earlier ids resolve to their own logs.
- Every claim cited at the point of use (Authors, venue year) or by official source; no counts or dates from
  our own pulls or runs in the task; the numbers stay in SCRUM-286.
- No Jira ids, no drafting scaffolding in the task; those stay here.

## Open questions

1. AIBOM: which specification is cited as the reference, CycloneDX ML-BOM (already SC-25) and SPDX 3.0 AI
   profile (to verify).
2. Whether "capability boundaries" is rated as testable by outputs only, or also by internals.

## Files

- `scrum289.md`: the task. `scrum289.html`: its readable build.
- `README.md`: this strategy.
