from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Эта страница открылась потому что: <br> '
                        '1. в настройках settings.py указан базовый url - urls.py <br>'
                        '2. в путях основного url.py включен include-м dz.url.py приложения <br>'
                        '3. в url.py приложения вызывается функция отображения index из файла view <br>'
                        '4. в которой этот текст </h1>')


def data(request):
    return HttpResponse('<h1>Здесь должны быть данные для моего проекта на Django</h1>')

def test(request):
    return HttpResponse('<h1>Здесь должны быть результаты теста моего проекта на Django</h1>')

