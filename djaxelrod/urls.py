# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.routers import DefaultRouter
from django.conf.urls import patterns, include
from django.contrib import admin

router = DefaultRouter()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include(router.urls)),
    (r'^', include(u'core.urls')),
)


