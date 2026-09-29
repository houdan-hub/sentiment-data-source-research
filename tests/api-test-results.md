# API Test Results

> Tested on 2026-09-29 using Python requests library. All tests run from local machine in Los Angeles, CA.

## Test Log

---

### Reddit API Test
**Date**: 2026-09-29
**Status**: ⚠️ Partially Completed — Public endpoint blocked; OAuth registration pending

#### What Was Tested
1. **Public JSON endpoint** (`https://www.reddit.com/r/{subreddit}/new.json`) — no authentication
2. **Public search endpoint** (`https://www.reddit.com/search.json`) — no authentication
3. **App registration** at https://www.reddit.com/prefs/apps

#### Test Code (Public Endpoint)
```python
import requests

headers = {"User-Agent": "sentiment-research/1.0 (educational use)"}
url = "https://www.reddit.com/r/technology/new.json"
params = {"limit": 5}

response = requests.get(url, headers=headers, params=params, timeout=30)
print(f"Status: {response.status_code}")
```

#### Results
- **Public endpoint status**: `403 Forbidden` (0.23s response)
- **Search endpoint status**: `403 Forbidden` (0.20s response)
- **Key finding**: Reddit now blocks all unauthenticated API access. The old `.json` endpoint trick no longer works. **OAuth authentication is mandatory.**

#### Issues Encountered
1. **reCAPTCHA dead loop during app registration**: The reCAPTCHA verification repeatedly reset when clicking "create app", preventing successful OAuth app creation. This appears to be a Reddit-side issue with the registration flow.
2. **403 on public endpoints**: Confirmed that unauthenticated access is fully blocked as of 2026.

#### Conclusion
Reddit API requires OAuth 2.0 authentication via a registered app. The free tier (100 req/min) is available for non-commercial use, but app registration must be completed (reCAPTCHA issue needs to be resolved, possibly by trying a different browser or time).

---

### GDELT API Test
**Date**: 2026-09-29
**Status**: ✅ Completed — ToneChart mode successful; ArtList rate-limited

#### What Was Tested
1. **ArtList mode** — fetch article list for keyword "Tesla"
2. **ToneChart mode** — fetch sentiment/tone distribution for keyword "Tesla"

#### Test Code
```python
import requests
import time

# GDELT requires min 5 seconds between requests
time.sleep(6)

url = "https://api.gdeltproject.org/api/v2/doc/doc"

# Test 1: ArtList mode
params_1 = {"query": "Tesla", "mode": "ArtList", "maxrecords": 5, "format": "json"}
resp_1 = requests.get(url, params=params_1, timeout=30)

# Test 2: ToneChart mode (with 6s delay before)
time.sleep(6)
params_2 = {"query": "Tesla", "mode": "ToneChart", "maxrecords": 5, "format": "json"}
resp_2 = requests.get(url, params=params_2, timeout=30)
```

#### Results

**ArtList Mode**:
- Status: `429 Too Many Requests` (9.61s response)
- Error: "Please limit requests to one every 5 seconds"
- Note: Rate limit triggered due to prior test requests; IP temporarily throttled

**ToneChart Mode**:
- Status: `200 OK` (24.86s response)
- Returns: `tonechart` array with sentiment bins
- Each bin contains: `bin` (tone score, negative = negative sentiment), `count` (number of articles), `toparts` (top articles in that bin)

#### Sample Response (ToneChart)
```json
{
  "tonechart": [
    {
      "bin": -18,
      "count": 1,
      "toparts": [
        {
          "url": "https://informer.rs/...",
          "title": "Saobracajna nesreca u Apatinu - Informer.rs"
        }
      ]
    },
    {
      "bin": -17,
      "count": 1,
      "toparts": [...]
    }
  ]
}
```

#### Key Findings
1. **Strict rate limit**: GDELT Doc API enforces 1 request per 5 seconds. High-volume users should use the BigQuery or ngrams dataset instead.
2. **Built-in sentiment**: ToneChart mode returns pre-computed sentiment bins, eliminating the need for a separate NLP model for news sentiment.
3. **Slow response**: ~25s per request due to rate limiting and server processing time. Not suitable for real-time applications.
4. **No API key required**: Completely free and open access.

#### Fields Available (ToneChart)
- `bin`: Tone/sentiment score (negative to positive scale)
- `count`: Number of articles in this sentiment bin
- `toparts`: Top articles with `url` and `title`

---

### Amazon Third-party API Test (Optional)
**Date**: Not tested
**Status**: ⬜ Not started — deferred to Phase 2

**Reason**: Amazon review data is planned for Phase 2 after the PoC validates the pipeline architecture. Third-party APIs (Canopy, ScrapeHero) require paid subscription or free trial signup, which is not necessary at this research stage.

---

## Summary Table

| API | Test Date | Status | Response Time | Key Finding |
|-----|-----------|--------|---------------|-------------|
| Reddit (public) | 2026-09-29 | ❌ 403 | 0.2s | Unauthenticated access fully blocked; OAuth required |
| Reddit (OAuth) | 2026-09-29 | ⚠️ Pending | N/A | reCAPTCHA registration issue |
| GDELT (ArtList) | 2026-09-29 | ⚠️ 429 | 9.6s | Rate limited (1 req/5s) |
| GDELT (ToneChart) | 2026-09-29 | ✅ 200 | 24.9s | Built-in sentiment data, free, no key |
| Amazon (3rd-party) | — | ⬜ Not tested | — | Deferred to Phase 2 |

## Test Environment
- **Python**: 3.14.7
- **Library**: requests 2.x
- **Location**: Los Angeles, CA
- **Date**: 2026-09-29
