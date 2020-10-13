from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.forms import inlineformset_factory # 한번에 여러개 입력받기
from .models import *

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout

# from .filters import OrderFilter

# 메인 페이지
# def opening(request):
# 	context = {}
# 	return render(request, 'app/opening.html',context)

def home(request):
	context = {}
	return render(request, 'app/index.html',context)

# 상품보기
def search(request):
	context = {}
	return render(request, 'app/search.html',context)

# # 상품만들기
# def makeproduct(request):
# 	context = {}
# 	return render(request, 'app/makeproduct.html',context)

# 랭킹
def rank(request):
	context = {}
	return render(request, 'app/rank.html',context)

# 회원가입
def registerPage(request):
	context = {}
	return render(request, 'app/register.html',context)
    
# 로그인
def loginPage(request):
	context = {}
	return render(request, 'app/login.html',context)

# 로그아웃
def logout(request):
	context = {}
	return redirect('login')

# My Page(로그인시 이모티콘 누르면 회원 개인페이지로 이동)
def customer(request):
	context = {}
	return render(request, 'app/customer.html',context)

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
