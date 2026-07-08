# website (nalbana.com) — README
*Evergreen. Status → `STATE.md`. Design system, property map, auth pattern → `CONTEXT.md` — link, don't restate. Global map → `../SYSTEM.md`.*

## Purpose
The portfolio website at **nalbana.com** (repo `nalbanders/Nalbana-Site`, GitHub Pages): password-gated marketing site (index + 6 property pages with galleries/floor plans), a public availability calendar, and a password-gated owner view with live rates and a direct-booking offer generator.

## Data sources
- `availability.json` — generated in-repo every 2h by `.github/workflows/fetch-availability.yml` → `fetch_availability.py` from 6 Airbnb iCal secrets (ICAL_* — duplicates of the FPA repo's copies).
- **Cross-repo reads from ops.nalbana.com** (FPA pipeline outputs): `bookings.json`, `pricelabs_rates.json`, `cleaning_schedule.json` — consumed by `calendar.html` and `owner.html`. These URLs are a contract; see `Nalbana_FPA/docs_meta/README.md`.
- `occupancy_notes.json` — manual notes.

## Key files
`index.html` + `10th-st|13th-st|21st-rd|22nd-rd|23rd-rd|jemez.html` (single-file pages, inline CSS/JS), `calendar.html`, `owner.html`, `fetch_availability.py`, `CNAME` (nalbana.com), listing photo folders ×6.

## Constraints
- Password `sessionStorage` gate is UI-only, not security — the site is world-readable to anyone with the password or direct file URLs.
- **Never mention the persona/multi-account architecture on this site** (WORKFLOW.md; hosting strategy is private).
- Single-file page pattern: all CSS/JS inline; follow the self-review checklist in WORKFLOW.md before commits.
- Deploys automatically on push to main (~1 min; CDN cache up to 10 min).
