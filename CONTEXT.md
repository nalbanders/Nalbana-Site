# Nalbana Properties — Project Context

## Property Map

| Nickname | Address | Beds | Baths | Type | Market | Image Folder | Sub-page | Airbnb ID | Airbnb Link |
|---|---|---|---|---|---|---|---|---|---|
| Villa Nalbana | 341 SW 21st Rd, Miami FL | 4 | 3 | STR | Miami · Brickell | `21st Rd Listing/` | `21st-rd.html` | 51283421 | https://www.airbnb.com/rooms/51283421 |
| Villa Armaza | 620 SW 22nd Rd, Miami FL | 4 | 4 | STR | Miami · Brickell | `22nd Rd Listing/` | `22nd-rd.html` | 587750272435957342 | https://www.airbnb.com/rooms/587750272435957342 |
| Villa Marqueza | 1745 SW 10th St, Miami FL | 5 | 3.5 | STR | Miami · Little Havana | `10th St Listing/` | `10th-st.html` | 1371543678014557369 | https://www.airbnb.com/rooms/1371543678014557369 |
| Villa Maganda | SW 23rd Rd, Miami FL | 4 | 3 | STR | Miami | `23rd Rd Listing/` | `23rd-rd.html` | 1297056429185208299 | https://www.airbnb.com/rooms/1297056429185208299 |
| Buko House | 1860 SW 13th St, Miami FL | 3 | 2 | STR | Miami · Little Havana | `13th St Listing/` | `13th-st.html` | 1376844965121549879 | https://www.airbnb.com/rooms/1376844965121549879 |
| Four Winds Trail | 329 Jemez Trl, Yucca Valley CA | 3 | 2 | STR | Yucca Valley | `Jemez Listing/` | `jemez.html` | 52732943 | https://www.airbnb.com/rooms/52732943 |

---

## Repository

- **GitHub repo:** https://github.com/nalbanders/Nalbana-Site
- **Live site:** https://nalbanders.github.io/Nalbana-Site/
- **Branch:** `main` — GitHub Pages deploys automatically on push (built-in `pages-build-deployment` workflow, no custom Actions file)
- **Deployment time:** ~1 min after push. CDN can cache for up to 10 min — use incognito to verify immediately.

---

## Website Structure

All files live in `/Users/nalband/Dropbox/Portfolio Management/Nalbana Website/`

### Files
- `index.html` — main portfolio page (single file, all CSS/JS inline)
- `10th-st.html`, `13th-st.html`, `21st-rd.html`, `22nd-rd.html`, `23rd-rd.html`, `jemez.html` — individual property detail pages
- `CONTEXT.md` — this file

### index.html sections
1. Password wall
2. Fixed nav (Properties / Track Record / About / Contact)
3. Hero — full-screen bg photo, title "Luxury Rentals, Expertly Managed", stats strip (6 properties, $850K+ TTM, 4+ years)
4. Properties grid — 6 cards, 340px min-width, 2px gap. Each card has clickable thumbnail + "Explore Property" link + "Airbnb" link
5. Track Record — dark section with 6 metrics
6. About — Armen Nalband bio, 2-col with photo
7. Contact — mailto:nalbana@gmail.com
8. Footer

### Property sub-pages (shared template pattern)
Each sub-page is a single HTML file with:
- Minified CSS in `<head>`
- Password wall (same pattern as index)
- Fixed nav with back link to `index.html`
- Ken Burns hero slideshow (3–4 slide variants, 6s interval)
- Property stats bar (beds/baths/guests/rating)
- Room-filtered masonry photo gallery (IntersectionObserver scroll-reveal, JS lightbox with keyboard nav)
- Interactive SVG floor plan with `data-room` hover/filter
- Sticky CTA bar (animates in on scroll)
- "You may also like" related properties section

### Design system
- Font: Georgia / Times New Roman serif
- Background: `#faf9f7` (off-white)
- Dark: `#0f0f0e`
- Gold accent: `#a89070` / `#d4b896` / `#c8b89a`
- Text: `#1a1a1a`
- Section padding: `100px 48px`
- Grid gap: `2px`

---

## Authentication

