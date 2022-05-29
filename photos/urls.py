from django.urls import path
from . import views

urlpatterns=[
    path('',  views.home, name='photos-home'),
    path('category/<str:pk>', views.category_page, name='category'),
    path('sCategory<str:pk>', views.categories, name='c'),
    path('location<str:pk>', views.location, name='l'),

]
