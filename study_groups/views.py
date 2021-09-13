from django.shortcuts import render, redirect

from users.models import Profile
from .models import *
from .forms import *
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
    form = StudyGroupForm(request.POST, request.FILES)
    if form.is_valid():
      group = form.save(commit=False)
      # 스터디를 생성한 사람이 그룹의 리더
      profile.group_id = group
      profile.is_leader = True
      group.save()
      profile.save()
      return redirect('study_groups')

  context = {'form' : form}
  return render(request, 'study_groups/group_form.html', context)

def group_update(request, pk):
  group = StudyGroup.objects.get(id=pk)
  form = StudyGroupForm(instance=group)

  if request.method == 'POST':
    form = StudyGroupForm(request.POST, request.FILES, instance=group)
    if form.is_valid():
      form.save()
      return redirect('study_group', pk=group.id)

  context = {
    'form': form,
  }
  return render(request, 'study_groups/group_form.html', context)

def group_delete(request, pk):
  group = StudyGroup.objects.get(id=pk)
  # 그룹 리더의 is_leader False로 값 변경
  profile = Profile.objects.filter(group_id=group, is_leader=True)
  if request.method == 'POST':
    profile.update(is_leader=False)
    group.delete()
    return redirect('study_groups')

  context = {'object': group}
  return render(request, 'delete_form.html', context)

def group_withdrawal(request, pk):
  group = StudyGroup.objects.get(id=pk)
  profile = request.user.profile

  if request.method == 'POST':
      # 다음 리더 선택
    if profile.is_leader == True:
      next = Profile.objects.get(id=request.POST['profile'])
      next.is_leader = True
      next.save()
    # 전 리더 탈퇴
    profile.group_id = None
    profile.is_leader = False
    profile.save()
    return redirect('profiles')

  context = {'profile': profile}
  if profile.is_leader == True:
    # 리더인 경우 리더자리를 위임할 사람 select
    profiles = Profile.objects.filter(is_leader=False, group_id=group)
    context['profiles'] = profiles
  return render(request, 'study_groups/withdrawal.html', context)