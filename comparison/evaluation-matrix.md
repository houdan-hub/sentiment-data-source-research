# Data Source Evaluation Matrix

## Side-by-Side Comparison

| Dimension | Amazon (3rd-party API) | Reddit (Official API) | G2/Capterra (Scraping) | GDELT 2.0 (News) |
|-----------|------------------------|----------------------|------------------------|-------------------|
| **Accessibility** | ⭐⭐⭐ Medium (paid API needed for text) | ⭐⭐⭐⭐ High (free non-commercial) | ⭐⭐ Low (no free API) | ⭐⭐⭐⭐⭐ Very High (free unlimited) |
| **Scalability** | ⭐⭐⭐⭐ High (pay-per-call) | ⭐⭐⭐ Medium (100 req/min cap) | ⭐⭐⭐ Medium (pay-per-result) | ⭐⭐⭐⭐⭐ Very High (no limits) |
| **Update Frequency** | ⭐⭐⭐⭐ Near real-time | ⭐⭐⭐⭐⭐ Real-time | ⭐⭐ Slow (days/weeks) | ⭐⭐⭐⭐⭐ 15-min updates |
| **Data Quality** | ⭐⭐⭐⭐⭐ Excellent (structured) | ⭐⭐⭐⭐ Good (noisy but rich) | ⭐⭐⭐⭐⭐ Excellent (structured) | ⭐⭐⭐ Good (news text) |
| **Sentiment Relevance** | ⭐⭐⭐⭐⭐ Direct customer feedback | ⭐⭐⭐⭐ Authentic discussions | ⭐⭐⭐⭐ Direct B2B feedback | ⭐⭐ Media/brand perspective |
| **Long-term Maintainability** | ⭐⭐⭐ Medium (3rd-party dependency) | ⭐⭐⭐⭐ High (official API) | ⭐⭐ Low (scraping fragile) | ⭐⭐⭐⭐⭐ Very High (Google-backed) |
| **Startup Cost** | $ Low-Medium | $0 Free | $$ Medium | $0 Free |
| **Commercial Use** | ✅ Yes (paid) | ⚠️ Free = non-commercial only | ✅ Yes (paid) | ✅ Yes (free) |

## Overall Ranking

1. **Reddit** — Best balance for PoC: free, real-time, well-documented, high sentiment relevance
2. **Amazon (3rd-party)** — Highest sentiment relevance but requires paid API; great for Phase 2
3. **GDELT 2.0** — Best free source for macro-level brand sentiment; supplementary source
4. **G2/Capterra** — Excellent data quality but limited to B2B, low frequency, hard to access

## Recommendation

### Phase 1 (PoC): Reddit
- Free official API with mature Python SDK (PRAW)
- Real-time data with high volume
- Allows us to validate the full pipeline architecture (ingestion → cleaning → sentiment → storage → dashboard) at zero cost

### Phase 2: Amazon Reviews (via Canopy or ScrapeHero API)
- Add the highest-quality direct customer sentiment data
- Pay-per-call model is manageable once pipeline is validated
- Start with a few product categories, expand based on results

### Supplementary: GDELT 2.0
- Add macro-level brand/industry sentiment monitoring
- Completely free, no maintenance burden
- Provides context that customer reviews alone can't capture
