# Amazon User Reviews — Data Source Evaluation

## Overview
Amazon product reviews are one of the richest sources of direct customer sentiment. Each review contains a star rating, review title, review text, timestamp, and verified purchase status.

## Access Methods

### Option 1: Amazon Product Advertising API (PA API) — Official
- **What you get**: Star ratings, review count, review summary
- **Critical Limitation**: The official PA API does **NOT** return the actual review text. You can only get aggregate ratings and links to the review page.
- **Requirements**: Amazon Associates account, AWS credentials
- **Rate limits**: 1 request/second, ~5000 requests/day (basic tier)
- **Cost**: Free, but requires affiliate account approval

### Option 2: Third-party APIs (Recommended for actual review text)
| Provider | Free Tier | Pricing | Notes |
|----------------|--------------------|---------------|-------------------------------------------|
| **Canopy API** | 100 requests/month | $0.01/request | REST + GraphQL, real-time, 350M+ products |
| **ScrapeHero** | Limited free trial | Pay-per-result | Focuses exclusively on reviews & ratings |
| **EasyParser** | Free trial available | Subscription-based | Structured review data with images |

### Option 3: Custom Web Scraping
- **What you get**: Full review data, no per-request cost
- **Risks**: Amazon has aggressive anti-bot measures (CAPTCHA, IP blocking), legal ToS concerns, high maintenance cost as Amazon changes page layout

## Evaluation

| Dimension | Rating | Notes |
|-----------|--------|-------|
| **Accessibility** | ⭐⭐⭐ | Official API can't get text; third-party APIs cost money; scraping is risky |
| **Scalability** | ⭐⭐⭐⭐ | Third-party APIs scale well, but cost grows linearly with volume |
| **Update Frequency** | ⭐⭐⭐⭐ | Near real-time via third-party APIs |
| **Data Quality** | ⭐⭐⭐⭐⭐ | Highly structured: star rating + title + text + verified purchase + timestamp |
| **Sentiment Relevance** | ⭐⭐⭐⭐⭐ | Reviews ARE direct customer sentiment — gold standard |
| **Long-term Maintainability** | ⭐⭐⭐ | Dependent on third-party providers; Amazon may change policies |

## Pros
- Highest direct customer sentiment relevance
- Rich structured data (rating + text + metadata)
- Massive volume across all product categories

## Cons
- Official API doesn't expose review text (major gotcha)
- Third-party APIs have ongoing costs
- Custom scraping is legally risky and high-maintenance

## References
- [Amazon PA API Documentation](https://affiliate-program.amazon.com/help/node/topic/G200650630)
- [Canopy API](https://www.canopyapi.co/)
- [ScrapeHero Amazon Reviews API](https://www.scrapehero.com/store/amazon-reviews-and-ratings-api/)
