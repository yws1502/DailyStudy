from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import Profile

def paginator_profile(request: object, profile: object, result: int) -> None:
  page = request.GET.get('page')
  paginator = Paginator(profile, result)

  try:
    profiles = paginator.page(page)
  except PageNotAnInteger:
    page = 1
    profiles = paginator.page(page)
  except EmptyPage:
    page = paginator.num_pages
    profiles = paginator.page(page)
  
  left_idx = int(page) - result
  if left_idx < 1:
    left_idx = 1
  
  right_idx = int(page) + result
  if right_idx > paginator.num_pages + 1:
    right_idx = paginator.num_pages + 1
  
  page_range = range(left_idx, right_idx)
  return profiles, page_range

def search_profile(request: object) -> None:
  search_query = ''
  if request.GET.get('search_query'):
    search_query = request.GET.get('search_query')
    
  profiles = Profile.objects.filter(
    Q(name__icontains = search_query) |
    Q(short_intro = search_query)
  )

  return profiles, search_query