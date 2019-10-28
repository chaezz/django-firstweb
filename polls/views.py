from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth

# 초기화면
def index(request):    
    return render(request, 'polls/login.html')

# 회원가입 버튼 클릭시
def signin(request):
    if request.method == 'POST' :        
        new_user = WebUser.object.create_user(user_id=request.POST["user_id"],name=request.POST["name"],pw=request.POST["pw"],birth=request.POST["birth"],gender=request.POST["gender"],subject=request.POST["subject"],)

    return render(request, 'polls/login.html',)

# 로그인 버튼 클릭시
def login(request):
    if request.method == 'POST' :  
        user_id = request.POST['user_id']
        pw = request.POST['pw']
        user = auth.authenticate(request, user_id=user_id, pw=pw)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'polls/login.html', {'error': 'user id or password is incorrect'})    
    else:
        return redirect('register')




def home(request):    
    return render(request, 'polls/index.html')

# 회원가입 링크
def register(request):
    return render(request, 'polls/register.html')

# 비밀번호찾기 링크
def forgotpassword(request):
    return render(request, 'polls/forgot-password.html')



# 회원 목록 test
def list(request):
    memberlist = WebUser.object.all()
    return render(request, 'polls/list.html', {'memberlist':memberlist})
# Create your views here.
