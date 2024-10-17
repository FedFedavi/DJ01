from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('page3/', views.page3, name='page3'),
    path('page4/', views.page4, name='page4'),

]
