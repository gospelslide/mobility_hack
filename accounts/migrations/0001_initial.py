# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-28 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('premium', models.IntegerField()),
                ('customer_email', models.EmailField(max_length=254)),
                ('term', models.IntegerField()),
                ('maturity_amt', models.IntegerField()),
                ('policy_id', models.CharField(max_length=254)),
            ],
        ),
    ]
