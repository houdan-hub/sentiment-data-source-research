# News APIs — Data Source Evaluation

## Overview
News APIs provide access to global news articles, which can be analyzed for sentiment related to brands, products, or industries. While news doesn't capture direct customer feedback, it provides macro-level舆论 (public opinion) and brand reputation signals.

## Access Methods

### Option 1: GDELT 2.0 (⭐ Recommended — Free & Unlimited)
- **Cost**: Completely free, commercial use allowed
- **Rate limits**: None
- **Update frequency**: Every 15 minutes
- **Coverage**: Global news in 100+ languages
- **Key features**: Event-level data, sentiment/tone scoring built-in, entity extraction
- **Access**: No API key needed, REST API or BigQuery

# GDELT API example — fetch events mentioning a keyword
import requests
url = "https://api.gdeltproject.org/api/v2/doc/doc"
params = {
    "query": "Tesla",
    "mode": "ArtList",
    "maxrecords": 10,
    "format": "json"
}
response = requests.get(url, params=params)
data = response.json()

### Option 2: NewsData.io
Free tier: 200 credits/day (10 articles per credit), 12-hour delay
Features: Built-in sentiment analysis, 89 languages, AI entity extraction
Commercial use: Allowed on free tier
Paid plans: Start at ~$15/month

### Option 3: NewsAPI.org
Free tier: 100 requests/day, 24-hour delay
# Critical limitation: Free tier cannot be used in production or staging environments
No built-in sentiment: You need to run your own NLP

### Option 4: NewsAPI.ai
Free tier: 2,000 free searches
Features: Built-in sentiment analysis, video/link extraction
Limitation: Only 30 days of historical data on free tier

## Evaluation (GDELT-focused)
Dimension	     Rating	          Notes
Accessibility	⭐⭐⭐⭐⭐	  GDELT is completely free, no API key, no rate limits
Scalability	    ⭐⭐⭐⭐⭐	  Unlimited access, designed for large-scale analysis
Update Frequency⭐⭐⭐⭐⭐     15-minute updates — near real-time for news
Data Quality	⭐⭐⭐	         News text is high quality, but not direct customer feedback
Sentiment Relevance	⭐⭐	     Media perspective, not customer voice; better for brand reputation than product sentiment
Long-term Maintainability	⭐⭐⭐⭐⭐	Backed by Google, very stable, exists since 2013

## Pros
GDELT is 100% free with no limits (best free data source in this list)
Near real-time updates (15 min)
Built-in sentiment/tone scoring (GDELT)
Global coverage across all industries
Extremely stable and well-maintained

## Cons
News is media perspective, NOT direct customer sentiment
Requires filtering to find relevant articles
Sentiment is about events/brands, not about specific product experiences
Many news APIs have restrictive free tiers (except GDELT)

## References
GDELT Project
GDELT API Documentation
NewsData.io
NewsAPI.org

