from django.contrib import admin
from django.urls import path, include
from .views import index, top_sellers

urlpatterns = [
    path('', index),
    path('top-sellers', top_sellers)
]
