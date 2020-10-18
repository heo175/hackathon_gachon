from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .forms import CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import Group

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout

# from .filters import OrderFilter

def exer(request):
    context = {}
    return render(request, 'app/exer.html',context)

# 메인 페이지
def opening(request):
	context = {}
	return render(request, 'app/opening.html',context)

def home(request):
	context = {}
	return render(request, 'app/index.html',context)

# 상품보기
def search(request):
	context = {}
	return render(request, 'app/search.html',context)

# 상품만들기
def make(request):
	context = {}
	return render(request, 'app/make.html',context)

# 랭킹
def rank(request):
	context = {}
	return render(request, 'app/rank.html',context)

# 회원가입
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, '계정생성완료' + user)

			return redirect('login')
	context = {'form':form}
	return render(request, 'app/register.html',context)
    
# 로그인
def loginPage(request):
   # if request.user.is_authenticated:
   #    return redirect('home')
   # else:
      if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')

         user = authenticate(request, username=username, password=password)  

         if user is not None:
            login(request, user)
            return redirect('home')
         else:
            messages.info(request,'아이디 혹은 비밀번호가 잘못입력되었습니다!')
      context  = { }
      return render(request, 'app/login.html',context)

# 로그아웃
def logoutUser(request):
    logout(request)
    return redirect('login')


# def createOrder(request):
# 	context = {}
# 	return render(request, 'app/order_form.html',context)

# def updateOrder(request):
# 	context = {}
# 	return render(request, 'app/dashboard.html',context)

# def deleteOrder(request, pk):
# 	order = Order.objects.get(id=pk)
# 	if request.method == "POST":
# 		order.delete()
# 		return redirect('/')
# 	context = {'item':order}
# 	return render(request, 'app/delete.html',context)


# My Page(로그인시 이모티콘 누르면 회원 개인페이지로 이동)
def mypage(request):
	context = {}
	return render(request, 'app/mypage.html',context)

# mypage_cart
def cart(request):
    context = {1, 2, 3}
    return render(request, 'app/mypage_cart.html',{"hi":context})


# mypage_history
def history(request):
    context = {}
    return render(request, 'app/mypage_history.html',context)

# mypage_modify
def modify(request):
    context = {}
    return render(request, 'app/mypage_modify.html',context)

# mypage_rank
def myrank(request):
    context = {}
    return render(request, 'app/mypage_rank.html',context)

# mypage_save
def save(request):
    context = {}
    return render(request, 'app/mypage_save.html',context)


# pay
def pay(request):
    context = {}
    return render(request, 'app/pay.html',context)
