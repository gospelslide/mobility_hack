from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from constants import *
from callfriend import begin
import requests

# Create your views here.
def view(request):
	begin()
	
	return redirect('')
