from django.urls import path
from .views import  ratings, sales, restaurant

urlpatterns = [
    path('ratings/', ratings),
    path('sales/', sales),
    path('restaurants/', restaurant)


]
