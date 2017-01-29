from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'post/$', views.add),
	url(r'messages/$', views.messages),
	url(r'messages_agent/$', views.messages_agent),
	url(r'post_file/$', views.Post_File),
	url(r'post_file_agent/$', views.Post_File_Agent),
]