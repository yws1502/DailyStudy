from django.urls import path

from .views import *

urlpatterns = [
  path('', study_groups, name='study_groups'),
  path('group/<str:pk>/', study_group, name="study_group"),
  path('group_create/', group_create, name="group_create"),
  
]