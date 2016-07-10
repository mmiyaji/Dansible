import os
from django.conf import settings
from django.conf.urls import url

from . import views

app_name = 'dansible'
urlpatterns = [
    url(r'^$', views.home, name='home'),
]
