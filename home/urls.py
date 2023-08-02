from django.contrib import admin
from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
]