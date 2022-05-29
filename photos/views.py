from django.shortcuts import render,redirect
from django.db.models import Q

import photos
from . models import *
from django.contrib import messages
# Create your views here.

#home view rendering pictures of all category

def home(req):
    '''''this view is triggered when ckient got to the home page'''

    
    
    search_photo=req.GET.get('search') #go get the user input 
    if search_photo:
        photos=Image.objects.filter(Q( category__name__icontains=search_photo)| Q(location__name__icontains=search_photo))
        context={
            'title':home,
            'photos':photos
        }
        return render(req, 'photos/home.html' , context)


    else:
    
        photos=Image.objects.all()
        context={
            'title':home,
            'photos':photos
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

#view rendered when sub--menu is clicked
def group(req):
     photos=Image.objects.filter(category)

     return redirect(req, "home",{'photos':photos})
   

    
