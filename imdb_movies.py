import time
from matplotlib import pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from selenium.webdriver.chrome.options import Options

from nltk.stem.porter import PorterStemmer
import gradio as gr
import string

driver = webdriver.Chrome()


def search_by_title(title):
    """
    Searches the movie with the title also using the function of
    search by URl
    Args:
        title (str): The movie title
    Returns:
        text (str): reviews of the movie
    Raises:
        if no movie found with title
    """
    driver.get("https://www.imdb.com")
    search = driver.find_element(By.NAME, 'q')
    search.send_keys(title, Keys.ENTER)
    time.sleep(2)
    try:
        result_movie = driver.find_element(By.XPATH,
                                           '/html/body/div[2]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]/div[2]/div/a')

        url = result_movie.get_attribute('href')
        text = Search_By_URL(url)
        return text
    except NoSuchElementException:
        print('No movie found')
    # return text


def Search_By_URL(movie_url):
    """
    Search movie by url and scrap reviews
    Args:
        movie_url: url of the movie
    Raises:
        if no movie found with url
    Returns:
        text: list of reviews in text file
    """
    text = ''
    print(movie_url.split('?')[0])
    driver.get(movie_url.split('?')[0] + 'reviews')
    for i in range(10):
        time.sleep(1)
        # driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        load_more_button = driver.find_element(By.XPATH, '//*[@id="load-more-trigger"]')
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(2)
        load_more_button.click()
        driver.execute_script(f"window.scrollBy(0,-2000)")
    try:
        reviews = driver.find_elements(By.CLASS_NAME, 'content')
        for review in reviews:
            text += review.text

    except NoSuchElementException:
        print('wrong URL')
    return text


def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.replace('\n', '')
    text = word_tokenize(text, 'english')
    text = [word for word in text if word not in stopwords.words('english')]
    # stemmer = PorterStemmer()
    # text = [stemmer.stem(word) for word in text]
    text = ' '.join(text)
    return text


score = SentimentIntensityAnalyzer()

title_input = gr.Textbox(lines=1, label="Enter movie title or URL :")


def analyze(movie_input):
    if movie_input.startswith("http"):
        text = Search_By_URL(movie_input)
    else:
        text = search_by_title(movie_input)
    scores_sentiment = score.polarity_scores(preprocess_text(text))
    plt.figure(figsize=(8, 6))
    plt.bar(scores_sentiment.keys(), scores_sentiment.values(), color=['red', 'gray', 'green'])
    plt.xlabel('Sentiment')
    plt.ylabel('Score')
    plt.title(driver.title)
    return plt


output_component = gr.Plot()
iface = gr.Interface(fn=analyze, inputs=title_input, outputs=output_component,
                     title='IMDB Movies Sentiment Analysis BY Hasnain Muavia')
iface.launch()
