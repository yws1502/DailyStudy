from django.shortcuts import render

from users.models import Profile
from .models import *
# Create your views here.

def study_groups(request):
  groups = StudyGroup.objects.all()
  context = {
    'groups' : groups,
  }
  return render(request, 'study_groups/groups.html', context)

def study_group(request, pk):
  group = StudyGroup.objects.get(id=pk)
  profiles = Profile.objects.filter(group_id=group.id)
  context = {
    'group' : group,
    'profiles' : profiles,
  }
  return render(request, 'study_groups/group.html', context)