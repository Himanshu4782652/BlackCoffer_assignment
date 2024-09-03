import requests
from bs4 import BeautifulSoup


def extract_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the article title and text elements
    title = soup.find("title").text
    article_text = soup.find("div", class_="article-content").text

    return title, article_text
