from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Policy(models.Model):
	name = models.CharField(max_length=254)
	start_date = models.DateField()
	end_date = models.DateField()
	premium = models.IntegerField()
	customer_email = models.EmailField()
	customer_name = models.CharField(max_length=254, null=True)
	maturity_amt = models.IntegerField()
	policy_id = models.CharField(max_length=254)
	pending = models.BooleanField(default=False)

class Online(models.Model):
	email = models.EmailField()
	is_free = models.BooleanField(default=True)