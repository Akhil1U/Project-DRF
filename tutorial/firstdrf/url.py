from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  RatingDetail, RatingList, RestaurantDetail, RestaurantList, SalesDetail, SalesList

urlpatterns = [
    ## Function based view - url pattern ~ only for refernce

    # path('ratings/', ratings),
    # path('sales/', sales),
    # path('sales/<int:pk>/', sales_details),
    # path('restaurants/', restaurant),

    ## class based view
    path('sales/', SalesList.as_view(), name='sales-list'),
    path('sales/<int:pk>/', SalesDetail.as_view(), name='sales-detail'),

    path('ratings/', RatingList.as_view(), name='rating-list'),
    path('ratings/<int:pk>/', RatingDetail.as_view(), name='rating-detail'),

    path('restaurants/', RestaurantList.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),

]
urlpatterns = format_suffix_patterns(urlpatterns)