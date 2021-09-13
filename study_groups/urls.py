from django.urls import path

from .views import *

urlpatterns = [
  path('', study_groups, name='study_groups'),
  
]