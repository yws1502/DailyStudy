from django.urls import path

from .views import *

urlpatterns = [
  path('', study_groups, name='study_groups'),
  path('group/<str:pk>/', study_group, name="study_group"),
  path('group_create/', group_create, name="group_create"),
  path('group_update/<str:pk>/', group_update, name="group_update"),
  path('group_delete/<str:pk>/', group_delete, name="group_delete"),

  path('group_withdrawal/<str:pk>/', group_withdrawal, name="group_withdrawal"),
  path('group_invite/<str:pk>/', group_invite, name="group_invite"),
  
]