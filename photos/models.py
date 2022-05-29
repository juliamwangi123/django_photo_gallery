from operator import mod
from pyexpat import model
from unicodedata import category, name
from django.db import models

# Create your models here.


class Category(models.Model):
    '''categories module'''
    # CATEGORY=(
    #     'fashion':'fashion'
    # )
    name=models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.name



class Location(models.Model):
    '''locataion module'''
    name=models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.name



class  Image(models.Model):
    '''image module'''
    name=models.CharField(max_length=40, blank=True)
    decription=models.TextField()
    image=models.ImageField(null=False, blank=True)
    category=models.ForeignKey(Category , on_delete=models.CASCADE)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    