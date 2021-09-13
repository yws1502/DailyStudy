from django.shortcuts import render

from .models import *
# Create your views here.

def study_groups(request):
  groups = StudyGroup.objects.all()
  context = {
    'groups' : groups,
  }
  return render(request, 'study_groups/groups.html', context)