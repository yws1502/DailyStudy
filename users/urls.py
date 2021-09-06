from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', profile_list, name='profile_list'),
]