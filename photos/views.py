from django.shortcuts import render
from . models import *
# Create your views here.

#home view rendering pictures of all category

def home(req):
    photos=Image.objects.all()
    context={
        'title':home,
        'photos':photos
    }
    return render(req, 'photos/home.html' , context)



def categoty_page(req):
    return render(req, 'photos/test.html')