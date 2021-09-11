from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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