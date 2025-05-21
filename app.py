import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random

# Load dataset
df = pd.read_csv("cleaned_netflix_data.csv")

st.title("Netflix Data Analysis Dashboard")

option = st.sidebar.selectbox(
    "Choose an Analysis",
    [
        "Content by Country",
        "Monthly Releases",
        "Top Genres",
        "Similar Content Recommender",
        "TV vs Movies Trend",
        "Rating Distribution",
        "Year Added vs Release Year"
    ]
)

if option == "Content by Country":
    country_counts = df['country'].value_counts().head(15)
    st.subheader("Top 15 Countries with Most Netflix Content")
    st.bar_chart(country_counts)

elif option == "Monthly Releases":
    df['date_added'] = pd.to_datetime(df['date_added'])
    df['month_added'] = df['date_added'].dt.month
    month_counts = df['month_added'].value_counts().sort_index()
    st.subheader("Content Releases by Month")
    st.line_chart(month_counts)

elif option == "Top Genres":
    all_genres = ', '.join(df['listed_in'].dropna()).split(', ')
    genre_counts = pd.Series(all_genres).value_counts().head(10)
    st.subheader("Top 10 Most Common Genres")
    st.bar_chart(genre_counts)

elif option == "Similar Content Recommender":
    st.subheader("Simple Genre-based Recommender")
    selected_genre = st.selectbox("Select Genre", df['listed_in'].dropna().unique())
    recommendations = df[df['listed_in'] == selected_genre][['title', 'type', 'country', 'release_year']].head(10)
    st.write(recommendations)

elif option == "TV vs Movies Trend":
    st.subheader("TV Shows vs Movies Over the Years")
    type_year_counts = df.groupby(['release_year', 'type']).size().unstack().fillna(0)
    st.line_chart(type_year_counts)

elif option == "Rating Distribution":
    st.subheader("Rating Distribution by Type")
    rating_counts = df.groupby(['rating', 'type']).size().unstack().fillna(0)
    st.bar_chart(rating_counts)

elif option == "Year Added vs Release Year":
    st.subheader("Year Added vs Release Year")
    df['year_added'] = pd.DatetimeIndex(df['date_added']).year
    year_diff = df[df['year_added'].notna() & df['release_year'].notna()]
    year_diff['difference'] = year_diff['year_added'] - year_diff['release_year']
    fig, ax = plt.subplots()
    sns.histplot(year_diff['difference'], bins=20, kde=True, ax=ax)
    ax.set_title("Distribution of Year Difference")
    st.pyplot(fig)
