from django.urls import path
from .views import *

urlpatterns = [
    path("profile/",profile,name='profile'),
    path("wishlist/",wishlist,name='wishlist'),
    path("shelf/",shelf,name='myshelf'),
]