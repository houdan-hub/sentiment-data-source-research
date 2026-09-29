# News APIs — Data Source Evaluation

## Overview
News APIs provide access to global news articles, which can be analyzed for sentiment related to brands, products, or industries. While news doesn't capture direct customer feedback, it provides macro-level public opinion and brand reputation signals.

## Access Methods

### Option 1: GDELT 2.0 (Recommended — Free & Unlimited)
- **Cost**: Completely free, commercial use allowed
- **Rate limits**: ⚠️ **Strict: 1 request per 5 seconds** (confirmed via testing 2026-09-29)
- **Update frequency**: Every 15 minutes
- **Coverage**: Global news in 100+ languages
- **Key features**: Event-level data, sentiment/tone scoring built-in, entity extraction
- **Access**: No API key needed, REST API or BigQuery
- **Response time**: ~25 seconds per request (due to rate limiting + server processing)

```python
# GDELT API example — fetch sentiment tone chart for a keyword
import requests
import time

# IMPORTANT: Wait at least 5 seconds between requests
time.sleep(6)

url = "https://api.gdeltproject.org/api/v2/doc/doc"
params = {
    "query": "Tesla",
    "mode": "ToneChart",  # Returns pre-computed sentiment bins
    "maxrecords": 5,
    "format": "json"
}
response = requests.get(url, params=params, timeout=30)
data = response.json()
# data["tonechart"] = array of {bin (sentiment score), count, toparts}
```

### Option 2: NewsData.io
- **Free tier**: 200 credits/day (10 articles per credit), 12-hour delay
- **Features**: Built-in sentiment analysis, 89 languages, AI entity extraction
- **Commercial use**: Allowed on free tier
- **Paid plans**: Start at ~$15/month

### Option 3: NewsAPI.org
- **Free tier**: 100 requests/day, 24-hour delay
- **Critical limitation**: Free tier cannot be used in production or staging environments
- **No built-in sentiment**: You need to run your own NLP

### Option 4: NewsAPI.ai
- **Free tier**: 2,000 free searches
- **Features**: Built-in sentiment analysis, video/link extraction
- **Limitation**: Only 30 days of historical data on free tier

## Testing Findings (2026-09-29)

### GDELT ToneChart Mode — ✅ Success
- **Status**: 200 OK
- **Response time**: 24.86 seconds
- **Returns**: `tonechart` array with sentiment bins
- **Each bin contains**: `bin` (tone score, negative = negative sentiment), `count` (article count), `toparts` (top articles with url/title)
- **Key benefit**: Pre-computed sentiment eliminates need for separate NLP model

### GDELT ArtList Mode — ⚠️ Rate Limited
- **Status**: 429 Too Many Requests
- **Error**: "Please limit requests to one every 5 seconds"
- **Cause**: IP temporarily throttled due to consecutive requests in testing
- **Lesson**: Must implement 5+ second delay between all GDELT API calls

### Practical Implications
- GDELT is **not suitable for real-time** applications due to 5s rate limit and ~25s response
- Best for **batch processing** and **daily/hourly aggregation**
- For higher volume, use GDELT BigQuery dataset or ngrams dataset
- ToneChart mode is excellent for **macro brand sentiment tracking**

## Evaluation (GDELT-focused)

| Dimension | Rating | Notes |
|-----------|--------|-------|
| **Accessibility** | ⭐⭐⭐⭐⭐ | GDELT is completely free, no API key, but strict 5s rate limit |
| **Scalability** | ⭐⭐⭐ | REST API limited to 1 req/5s; use BigQuery for large scale |
| **Update Frequency** | ⭐⭐⭐⭐⭐ | 15-minute updates — near real-time for news |
| **Data Quality** | ⭐⭐⭐ | News text is high quality, but not direct customer feedback |
| **Sentiment Relevance** | ⭐⭐ | Media perspective, not customer voice; better for brand reputation |
| **Long-term Maintainability** | ⭐⭐⭐⭐⭐ | Backed by Google, very stable, exists since 2013 |

## Pros
- GDELT is 100% free with no API key required
- Built-in sentiment/tone scoring via ToneChart mode
- Global coverage across all industries and languages
- Extremely stable and well-maintained (Google-backed)
- 15-minute update frequency

## Cons
- **Strict rate limit**: 1 request per 5 seconds (not "unlimited" as commonly claimed)
- **Slow response**: ~25s per request, not suitable for real-time
- News is media perspective, NOT direct customer sentiment
- Requires filtering to find relevant articles
- Sentiment is about events/brands, not about specific product experiences
- Many news APIs have restrictive free tiers (except GDELT)

## References
- [GDELT Project](https://www.gdeltproject.org/)
- [GDELT API Documentation](https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/)
- [GDELT BigQuery Dataset](https://cloud.google.com/blog/products/gcp/google-bigquery-public-datasets-now-include-gdelt)
- [NewsData.io](https://newsdata.io/)
- [NewsAPI.org](https://newsapi.org/)
