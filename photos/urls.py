from django.urls import path
from . import views

urlpatterns=[
    path('',  views.home, name='photos-home'),
    path('category/<str:pk>', views.category_page, name='category'),
    path('search/', views.search, name='search' )
]
