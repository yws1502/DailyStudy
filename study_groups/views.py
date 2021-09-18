from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.models import Profile, Message
from common.utils import *
from .models import *
from .forms import *
# from .utils import *
# Create your views here.

def study_groups(request):
  groups = StudyGroup.objects.all()
  groups, search_query = search_groups(request)
  groups, page_range = paginator_object(request, groups, 3)

  context = {
    'groups' : groups,
    'page_range' : page_range,
    'search_query' : search_query,
  }
  return render(request, 'study_groups/groups.html', context)

def study_group(request, pk):
  group = StudyGroup.objects.get(id=pk)
  profiles = Profile.objects.filter(group_id=group.id)
  member_count = profiles.count()
  context = {
    'group' : group,
    'profiles' : profiles,
    'member_count' : member_count,
  }
  return render(request, 'study_groups/group.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def group_leave(request, pk):
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

@login_required(login_url='login')
def group_invite(request):
  profiles, search_query = search_invite(request)
  profiles, page_range = paginator_object(request, profiles, 6)
  
  if request.method == 'POST':
    sender = request.user.profile
    group_name = StudyGroup.objects.get(id=sender.group_id.id)
    for pk in request.POST.getlist('invite'):
      recipient = Profile.objects.get(id=pk)
      # 초대 메시지 전송하기
      Message.objects.create(
        recipient = recipient,
        sender = sender,
        name = sender.name,
        subject = '%s 스터디그룹 초대 메세지' % group_name,
        body = '%s님! 저희 %s와 함께 공부해보아요!' % (recipient.name, group_name),
        is_invite = True
      )
    return redirect('profiles')

  context = {
    'profiles': profiles,
    'search_query': search_query,
    'page_range': page_range
  }
  return render(request, 'study_groups/group_invite.html', context)