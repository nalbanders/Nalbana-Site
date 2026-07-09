# STATE.md — website (nalbana.com)
*Volatile. Seeded by the 2026-07-08 audit.*

**Last touched:** 2026-07-09 — owner.html false red-◇ cleaning diamonds fixed; calendar.html + owner.html now consume the shared classifier `ops.nalbana.com/cleaning_classify.js` (built; awaiting Armen's commit/push — push Nalbana_FPA FIRST so the classifier exists before this deploys).

## What's broken / open
- Cross-repo dependency on ops.nalbana.com JSONs was undocumented until this audit — now a named contract (see README). Long-term cleanup: MIGRATION_PLAN step 11 (retire duplicate ICAL secrets).
- ICAL_* secrets duplicated with Nalbana_FPA repo — iCal URL rotation must be done in both repos until step 11.

## What's next
1. Nothing urgent. Portfolio-website improvements are roadmap priority 4 (after guest diligence, FP&A, marketing).

## Session log
- 2026-07-09 — Fixed owner.html cleaning diamonds: page never fetched `cleaning_schedule.json`, so its stale `cleaningDiamond()` fork showed red ◇ "NOT scheduled" for cleanings that WERE on the cleaner's calendar (smoke test: 14 of 15 upcoming cleanings were false-red). owner.html now fetches the schedule, applies suppression + property whitelist (Jemez excluded, matching calendar.html), and both owner.html and calendar.html consume the shared classifier `ops.nalbana.com/cleaning_classify.js` (new 4th contract file; classification shared, site palette local; pages skip diamonds gracefully if the script fails to load). Full diagnosis: `Nalbana_FPA/docs_meta/STATE.md` session log.
- 2026-07-08 — Audit: added README/STATE; no site changes.
