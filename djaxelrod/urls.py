# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.routers import DefaultRouter
from django.conf.urls import patterns, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

urlpatterns = patterns(
    '',

    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include(router.urls)),
    (r'', include(u'social.apps.django_app.urls', namespace='social')),
    (r'', include(u'core.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
