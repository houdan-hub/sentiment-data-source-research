# API Test Results

> Tested on 2026-09-29 and 2026-10-02.

## Test Log

---

### Reddit API Test
**Date**: 2026-09-29
**Status**: ❌ Denied — application rejected by Reddit

Reddit rejected the API access request (ticket 18531647), citing non-compliance with the Responsible Builder Policy. Reddit is treated as **unavailable for this project**.

---

### GDELT API Test
**Date**: 2026-09-29
**Status**: ✅ Completed

- ArtList mode: 429 rate limited (1 req/5s)
- ToneChart mode: 200 OK, returns built-in sentiment bins, ~25s response
- No API key needed, completely free
- Content is news/media, not direct customer feedback

---

### Google Play Reviews Test
**Date**: 2026-10-02
**Status**: ✅ Completed — multi-app, pagination, and repeated collection all verified

**Library**: google-play-scraper v1.2.7 (free, no API key)
**Location**: Los Angeles, CA (local machine)

#### Test 1: Multi-App Feasibility
- 4 apps across different categories: WhatsApp (Social), Spotify (Music), Candy Crush Saga (Game), Google Maps (Navigation)
- Fetched 10-20 newest reviews per app

| App | Category | Reviews | Response Time |
|-----|----------|---------|---------------|
| WhatsApp | Social | 10 | 0.15s |
| Spotify | Music | 10 | 0.16s |
| Candy Crush | Game | 10 | 0.16s |
| Google Maps | Navigation | 10 | 0.14s |

#### Test 2: Pagination
- Page 2 returned additional reviews in 0.27s
- Continuation token works for fetching historical reviews

#### Test 3: Repeated Collection (polling)
- Fetched WhatsApp reviews twice, 30 seconds apart
- Both calls returned successfully, no rate limiting or errors
- No new reviews in 30 seconds (expected — reviews don't arrive every second)
- **Conclusion**: endpoint supports repeated polling; can be scheduled hourly to catch new reviews

#### Sample Real Reviews
```
WhatsApp:  Anna Phume, 1 star, "Good" (2026-10-01)
Spotify:   Rupesh S, 4 stars, "good app, but ads that come when we dont use Premium is just simply irritating" (2026-10-01)
Candy Crush: Rachael Wambui, 3 stars, "ive paid ksh 500 for 30 dollars only to get none. what's up??" (2026-10-01)
Google Maps: Gerald Doherty, 3 stars, "just did not work in Norfolk plus Suffolk nothing but dropped out" (2026-10-01)
```

#### Available Fields per Review
reviewId, userName, userImage, content, score, thumbsUpCount, reviewCreatedVersion, at, replyContent, repliedAt, appVersion

#### Key Findings
1. **Extremely fast**: 0.14-0.18s per request (vs GDELT's 25s)
2. **No API key, no registration, no quota** — completely free
3. **Structured data**: star rating + review text + timestamp + app version
4. **Real-time**: reviews from 2026-10-01 fetched on 2026-10-02
5. **Pagination works** for historical backfill
6. **Repeated polling works** — can schedule hourly collection
7. **Direct customer feedback** — highly relevant for sentiment analysis

---

### Amazon Third-party API Test
**Date**: Not tested
**Status**: ⚠️ Canopy free tier (100 req/month) too limited per John's feedback

---

## Summary Table

| API | Date | Status | Response Time | Key Finding |
|-----|------|--------|---------------|-------------|
| Reddit | 2026-09-29 | ❌ Denied | N/A | Application rejected; unavailable |
| GDELT | 2026-09-29 | ✅ Works | ~25s | Free but slow; news not customer feedback |
| Google Play | 2026-10-02 | ✅ Works | 0.14-0.18s | Fast, free, structured; pagination + polling verified |
| Amazon (Canopy) | — | ⚠️ Limited | — | 100 req/month free tier insufficient |