- **Password:** `1986`
- **Mechanism:** `sessionStorage` key `nalbana_auth = '1'`
- Authenticate once on any page → all other pages in the same browser tab skip the password wall
- Direct navigation to a sub-page URL (fresh tab) → password required
- Closing the tab clears the session

### Password script pattern (index.html — formatted)
```js
const SITE_PASSWORD = '1986';
const AUTH_KEY = 'nalbana_auth';
if (sessionStorage.getItem(AUTH_KEY) === '1') {
  document.getElementById('pw-overlay').style.display = 'none';
}
function checkPassword() {
  const val = document.getElementById('pw-input').value;
  if (val === SITE_PASSWORD) {
    sessionStorage.setItem(AUTH_KEY, '1');
    document.getElementById('pw-overlay').style.display = 'none';
  } else {
    document.getElementById('pw-error').textContent = 'Incorrect password.';
    document.getElementById('pw-input').value = '';
  }
}
document.getElementById('pw-input').addEventListener('keydown', function(e) {
  if (e.key === 'Enter') checkPassword();
});
```

### Password script pattern (sub-pages — minified)
```js
const SITE_PASSWORD='1986';
const AUTH_KEY='nalbana_auth';
if(sessionStorage.getItem(AUTH_KEY)==='1'){document.getElementById('pw-overlay').style.display='none';}
function checkPassword(){if(document.getElementById('pw-input').value===SITE_PASSWORD){sessionStorage.setItem(AUTH_KEY,'1');document.getElementById('pw-overlay').style.display='none';}else{document.getElementById('pw-error').textContent='Incorrect password.';document.getElementById('pw-input').value='';}}
document.getElementById('pw-input').addEventListener('keydown',e=>{if(e.key==='Enter')checkPassword();});
```

---

## Photo Conventions

- Airbnb photos: `airbnb-001-[hash].jpg`, `airbnb-002-[hash].jpg`, etc.
- Zillow exterior photos: `zillow-ext-001.jpg`, `zillow-ext-002.jpg`, etc.
- Professional shoot (10th St only): `exterior-050-...jpg`, `exterior-057-...jpg` (1oakstudios)
- Cover/drone shots (22nd Rd): `cover-2J9A4615.jpg`, `drone-01.jpg` through `drone-05.jpg`
- Jemez hero: `airbnb-044-d34cd7c8.jpg` (lounge chairs / Joshua tree)

---

## Site Notes

- 10th St has professional exterior photos from 1oakstudios in addition to Airbnb photos
- 22nd Rd has a dedicated blue-hour cover photo (`cover-2J9A4615.jpg`) and drone shots
- Hero background: `10th St Listing/exterior-057- 1745 SW 10th St_1oakstudiosdrone_13.jpg`
- About section photo: `10th St Listing/exterior-050- 1745 SW 10th St_1oakstudios_74.jpg`
- Four Winds Trail (Jemez) is the only non-Miami property — rated 5.0★ vs 4.9★ for Miami
- Contact email: nalbana@gmail.com
- TTM Revenue: $850K+ | Self-managed since 2021

---

## Calendar Page — `calendar.html` (COMPLETE)

### Live URL
`https://nalbanders.github.io/Nalbana-Site/calendar.html`

### Overview
Horizontal Gantt-style multi-property availability calendar. Password-protected (same `1986` / sessionStorage pattern). Fetches three data sources on load via `Promise.all`, merges them into a per-property/per-day lookup, renders a scrollable `<table>`.

### Files
| File | Purpose |
|---|---|
| `calendar.html` | The calendar page — all CSS/JS inline |
| `availability.json` | Written by GitHub Action (iCal fetch). Source of truth for blocked dates. |
| `occupancy_notes.json` | Manual non-Airbnb blocks (direct bookings, leases, maintenance). Currently `[]`. |
| `fetch_availability.py` | Python script fetching 6 iCal feeds, parsing VEVENTs, writing `availability.json`. Stdlib only. |
| `.github/workflows/fetch-availability.yml` | Runs `fetch_availability.py` every 2 hrs + on `workflow_dispatch`. Commits with `[skip ci]`. Requires `permissions: contents: write`. |

