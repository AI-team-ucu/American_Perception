## Data Preprocessing

### Project Overview

This repository is part of a semester AI project in order to analyse YouTube comments about the war in Ukraine.
We collect data from CNN news YouTube channel, clean it, analyze user sentiment and semantics, and later use it for fake/true news classification.

### What Each File Does
- **ids.txt** – list of YouTube video IDs.
- **youtube_comments_ytdlp.ipynb** – loads video data and comments.
- **preprocess_data.ipynb** – removes noise, filters English text, checks validity with LinearCSV.
- **YouTube_Sentiment_Analysis.ipynb** – performs sentiment analysis using simple NLP models.
- **YouTube_Sentiment_Analysis_GPU.ipynb** – uses BERT for deeper semantic and sentiment analysis.
- **youtube_comments_english.csv** – final cleaned dataset for modeling.

### Tools & Libraries

- Python 3 – main programming language
- pandas – for working with CSV files and DataFrames
- numpy – for numerical operations
- yt-dlp – to download YouTube video data and comments
- nltk – text preprocessing (tokenization, stopwords, lemmatization)
- spaCy – additional lemmatization and NLP pipeline

### Workflow
1. Collect video IDs and download comments.
2. Clean and validate text.
3. Analyze sentiment and meaning (in another repo).
4. Use results for fake/true news detection and public perception analysis (in another repo).

