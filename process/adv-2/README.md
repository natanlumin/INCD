# SCRUM-294 (ADV-2): classify every threat and adversarial technique through the cycle, strategy

Item folder for SCRUM-294, ADV-2 in the plan. Report sections 2.3 (threat classification and decision
cycle) and Appendix A (threat disposition table). Wave 4; blocked by ADV-1 (SCRUM-283) and THR-4
(SCRUM-293); blocks ADV-3 (SCRUM-302). Natan 0.75d, Dan 0.25d.

`adv2-disposition.html` is the disposition table, published at
https://claude.ai/artifact/YGQLUH5WFXVUMu3pvjQoYd.

## State on 25 November 2026

- 21 of 21 register rows (T1 to T21) carry a disposition, rationale and decision date; zero unclassified.
- Dispositions: 9 demonstration and Advisor, 3 Advisor candidate, 5 demonstration, 4 theoretical only.
- Disputed, for Dan: T4, T9, T20, each with a proposed decision and an alternative.
- Dan's signature: pending.

## To redo when THR-4 (SCRUM-293) is generated

1. **Replace the inventory.** The table uses the register as it stands: T1 to T8 from
   `process/huggingface/hub-supply-chain-threats.md` (Table 6) and T9 to T21 from
   `process/scrum-288/scrum288.md` (Table 3). Re-key every row to THR-4's ids and names.
2. **Classify every new row.** Any THR-4 row or technique without a T1 to T21 counterpart gets a disposition,
   rationale and date; techniques split out of a threat get their own row and their own blackbox or
   whitebox tag.
3. **Re-check the completeness count** against THR-4's total, not against 21.
4. **Re-read the gate against ADV-1 (SCRUM-283).** The four dispositions and the three-condition promotion
   test are proposed here because ADV-1 is not in this repository.
5. Then Dan adjudicates the disputed rows and signs.
