# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..user_auth.models import User
# Create your models here.
class PokeManager(models.Manager):
    def addPoke(self, postData, session_id):
        results = {'status': True, 'errors': []}
        if not postData['submit']:
            results['status'] = False
            results['errors'].append('You must use the poke button to poke')
        if not postData['submit'].isdigit():
            results['status'] = False
            results['errors'].append("that doesn't work")
        return results


# Create your models here.

class Poke(models.Model):
	poker = models.ForeignKey('User_Auth.User', models.DO_NOTHING, related_name="Poker")
	pokee = models.ForeignKey('User_Auth.User', models.DO_NOTHING, related_name="Pokee")
	count = models.IntegerField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
objects = PokeManager()

class PokeRef(models.Model):
	poker = models.ForeignKey('User_Auth.User', models.DO_NOTHING, related_name="PokerRef")
	pokeeref = models.ForeignKey('User_Auth.User', models.DO_NOTHING, related_name="PokeeRef")
	count = models.IntegerField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
