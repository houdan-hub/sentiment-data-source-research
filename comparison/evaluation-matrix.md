# Data Source Evaluation Matrix

## Side-by-Side Comparison

| Dimension | Amazon (3rd-party API) | Reddit (Official API) | G2/Capterra (Scraping) | GDELT 2.0 (News) |
|-----------|------------------------|----------------------|------------------------|-------------------|
| **Accessibility** | ⭐⭐⭐ Medium (paid API needed for text) | ⭐⭐ **Low** (manual application required; self-service disabled in 2026) | ⭐⭐ Low (no free API) | ⭐⭐⭐⭐⭐ Very High (free, no key, but 5s rate limit) |
| **Scalability** | ⭐⭐⭐⭐ High (pay-per-call) | ⭐⭐⭐ Medium (100 req/min upon approval) | ⭐⭐⭐ Medium (pay-per-result) | ⭐⭐⭐ Low (1 req/5s via REST; BigQuery for scale) |
| **Update Frequency** | ⭐⭐⭐⭐ Near real-time | ⭐⭐⭐⭐⭐ Real-time | ⭐⭐ Slow (days/weeks) | ⭐⭐⭐⭐⭐ 15-min updates |
| **Data Quality** | ⭐⭐⭐⭐⭐ Excellent (structured) | ⭐⭐⭐⭐ Good (noisy but rich) | ⭐⭐⭐⭐⭐ Excellent (structured) | ⭐⭐⭐ Good (news text) |
| **Sentiment Relevance** | ⭐⭐⭐⭐⭐ Direct customer feedback | ⭐⭐⭐⭐ Authentic discussions | ⭐⭐⭐⭐ Direct B2B feedback | ⭐⭐ Media/brand perspective |
| **Long-term Maintainability** | ⭐⭐⭐ Medium (3rd-party dependency) | ⭐⭐⭐ **Medium-Low** (policy changes frequently; approval uncertain) | ⭐⭐ Low (scraping fragile) | ⭐⭐⭐⭐⭐ Very High (Google-backed) |
| **Startup Cost** | $ Low-Medium | $0 Free (upon approval) | $$ Medium | $0 Free |
| **Commercial Use** | ✅ Yes (paid) | ⚠️ Requires enterprise agreement | ✅ Yes (paid) | ✅ Yes (free) |
| **Time to First Data** | Days (signup + trial) | **Weeks** (manual review) | Days (signup + scraping) | **Minutes** (works immediately) |

## Key Risk: Reddit Onboarding Barrier
As of 2026, Reddit no longer allows self-service creation of script-type developer apps. New accounts must submit a manual API request ticket and wait for review (days to weeks, no SLA, approval not guaranteed). This is a significant risk for the PoC timeline.

## Overall Ranking (adjusted for 2026 policy)

1. **GDELT 2.0** — Immediately usable, free, no approval needed, built-in sentiment. Best for rapid PoC despite slow rate limits.
2. **Amazon (3rd-party)** — Highest sentiment relevance; signup is straightforward (free trial available). Great Phase 1+ option.
3. **Reddit** — Best data quality and relevance, but onboarding barrier is high. Submit application now; can use immediately once approved.
4. **G2/Capterra** — Excellent data quality but limited to B2B, low frequency, scraping-dependent.

## Recommendation (Revised 2026-09-29)

### Immediate Start: GDELT 2.0 + Amazon Reviews
- **GDELT** is ready to use right now — no signup, no approval, works immediately
- **Amazon reviews** via Canopy API (free 100 req/month) can be set up in minutes
- This lets us start the PoC immediately without waiting for Reddit approval

### Parallel Track: Reddit Application
- Submit the Reddit developer API request ticket now
- Once approved (days to weeks), add Reddit as the primary high-volume source
- Reddit remains the long-term best source for authentic customer sentiment

### Phase 2: Expand to Amazon at Scale
- Move from free trial to paid Canopy/ScrapeHero API
- Add more product categories and monitoring
