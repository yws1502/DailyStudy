from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import *
from .forms import *
# Create your views here.

## Login / Logout / Register ##
def login_user(request):
    page = 'login'
    # 로그인된 상태로 URL로 접근하는 경우 예외처리
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        # front에서 보낸 데이터 확인
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            # USER 정보 확인
            user = User.objects.get(username=username)
        except:
            messages.error(request, '회원정보를 찾을 수 없습니다.')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            messages.success(request, '로그인 되었습니다.')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, '아이디 혹은 비밀번호가 틀렸습니다.')
    return render(request, 'users/login_register.html', {'page':page})

def logout_user(request):
    logout(request)
    messages.success(request, '로그아웃 되었습니다.')
    return redirect('login')

def register_user(request):
    page = 'register' # html파일 한개로 login, register page 처리하기 위한 변수
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower() # 소문자로 통일
            user.save()
            messages.success(request, '회원가입 되었습니다.')
            login(request, user)
            return redirect('profile_update') # profile 생성하는데로 이동하기
        else:
            messages.error(request, '회원가입 도중 오류가 발생하였습니다.')

    context = {'form' : form, 'page' : page}
    return render(request, 'users/login_register.html', context)

## profile ##
def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles' : profiles,
    }
    return render(request, 'users/profiles.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    algorithms = profile.algorithm_set.all()
    context = {
        'profile' : profile,
        'algorithms' : algorithms,
    }
    return render(request, 'users/profile.html', context)

def profile_update(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=profile.id)

    context = {'form' : form}
    return render(request, 'users/profile_update.html', context)

## Algorithm ##
def algorithm_create(request):
    profile = request.user.profile
    form = AlgorithmForm()
    if request.method == 'POST':
        form = AlgorithmForm(request.POST)
        if form.is_valid():
            algorithm = form.save(commit=False)
            algorithm.profile_id = profile
            profile.solved_count += 1
            profile.save()
            algorithm.save()
            return redirect('profile', pk=profile.id)

    context = {'form' : form}
    return render(request, 'users/algorithm_form.html', context)

def algorithm_update(request, pk):
    algorithm = Algorithm.objects.get(id=pk)
    form = AlgorithmForm(instance=algorithm)
    if request.method == 'POST':
        form = AlgorithmForm(request.POST, request.FILES, instance=algorithm)
        form.save()
        return redirect('profile', pk=request.user.profile.id)

    context = {'form':form, 'algorithm':algorithm}
    return render(request, 'users/algorithm_form.html', context)

def algorithm_delete(request, pk):
    profile = request.user.profile
    algorithm = Algorithm.objects.get(id=pk)

    if request.method == 'POST':
        profile.solved_count -= 1
        profile.save()
        algorithm.delete()
        return redirect('profile', pk=profile.id)

    context = {'object':algorithm}
    return render(request, 'delete_form.html', context)
