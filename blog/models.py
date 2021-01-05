from django.db import models
from django.urls import *

# Create your models here.
class Post(models.Model):
    model =models.CharField(max_length=64)
    owner=models.CharField(max_length=64)
    price=models.IntegerField()
    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('home')    
        return reverse('detail',args=[str(self.id)] )