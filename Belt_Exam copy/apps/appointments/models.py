# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..user_auth.models import User
import datetime
from datetime import date, timedelta
# Create your models here.
class AppointmentManager(models.Manager):
    def add_appt(self, postData):
        results = {'status':True, 'errors':[]}
        if postData['a_date'] == '':
            results['status'] = False
            results['errors'].append("A date is required.")
        elif datetime.datetime.strptime(postData['a_date'], '%Y-%m-%d') < datetime.datetime.now() - timedelta(days=1):
            results['status'] = False
            results['errors'].append("Please enter a scheduled current or future date.")
        if postData['a_time'] == '':
            results['status'] = False
            results['errors'].append("A scheduled time is required.")
        if postData['a_task'] == "":
            results['status'] = False
            results['errors'].append("Please enter a task or description of this activity.")
#        if postData['a_status'] == "":
#            results['status'] = False
 #           results['errors'].append("Please enter a status for this activity.")
        if results['status'] == True:
            new_appt = self.create(task=postData['a_task'], status='pending', date=postData['a_date'], time=postData['a_time'])
            new_appt.save()
        else:
            print results['errors']
        return results

    def update_appt(self, postData):
        results = {'status':True, 'errors':[]}
        print postData['up_date']
        if postData['up_date'] == '':
            results['status'] = False
            results['errors'].append("Date is required.")
        if postData['up_time'] == '':
            results['status'] = False
            results['errors'].append("Time is required.")
        if postData['up_task'] == "":
            results['status'] = False
            results['errors'].append("Please enter a task.")
        if postData['up_status'] == "":
            results['status'] = False
            results['errors'].append("Please enter a status for this activity.")
        if results['status'] == True:
            appt = self.get(id=postData['appt_id'])
            appt.task = postData['up_task']
            appt.status = postData['up_status']
            appt.date = postData['up_date']
            appt.time = postData['up_time']
            appt.save()
        else:
            print results['errors']
        return results

class Appointment(models.Model):
    task = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    objects = AppointmentManager()