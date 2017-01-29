from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from constants import *
from accounts.models import Policy
from chat.models import Chat
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from mobility_hack import settings
from .forms import DocumentForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Chat,Document
from os import listdir
from os.path import isfile, join ,abspath
import os, sys, pickle
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

def messages_agent(request):
    c = Chat.objects.all()
    return render(request, 'messages.html', {'chat': c})        

@csrf_exempt
def Post_File(request):
    if request.method == 'POST' :
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            myfile = request.FILES['docfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            path = "C:/Django/hack/mobility_hack/media/" + str(myfile.name)
            chat2 = Chat(user=request.user, message=path,isFile=False)
            print(path)
            attach_val = 1
            chat2.save()
            uploaded_file_url = fs.url(filename)
            c = Chat.objects.all()
            form = DocumentForm()
            return render(request, "chat.html", {'chat': c,'form': form })
    else:
        uploaded_file_url = fs.url(filename)
        c = Chat.objects.all()
        form = DocumentForm()
        return render(request, "chat.html", {'chat': c,'form': form })    

def Home(request):
    c = Chat.objects.all()
    form = DocumentForm() # A empty, unbound form
    documents = Document.objects.all()
    return render(request, "chat.html", {'home': 'active', 'chat': c,'document':documents,'form': form })        

@csrf_exempt
def Post_File_Agent(request):
    if request.method == 'POST' :
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            myfile = request.FILES['docfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            path = "C:/Django/hack/mobility_hack/media/" + str(myfile.name)
            chat2 = Chat(user=request.user, message=path,isFile=False)
            print(path)
            attach_val = 1
            chat2.save()
            uploaded_file_url = fs.url(filename)
            c = Chat.objects.all()
            form = DocumentForm()
            return render(request, "agent_chat.html", {'chat': c,'form': form })
    else:
        uploaded_file_url = fs.url(filename)
        c = Chat.objects.all()
        form = DocumentForm()
        return render(request, "agent_chat.html", {'chat': c,'form': form })        