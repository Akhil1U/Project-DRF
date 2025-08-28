from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rating, Sales, Restaurant
from .serializers import RatingSerializer, SalesSerializer, RestaurantSerializer



@api_view(['GET', 'POST'])
def ratings(request):
    if request.method == 'GET':
        rating = Rating.objects.all()
        serializer = RatingSerializer(rating, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def sales(request):
    if request.method == 'GET':
        saling = Sales.objects.all()
        serializer = SalesSerializer(saling, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def restaurant(request):
    if request.method == 'GET':
        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)