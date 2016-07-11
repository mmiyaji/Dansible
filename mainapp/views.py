#!/usr/bin/env python
# encoding: utf-8
'''
views.py

Created by mmiyaji on 2016-07-10.
Copyright (c) 2016  ruhenheim.org. All rights reserved.
'''
from django.shortcuts import render
from django.http import HttpResponse

import os, re, sys, commands, time, datetime, random, logging
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.utils.encoding import force_unicode, smart_str
from django.core import serializers
from django.conf import settings
from django.http import Http404

from django.template.loader import get_template
logger = logging.getLogger(__name__)

def home(request):
    """
    Case of GET REQUEST '/'
    home page
    """
    temp_values = {
        "subscroll":True,
    }
    return render(request, 'general/index.html', temp_values)

def login_view(request):
    #強制的にログアウト
    logout(request)
    username = password = ''

    login_failed = False

    if request.POST:
        username = request.POST['username'].replace(' ', '').lower()
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            login_failed = True

    temp_values = {
        "login_failed": login_failed
    }
    return render(request, 'general/login.html', temp_values)

def signup_view(request):
    #強制的にログアウト
    logout(request)
    username = password = password2 = ''

    signup_failed = False
    login_failed = False

    if request.POST:
        username = request.POST['username'].replace(' ', '').lower()
        password = request.POST['password']
        password2 = request.POST['password_confirm']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        # is_staff = request.POST['is_staff']

        if password == password2 and valid_pass(password) == 0:
            if not User.objects.filter(username=username):
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/')
        signup_failed = True
        temp_values = {
            "signup_failed": signup_failed,
            "login_failed": login_failed,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
        }
        return render(request, 'general/login.html', temp_values)
    else:
        return HttpResponseRedirect("/login/")


def valid_pass(password):
    """
    validate password
    Arguments:
    - `password`:
    """
    if len(password) < 6:
        return 1
    return 0
