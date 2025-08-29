from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  ratings, sales, restaurant,sales_details

urlpatterns = [
    path('ratings/', ratings),
    path('sales/', sales),
    path('sales/<int:pk>/', sales_details),
    path('restaurants/', restaurant)


]
urlpatterns = format_suffix_patterns(urlpatterns)