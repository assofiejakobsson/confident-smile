from django.urls import path
from . import views

app_name = 'siteinfo'

urlpatterns = [

    path('faq/', views.faq_list, name='faq_list'),
    path('faq/<int:faq_id>/', views.faq_detail, name='faq_detail'),

    
]




