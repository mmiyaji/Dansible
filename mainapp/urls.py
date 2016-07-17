import os
from django.conf import settings
from django.conf.urls import url

from . import views
from . import server
from . import config
from . import ostemplate

app_name = 'dansible'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^server/$', server.home, name='server_home'),
    url(r'^server/(?P<target_id>\w+)/$', server.detail, name='server_detail'),
    url(r'^config/$', config.home, name='config_home'),
    url(r'^config/(?P<target_id>\w+)/$', config.detail, name='config_detail'),
    url(r'^ostemplate/$', ostemplate.home, name='ostemplate_home'),
    url(r'^ostemplate/(?P<target_id>\w+)/$', ostemplate.detail, name='ostemplate_detail'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^signup/$', views.signup_view, name='signup'),
]
