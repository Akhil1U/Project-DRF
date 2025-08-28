from firstdrf.models import Restaurant, Rating, Sales
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from pprint import pprint
def run():
   user = User.objects.first()
   restaurant = Restaurant.objects.first()

#    print(Rating.objects.get_or_create(  ## this will create data if not exist else retreive data if not exist
#       Restaurant = restaurant,
#       User = user,
#       Rating = 4
#    ))