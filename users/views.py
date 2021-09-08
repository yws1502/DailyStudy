from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import *
from .forms import *
# Create your views here.

## Login / Logout / Register ##
def login_user(request):
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
    return render(request, 'users/login_register.html')

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
            return redirect('#') # profile 생성하는데로 이동하기
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