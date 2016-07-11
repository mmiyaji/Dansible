import os
from django.conf import settings
from django.conf.urls import url

from . import views

app_name = 'dansible'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^signup/$', views.signup_view, name='signup'),
]
