# product-review-analyzer
# 🧠 Product Review Sentiment Analyzer

A simple Python-based command-line tool that analyzes the sentiment of product reviews using natural language processing (NLP). Built to simulate a basic Amazon-style review analyzer.

---

## 🚀 Features

- Accepts text input (customer product reviews)
- Uses **TextBlob** to calculate sentiment polarity
- Classifies sentiment as:
  - ✅ Positive
  - ⚠️ Neutral
  - ❌ Negative
- Works with Python 2 or Python 3

---

## 📦 Requirements

- Python 2.7+ or Python 3.x
- [TextBlob](https://textblob.readthedocs.io/en/dev/)

Install dependencies:

```bash
pip install textblob
python -m textblob.download_corpora
