"""Following instructions from 
https://tutorial.djangogirls.org/en/django_urls/"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
