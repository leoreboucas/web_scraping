from django.shortcuts import render
from .utils import news_access

URL = "https://www.investing.com/news/latest-news"

def home(request):
    notices = news_access(URL)
    return render(
        request,
        'home/index.html', {
            'notices': notices
            }
        )