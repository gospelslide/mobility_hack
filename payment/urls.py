from django.conf.urls import url, include
from . import views

urlpatterns = [
		url(r'initiate/$', views.paymentform),
		url(r'capture/$', views.capture),
		url(r'success/$', views.success),
	]