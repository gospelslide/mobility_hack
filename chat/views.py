from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from constants import *
from accounts.models import Policy
from chat.models import Chat
import requests

# Create your views here.
def add(request):
	if request.method == "POST":
		msg = request.POST.get('msgbox', None)
		print (msg)
		c = Chat(user=request.user, message=msg)
		if msg != '':
			c.save()
			return JsonResponse({ 'msg': msg, 'user': c.user.username })            
	else:
		return HttpResponse('Request must be POST.')


def messages(request):
    c = Chat.objects.all()
    return render(request, 'messages.html', {'chat': c})