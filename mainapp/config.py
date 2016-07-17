#!/usr/bin/env python
# encoding: utf-8
"""
config.py

Created by mmiyaji on 2016-07-17.
Copyright (c) 2016  ruhenheim.org. All rights reserved.
"""

from views import *

def home(request):
    """
    Case of GET REQUEST '/config/'
    Arguments:
    - `request`:
    """
    page=1
    span = 15
    order = "-created_at"
    page = request.GET.get('page', page)
    span = request.GET.get('span', span)
    configs,entry_count = Config.get_items(span=span, page=page)

    temp_values = {
        "target":"config",
        "title":u"Config定義一覧ページ",
        "configs":configs,
        "subscroll":True,
    }
    return render(request, 'server/index.html', temp_values)

def detail(request, target_id):
    """
    Case of GET REQUEST '/config/{id}'
    Arguments:
    - `request`:
    """
    temp_values = {
        "subscroll":True,
    }
    return render(request, 'server/detail.html', temp_values)
