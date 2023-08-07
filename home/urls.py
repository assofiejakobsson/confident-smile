from django.contrib import admin  
from django.urls import path     
from . import views              

# Naming the app, which helps in URL namespacing
app_name = 'home'                

# URL patterns for the home app
urlpatterns = [
    
    path('', views.index, name='home'),
]
