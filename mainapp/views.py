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
logger = logging.getLogger('app')

def home(request):
    """
    Case of GET REQUEST '/'
    home page
    """
    temp_values = {
        "subscroll":True,
        }
    return render(request, 'general/index.html', temp_values)
