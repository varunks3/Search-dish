from django.urls import path
from .views import search_dishes, index

urlpatterns = [
    path('search/', search_dishes, name='search_dishes'),
    path('', index, name='index'),
]
