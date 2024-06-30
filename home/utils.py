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
    news_url = "https://www.investing.com/"

    for i in search_notices:
        id += 1 
        title = i.find("div", class_='news-analysis-v2_content__z0iLP')
        link = {'href': news_url + title.a.get('href') ,'legend': title.a.get_text()}
        text = title.p.get_text()
        notices_titles[id] = {'link': link, 'text': text}
    return notices_titles
