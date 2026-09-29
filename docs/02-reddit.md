# Reddit API — Data Source Evaluation

## Overview
Reddit is a massive network of community forums (subreddits) where users discuss products, share experiences, ask questions, and express opinions. It captures authentic, unscripted customer sentiment in real-time.

## ⚠️ Critical: Reddit Responsible Builder Policy Update (2026)

As of 2026, Reddit has significantly changed its API access policy. The old self-service app creation flow at `reddit.com/prefs/apps` is effectively **disabled for new accounts**. When attempting to create a script-type app:
- The reCAPTCHA verification silently resets on submit
- No error message, no confirmation — the button simply does nothing

This is **not a browser bug or IP issue**. It is a deliberate policy change. New developers must now submit a **manual application ticket** for API access, with no guaranteed approval or turnaround time.

### Application Paths
| Use Case | Ticket Form |
|----------|-------------|
| Non-commercial app development (our PoC) | [Developer API Request](https://support.reddithelp.com/hc/en-us/requests/new?ticket_form_id=14868593862164&tf_42139884615700=api_request_type_developer_clone) |
| Commercial use | [Enterprise API Request](https://support.reddithelp.com/hc/en-us/requests/new?ticket_form_id=14868593862164&tf_42139884615700=api_request_type_enterprise_clone) |
| Academic research | [RFR Program Application](https://support.reddithelp.com/hc/en-us/requests/new?ticket_form_id=14868593862164&tf_42139884615700=api_request_type_researcher_clone) |

### Key Policy Restrictions
- **Approval required before any API access** — no instant credentials
- **No data retention beyond immediate project needs** (researchers)
- **No AI model training** on Reddit data without explicit approval
- **No commercialization** without enterprise agreement
- **Transparency required** — no multiple accounts or duplicate applications
- Rate limits still apply (100 req/min for approved apps)

## Access Method: Official Reddit API (via PRAW Python library)

### Current Setup Process (2026)
1. Create a Reddit account
2. Submit a developer API request ticket at the link above
3. Wait for manual review (days to weeks, no SLA)
4. Upon approval, receive `client_id` and `client_secret`
5. Use PRAW library to authenticate

### Free Tier Limits (upon approval)
- **Rate limit**: 100 requests per minute per OAuth client ID
- **Usage**: Non-commercial, personal use only
- **Authentication**: OAuth 2.0 required
- **Commercial use**: Requires enterprise agreement

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

### Unauthenticated Access Blocked
- `GET https://www.reddit.com/r/technology/new.json` → **403 Forbidden** (0.23s)
- `GET https://www.reddit.com/search.json?q=...` → **403 Forbidden** (0.20s)
- **Conclusion**: OAuth authentication is mandatory. No unauthenticated path exists.

### Self-service App Creation Disabled
- reCAPTCHA resets silently on "create app" click at `/prefs/apps`
- Confirmed as policy change, not a technical glitch
- Manual ticket submission is now the only path

## Evaluation

| Dimension | Rating | Notes |
|-----------|--------|-------|
| **Accessibility** | ⭐⭐ | Free upon approval, but self-service signup disabled; manual review with unknown turnaround |
| **Scalability** | ⭐⭐⭐ | 100 req/min cap upon approval; enterprise tier for scale |
| **Update Frequency** | ⭐⭐⭐⭐⭐ | Near real-time — new posts visible within seconds |
| **Data Quality** | ⭐⭐⭐⭐ | Rich discussion content, but has noise, trolls, and spam |
| **Sentiment Relevance** | ⭐⭐⭐⭐ | Authentic user discussions; requires filtering for relevant posts |
| **Long-term Maintainability** | ⭐⭐⭐ | Official API exists but policy changes frequently; approval not guaranteed |

## Pros
- Real-time data with massive volume upon approval
- Mature Python ecosystem (PRAW library)
- Authentic, unscripted user opinions
- Wide coverage across all industries/topics
- Free for approved non-commercial use

## Cons
- **High onboarding barrier**: Manual application required, no self-service
- **Approval not guaranteed**, turnaround time unknown (days to weeks)
- Free tier is non-commercial only
- 100 req/min rate limit
- No unauthenticated access as of 2026
- No AI model training permitted
- Data is noisy — requires filtering
- Policy has changed repeatedly since 2023

## References
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [PRAW Python Library](https://praw.readthedocs.io/)
- [Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/26410290525844)
- [Developer Platform & Accessing Reddit Data](https://support.reddithelp.com/hc/en-us/articles/14945211791892)
- [Developer API Request Form](https://support.reddithelp.com/hc/en-us/requests/new?ticket_form_id=14868593862164&tf_42139884615700=api_request_type_developer_clone)
