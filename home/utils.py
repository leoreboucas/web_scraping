import requests
from bs4 import BeautifulSoup

# O header 'User-Agent' é utilizado no programa para identificar o software cliente que está fazendo a requisição HTTP. Isso permite que o servidor saiba qual tipo de dispositivo ou aplicação está acessando seus recursos, facilitando a adaptação da resposta conforme necessário.

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.124 Safari/537.36"
}

# Função responsável pela raspagem de dados do site.

def news_access(url):
    
    # A variável "r" é usada para fazer a requisição HTTP, enquanto a variável "soup" utiliza o BeautifulSoup para organizar e analisar a resposta dessa requisição.
    
    r = requests.get(f"{url}", headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    # Essa parte do código é a parte principal que é pegar os dados na página e transformar em uma dict(dicionário) que contém o título da notícia que direciona para o link original e o conteúdo da notícia
    
    search_notices = soup.find("ul", {
        "data-test":"news-list"
    })

    notices_titles = {}
    id = 0
    news_url = "https://www.investing.com"

    for notice in search_notices:
        id += 1 
        
        notice_title = notice.find('a', {
            'data-test': 'article-title-link'
        })
        
        notice_href = news_url + notice_title.get('href')
        
        notice_description = notice.find('p', {
        'data-test': 'article-description'
        }).get_text()
        link_info = {'href': notice_href ,'legend': notice_title.get_text()}
        notices_titles[id] = {'link': link_info, 'text': notice_description}
    return notices_titles

news_access('https://www.investing.com/news/latest-news')
