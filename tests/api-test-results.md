# API Test Results

> Tested on 2026-09-29 using Python requests library. All tests run from local machine in Los Angeles, CA.

## Test Log

---

### Reddit API Test
**Date**: 2026-09-29
**Status**: ⚠️ Blocked by platform policy — manual application submitted

#### What Was Tested
1. **Public JSON endpoint** (`https://www.reddit.com/r/{subreddit}/new.json`) — no authentication
2. **Public search endpoint** (`https://www.reddit.com/search.json`) — no authentication
3. **Self-service app registration** at https://www.reddit.com/prefs/apps

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
- **Self-service app creation**: reCAPTCHA silently resets on submit

#### Root Cause Identified
Reddit's **Responsible Builder Policy** (2026 update) has disabled self-service script app creation for new accounts. This is not a browser or IP issue — it is a deliberate platform policy change. New developers must now submit a manual ticket for API access:
- Developer (non-commercial): https://support.reddithelp.com/hc/en-us/requests/new?ticket_form_id=14868593862164&tf_42139884615700=api_request_type_developer_clone
- Approval is not guaranteed; turnaround time is unknown (days to weeks)

#### Current Status
- Developer API request ticket has been submitted
- Waiting for Reddit platform review
- Full authenticated API testing is blocked until approval
- Unauthenticated public endpoints return 403

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

**ToneChart Mode**:
- Status: `200 OK` (24.86s response)
- Returns: `tonechart` array with sentiment bins (bin score, count, top articles)

#### Key Findings
1. **Strict rate limit**: 1 request per 5 seconds
2. **Built-in sentiment**: ToneChart returns pre-computed sentiment bins
3. **Slow response**: ~25s per request; not suitable for real-time
4. **No API key required**: Completely free

---

### Amazon Third-party API Test (Optional)
**Date**: Not tested
**Status**: ⬜ Not started — deferred to Phase 2

---

## Summary Table

| API | Test Date | Status | Response Time | Key Finding |
|-----|-----------|--------|---------------|-------------|
| Reddit (public) | 2026-09-29 | ❌ 403 | 0.2s | Unauthenticated access fully blocked |
| Reddit (OAuth) | 2026-09-29 | ⏳ Pending | N/A | Manual application submitted; awaiting review |
| GDELT (ArtList) | 2026-09-29 | ⚠️ 429 | 9.6s | Rate limited (1 req/5s) |
| GDELT (ToneChart) | 2026-09-29 | ✅ 200 | 24.9s | Built-in sentiment data, free, no key |
| Amazon (3rd-party) | — | ⬜ Not tested | — | Deferred to Phase 2 |

## Test Environment
- **Python**: 3.14.7
- **Library**: requests 2.x
- **Location**: Los Angeles, CA
- **Date**: 2026-09-29
