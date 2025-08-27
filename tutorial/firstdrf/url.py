# myapp/urls.py

from django.urls import path
from .views import author_list, book_list

urlpatterns = [
    path('authors/', author_list),
    path('books/', book_list),
]
