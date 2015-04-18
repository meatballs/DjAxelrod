# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.routers import DefaultRouter
from django.conf.urls import patterns, include
from django.contrib import admin

urlpatterns = patterns('', (r'^admin/', include(admin.site.urls)),)

router = DefaultRouter()
urlpatterns += router.urls
