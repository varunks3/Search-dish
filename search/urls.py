from django.urls import path
from .views import search_dishes

urlpatterns = [
    path('', search_dishes, name='search_dishes'),
]
