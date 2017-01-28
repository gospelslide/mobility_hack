from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from constants import *
import requests

# Create your views here.
def paymentform(request):
	return render(request,'payment_form.html')


def capture(request):
	url = "https://api.razorpay.com/v1/payments/"
	payment_id = request.POST.get("razorpay_payment_id")
	amount = request.POST.get("amount")
	url += payment_id
	url += "/capture/"
	resp = requests.post(url, 
		data={'amount' : amount}, auth=(RAZOR_ID, RAZOR_KEY))
	return redirect('/payment/success')


def success(request):
	return HttpResponse("Payment Successful!")