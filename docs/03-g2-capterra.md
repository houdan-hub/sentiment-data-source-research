# G2 / Capterra — Data Source Evaluation

## Overview
G2 and Capterra are the leading B2B software review platforms. They host structured, verified reviews of business software products, with detailed pros/cons, ratings by category, reviewer role, company size, and usage duration.

### Important Update (Feb 2026)
G2 acquired Capterra, GetApp, and Software Advice from Gartner for $110M. All four major B2B review platforms are now under G2's umbrella.

## Access Method

### No Official Free API
- G2 does not offer a public, free API for review data
- G2's official data products are enterprise-focused (Buyer Intent, Market Reports)
- Capterra (now part of G2) similarly has no free public API

### Option 1: Third-party Scraping Services (Apify, etc.)
| Service | What it provides | Pricing Model |
|---------|-----------------|---------------|
| **Apify G2 Reviews Scraper** | 41 fields per review: rating, pros, cons, NPS, reviewer role, company size, region | Pay per result |
| **Apify Software Reviews Scraper** | Unified data across G2, Capterra, TrustRadius, GetApp | Pay per result |
| **Outscraper** | Reviews from G2, Trustpilot, Glassdoor, Yelp | Pay per result |

### Option 2: Custom Web Scraping
- G2 uses Cloudflare + DataDome anti-bot protection
- High technical barrier, high maintenance cost
- Not recommended for a PoC

## Evaluation

| Dimension | Rating | Notes |
|-----------|--------|-------|
| **Accessibility** | ⭐⭐ | No free API; requires paid third-party scraping services |
| **Scalability** | ⭐⭐⭐ | Pay-per-result model scales, but costs add up |
| **Update Frequency** | ⭐⭐ | B2B reviews are posted infrequently (days/weeks between new reviews per product) |
| **Data Quality** | ⭐⭐⭐⭐⭐ | Highly structured: pros/cons separated, category ratings, reviewer demographics |
| **Sentiment Relevance** | ⭐⭐⭐⭐ | Direct product feedback, but only covers B2B software |
| **Long-term Maintainability** | ⭐⭐ | Dependent on scraping; website changes can break integrations |

## Pros
- Extremely high data quality and structure
- Pros/cons are explicitly separated (great for aspect-based sentiment)
- Reviewer context (role, company size, usage duration) adds depth
- Verified reviews reduce fake content

## Cons
- No free official API
- Only covers B2B software (not general consumer products)
- Low update frequency — not "live" data
- Scraping dependencies are fragile and costly
- G2 consolidation may lead to policy changes

## References
- [G2 Official Site](https://www.g2.com/)
- [Apify G2 Reviews Scraper](https://apify.com/zhorex/g2-reviews-scraper)
- [G2 acquires Capterra (Feb 2026)](https://toolradar.com/blog/software-comparison-website)
