# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User, Appointment
from datetime import datetime, timedelta
from django.contrib import messages

# Create your views here.
def logout(request):
    request.session.clear()
    return redirect('auth:index')

def appts(request):
    request.session['today'] = datetime.now().strftime('%Y-%m-%d')
    context = {
        'today_appts': Appointment.objects.filter(date=request.session['today']).order_by('date', 'time'),
        'other_appts': Appointment.objects.exclude(date=request.session['today']).order_by('date', 'time'),
    }
    return render(request, 'appointments/appts.html', context)

def add_appt(request):
    add_appt_context = {
        'a_task': request.POST['appt_task'],
        'a_date': request.POST['appt_date'],
        'a_time': request.POST['appt_time'],
    }
    add_appt_results = Appointment.objects.add_appt(add_appt_context)
    if add_appt_results['status'] == True:
        return redirect('appointments:appts')
    else:
        for error_str in add_appt_results['errors']:
            messages.add_message(request, messages.ERROR, error_str)
        return redirect('appointments:appts')

def update_page(request, appt_id):
    appt=Appointment.objects.get(id=appt_id)
    context = {
        'appt': appt,
    }
    return render(request, 'appointments/update.html', context)

def update(request, appt_id):
    if request.method == "POST":
        update_context = {
            'up_task': request.POST['update_task'],
            'up_date': request.POST['update_date'],
            'up_time': request.POST['update_time'],
            'up_status': request.POST['update_status'],
            'appt_id': appt_id,
        }
        update_appt_results = Appointment.objects.update_appt(update_context)
        if update_appt_results['status'] == True:
            return redirect('appointments:appts')
        else:
            for error_str in update_appt_results['error_list']:
                messages.add_message(request, messages.ERROR, error_str)
            id_appt = request.session['appt_id']
            return redirect('update_page', kwargs={'appt_id':id_appt})

def delete(request, appt_id):
    a_appointment = Appointment.objects.get(id=appt_id)
    a_appointment.delete()
    return redirect('appointments:appts')