# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
#    User.objects.all().delete()
    return render(request, 'user_auth/index.html')

def test(request):
 #   print "I'm in test"
 #   print request.POST
    results = User.objects.test_outcome(request.POST)
 #   print results
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    if results['status'] == True:
        person = User.objects.get(email = request.POST['email'])
        messages.success(request, "Welcome, " + person.name + "!")
        return redirect('appointments:appts')

def login(request):
    print "I'm Home"
    print request.POST
    results = User.objects.login(request.POST)
    print results
    if results['status'] == False:
        messages.error(request, 'Invalid email and password combination.')
        return redirect('/')
    person = User.objects.get(email = request.POST['email'])
    messages.success(request, "Welcome, " + person.name + "!")
    return redirect('appointments:appts')

def logout(request):
    request.session.clear()
    return redirect('auth:index')


#def Dashboard(request):
   # return render(request, 'appointments:appts')

# Create your views here.
