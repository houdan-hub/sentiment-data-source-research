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

## Recommendation (Updated 2026-09-29)
**Start immediately with GDELT 2.0 (no signup needed) + Amazon reviews via Canopy API (free trial). Submit Reddit developer application in parallel; add Reddit as soon as approved.**

Reddit remains the best long-term source for authentic customer sentiment, but as of 2026 Reddit requires manual API approval (days to weeks, no SLA). We should not block the PoC on this.

See [`comparison/evaluation-matrix.md`](comparison/evaluation-matrix.md) for the full comparison.

## Key Testing Findings (2026-09-29)
- **Reddit**: Self-service app creation is disabled under the Responsible Builder Policy. Public endpoints return 403. Manual API request ticket submitted; awaiting review.
- **GDELT**: ToneChart mode works immediately, returns built-in sentiment bins. Strict rate limit: 1 request/5 seconds, ~25s response. No API key needed.
- Full test details: [`tests/api-test-results.md`](tests/api-test-results.md)

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
