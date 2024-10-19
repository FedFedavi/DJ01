from django.shortcuts import render
from .models import News_post
from .models import Dz_post

# Create your views here.


def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})


def home_dz(request):
    news = Dz_post.objects.all()
    return render(request, 'news/news.html', {'news_dz': news})
