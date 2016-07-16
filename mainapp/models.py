#!/usr/bin/env python
# encoding: utf-8
"""
models.py

Created by mmiyaji on 2016-07-11.
Copyright (c) 2016  ruhenheim.org. All rights reserved.
"""

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import models as auth_models

class ServerAttribute(models.Model):
    """
    属性モデル
    """
    name = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    comment = models.TextField(default="")

    isvalid = models.BooleanField(default=True, db_index=True)
    updated_at = models.DateTimeField(auto_now = True, db_index=True)
    created_at = models.DateTimeField(auto_now_add = True, db_index=True)
    @staticmethod
    def get_all():
        return ServerAttribute.objects.filter(isvalid__exact=True)
    @staticmethod
    def get_items(page=0, span=10):
        result = ServerAttribute.objects.filter(isvalid__exact=True)
        if page!=0:
            page = page*span - span
            endpage = page + span
        return result[page:endpage],result.count()
    @staticmethod
    def get_list():
        return ServerAttribute.objects.all()
    @staticmethod
    def get_by_id(id):
        result=None
        try:
            result = ServerAttribute.objects.get(id=int(id))
        except:
            result = None
        return result
    @staticmethod
    def get_by_name(name=""):
        result=None
        try:
            result = ServerAttribute.objects.filter(name=name).get()
        except:
            result = None
        return result
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/server_attribute/%s" % self.id

class Server(models.Model):
    """
    サーバモデル
    """
    name = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    comment = models.TextField(default="")

    isvalid = models.BooleanField(default=True, db_index=True)
    updated_at = models.DateTimeField(auto_now = True, db_index=True)
    created_at = models.DateTimeField(auto_now_add = True, db_index=True)
    @staticmethod
    def get_all():
        return Server.objects.filter(isvalid__exact=True)
    @staticmethod
    def get_items(page=0, span=10):
        result = Server.objects.filter(isvalid__exact=True)
        if page!=0:
            page = page*span - span
            endpage = page + span
        return result[page:endpage],result.count()
    @staticmethod
    def get_list():
        return Server.objects.all()
    @staticmethod
    def get_by_id(id):
        result=None
        try:
            result = Server.objects.get(id=int(id))
        except:
            result = None
        return result
    @staticmethod
    def get_by_name(name=""):
        result=None
        try:
            result = Server.objects.filter(name=name).get()
        except:
            result = None
        return result
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/server/%s" % self.id

class OSTemplate(models.Model):
    """
    OSテンプレートモデル
    """
    name = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    comment = models.TextField(default="")

    server_attribute = models.ForeignKey(ServerAttribute, db_index=True)

    isvalid = models.BooleanField(default=True, db_index=True)
    updated_at = models.DateTimeField(auto_now = True, db_index=True)
    created_at = models.DateTimeField(auto_now_add = True, db_index=True)
    @staticmethod
    def get_all():
        return OSTemplate.objects.filter(isvalid__exact=True)
    @staticmethod
    def get_items(page=0, span=10):
        result = OSTemplate.objects.filter(isvalid__exact=True)
        if page!=0:
            page = page*span - span
            endpage = page + span
        return result[page:endpage],result.count()
    @staticmethod
    def get_list():
        return OSTemplate.objects.all()
    @staticmethod
    def get_by_id(id):
        result=None
        try:
            result = OSTemplate.objects.get(id=int(id))
        except:
            result = None
        return result
    @staticmethod
    def get_by_name(name=""):
        result=None
        try:
            result = OSTemplate.objects.filter(name=name).get()
        except:
            result = None
        return result
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/os_template/%s" % self.id

class ConfigFile(models.Model):
    """
    設定モデル
    """
    name = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    comment = models.TextField(default="")

    file_path = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    file_permittion = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    file_owner = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    file_group = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)

    isvalid = models.BooleanField(default=True, db_index=True)
    updated_at = models.DateTimeField(auto_now = True, db_index=True)
    created_at = models.DateTimeField(auto_now_add = True, db_index=True)
    @staticmethod
    def get_all():
        return ConfigFile.objects.filter(isvalid__exact=True)
    @staticmethod
    def get_items(page=0, span=10):
        result = ConfigFile.objects.filter(isvalid__exact=True)
        if page!=0:
            page = page*span - span
            endpage = page + span
        return result[page:endpage],result.count()
    @staticmethod
    def get_list():
        return ConfigFile.objects.all()
    @staticmethod
    def get_by_id(id):
        result=None
        try:
            result = ConfigFile.objects.get(id=int(id))
        except:
            result = None
        return result
    @staticmethod
    def get_by_name(name=""):
        result=None
        try:
            result = ConfigFile.objects.filter(name=name).get()
        except:
            result = None
        return result
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/config_file/%s" % self.id

