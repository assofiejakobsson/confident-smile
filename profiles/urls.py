from django.urls import path
from . import views
from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
#from .models import UserProfile, Wishlist
#from products.models import Product

app_name = 'profiles'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'), 
]