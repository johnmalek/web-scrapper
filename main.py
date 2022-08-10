# Python project to scrape the washingpost news site and return the title and body of a certain article

import requests
from bs4 import BeautifulSoup

news_site_url = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"

response = requests.get(url=news_site_url)
data = response.text

soup = BeautifulSoup(data, "html.parser")
title = soup.find(name="h1", id="main-content")
content = soup.find(name="div", class_="grid-body")
print(title.getText())
print(content.getText())
