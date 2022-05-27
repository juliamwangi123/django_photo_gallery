from django.shortcuts import render

# Create your views here.

#home view rendering pictures of all category

def home(req):
    return render(req, 'photos/home.html')