### iCal secrets (in Nalbana-Site repo secrets, NOT Nalbana_FPA)
`ICAL_10TH`, `ICAL_21ST`, `ICAL_22ND`, `ICAL_23RD`, `ICAL_13TH`, `ICAL_JEMEZ`

### Data architecture (three layers)
**Layer 1 — iCal (availability.json):** Sets all blocked dates as `airbnb_block`. Ground truth for future dates.

**Layer 2 — bookings.json** (`https://nalbanders.github.io/Nalbana_FPA/bookings.json`):
- **Past dates** (before today): iCal drops old events, so bookings.json is source of truth → writes `airbnb_confirmed` unconditionally.
- **Future dates**: iCal is live truth. If day is in both → `airbnb_confirmed` (enriched). If in bookings.json only → `airbnb_conflict` (Airbnb likely modified/cancelled — shown in amber with outline).

**Layer 3 — occupancy_notes.json:** Non-Airbnb blocks (direct, lease, maintenance, hold). Writes unconditionally on top of iCal.

### Block type → CSS class → color
| Type | Color | Visual |
|---|---|---|
| `airbnb_confirmed` | `#4a7868` | Solid teal-green pill |
| `airbnb_block` | `#2e2c2a` | Diagonal stripe pattern |
| `airbnb_conflict` | `#6a4a10` | Amber + orange outline — booking in DB but not in iCal |
| `direct` | `#6a4a2a` | Warm brown |
| `lease` | `#2a4e68` | Steel blue |
| `maintenance` | `#4a4a28` | Olive |
| `hold` | `#502840` | Plum |

### Key JS config constants
```js
const DAYS_BEFORE = 60;   // days of history before today
const DAYS_TOTAL  = 180;  // total days rendered
```
Page loads scrolled to today. Scroll left for history.

### groupId() function
Groups adjacent cells into pill shapes (solo/start/mid/end). For `airbnb_confirmed` uses confirmation code; for occupancy notes uses `start|end`; for raw blocks uses `type`.

### Known gotchas
- **Git stash conflicts:** The availability bot pushes `availability.json` to Nalbana-Site every 2 hrs. If bot commits between your local commits, push is rejected. Fix: `git pull --rebase origin main && git push origin main`. Do NOT use `git stash` — it causes the stash pop to re-apply old state and overwrite local edits. The bot only ever touches `availability.json` so there's never a real conflict with `calendar.html`.
- **GitHub Pages CDN cache:** Changes can take 1–3 min after the `pages-build-deployment` Action goes green. Use incognito or DevTools → right-click reload → "Empty Cache and Hard Reload" if stuck.
- **Temporal dead zone:** Auth check `if (sessionStorage.getItem(AUTH_KEY))` must be at the BOTTOM of the `<script>` block, after all `const` declarations.
- **iCal secrets must be in Nalbana-Site repo**, not Nalbana_FPA.

### Refreshing bookings data
The calendar fetches bookings.json live on every page load. When a new booking is forwarded and processed through the FPA pipeline, just hard-refresh the calendar page — no action needed on the Nalbana-Site side.

### FPA → Site nav link
Added `Site ↗` link to `/Nalbana_FPA/docs/nav.js` (external, opens in new tab). Required adding `match: []` to avoid a crash in `isActive()` — external links have no match array.

---

## Next Project: Global Availability Calendar

### Goal
Add a multi-property availability calendar to the website showing which dates are booked vs. available across the 5 Miami properties (Jemez optional).

### Data architecture (three layers)

#### Layer 1 — iCal feeds (availability truth)
Airbnb exposes a private iCal `.ics` URL per listing. This is the **ground truth** for blocked dates — it captures everything: confirmed Airbnb bookings, manually blocked dates, maintenance holds, LTR blocks. A scheduled GitHub Action on the Nalbana-Site repo fetches all 5 Miami iCal feeds on a schedule (every 1–2 hours), parses VEVENT blocked ranges, and writes `availability.json` to the repo. The calendar page reads this file (same-origin, no CORS).

