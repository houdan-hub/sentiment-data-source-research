# Sentiment Analysis Pipeline — Data Source Research
Research and evaluation of live data sources for sentiment analysis pipeline

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
1. Reddit (Official API) 普通网友对某款消费电子产品的看法
2. Amazon Reviews (Third-party APIs) 消费者买完实物商品后的真实体验
3. GDELT 2.0 (Global News) 全球新闻媒体对某个公司的报道倾向
4. G2 / Capterra (B2B Software Reviews) 企业客户对一款 SaaS 软件的满意度

## Recommendation
**Start with Reddit for the initial PoC, with Amazon reviews as a Phase 2 addition.**

See [`comparison/evaluation-matrix.md`](comparison/evaluation-matrix.md) for the full comparison.

## Repository Structure
├── README.md          
├── docs/              
│   ├── 01-amazon-reviews.md
│   ├── 02-reddit.md
│   ├── 03-g2-capterra.md
│   └── 04-news-apis.md
├── comparison/        
│   └── evaluation-matrix.md
└── tests/            
    └── api-test-results.md
