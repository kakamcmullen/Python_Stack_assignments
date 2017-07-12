from django.conf.urls import url
from . import views


app_name='auth'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user_registration$', views.test, name='register'),
    url(r'^user_validation$', views.login, name='login'),
    url(r'^user_logout$', views.logout, name='logout'),
#   url(r'^Dashboard$', views.Dashboard, name='Dashboard'),
]