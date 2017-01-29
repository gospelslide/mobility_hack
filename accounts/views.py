from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from constants import *
from chat.forms import DocumentForm
from chat.models import Chat,Document
from callfriend import begin
import requests
from scripts import rawFileProcessor
import pickle
from nltk.corpus import wordnet

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

	for i in range(5):
		resp['items'][i]['amount']/=100
	return render(request, 'dashboard.html', {'user': current_user, 'transactions': resp})


def log_out(request):
	logout(request)
	return redirect('/accounts/login')



def chatbot(request):
		# if this is a POST request we need to process the form data
	if request.method == 'GET':

		# print request.data
		query = request.GET.get('query')
		print("Query is_______" + query)

		rp = rawFileProcessor.rawFileProcessor()
		query_keywords = rp.extract_keywords(query)

		print("query_keywords")
		print (query_keywords)

		with open("data/pickleDumps/kn.pickle", "rb") as input_file:
			c = pickle.load(input_file)

		print(c)
		maxKey = 0
		for key,value in c.items():
			temp1 = value['keywords'].split("_")
			print(" keywords")
			print(temp1)
			numCommon = len(list(set(temp1).intersection(query_keywords)))
			if numCommon>maxKey:
				maxKey = key

		print(numCommon)

		def cal_similarity():
			if numCommon==0 or numCommon==1:
				tempScore = 0;
				maxScore = 0
				for key,value in c.iteritems():
					tempScore = 0;
					temp1 = value['keywords'].split("_")
					for t in temp1:
						synsetsNew = wordnet.synsets(t)[0]
						if not synsetsNew(q):
							continue
						else:
							for q in query_keywords:
								if not wordnet.synsets(q):
									continue
								else:
									print(wordnet.synsets(q))
									tempScore = tempScore + synsetsNew[0].wup_similarity(wordnet.synsets(q)[0])
							
							if tempScore>maxScore:
								print(maxScore)
								maxScore = tempScore
								print("key is :"+key)



		print("matched keywords" + c[maxKey]['keywords'])	
		answer = c[maxKey]['answer']
		print("answer is :"+answer)

		if maxKey == 0:
			answer = "Sorry I could not get you"


		# return json response
		return JsonResponse({'answer' : answer})



	# if a GET (or any other method) we'll create a blank form
	else:
		return JsonResponse({'answer' : 'invalid request'})

	return render(request, 'training/index.html', {'form': form, 'title': "Input Text Para"})
	return render(request, 'chatbot.html')


def chat(request):
	c = Chat.objects.all()
	form = DocumentForm() # A empty, unbound form
	documents = Document.objects.all()
	return render(request, "chat.html", {'home': 'active', 'chat': c,'document':documents,'form': form })        

def call(request):
	begin()
	return redirect('/accounts/chat')
