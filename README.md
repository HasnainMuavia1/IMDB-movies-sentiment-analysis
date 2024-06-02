
# IMDB Movies Sentiment Analysis App

Welcome to the IMDB Movies Sentiment Analysis App! This application allows you to analyze user reviews for movies on IMDB to determine their overall sentiment. You can enter either the movie name or the URL to fetch reviews. Using the URL provides faster results, while using the movie name maybe not match with the actual movie or it matched with many movies so that sometimes you get not accurate results.

# Features
- Scrape Reviews: Retrieve user reviews from the IMDB website using Selenium.
- Sentiment Analysis: Preprocess textual data with NLTK and analyze sentiment using the VADER algorithm.
- Interactive Visualization: Visualize sentiment analysis results with Matplotlib through the Gradio interface.

# 1 - Input Options:

- Movie Name: Enter the name of the movie. Note that this might return multiple matches, so ensure you select the correct one to avoid inaccurate results.
- Movie URL: Enter the URL of the movie on IMDB for faster and more accurate review retrieval.
# Data Preprocessing:

The textual data from user reviews is preprocessed using the NLTK library.
Sentiment Analysis:

The VADER (Valence Aware Dictionary and sEntiment Reasoner) algorithm is used to perform sentiment analysis on the preprocessed data.
Visualization:

Results are visualized using Matplotlib and displayed via the Gradio interface.
# Requirements 
- Gradio
- Matplotlib
- gradio torch
- NLTK
- Python 3.x
- Selenium

## Authors

- [@HasnainMuavia](https://github.com/HasnainMuavia1)


## Screenshots

![App Screenshot](https://i.ibb.co/gDL6yBB/Screenshot-2024-06-02-175305.pngb)

