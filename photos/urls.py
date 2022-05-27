from django.urls import path
from . import views

urlpatterns=[
    path('',  views.home, name='photos-home'),
    path('test', views.categoty_page, name='test')
]
