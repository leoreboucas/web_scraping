import requests
from bs4 import BeautifulSoup

URL = "https://www.investing.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.124 Safari/537.36"
}


def news_access(url):
    r = requests.get(f"{URL}{url}", headers=headers)

    site = BeautifulSoup(r.text, "html.parser")

    search_notices = site.find("ul", {
        "data-test":"news-list"
    })

    notices_titles = []

    for i in search_notices:
        title = i.find("a", {
            "data-test": "article-title-link"
            })
        notices_titles.append(title.get_text())
  

news_access("/news/latest-news")