# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-01 03:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_auto_20170629_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
    ]
