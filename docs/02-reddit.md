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

## Evaluation

| Dimension | Rating | Notes |
|-----------|--------|-------|
| **Accessibility** | ⭐⭐⭐⭐ | Free for non-commercial, well-documented, mature Python SDK |
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
- Data is noisy — requires filtering and relevance scoring
- Not all posts are product/customer-sentiment related

## References
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [PRAW Python Library](https://praw.readthedocs.io/)
- [Reddit API Rate Limits](https://support.reddithelp.com/hc/en-us/articles/16160319875092)
