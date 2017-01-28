from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from constants import *

# Create your views here.
def log(request):
	return render(request,'sign-in.html')


def verify(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')

		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('/accounts/home')
		else:
			return redirect('/accounts/login')


def home(request):
	current_user = request.user
	return render(request, 'index.html', {'user': current_user})


def log_out(request):
	logout(request)
	return redirect('/accounts/login')