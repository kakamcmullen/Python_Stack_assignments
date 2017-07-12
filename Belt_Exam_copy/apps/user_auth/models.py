# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def test_outcome(self, postData):
        print postData
        results = {'status':True, 'errors':[]}
        if not postData['name'] or len(postData['name']) < 2:
            results['status'] = False
            results['errors'].append('Name must be between 2 and 30 characters long')
        #if not postData['name'].isalpha():
            #results['status'] = False
            #results['errors'].append('Name may not contain numbers')
        if not postData['alias'] or len(postData['alias']) < 2:
            results['status'] = False
            results['errors'].append('Alias must be between 2 and 30 characters long')
        if not postData['alias'].isalpha():
            results['status'] = False
            results['errors'].append('Alias may not contain numbers')
        if not postData['dob']:
            results['status'] = False
            results['errors'].append("Birthday is required in 10 Characters mm/dd/yyyy pattern")
        if User.objects.filter(email = postData['email']).exists():
            results['status'] = False
            results['errors'].append('email address is already registered')
        if not postData['email'] or len(postData['email']) < 5:
            results['status'] = False
            results['errors'].append('email address is not valid')
        if not EMAIL_REGEX.match(postData['email']):
            results['status'] = False
            results['errors'].append('This email address does not match the expected email pattern: joe@example.com ')
        if not postData['password'] or len(postData['password']) < 7:
            results['status'] = False
            results['errors'].append('invalid password')
        if postData['password_confirmation'] != postData['password']:
            results['status'] = False
            results['errors'].append('passwords do not match')
        if results['status'] == True:
            password = postData['password'].encode() #this is to transliterate to a unicode string
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            print hashed
            user = User.objects.create(
                name = postData['name'],
                alias = postData['alias'], 
                email = postData['email'],
                dob = postData['dob'], 
                password=hashed)
            user.save()
        return results

    def login(self, postData):
        results = {'status': True, 'errors': [], 'user': None}
        print postData
        if User.objects.filter(email = postData['email']):
            hashed = User.objects.get(email = postData['email']).password
            hashed = hashed.encode('utf-8')
            password = postData['password']
            password = password.encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                results['status'] = True
                results['results'].append("Welcome Back, " + User.objects.get(email = postData['email']).name + "!")
            else:
                results['status'] = False
        else:
            results['status'] = False
            return results

class User(models.Model):
    name = models.CharField(max_length=30)
    alias = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    dob = models.DateField()
    poked = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
