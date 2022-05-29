from django.shortcuts import render,redirect
from django.db.models import Q

from . models import *
from django.contrib import messages
# Create your views here.

#home view rendering pictures of all category

def home(req):
    '''''this view is triggered when ckient got to the home page'''
    categories=Category.objects.all()
    locations=Location.objects.all()
    
    search_photo=req.GET.get('search') #go get the user input 
    if search_photo:
        photos=Image.objects.filter(Q( category__name__icontains=search_photo)| Q(location__name__icontains=search_photo))
        context={
            'title':home,
            'photos':photos,
            'categories':categories,
            'locations':locations
        }
        return render(req, 'photos/home.html' , context)


    else:
    
        photos=Image.objects.all()
        context={
            'title':home,
            'photos':photos,
            'categories':categories,
            'locations':locations

        }
        return render(req, 'photos/home.html' , context)



#view rendered when an image is clicked

def category_page(req, pk):
    '''''this view is triggered when user click a specific image'''
    photos=Image.objects.get(id=pk)
    print(photos.name)
    print(photos.decription)

    # photos in the  same category as the one above
    allphotos=Image.objects.filter(category=photos.category)
    context={
        'title':category_page,
        'photos':photos,
        'allphotos':allphotos,
    }
    return render(req, 'photos/category.html', context)

#page triggered in relation to category and location

def categories(req, pk):
    categories=Category.objects.get(id=pk)

    photos=Image.objects.filter(category=categories)

    return render(req, 'photos/categories.html', { 'photos':photos })


def location(req, pk):
    locations=Location.objects.get(id=pk)

    photosl=Image.objects.filter(location=locations)

    return render(req, 'photos/location.html', {  'photosl':photosl })




    
