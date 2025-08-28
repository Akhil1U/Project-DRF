from rest_framework import serializers
from firstdrf.models import Rating, Sales, Restaurant
from django.contrib.auth.models import User



class RatingSerializer(serializers.ModelSerializer):
     class Meta: 
        model = Rating 
        fields = ['id', 'User', 'Restaurant', 'Rating']


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['id','Restaurant','Income','Datetime']


class RestaurantSerializer(serializers.ModelSerializer):
    # Restaurant_type = Models.CharField(source='get_Restaurant_type_display', read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id','name','website','date_opened','latitude','longitude','Restaurant_type']