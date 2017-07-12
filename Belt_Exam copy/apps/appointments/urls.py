
from django.conf.urls import url
from . import views


app_name = 'appointments'
urlpatterns = [
    url(r'^logout$', views.logout),
    url(r'^appts$', views.appts, name='appts'),
    url(r'^add_appt$', views.add_appt, name='add_appt'),
    url(r'^appts/(?P<appt_id>\d+)$', views.update_page, name="update_page"),
    url(r'^update/(?P<appt_id>\d+)$', views.update, name="update"),
    url(r'^appts/(?P<appt_id>\d+)/delete$', views.delete, name='delete'),
]
