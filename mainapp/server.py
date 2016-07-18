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

def detail(request, target_uuid):
    """
    Case of GET REQUEST '/server/{uuid}'
    Arguments:
    - `request`:
    """
    server = Server.get_by_uuid(target_uuid)
    if not server:
        # 見つからない場合は404エラー送出
        raise Http404
    temp_values = {
        "target":"server",
        "title":u"サーバ詳細[ %s ]" % server.name,
        "server":server,
        "subscroll":True,
        "datepicker":"datepicker",
        }
    return render(request, 'server/detail.html', temp_values)

@csrf_protect
def delete(request, target_uuid):
    """
    Case of DELETE REQUEST '/server/<target_uuid>/delete/'
    対象の削除
    DELETE/POST リクエストにのみレスポンス
    """
    request_type = request.method
    logger.debug(request_type)
    if request_type == 'GET':
        raise Http404
    elif request_type == 'OPTION' or request_type == 'HEAD':
        return HttpResponse("OK")
    elif request_type == 'POST' or request_type == 'DELETE':
        server = Server.get_by_uuid(target_uuid)
        if not server:
            # 見つからない場合は404エラー送出
            raise Http404
        server.delete()
        return HttpResponseRedirect("/server/")

@csrf_protect
def update(request, target_uuid):
    """
    Case of UPDATE REQUEST '/server/<target_uuid>/update/'
    対象の更新
    UPDATE/POST リクエストにのみレスポンス
    """
    request_type = request.method
    logger.debug(request_type)
    if request_type == 'GET':
        raise Http404
    elif request_type == 'OPTION' or request_type == 'HEAD':
        return HttpResponse("OK")
    elif request_type == 'POST' or request_type == 'UPDATE':
        server = Server.get_by_uuid(target_uuid)
        if not server:
            # 見つからない場合は404エラー送出
            raise Http404
        server.save()
        # 元のページにリダイレクト ブラウザのキャッシュで更新されてない画面が出るのを防止
        return HttpResponseRedirect("/server/%s/?update=%d" % (target_id, datetime.datetime.now().microsecond))
    else:
        raise Http404

@csrf_protect
def add(request):
    """
    Case of UPDATE REQUEST '/server/add/'
    対象の更新
    POST リクエストにのみレスポンス
    """
    request_type = request.method
    logger.debug(request_type)
    if request_type == 'GET':
        raise Http404
    elif request_type == 'OPTION' or request_type == 'HEAD':
        return HttpResponse("OK")
    elif request_type == 'POST':
        servername = request.POST['servername']
        comment = request.POST['comment']
        server = Server()
        server.name = servername
        server.comment = comment
        server.save()
        target_uuid = server.uuid
        # 元のページにリダイレクト ブラウザのキャッシュで更新されてない画面が出るのを防止
        return HttpResponseRedirect("/server/%s/?update=%d" % (target_uuid, datetime.datetime.now().microsecond))
    else:
        raise Http404
