from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):    
    return render(request, 'polls/register.html')

def dojoin(request):
    if request.method == 'post' :
        id = 15
        pw = 15
        new_user = WebUser(user_id=id, user_pw=pw)
        new_user.save()    
            
    return render(request, 'polls/login.html')
# Create your views here.
