# API Test Results

> Tested on 2026-09-29 and 2026-10-02.

## Test Log

---

### Reddit API Test
**Date**: 2026-09-29
**Status**: ❌ Denied — application rejected by Reddit

#### What Was Tested
1. Public JSON endpoint (no auth) → 403 Forbidden
2. Self-service app registration at /prefs/apps → reCAPTCHA dead loop
3. Manual developer API request ticket → **Rejected** by Reddit Data Team

#### Result
Reddit rejected the API access request, citing non-compliance with the Responsible Builder Policy. Reddit is treated as **unavailable for this project** per John's guidance.

---

### GDELT API Test
**Date**: 2026-09-29
**Status**: ✅ Completed

#### Results
- ArtList mode: 429 rate limited (1 req/5s)
- ToneChart mode: 200 OK, returns built-in sentiment bins, ~25s response
- No API key needed, completely free

---

### Google Play Reviews Test
**Date**: 2026-10-02
**Status**: 🔄 Test script ready — pending local execution

#### What Was Tested
- Library: `google-play-scraper` (v1.2.7, installed successfully)
- Test script: [`tests/test_gplay_reviews.py`](test_gplay_reviews.py)
- Cloud environment could not reach Google Play (network blocked), but the library is installed and documented
- Test script fetches 20 newest reviews from 4 sample apps: WhatsApp, Spotify, Candy Crush, Google Maps

#### Expected Data Fields
| Field | Description |
|-------|-------------|
| reviewId | Unique review ID |
| userName | Reviewer name |
| content | Review text (sentiment data) |
| score | Star rating 1-5 |
| thumbsUpCount | Helpful votes |
| at | Timestamp |
| reviewCreatedVersion | App version |
| replyContent | Developer response |

#### To Run Locally
```bash
pip install google-play-scraper
python test_gplay_reviews.py
```

---

### Amazon Third-party API Test
**Date**: Not tested
**Status**: ⬜ Not started — Canopy free tier (100 req/month) is too limited per John's feedback

---

## Summary Table

| API | Date | Status | Key Finding |
|-----|------|--------|-------------|
| Reddit | 2026-09-29 | ❌ Denied | Application rejected; unavailable per policy |
| GDELT | 2026-09-29 | ✅ Works | Free, built-in sentiment, but 5s rate limit, news not customer feedback |
| Google Play | 2026-10-02 | 🔄 Script ready | Free, no API key, structured customer reviews; pending local run |
| Amazon (Canopy) | — | ⚠️ Limited | 100 req/month free tier insufficient |
