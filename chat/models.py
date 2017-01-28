from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Chat(models.Model):
   created = models.DateTimeField(auto_now_add=True)
   user = models.ForeignKey(User)
   message = models.CharField(max_length=200)

   def __unicode__(self):
       return self.message