class ConfigData(models.Model):
    """
    設定モデル
    """
    name = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    comment = models.TextField(default="")

    file_path = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    file_permittion = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    file_owner = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    file_group = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)

    isvalid = models.BooleanField(default=True, db_index=True)
    updated_at = models.DateTimeField(auto_now = True, db_index=True)
    created_at = models.DateTimeField(auto_now_add = True, db_index=True)
    @staticmethod
    def get_all():
        return ConfigData.objects.filter(isvalid__exact=True)
    @staticmethod
    def get_items(page=0, span=10):
        result = ConfigData.objects.filter(isvalid__exact=True)
        if page!=0:
            page = page*span - span
            endpage = page + span
        return result[page:endpage],result.count()
    @staticmethod
    def get_list():
        return ConfigData.objects.all()
    @staticmethod
    def get_by_id(id):
        result=None
        try:
            result = ConfigData.objects.get(id=int(id))
        except:
            result = None
        return result
    @staticmethod
    def get_by_name(name=""):
        result=None
        try:
            result = ConfigData.objects.filter(name=name).get()
        except:
            result = None
        return result
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/config_data/%s" % self.id

class ConfigCommand(models.Model):
    """
    設定モデル
    """
    name = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    comment = models.TextField(default="")

    command = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    command_user = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)

    isvalid = models.BooleanField(default=True, db_index=True)
    updated_at = models.DateTimeField(auto_now = True, db_index=True)
    created_at = models.DateTimeField(auto_now_add = True, db_index=True)
    @staticmethod
    def get_all():
        return ConfigCommand.objects.filter(isvalid__exact=True)
    @staticmethod
    def get_items(page=0, span=10):
        result = ConfigCommand.objects.filter(isvalid__exact=True)
        if page!=0:
            page = page*span - span
            endpage = page + span
        return result[page:endpage],result.count()
    @staticmethod
    def get_list():
        return ConfigCommand.objects.all()
    @staticmethod
    def get_by_id(id):
        result=None
        try:
            result = ConfigCommand.objects.get(id=int(id))
        except:
            result = None
        return result
    @staticmethod
    def get_by_name(name=""):
        result=None
        try:
            result = ConfigCommand.objects.filter(name=name).get()
        except:
            result = None
        return result
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/config_command/%s" % self.id

class Config(models.Model):
    """
    設定モデル
    """
    CONFIG_CHOICES = (
        ('f', 'File'),
        ('d', 'Data'),
        ('c', 'Command'),
    )
    name = models.CharField(max_length = 100, default="", blank=False, null=False, db_index=True)
    comment = models.TextField(default="")
    config_type = models.CharField(max_length = 10, choices=CONFIG_CHOICES, default="c", blank=False, null=False, db_index=True)

    config_file = models.ForeignKey(ConfigFile, db_index=True)
    config_data = models.ForeignKey(ConfigData, db_index=True)
    config_command = models.ForeignKey(ConfigCommand, db_index=True)

    isvalid = models.BooleanField(default=True, db_index=True)
    updated_at = models.DateTimeField(auto_now = True, db_index=True)
    created_at = models.DateTimeField(auto_now_add = True, db_index=True)
    @staticmethod
    def get_all():
        return Config.objects.filter(isvalid__exact=True)
    @staticmethod
    def get_items(page=0, span=10):
        result = Config.objects.filter(isvalid__exact=True)
        if page!=0:
            page = page*span - span
            endpage = page + span
        return result[page:endpage],result.count()
    @staticmethod
    def get_list():
        return Config.objects.all()
    @staticmethod
    def get_by_id(id):
        result=None
        try:
            result = Config.objects.get(id=int(id))
        except:
            result = None
        return result
    @staticmethod
    def get_by_name(name=""):
        result=None
        try:
            result = Config.objects.filter(name=name).get()
        except:
            result = None
        return result
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/config/%s" % self.id

class Meta:
    ordering = ['-created_at']
