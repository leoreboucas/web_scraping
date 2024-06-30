from django.shortcuts import render
from .utils import news_access


# Essa view é a que cria o template para o index.html, nele contém a variável notices que pega as notícias da função news_acess do arquivo utils.py e conecta ao arquivo html
URL = "https://www.investing.com/news/latest-news"

def home(request):
    notices = news_access(URL)
    return render(
        request,
        'home/index.html', {
            'notices': notices
            }
        )