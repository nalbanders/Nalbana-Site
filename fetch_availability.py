#!/usr/bin/env python3
"""
fetch_availability.py
─────────────────────
Fetches Airbnb iCal feeds for all Nalbana properties and writes
availability.json to the repo root.

Called by the GitHub Actions workflow `.github/workflows/fetch-availability.yml`.
Each iCal URL is passed via environment variable (stored as a repo Secret):

  ICAL_10TH   → Villa Marqueza (1745 SW 10th St)
  ICAL_21ST   → Villa Nalbana  (341 SW 21st Rd)
  ICAL_22ND   → Villa Armaza   (620 SW 22nd Rd)
  ICAL_23RD   → Villa Maganda  (SW 23rd Rd)
  ICAL_13TH   → Buko House     (1860 SW 13th St)
  ICAL_JEMEZ  → Four Winds Trail (329 Jemez Trl, Yucca Valley CA)

Local test:
  ICAL_10TH="https://..." ICAL_21ST="https://..." python fetch_availability.py

Output: availability.json (same directory as this script)
"""

import json
import os
import sys
from datetime import datetime, timezone
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen

# ── Property → env-var mapping ──────────────────────────────────────────────
PROPERTIES = {
    "10th":  "ICAL_10TH",
    "21st":  "ICAL_21ST",
    "22nd":  "ICAL_22ND",
    "23rd":  "ICAL_23RD",
    "13th":  "ICAL_13TH",
    "jemez": "ICAL_JEMEZ",
}

HEADERS = {"User-Agent": "NalbanaCalendar/1.0 (+https://nalbanders.github.io/Nalbana-Site/)"}


def fetch_ical(url: str) -> str:
    """Download an iCal feed and return its text content."""
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def parse_events(ics_text: str) -> list[dict]:
    """
    Parse VEVENT blocks from iCal text.

    Returns a list of dicts: { "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" }
    where `end` is exclusive (matches iCal DTEND convention for all-day events).

    Handles iCal line folding (continuation lines start with a space or tab).
    Captures both:
      DTSTART;VALUE=DATE:20260515
      DTSTART:20260515
    """
    # Unfold folded lines
    raw_lines = ics_text.splitlines()
    lines: list[str] = []
    for raw in raw_lines:
        if raw.startswith((" ", "\t")) and lines:
            lines[-1] += raw.lstrip()
        else:
            lines.append(raw)

    events: list[dict] = []
    cur: dict | None = None

    for line in lines:
        stripped = line.strip()

        if stripped == "BEGIN:VEVENT":
            cur = {}
        elif stripped == "END:VEVENT":
            if cur is not None and "start" in cur and "end" in cur:
                events.append(cur)
            cur = None
        elif cur is not None:
            # Split on first ":" — the property name may contain parameters (e.g. DTSTART;VALUE=DATE)
            colon_idx = stripped.find(":")
            if colon_idx == -1:
                continue
            prop_name = stripped[:colon_idx]
            prop_val  = stripped[colon_idx + 1:]

            if prop_name.startswith("DTSTART"):
                date_str = _extract_date(prop_val)
                if date_str:
                    cur["start"] = date_str
            elif prop_name.startswith("DTEND"):
                date_str = _extract_date(prop_val)
                if date_str:
                    cur["end"] = date_str

    return events


def _extract_date(value: str) -> str | None:
    """
    Extract YYYY-MM-DD from an iCal date value.

    Handles:
      20260515            (all-day DATE)
      20260515T120000Z    (datetime — we take just the date portion)
    """
    raw = value.strip()[:8]  # First 8 chars are always YYYYMMDD
    if len(raw) == 8 and raw.isdigit():
        return f"{raw[:4]}-{raw[4:6]}-{raw[6:8]}"
    return None


def main() -> None:
    result: dict = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "properties": {},
    }

    errors = 0
    for key, env_var in PROPERTIES.items():
        url = os.environ.get(env_var, "").strip()

        if not url:
            print(f"  SKIP  {key:<6}  ({env_var} not set)")
            result["properties"][key] = []
            continue

        try:
            ics_text = fetch_ical(url)
            events = parse_events(ics_text)
            result["properties"][key] = events
            print(f"  OK    {key:<6}  {len(events):3d} blocked range(s)")
        except HTTPError as e:
            print(f"  ERR   {key:<6}  HTTP {e.code}: {e.reason}", file=sys.stderr)
            result["properties"][key] = []
            errors += 1
        except URLError as e:
            print(f"  ERR   {key:<6}  {e.reason}", file=sys.stderr)
            result["properties"][key] = []
            errors += 1
        except Exception as e:  # noqa: BLE001
            print(f"  ERR   {key:<6}  {e}", file=sys.stderr)
            result["properties"][key] = []
            errors += 1

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "availability.json")
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    print(f"\n  Wrote {output_path}")

    if errors:
        print(f"\n  ⚠  {errors} property/ies failed — availability.json may be incomplete", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
