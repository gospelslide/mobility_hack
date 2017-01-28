from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Messages(models.Model):
	sender = models.EmailField(max_length=254)
	reciever = models.EmailField(max_length=254)
	message = models.CharField(max_length=1024)
	time = models.DateTimeField(auto_now_add=True)
	read = models.BooleanField(default=False)
	is_attachment = models.BooleanField(default=False)
	path = models.CharField(max_length=254)


1