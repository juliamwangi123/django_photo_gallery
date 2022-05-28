from multiprocessing import context
from django.shortcuts import render

import photos
from . models import *
# Create your views here.

#home view rendering pictures of all category

def home(req):
    '''''this view is triggered when ckient got to the home page'''
    photos=Image.objects.all()
    context={
        'title':home,
        'photos':photos
    }
    return render(req, 'photos/home.html' , context)



def category_page(req, pk):
    '''''this view is triggered when user click a specific image'''
    photos=Image.objects.get(id=pk)

    # photos in the  same category as the one above
    allphotos=Category.objects.filter(id=pk)

    context={
        'title':category_page,
        'photos':photos,
        'allphotos':allphotos
    }
    return render(req, 'photos/category.html', context)