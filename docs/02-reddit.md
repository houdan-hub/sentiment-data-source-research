# Reddit API — Data Source Evaluation

## Overview
Reddit is a massive network of community forums (subreddits) where users discuss products, share experiences, ask questions, and express opinions. It captures authentic, unscripted customer sentiment in real-time.

## Access Method: Official Reddit API (via PRAW Python library)

### Setup
1. Create a Reddit account
2. Go to https://www.reddit.com/prefs/apps
3. Click "create another app..." → Select "script"
4. Fill in name, description, about URL, redirect URI (http://localhost:8080)
5. Note your `client_id` (under the app name) and `client_secret`

### Free Tier Limits
- **Rate limit**: 100 requests per minute per OAuth client ID
- **Usage**: Non-commercial, personal, academic use only
- **Authentication**: OAuth 2.0 required (no unauthenticated access)
- **Pagination**: Up to 100 items per listing response
- **Commercial use**: Requires enterprise agreement (contact Reddit)

### Python Quick Start (PRAW)
```python
import praw

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="sentiment_analysis_bot/1.0 by YOUR_USERNAME"
)

# Fetch latest posts from a subreddit
subreddit = reddit.subreddit("productreviews")
for post in subreddit.new(limit=10):
    print(f"Title: {post.title}")
    print(f"Score: {post.score}")
    print(f"Content: {post.selftext[:200]}")
    print("---")
```

## Testing Findings (2026-09-29)

### Critical: Unauthenticated Access Now Blocked
The old public `.json` endpoint trick (appending `.json` to any Reddit URL) **no longer works**. Testing confirmed:
- `GET https://www.reddit.com/r/technology/new.json` → **403 Forbidden** (0.23s)
- `GET https://www.reddit.com/search.json?q=...` → **403 Forbidden** (0.20s)

**Conclusion**: OAuth 2.0 authentication via a registered app is now mandatory. There is no unauthenticated access path.

### App Registration Issue
During testing, the reCAPTCHA verification on the app registration page entered a dead loop — verification would reset each time "create app" was clicked. This appears to be a Reddit-side issue. Workarounds:
- Try a different browser (Chrome → Edge/Firefox)
- Use incognito/private mode
- Disable ad blockers and VPN
- Try again at a different time

## Evaluation

| Dimension | Rating | Notes |
|-----------|--------|-------|
| **Accessibility** | ⭐⭐⭐ | Free for non-commercial, but OAuth registration required; reCAPTCHA issues reported |
| **Scalability** | ⭐⭐⭐ | 100 req/min cap; enterprise tier needed for large-scale |
| **Update Frequency** | ⭐⭐⭐⭐⭐ | Near real-time — new posts visible within seconds |
| **Data Quality** | ⭐⭐⭐⭐ | Rich discussion content, but has noise, trolls, and spam |
| **Sentiment Relevance** | ⭐⭐⭐⭐ | Authentic user discussions; requires filtering for relevant posts |
| **Long-term Maintainability** | ⭐⭐⭐⭐ | Official API is stable; policy tightened in 2023 but still reliable |

## Pros
- Free for non-commercial use (great for PoC)
- Real-time data with massive volume
- Mature Python ecosystem (PRAW library)
- Authentic, unscripted user opinions
- Wide coverage across all industries/topics

## Cons
- Free tier is non-commercial only (need enterprise for production)
- 100 req/min rate limit
- OAuth registration can be tricky (reCAPTCHA issues)
- No unauthenticated access as of 2026
- Data is noisy — requires filtering and relevance scoring
- Not all posts are product/customer-sentiment related

## References
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [PRAW Python Library](https://praw.readthedocs.io/)
- [Reddit API Rate Limits](https://support.reddithelp.com/hc/en-us/articles/16160319875092)
- [Developer Platform & Accessing Reddit Data](https://support.reddithelp.com/hc/en-us/articles/14945211791892)
