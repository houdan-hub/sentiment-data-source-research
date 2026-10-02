# Google Play Reviews — Data Source Evaluation

## Overview
Google Play hosts reviews for millions of Android apps. Each review includes a star rating, review text, timestamp, app version, thumbs-up count, and developer reply. This is direct, structured customer feedback for mobile apps — highly relevant for sentiment analysis.

## Access Method: google-play-scraper (Python library)

### What it is
`google-play-scraper` is a free, open-source Python library that crawls the Google Play Store. No API key, no registration, no paid tier.

- **GitHub**: https://github.com/JoMingyu/google-play-scraper
- **PyPI**: `pip install google-play-scraper`
- **License**: Unlicense (public domain)

### Key Features
- Fetch reviews by app ID (package name)
- Sort by: Newest, Most Relevant, Highest Rating, Lowest Rating
- Filter by score (1-5 stars)
- Pagination via continuation token (up to 200 reviews per page)
- Support for language and country filtering
- Fetch all reviews (reviews_all) for historical backfill
- Also fetches app metadata: ratings, installs, developer info, histograms

### Review Data Fields
| Field | Type | Description |
|-------|------|-------------|
| `reviewId` | string | Unique review identifier |
| `userName` | string | Reviewer username |
| `userImage` | string | Reviewer avatar URL |
| `content` | string | Review text (the main sentiment data) |
| `score` | integer | Star rating 1-5 |
| `thumbsUpCount` | integer | Number of helpful votes |
| `reviewCreatedVersion` | string | App version when review was written |
| `at` | datetime | Review timestamp |
| `replyContent` | string | Developer response (if any) |
| `repliedAt` | datetime | Developer response timestamp |
| `appVersion` | string | Current app version |

### Python Quick Start
```python
from google_play_scraper import Sort, reviews

result, continuation_token = reviews(
    'com.whatsapp',          # App package name
    lang='en',                # Language
    country='us',             # Country
    sort=Sort.NEWEST,         # Sort order
    count=50,                 # Number of reviews (max 200 per page)
)

for review in result:
    print(f"[{review.score}★] {review.userName}: {review.content[:100]}")
    print(f"  Date: {review.at}, Version: {review.reviewCreatedVersion}")
    print(f"  Helpful: {review.thumbsUpCount}")
    if review.replyContent:
        print(f"  Developer replied: {review.replyContent[:80]}")
    print()

# Fetch next page
result, continuation_token = reviews(
    'com.whatsapp',
    continuation_token=continuation_token
)
```

### Sample Review (from official docs)
```python
{
    'reviewId': '793226de-e6cf-439f-8ea8-ea6b1f6afc9e',
    'userName': 'LiviaBrannock',
    'content': "The graphics are just the cutest, this game always makes me smile...",
    'score': 5,
    'thumbsUpCount': 239,
    'reviewCreatedVersion': '1.32.0',
    'at': datetime(2021, 3, 25, 15, 52, 53),
    'replyContent': None,
    'repliedAt': None,
    'appVersion': '1.32.0'
}
```

## Evaluation

| Dimension | Rating | Notes |
|-----------|--------|-------|
| **Accessibility** | ⭐⭐⭐⭐⭐ | Free open-source library, no API key, no registration, no quotas |
| **Scalability** | ⭐⭐⭐⭐ | Pagination supports large volumes; ~200 reviews per request; rate limit needed to avoid blocking |
| **Update Frequency** | ⭐⭐⭐⭐⭐ | Near real-time — fetch newest reviews on demand |
| **Data Quality** | ⭐⭐⭐⭐⭐ | Highly structured: rating + text + timestamp + version + helpful votes + dev replies |
| **Sentiment Relevance** | ⭐⭐⭐⭐⭐ | Direct customer feedback — the gold standard for product sentiment |
| **Long-term Maintainability** | ⭐⭐⭐ | Third-party scraper; Google Play UI changes could break it, but library is actively maintained |
| **Cost** | $0 | Completely free |
| **Commercial Use** | ⚠️ | Scraper is public domain, but scraping Google Play may violate their ToS; acceptable for research/prototype |

## Pros
- **Free and unlimited** — no 100/month limit like Canopy, no API key needed
- **Direct customer feedback** — actual user reviews with star ratings, not media/news
- **Rich structured data** — score, text, timestamp, app version, helpful votes, developer replies
- **Real-time** — sort by newest, can poll for fresh reviews
- **Multi-app coverage** — millions of apps across all categories
- **Active library** — well-maintained, good documentation
- **No rate limit officially** — but should add delays to avoid IP blocking

## Cons
- **ToS risk** — scraping Google Play is technically against their Terms of Service (common for research/prototype use)
- **Fragile** — Google Play page structure changes could break the scraper
- **No official API** — this is an unofficial scraper, not a Google-endorsed data source
- **Only Android** — no iOS App Store reviews
- **Rate limiting** — aggressive crawling may get IP blocked; need sleep between requests
- **Data retention** — no guarantee of long-term availability

## Comparison with Other Sources

| | Google Play Reviews | GDELT | Canopy (Amazon) |
|---|---|---|---|
| Data type | Customer reviews | News articles | Customer reviews |
| Cost | Free | Free | $0.01/review |
| Volume limit | Unlimited (with delays) | 1 req/5s | 100/month free |
| Structured sentiment | ★ Rating + text | Pre-computed tone | ★ Rating + text |
| Real-time | Yes | 15-min delay | Yes |
| Direct feedback | Yes (users) | No (media) | Yes (customers) |
| Setup effort | pip install | pip install | Sign up + API key |

## References
- [google-play-scraper on GitHub](https://github.com/JoMingyu/google-play-scraper)
- [Google Play Store](https://play.google.com)
