from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from constants import *
from accounts.models import Policy
from callfriend import begin
import requests

# Create your views here.
def log(request):
	return render(request,'agent_login.html')

def verify(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_staff:
				login(request, user)
				return redirect('/agent/home')
			else:
				return redirect('/agent/login')
		else:
			return redirect('/agent/login')

def initiate_payment(request):
	return render(request, 'initiate_payment.html')


def add_payment(request):
	username = request.POST.get("username")
	email = request.POST.get("email")
	policy_name = request.POST.get("policy_name")
	policy_id = request.POST.get("p_id")
	premium = request.POST.get("premium")
	start_date = request.POST.get("start_d")
	end_date = request.POST.get("last_d")
	maturity_amt = request.POST.get("mat_amt")
	pol = Policy(customer_email=email, name=policy_name,
				policy_id=policy_id, premium=premium, start_date=start_date, 
				end_date=end_date, maturity_amt=maturity_amt)
	pol.save()
	return redirect('/agent/home/')


def home(request):
	policies = Policy.objects.all()
	return render(request, 'agent_dashboard.html', {'policies': policies})


def log_out(request):
	logout(request)
	return redirect('/agent/login')


def chat(request):
	return render(request, 'agent_chat.html')


def call(request):
	begin()
	return redirect('/agent/home')
