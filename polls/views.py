from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import WebUser, Book, Rentlist
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import get_object_or_404

# 초기화면
def index(request):    
    return render(request, 'polls/login.html')

# 회원가입 버튼 클릭시
def signin(request):
    if request.method == 'POST' :        
        new_user = WebUser(user_id=request.POST["user_id"],name=request.POST["name"],pw=request.POST["pw"],birth=request.POST["birth"],gender=request.POST["gender"],subject=request.POST["subject"],)
        print("회원가입성공")        
        new_user.save()
    return render(request, 'polls/login.html')

# 로그인 버튼 클릭시
def login(request):
    m = WebUser.objects.get(user_id=request.POST['user_id'])
    if m.pw == request.POST['pw']:
        # request.session['user_id'] = m.id 
        user_id = request.POST["user_id"]
        pw = request.POST["pw"]       
        response = redirect('index1')
        response.set_cookie('user_id',user_id)
        response.set_cookie('pw',pw)                
        return response
    else:
        return HttpResponse("Your username or password didn't match.")
   
# test
def index1(request):
    Books = Book.objects.all()
    context = { 'Books' : Books}    
    return render(request, 'polls/index1.html', context)

def bookdetail(request,pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'polls/bookdetail.html', {'book': book})

def rent(request,pk):
    book = Book.objects.get(pk=pk)
    selection = request.POST['rent']
    rentlist = Rentlist(user_id = request.COOKIES.get('user_id'), isbn = book, date = "현재날짜")
    rentlist.save()
    return HttpResponse(" 회원님의 " + book.name + " 책의 대여가 완료되었습니다.") 

def rentlist1(request):
    booklist = Rentlist.objects.filter(user_id = request.COOKIES.get('user_id'))
    context = {'booklist' : booklist}
    return render(request, 'polls/test.html', context)


def test1(request):
    book = Book.objects.get(isbn = 6543)
    rentlist = Rentlist.objects.create(user_id = request.COOKIES.get('user_id'), isbn = book, date = "현재날짜")
    rentlist.save()    
    return HttpResponse(str(book.isbn) + "입니다.")

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
