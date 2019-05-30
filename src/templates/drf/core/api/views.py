# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token 
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from ..util.auth import CUDPermission
# from .models import <Model>

# from .serializers import <Serializer>

#--------------------------------------------------------------------------------------
# CRUD ViewSet <Your Viewset Name>
#--------------------------------------------------------------------------------------        
'''
class <Viewset CRUD>ViewSet( 
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    permission_classes = (CUDPermission,)
    authentication_classes = [TokenAuthentication, ]
    queryset = <Model>.objects.all()
    serializer_class = <Serializer>Serializer
'''

#--------------------------------------------------------------------------------------
# READ ViewSet <Your Viewset Name>
#--------------------------------------------------------------------------------------        
'''
class <Viewset>ListView(generics.ListAPIView):

    permission_classes = (CUDPermission,)
    authentication_classes = [TokenAuthentication, ]                    
    serializer_class = <Serializer>Serializer    
    queryset = <Model>.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('', )
    ordering_fields = ('', )
'''
