from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'login/$', views.log),
	url(r'verify/$', views.verify),
	url(r'home/$', views.home),
	url(r'logout/$', views.log_out),
	url(r'chatbot/$', views.chatbot),
	url(r'chat/$', views.chat),
]