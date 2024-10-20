from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news_home'),
    path('dz/', views.home_dz, name='news_dz'),
    path('add_news/', views.add_news, name='add_news'),
]
