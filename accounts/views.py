from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from constants import *
import requests

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
	url = "https://api.razorpay.com/v1/payments/?count=5"
	resp = requests.get(url, data={}, 
		auth=(RAZOR_ID, RAZOR_KEY)).json()
	return render(request, 'dashboard.html', {'user': current_user, 'transactions': resp})


def log_out(request):
	logout(request)
	return redirect('/accounts/login')



def chatbot(request):
	return render(request, 'chatbot.html')


def chat(request):
	return render(request, 'chat.html')

