import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.124 Safari/537.36"
}

def news_access(url):
    r = requests.get(f"{url}", headers=headers)

    site = BeautifulSoup(r.text, "html.parser")

    search_notices = site.find("ul", {
        "data-test":"news-list"
    })

    notices_titles = {}
    id = 0
    news_url = "https://www.investing.com/"

    for i in search_notices:
        id += 1 
        title = i.find("div", class_='news-analysis-v2_content__z0iLP')
        link = {'href': news_url + title.a.get('href') ,'legend': title.a.get_text()}
        text = title.p.get_text()
        notices_titles[id] = {'link': link, 'text': text}
    return notices_titles

news_access('https://www.investing.com/news/latest-news')