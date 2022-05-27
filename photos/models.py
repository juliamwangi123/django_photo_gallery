from pyexpat import model
from unicodedata import category, name
from django.db import models

# Create your models here.


class Category(models.Model):
    '''categories module'''
    name=models.CharField(max_length=40, blank=True)




class Location(models.Model):
    '''locataion module'''
    name=models.CharField(max_length=40, blank=True)


class  Image(models.Model):
    '''image module'''
    name=models.CharField(max_length=40, blank=True)
    decription=models.TextField()
    image=models.ImageField(null=False, blank=True)
    category=models.ForeignKey(Category)
    location=models.ForeignKey(Category)


    