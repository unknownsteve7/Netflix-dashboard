# 🎬 Netflix Data Analysis Dashboard

An interactive data analysis dashboard built with **Streamlit** that explores Netflix's content library — uncovering trends, genre distributions, country breakdowns, and content release patterns using real-world data.

---

## 📖 Project Description

This project provides an interactive, browser-based dashboard for analysing Netflix's catalogue of movies and TV shows. It is aimed at data enthusiasts, analysts, and learners who want to explore real-world streaming data through engaging visualisations.

The app is powered by a cleaned version of the [Netflix Movies and TV Shows dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows) (~5,300 titles) and built with a Netflix-themed dark UI (black background, red accent colour).

Users can navigate between seven analysis views using a sidebar menu — no coding required.

---

## ✨ Features

| Analysis View | Description |
|---|---|
| **Content by Country** | Bar chart of the top 15 countries with the most Netflix titles |
| **Monthly Releases** | Line chart showing how many titles were added to Netflix each month |
| **Top Genres** | Bar chart of the 10 most common genres across all titles |
| **Similar Content Recommender** | Select a genre and get a list of matching titles (type, country, year) |
| **TV vs Movies Trend** | Line chart comparing TV shows and movies released each year |
| **Rating Distribution** | Bar chart of content ratings (e.g. TV-MA, PG-13) split by type |
| **Year Added vs Release Year** | Histogram showing the gap between a title's release year and when it was added to Netflix |

---

## 📂 Project Structure

```
Netflix-dashboard/
├── app.py                    # Main Streamlit application
├── cleaned_netflix_data.csv  # Pre-processed Netflix dataset (~5,300 rows)
├── netflix_titles.csv        # Raw Netflix dataset (~8,800 rows)
├── requirements.txt          # Python dependencies
└── .streamlit/
    └── config.toml           # Netflix-themed dark UI configuration
```

---

## 🚀 Run Locally

**1. Clone the repository:**
```bash
git clone https://github.com/unknownsteve7/Netflix-dashboard.git
cd Netflix-dashboard
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Launch the app:**
```bash
streamlit run app.py
```

The dashboard will open automatically at `http://localhost:8501` in your browser.

---

## 📊 Dataset

- **File used:** `cleaned_netflix_data.csv` (~5,300 titles after cleaning)
- **Raw source:** `netflix_titles.csv` (~8,800 titles)
- **Columns:** `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in` (genres), `description`
- **Coverage:** Movies and TV shows available on Netflix, spanning release years up to 2021

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Web app framework for the interactive dashboard |
| **Pandas** | Data loading, cleaning, and aggregation |
| **Matplotlib** | Custom plot rendering |
| **Seaborn** | Statistical visualisation (histogram with KDE) |
| **NetworkX** | Included as a dependency for potential network graph extensions |

---

## 💡 Inspiration

Built as a hands-on data analysis and visualisation project using a real-world streaming dataset. Great for learning Pandas aggregation, Streamlit layout patterns, and turning raw CSV data into actionable insights.

