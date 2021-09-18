from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from study_groups.models import StudyGroup
from users.models import Profile

## paginator
def paginator_object(request: object, object: object, result: int) -> None:
  page = request.GET.get('page')
  paginator = Paginator(object, result)

  try:
    objects = paginator.page(page)
  except PageNotAnInteger:
    page = 1
    objects = paginator.page(page)
  except EmptyPage:
    page = paginator.num_pages
    objects = paginator.page(page)
  
  left_idx = int(page) - result
  if left_idx < 1:
    left_idx = 1
  
  right_idx = int(page) + (result+1)
  if right_idx > paginator.num_pages + 1:
    right_idx = paginator.num_pages + 1
  
  page_range = range(left_idx, right_idx)
  return objects, page_range


## search bar
def search_profile(request: object) -> None:
  search_query = ''
  if request.GET.get('search_query'):
    search_query = request.GET.get('search_query')
    
  profiles = Profile.objects.filter(
    Q(name__icontains = search_query) |
    Q(short_intro = search_query)
  )
  return profiles, search_query

def search_algorithm(request: object, algorithms: object) -> None:
  search_query = ''
  if request.GET.get('search_query'):
    search_query = request.GET.get('search_query')
  
  ret = algorithms.filter(
    Q(name__icontains=search_query) |
    Q(description__icontains=search_query) |
    Q(type__icontains=search_query)
  )
  return ret, search_query

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
