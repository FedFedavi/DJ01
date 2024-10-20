from django.shortcuts import render, redirect
from .models import News_post
from .models import Dz_post
from .forms import News_postForm

# Create your views here.


def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})


def home_dz(request):
    news = Dz_post.objects.all()
    return render(request, 'news/news.html', {'news_dz': news})


def add_news(request):
    error = ""
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Данные внесены некорректно'

    form = News_postForm()
    return render(request, 'news/add_news.html', {'form': form, 'errors': error})
