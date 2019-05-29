# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework import permissions
from rest_framework import exceptions

class CUDPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        username = request.user.username
        #if request.method in permissions.SAFE_METHODS:
        if request.method in permissions.SAFE_METHODS and username == 'zaca':
            return True
        elif username == 'nosfe':
            return True
        else:
            return False