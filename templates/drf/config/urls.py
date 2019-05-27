# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    re_path(r'^api/', include('ramais.api.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
