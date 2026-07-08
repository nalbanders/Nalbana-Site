# STATE.md — website (nalbana.com)
*Volatile. Seeded by the 2026-07-08 audit.*

**Last touched:** code 2026-07-01 (bk-end rounding fix on back-to-back stubs); audit 2026-07-08 (docs only). Site verified live.

## What's broken / open
- Cross-repo dependency on ops.nalbana.com JSONs was undocumented until this audit — now a named contract (see README). Long-term cleanup: MIGRATION_PLAN step 11 (retire duplicate ICAL secrets).
- ICAL_* secrets duplicated with Nalbana_FPA repo — iCal URL rotation must be done in both repos until step 11.

## What's next
1. Nothing urgent. Portfolio-website improvements are roadmap priority 4 (after guest diligence, FP&A, marketing).

## Session log
- 2026-07-08 — Audit: added README/STATE; no site changes.
