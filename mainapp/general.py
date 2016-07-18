#!/usr/bin/env python
# encoding: utf-8
"""
general.py

Created by mmiyaji on 2016-07-17.
Copyright (c) 2016  ruhenheim.org. All rights reserved.
"""

from views import *

def home(request):
    """
    Case of GET REQUEST '/'
    home page
    """
    temp_values = {
        "subscroll":True,
    }
    return render(request, 'general/index.html', temp_values)

@csrf_protect
def login_view(request):
    #強制的にログアウト
    logout(request)
    username = password = ''
    first_name = last_name = email = ''
    error_list = []
    error_target = []

    if request.GET:
        username = request.GET.get('username','')
        first_name = request.GET.get('first_name','')
        last_name = request.GET.get('last_name','')
        email = request.GET.get('email','')
        error_code = request.GET.get('error_code','')
    elif request.POST:
        if 'siginup' in request.POST:
            signup_view(request)
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    error_list.append('login_failed')
            else:
                error_list.append('login_failed')

    temp_values = {
        "error_list": error_list,
        "error_target": error_target,
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
    }
    return render(request, 'general/login.html', temp_values)

@csrf_protect
def signup_view(request):
    username = password = password2 = ''

    first_name = last_name = email = ''
    error_list = []
    error_target = []

    if request.POST:
        username = request.POST['username']
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
            else:
                error_list.append('wrong_user')
                error_list.append('signup_failed')
        else:
            error_list.append('wrong_password')
            error_list.append('signup_failed')
            error_target.append('password')
            error_target.append('password2')
        temp_values = {
            "error_list": error_list,
            "error_target": error_target,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
        }
        # query = urlencode(temp_values)
        # url = ''.join([
        #     reverse('dansible:login'),
        #     '?',
        # query])
        # return HttpResponseRedirect(url)
        return render(request, 'general/login.html', temp_values)
    else:
        raise Http404
