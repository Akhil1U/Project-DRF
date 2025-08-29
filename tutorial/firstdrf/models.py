from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):

    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'indian'
        CHINES = 'CH', 'chines'
        ITALIAN = 'IT', 'italian'
        MAXICAN = 'MA', 'maxican'
        GREEK = 'GR', 'greek'
        FASTFOOD = 'FF', 'fast food'
        OTHER = 'OT', 'other'

    name = models.CharField(max_length=100)
    website = models.URLField(null=True, blank=True)
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    Restaurant_type = models.CharField(choices=TypeChoices, max_length=2)

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='Rating')
    Rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"rating: {self.Rating}"
    
class Sales(models.Model):
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='Sales')
    Income = models.DecimalField(max_digits=8,decimal_places=2)
    Datetime = models.DateTimeField()