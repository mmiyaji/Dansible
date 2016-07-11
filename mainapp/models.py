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


class Meta:
    ordering = ['-created_at']
