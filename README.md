# Sentiment Analysis Pipeline — Data Source Research

> Research and evaluation of live data sources for sentiment analysis pipeline

## Background
This repository documents the research, evaluation, and testing of potential live data sources to support the sentiment analysis pipeline at Sciencia AI.

The goal is to identify the most suitable data source(s) for capturing real-time customer sentiment, with consideration for accessibility, cost, scalability, and long-term maintainability.

## Objective
Evaluate potential live data sources across the following dimensions:
- **Accessibility** — How easy is it to get access? Free tier? API key required?
- **Scalability** — Can it handle increasing data volume as the pipeline grows?
- **Update Frequency** — How fresh is the data? Real-time / hourly / daily?
- **Data Quality** — Is the data structured? Clean? Relevant?
- **Sentiment Relevance** — Does the data directly reflect customer sentiment?
- **Long-term Maintainability** — Is the source stable? Likely to exist in 1-2 years?

## Shortlisted Sources
1. **Reddit (Official API)** — Real-time user discussions and opinions across all product categories
2. **Amazon Reviews (Third-party APIs)** — Structured customer reviews with verified purchase status
3. **GDELT 2.0 (Global News)** — Macro-level news sentiment and brand reputation signals
4. **G2 / Capterra (B2B Software Reviews)** — High-quality structured B2B software reviews

## Recommendation
**Start with Reddit for the initial PoC, with Amazon reviews as a Phase 2 addition.**

See [`comparison/evaluation-matrix.md`](comparison/evaluation-matrix.md) for the full comparison.

## Repository Structure
```
.
├── README.md                          # This file — overview & recommendation
├── docs/
│   ├── 01-amazon-reviews.md           # Amazon reviews deep-dive
│   ├── 02-reddit.md                   # Reddit API deep-dive
│   ├── 03-g2-capterra.md              # G2/Capterra deep-dive
│   └── 04-news-apis.md                # News APIs (GDELT etc.) deep-dive
├── comparison/
│   └── evaluation-matrix.md           # Side-by-side comparison table
└── tests/
    └── api-test-results.md            # Actual API test code & results
```

## Progress
- [x] Repository setup & research framework
- [x] Documentation for all 4 candidate data sources
- [x] Evaluation matrix & recommendation
- [ ] Reddit API testing
- [ ] GDELT API testing
- [ ] Final review & email to John
