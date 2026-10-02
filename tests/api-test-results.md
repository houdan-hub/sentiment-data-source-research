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
**Status**: ✅ Completed — successful, excellent results

**Library**: google-play-scraper v1.2.7 (free, no API key)
**Location**: Los Angeles, CA (local machine)

#### Test Setup
- 4 apps across different categories: WhatsApp (Social), Spotify (Music), Candy Crush Saga (Game), Google Maps (Navigation)
- Fetched 20 newest reviews per app, then tested pagination (page 2)
- Language: English, Country: US

#### Results

| App | Category | Reviews | Response Time | Avg Score | Avg Content Length | Dev Replies |
|-----|----------|---------|---------------|-----------|--------------------|-------------|
| WhatsApp | Social | 20 | 0.18s | 4.45★ | ~100 chars | tested |
| Spotify | Music | 20 | 0.16s | 3.65★ | ~100 chars | tested |
| Candy Crush Saga | Game | 20 | 0.15s | 4.85★ | ~100 chars | tested |
| Google Maps | Navigation | 20 | 0.17s | 3.40★ | 106 chars | 2/20 |

**Pagination**: Page 2 returned 20 more reviews in 0.27s — pagination works smoothly.

#### Sample Review (Google Maps)
```json
{
  "reviewId": "24e1e07c-678c-475f-b788-aaec3365829c",
  "userName": "Reena Kumari",
  "score": 5,
  "content": "Nice series",
  "at": "2026-09-30 17:33:18",
  "thumbsUpCount": 0,
  "reviewCreatedVersion": "26.38.01.980791571",
  "replyContent": null
}
```

#### Available Fields
`reviewId`, `userName`, `userImage`, `content`, `score`, `thumbsUpCount`, `reviewCreatedVersion`, `at`, `replyContent`, `repliedAt`, `appVersion`

#### Key Findings
1. **Extremely fast**: 0.15-0.18s per request (vs GDELT's 25s)
2. **No API key, no registration, no quota** — completely free
3. **Structured data**: star rating + review text + timestamp + app version + helpful votes
4. **Real-time**: newest reviews available (test fetched reviews from 2026-09-30, 2 days prior)
5. **Pagination works**: continuation token for fetching historical reviews
6. **Developer replies** included — useful for context
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
| Google Play | 2026-10-02 | ✅ Works | 0.15-0.18s | Fast, free, structured customer reviews — best fit |
| Amazon (Canopy) | — | ⚠️ Limited | — | 100 req/month free tier insufficient |
