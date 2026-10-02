# Sentiment Analysis Pipeline — Data Source Research

> Research and evaluation of live data sources for sentiment analysis pipeline

## Background
This repository documents the research, evaluation, and testing of potential live data sources to support the sentiment analysis pipeline at Sciencia AI.

## Shortlisted Sources
1. **Google Play Reviews (google-play-scraper)** — Direct, structured customer reviews with ratings, text, timestamps
2. **GDELT 2.0 (Global News)** — Macro-level news sentiment with built-in tone scoring
3. **Amazon Reviews (Canopy API)** — Structured product reviews, but limited free tier
4. **Reddit** — Application denied; unavailable per Responsible Builder Policy

## Recommendation (Updated 2026-10-02)
**Primary source: Google Play Reviews** — free, no API key, no quota, direct customer feedback with ratings and text. Multi-app feasibility test, pagination, and repeated collection all verified.

**Supplementary: GDELT** for macro news sentiment (not customer feedback).

See [`comparison/evaluation-matrix.md`](comparison/evaluation-matrix.md) for the full comparison.

## Repository Structure
```
.
├── README.md
├── docs/
│   ├── 01-amazon-reviews.md
│   ├── 02-reddit.md
│   ├── 03-g2-capterra.md
│   ├── 04-news-apis.md
│   └── 05-google-play-reviews.md
├── comparison/
│   └── evaluation-matrix.md
└── tests/
    ├── api-test-results.md
    ├── test_gplay_reviews.py
    └── gplay_test_output.json
```

## Progress
- [x] Research on all candidate data sources
- [x] GDELT API tested and documented
- [x] Reddit application attempted and rejected
- [x] Google Play reviews feasibility test completed (multi-app, pagination, repeated collection)
- [x] All test results and evidence documented in this repo
- [x] Recommendation finalized
