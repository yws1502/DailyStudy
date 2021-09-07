from django.shortcuts import render

from .models import *
from .forms import *
# Create your views here.

def profile_list(request):
    profiles = Profile.objects.all()
    context = {
        'profiles' : profiles,
    }
    return render(request, 'users/profile_list.html', context)