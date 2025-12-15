## American Perception of the Ukraine War – Data & Sentiment Pipeline

### Project Overview

This repository is part of a semester AI project on **“American perception of Ukrainians during the Russia–Ukraine war”**. We analyze YouTube comments under CNN news videos to understand how sentiment in the U.S. audience changes over time. The pipeline collects comments, cleans and filters them, generates sentiment and stance labels using transformer models, and then visualizes daily and smoothed sentiment trends.

The data and notebooks here focus mainly on:
- building a clean comment dataset,
- labeling sentiment and stance with modern LLMs and transformers,
- aggregating results into timelines of public perception.

### Repository Structure & What Each File Does

**Root notebooks**

- `gather_youtube.ipynb` – collects video IDs from CNN and downloads comments into raw CSV files.
- `load_comments_and_preprocess.ipynb` – loads raw comments, cleans text (URLs, emojis, mentions, very short messages), normalizes encoding and language, and saves a cleaned version to `data/youtube_comments.csv`.
- `model_train.ipynb` – uses Qwen2.5-1.5B-Instruct to generate sentiment labels (negative / neutral / positive) and trains a DistilBERT-based classifier on these pseudo-labels.
- `sentiment_analysis.ipynb` – runs the trained DistilBERT model on the full dataset and computes per‑comment sentiment.
- `sentiment_analysis_final.ipynb` – final sentiment pipeline: inference, daily aggregation, rolling averages and export of data for plots.
- `stance_basic.ipynb` – first experiments with stance classification (pro‑Ukrainian / pro‑Russian / neutral).
- `stance_full.ipynb` – extended stance modeling and analysis.
- `visualization.ipynb` – creates static and interactive visualizations of sentiment timelines.
- `visualization_sentiment.ipynb` – generates yearly Plotly plots (2023, 2024, 2025) and saves them as HTML for the demo site.

**Data folder (`data/`)**

- `video_ids_1.txt`, `video_ids_2.txt` – lists of CNN YouTube video IDs related to the Russia–Ukraine war.
- `youtube_comments.csv` – cleaned comment dataset with timestamps and basic metadata.
- `full_dataset_with_stats.xlsx` – enriched dataset with sentiment scores, stance labels and additional statistics for analysis.
- `sentiment_extrema_by_date.xlsx` – table of dates with local sentiment maxima and minima (daily and smoothed series).
- `sentiment_extrema_videos.xlsx` – video‑level information for days with strong sentiment changes (helps link peaks to specific news videos).

**Docs folder (`docs/`)**

- Contains the small demo website that embeds interactive Plotly plots (`sentiment_2023.html`, `sentiment_2024.html`, `sentiment_2025.html`) to show how American sentiment toward Ukraine changes from 2023 to 2025.

### Tools & Libraries
- Python 3 – main language  
- `pandas`, `numpy` – data loading, cleaning and aggregation  
- `yt-dlp` / YouTube Data API – collecting video metadata and comments  
- `transformers` (Hugging Face) – Qwen2.5-1.5B-Instruct, DistilBERT and tokenizers  
- `vllm` – high‑throughput, memory‑efficient serving of Qwen2.5-1.5B-Instruct for pseudo‑label generation on GPU  
- `torch` – model training and inference  
- `plotly`, `matplotlib` – visualization and interactive HTML plots

### Workflow

1. **Collect comments from CNN**
   - Use `gather_youtube.ipynb` with `video_ids_*.txt` to download comments from CNN news videos about the Russia–Ukraine war.
2. **Preprocess and clean**
   - Run `load_comments_and_preprocess.ipynb` to remove noise (URLs, emojis, bots, very short messages), normalize text and save `youtube_comments.csv`.
3. **Label sentiment with Qwen2.5-1.5B-Instruct**
   - In `model_train.ipynb`, use Qwen2.5-1.5B-Instruct as a teacher model to label comments as negative, neutral or positive toward Ukraine / the war.  
   - The model is served with the `vllm` library to get fast batched inference and better GPU memory usage on an 8 GB RTX‑class GPU. This makes it feasible to label hundreds of thousands of comments locally.  
   - Qwen2.5-1.5B is chosen instead of larger 7B models because it fits into 8 GB VRAM when combined with vLLM and quantization tricks.
4. **Train DistilBERT student model**
   - Fine‑tune a DistilBERT classifier on the Qwen‑labeled data to obtain a lightweight model for sentiment analysis on the full dataset.
5. **Run sentiment and stance analysis**
   - Use `sentiment_analysis*.ipynb` and `stance_*.ipynb` to predict sentiment and stance for all comments and store results.
6. **Aggregate sentiment over time**
   - Group by date, compute daily mean sentiment and apply a 7‑day rolling average to get smoother trends of American perception.
7. **Analyze peaks and videos**
   - Use `full_dataset_with_stats.xlsx`, `sentiment_extrema_by_date.xlsx` and `sentiment_extrema_videos.xlsx` to study where sentiment changes sharply and which videos drive these shifts.
8. **Visualize American perception**
   - Generate yearly interactive plots (`sentiment_2023/2024/2025.html`) and show them via the simple landing page in `docs/`, highlighting how U.S. sentiment toward Ukraine evolves over time.
