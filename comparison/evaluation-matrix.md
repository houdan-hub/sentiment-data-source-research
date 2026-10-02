# Data Source Evaluation Matrix

## Side-by-Side Comparison

| Dimension | Google Play Reviews | GDELT 2.0 (News) | Amazon (Canopy) | Reddit |
|-----------|---------------------|-------------------|-----------------|--------|
| **Accessibility** | ⭐⭐⭐⭐⭐ Free, no key, pip install | ⭐⭐⭐⭐⭐ Free, no key | ⭐⭐⭐ Free 100/mo | ⭐⭐ Denied |
| **Scalability** | ⭐⭐⭐⭐ Pagination, no hard quota | ⭐⭐⭐ 1 req/5s | ⭐⭐⭐ 100/mo free | N/A |
| **Update Frequency** | ⭐⭐⭐⭐⭐ Real-time (newest) | ⭐⭐⭐⭐⭐ 15-min | ⭐⭐⭐⭐ Near real-time | N/A |
| **Data Quality** | ⭐⭐⭐⭐⭐ Structured: rating+text+time+version | ⭐⭐⭐ News text | ⭐⭐⭐⭐⭐ Structured | N/A |
| **Sentiment Relevance** | ⭐⭐⭐⭐⭐ Direct customer reviews | ⭐⭐ Media perspective | ⭐⭐⭐⭐⭐ Direct customer feedback | N/A |
| **Long-term Maintainability** | ⭐⭐⭐ Scraper may break on UI changes | ⭐⭐⭐⭐⭐ Google-backed | ⭐⭐⭐ 3rd-party dependency | N/A |
| **Cost** | $0 | $0 | $0.01/review after free tier | N/A |
| **Time to First Data** | **Minutes** | Minutes | Days (signup) | N/A |

## Current Ranking

1. **Google Play Reviews** — Free, unlimited, structured customer feedback, real-time, no signup. Best fit for sentiment analysis pipeline.
2. **GDELT 2.0** — Good supplementary source for macro news sentiment, but not direct customer feedback.
3. **Amazon (Canopy)** — High quality but limited free tier; revisit later.
4. **Reddit** — Unavailable (application rejected).

## Recommendation (Updated 2026-10-02)

### Primary Source: Google Play Reviews
- Free open-source library (`google-play-scraper`), no API key, no quota
- Direct customer reviews with star ratings and text
- Real-time access to newest reviews
- Multi-app coverage across categories
- Start with a focused feasibility test on 3-4 sample apps

### Supplementary: GDELT
- Keep as secondary source for macro brand/news sentiment
- Not a replacement for customer feedback

### Deferred
- Amazon Canopy: free tier too limited; revisit when pipeline validates
- Reddit: denied by policy; not pursuing
