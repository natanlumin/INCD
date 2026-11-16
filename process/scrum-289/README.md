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

## Definition of done (acceptance criteria), with where the task will answer each

| Criterion | Planned answer | State |
|---|---|---|
| Drafted subsections | 6.2 attestable properties; 6.3 properties discoverable only by testing | not started |
| An evidence-strength rating per attestable property | one row per property named by the Jira (publisher identity, training-data disclosure, model card, AIBOM/SBOM, signing and attestation, licence lineage), rated on ASM-1's evidence kinds: guaranteed (the platform enforces it), declared (stated, unverified), readable (read from the file), with the measured frequency of each declared field from LAND-2 cited by section, not by number | not started |
| A clear public-versus-discoverable split table | one table: property, attestable or testable, evidence kind (ASM-1 Table 1), who answers, exists in possession, exists by proxy, test family | not started |
| A blunt statement of what is currently neither attestable nor practically testable | a short boxed list, each item cited: e.g. an unknown trigger in a generative model (SCRUM-288 T10: TH-12, TH-14); training data actually used (declared only; SCRUM-288 T9); a model held only by proxy, whose file-side properties are neither attestable nor testable (ASM-1 Table 1) | not started |
| "The split is what makes the testing methodology necessary" | the closing argument of 6.3, from the gap rule of ASM-1: every declared item is a gap | not started |
| Blocked by ASM-1 and LAND-2 | ASM-1 = SCRUM-284, drafted; LAND-2 = SCRUM-286, drafted. Unblocked | met |

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

- `README.md`: this strategy. The task `scrum289.md` follows once SCRUM-288 is complete.
