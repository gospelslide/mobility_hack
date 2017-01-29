from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'login/$', views.log),
	url(r'verify/$', views.verify),
	url(r'home/$', views.home),
	url(r'logout/$', views.log_out),
	url(r'chat/$', views.chat),
	url(r'initiate_payment/$', views.initiate_payment),
	url(r'add_payment/$', views.add_payment),
	url(r'call/$', views.call),
	url(r'find/$', views.find,name='name'),
	# url(r'search/$', views.search),
]