**iCal URLs needed** — Armen to provide (Airbnb → Hosting → select property → Calendar → Export calendar → copy `.ics` URL):
- Villa Marqueza (10th)
- Villa Nalbana (21st)
- Villa Armaza (22nd)
- Villa Maganda (23rd)
- Buko House (13th)

**Non-Airbnb occupancy** (leases, direct bookings): Armen manually blocks the dates on Airbnb → iCal automatically captures the block. The *reason* is passed separately via Layer 3.

#### Layer 2 — bookings.json (Airbnb enrichment)
Already published daily at `https://nalbanders.github.io/Nalbana_FPA/bookings.json` by the FP&A pipeline (9 AM ET). Overlaid on top of iCal to enrich confirmed Airbnb blocks with guest name, payout, hometown etc. **Not** the availability source of truth — iCal is.

**bookings.json schema:**
```json
{
  "CONFIRMATION_CODE": {
    "property": "10th" | "21st" | "22nd" | "23rd" | "13th" | "jemez",
    "check_in": "YYYY-MM-DD",
    "check_out": "YYYY-MM-DD",
    "status": "confirmed" | "canceled",
    "guest_name": "...",
    "payout": 0.00,
    "nights": N,
    "guests": N,
    "hometown": "..."
  }
}
```

#### Layer 3 — occupancy_notes.json (non-Airbnb annotation)
Labels manually-blocked iCal ranges with a reason (lease, direct booking, maintenance). Populated via email — the unified input channel for all non-Airbnb occupancy. No separate form or backend needed.

**Email convention:**
- **To:** pipeline Gmail address (same one booking_ingester.py reads)
- **Subject:** `OCCUPANCY — [property nickname]` e.g. `OCCUPANCY — Villa Nalbana`
- **Body or attachment:** anything — pipeline uses Claude to extract dates/type/notes from whatever is present (structured text for direct bookings, forwarded PDF for leases)

**Direct booking example email body:**
```
Guest: John Smith
Dates: Aug 1–10 2026
Rate: $500/night
Notes: friend of Armen, no cleaning fee
```

**Lease example:** just forward the lease PDF with subject `OCCUPANCY — Buko House`

**Pipeline:** extend `booking_ingester.py` (or add `occupancy_ingester.py`) to look for `OCCUPANCY —` subject pattern, call Claude API to extract structured fields, write to `agents/fp-and-a/occupancy_notes.json` → synced to `docs/` by the existing GitHub Action.

**Calendar UX:** a "Record Booking" button on `calendar.html` opens a pre-filled `mailto:` link with subject template already set — one click, fill in the blanks, send.

**occupancy_notes.json schema (proposed):**
```json
[
  {
    "property": "21st",
    "start": "2026-08-01",
    "end": "2026-08-10",
    "type": "direct" | "lease" | "maintenance" | "hold",
    "note": "John Smith — friend rate $500/night",
    "ingested_at": "ISO timestamp"
  }
]
```

### Calendar UI design (reference: Airbnb multi-listing calendar)
- Horizontal timeline: X-axis = dates (scrollable, show ~8–10 weeks ahead)
- Y-axis = one row per Miami property (labeled with property nickname)
- Blocked dates: dark/hatched fill — Airbnb blocks shown differently from lease/direct blocks
- Available dates: light/open
- Hover/tooltip: show enrichment from bookings.json (guest name, nights, payout) or occupancy note reason
- No need to show guest names in the main view — just available vs. blocked
- Matches Nalbana site design system (dark/gold/serif aesthetic)
- Lives on a dedicated `calendar.html` linked from the nav on index.html
- Password protected with same sessionStorage auth pattern (AUTH_KEY = 'nalbana_auth', password = '1986')

### Property name mapping
| iCal / bookings.json key | Display name | Airbnb listing ID |
|---|---|---|
| `10th` | Villa Marqueza | 1371543678014557369 |
| `21st` | Villa Nalbana | 51283421 |
| `22nd` | Villa Armaza | 587750272435957342 |
| `23rd` | Villa Maganda | 1297056429185208299 |
| `13th` | Buko House | 1376844965121549879 |
| `jemez` | Four Winds Trail | 52732943 (optional — CA property) |
