from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from users.models import Profile
from .models import StudyGroup

def paginator_group(request, groups, results):
  page = request.GET.get('page')
  paginator = Paginator(groups, results)

  try:
    groups = paginator.page(page)
  except PageNotAnInteger:
    page = 1
    groups = paginator.page(page)
  except EmptyPage:
    page = paginator.num_pages
    groups = paginator.page(page)
  
  left_idx = int(page) - results
  if left_idx < 1:
    left_idx = 1

  right_idx = int(page) + (results + 1)
  if right_idx > paginator.num_pages + 1:
    right_idx = paginator.num_pages + 1

  page_range = range(left_idx, right_idx)
  return groups, page_range

def search_groups(request):
  search_query = ''
  if request.GET.get('search_query'):
    search_query = request.GET.get('search_query')
  profiles = Profile.objects.filter(name__icontains=search_query)

  objects = StudyGroup.objects.distinct().filter(
    Q(name__icontains=search_query) |
    Q(profile__in=profiles)
  )
  return objects, search_query

def search_invite(request):
  search_query = ''
  if request.GET.get('search_query'):
    search_query = request.GET.get('search_query')

  invite_list = Profile.objects.filter(
    Q(name__icontains=search_query) &
    Q(group_id=None)
  )
  return invite_list, search_query
