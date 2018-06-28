# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Article, Like, Comment

from django.contrib import admin

# Register your models here.
admin.site.register(Article)
admin.site.register(Like)
admin.site.register(Comment)