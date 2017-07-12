# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User, Poke, PokeRef
from datetime import datetime, timedelta
from django.contrib import messages

# Create your views here.
def logout(request):
    request.session.clear()
    return redirect('auth:index')

def dashboard(request):
    	currentUser = User.objects.get(email=request.session['user'])
	context = {
		'self' : currentUser,
		'users' : User.objects.all().exclude(email=request.session['user']),
		'selfcount' : PokeRef.objects.values('poker').distinct().filter(pokeeref=User.objects.get(email=request.session['user'])).count(),
		'eachcount' : PokeRef.objects.filter(pokeeref=currentUser),
		'pokees': Poke.objects.all().exclude(pokee=currentUser).annotate(summed=Sum('count')).order_by('pokee'),
		'notpoked': User.objects.filter(poked=False)
	}
	print context['eachcount']
	return render(request, 'poke/dashboard.html', context)

def poke(request, id):
	updated = Poke.objects.get(pokee=User.objects.get(id=id))
	updated.count += 1
        updated.save()
