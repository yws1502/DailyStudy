from django.shortcuts import render, redirect

from users.models import Profile

from .forms import *
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

def group_create(request):
  form = StudyGroupForm()
  profile = request.user.profile
  
  if request.method == 'POST':
    form = StudyGroupForm(request.POST)
    if form.is_valid():
      group = form.save(commit=False)
      # 스터디를 생성한 사람이 그룹의 리더
      profile.group_id = group
      profile.is_leader = True
      group.save()
      profile.save()
      return redirect('study_groups')

  context = {'form' : form}
  return render(request, 'study_groups/group_create.html', context)