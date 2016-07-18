#!/usr/bin/env python
# encoding: utf-8
"""
server.py

Created by mmiyaji on 2016-07-17.
Copyright (c) 2016  ruhenheim.org. All rights reserved.
"""

from views import *

def home(request):
    """
    Case of GET REQUEST '/server/'
    Arguments:
    - `request`:
    """
    page=1
    span = 15
    order = "-created_at"
    page = request.GET.get('page', page)
    span = request.GET.get('span', span)
    server_list,entry_count = Server.get_items(span=span, page=page)

    temp_values = {
        "target":"server",
        "title":u"サーバ定義一覧ページ",
        "server_list":server_list,
        "subscroll":True,
    }
    return render(request, 'server/index.html', temp_values)

def detail(request, target_id):
    """
    Case of GET REQUEST '/server/{id}'
    Arguments:
    - `request`:
    """
    temp_values = {
        "subscroll":True,
    }
    return render(request, 'server/detail.html', temp_values)
