from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rating, Sales, Restaurant
from .serializers import RatingSerializer, SalesSerializer, RestaurantSerializer

## for class based views
from rest_framework import mixins, generics


# sales view
class SalesList(generics.ListCreateAPIView): # for get and post request
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class SalesDetail(generics.RetrieveUpdateDestroyAPIView): # for get put delete & option request
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

# Rating view
class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()

# Restaurant view
class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


########## only for reference : this is function based view ---------------------------------------


# @api_view(['GET', 'POST', 'DELETE'])
# def ratings(request):
#     if request.method == 'GET':
#         rating = Rating.objects.all()
#         serializer = RatingSerializer(rating, many = True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = RatingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'POST'])
# def sales(request, format = None):
    
#     if request.method == 'GET':
#         saling = Sales.objects.all()
#         serializer = SalesSerializer(saling, many = True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = SalesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def sales_details(request, pk, format = None):  # this view is same for every model views so for reusa this code we can use class based view .
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         sale = Sales.objects.get(pk=pk)
#     except Sales.DoesNotExist:
#         return HttpResponse(status=404)
    
#     # below code is same for all...
#     if request.method == 'GET':
#         serializer = SalesSerializer(sale)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SalesSerializer(sale, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         sale.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'POST'])
# def restaurant(request):
#     if request.method == 'GET':
#         restaurant = Restaurant.objects.all()
#         serializer = RestaurantSerializer(restaurant, many = True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = RestaurantSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)