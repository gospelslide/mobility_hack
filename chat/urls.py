from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'post/$', views.add),
	url(r'messages/$', views.messages),
	url(r'^post_file/$', views.Post_File),
]