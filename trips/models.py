from django.db import models
from accounts.models import CustomUser


class Country(models.Model):
    name = models.CharField(max_length=200)
    continent = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

class Trip(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='user')
    country = models.ForeignKey(Country, on_delete=models.CASCADE,related_name='country')
    city = models.CharField(max_length=120)
    rating = models.PositiveIntegerField()
    budget = models.PositiveIntegerField()
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city

    
