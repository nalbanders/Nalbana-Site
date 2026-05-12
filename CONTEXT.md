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

## Next Project: Global Availability Calendar

### Goal
Add a multi-property availability calendar to the website showing which dates are booked vs. available across the 5 Miami properties (Jemez optional).

### Data source: bookings.json (already exists — use this, NOT iCal)

The FP&A daily pipeline (Nalbana_FPA repo) already ingests booking confirmation emails from Gmail every day at 9 AM ET and publishes the result to GitHub Pages:

**Live URL:** `https://nalbanders.github.io/Nalbana_FPA/bookings.json`

GitHub Pages serves with `Access-Control-Allow-Origin: *` so the calendar page can `fetch()` this URL directly cross-origin — no proxy, no new infrastructure needed.

### bookings.json schema
```json
{
  "CONFIRMATION_CODE": {
    "guest_name": "...",
    "property": "10th" | "21st" | "22nd" | "23rd" | "13th" | "jemez",
    "listing_id": "...",
    "check_in": "YYYY-MM-DD",
    "check_out": "YYYY-MM-DD",
    "nights": N,
    "payout": 0.00,
    "status": "confirmed" | "canceled",
    "platform": "airbnb",
    "ingested_at": "ISO timestamp",
    "booked_at": "YYYY-MM-DD",
    "guests": N,
    "hometown": "..."
  }
}
```

- **37 bookings** as of May 12, 2026
- **Date range:** 2026-04-30 → 2026-07-23
- **Filter:** use only `status === "confirmed"` for blocked dates
- **Updated:** daily at 9 AM ET automatically by the pipeline

### Pipeline source (Nalbana_FPA repo)
- **Repo:** `https://github.com/nalbanders/Nalbana_FPA`
- **Workflow:** `.github/workflows/daily_pipeline.yml` — step "Ingest booking emails" runs `agents/fp-and-a/booking_ingester.py`, writes `agents/fp-and-a/bookings.json`, then copies to `docs/bookings.json`
- **Local path:** `/Users/nalband/Dropbox/Portfolio Management/Nalbana_FPA/agents/fp-and-a/bookings.json`

### Calendar UI design (reference: Airbnb multi-listing calendar)
- Horizontal timeline: X-axis = dates (scrollable, show ~8–10 weeks ahead)
- Y-axis = one row per Miami property (label with property nickname)
- Confirmed bookings = blocked/dark fill (diagonal hatch pattern like Airbnb)
- Available dates = light / open
- No need to show guest names or prices — just available vs. blocked
- Should match the Nalbana site design system (dark/gold/serif aesthetic)
- Lives on a dedicated `calendar.html` page linked from the nav on index.html
- Password protected with same sessionStorage auth pattern as other pages

### Property name mapping (bookings.json → display name)
| bookings.json `property` | Display name |
|---|---|
| `10th` | Villa Marqueza |
| `21st` | Villa Nalbana |
| `22nd` | Villa Armaza |
| `23rd` | Villa Maganda |
| `13th` | Buko House |
| `jemez` | Four Winds Trail |
