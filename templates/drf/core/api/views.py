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
from .models import Ramal
from .models import RamalAdmin
from .models import SetorFuncionarioRamal
from .models import Setor
from .serializers import RamalSerializer
from .serializers import RamalAdminSerializer
from .serializers import SetorFuncionarioRamalSerializer
from .serializers import SetorSerializer
from consumer.lib import helper

from cmcreport.lib.views import CMCReportView

#--------------------------------------------------------------------------------------
# 
#--------------------------------------------------------------------------------------        
class RamalViewSet( 
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    permission_classes = (CUDPermission,)
    authentication_classes = [TokenAuthentication, ]
    queryset = Ramal.objects.all()
    serializer_class = RamalSerializer

#--------------------------------------------------------------------------------------
# 
#--------------------------------------------------------------------------------------        
class SetorFuncionarioRamalListView(generics.ListAPIView):

    permission_classes = (CUDPermission,)
    authentication_classes = [TokenAuthentication, ]                    
    serializer_class = SetorFuncionarioRamalSerializer    
    queryset = SetorFuncionarioRamal.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('set_nome', 'pes_nome', )
    ordering_fields = ('set_nome', 'pes_nome', )

#--------------------------------------------------------------------------------------
# 
#--------------------------------------------------------------------------------------        
class RamalAdminListView(generics.ListAPIView):

    permission_classes = (CUDPermission,)
    authentication_classes = [TokenAuthentication, ]                    
    serializer_class = RamalAdminSerializer    
    queryset = RamalAdmin.objects.all()

#--------------------------------------------------------------------------------------
# 
#--------------------------------------------------------------------------------------        
class SetorAdminListView(generics.ListAPIView):

    permission_classes = (CUDPermission,)
    authentication_classes = [TokenAuthentication, ]                    
    serializer_class = SetorSerializer    
    queryset = Setor.objects.all()    

#--------------------------------------------------------------------------------------
# Imprime chamado
#--------------------------------------------------------------------------------------        
class GeraPdfRamais(CMCReportView):
    template_name = 'relatorio/ramais.html'
    download_filename = 'lista_ramais.pdf'

    def get_context_data(self, **kwargs):
        context = super(CMCReportView, self).get_context_data(encoding =u"utf-8", **kwargs)
        context['title'] = 'Listagem de Ramais'
        context['pagesize'] = 'A4 portrait'
        context['ramais'] = self.ramais

        return context

    def get(self, request, *args, **kwargs):

        context = super(CMCReportView, self).get_context_data(encoding =u"utf-8", **kwargs)
        parametros = request.GET.get('parametros', None)
        ramais = []
        if parametros is None:
            ramais = SetorFuncionarioRamal.objects.all().order_by('set_id', 'pes_nome')
        else:            
            ramais = SetorFuncionarioRamal.objects.filter(Q(pes_nome__icontains=parametros) | Q(set_nome__icontains=parametros) | Q(numero__icontains=parametros)).order_by('set_id', 'pes_nome')
        self.ramais = ramais

        return super(GeraPdfRamais, self).get(request, *args, **kwargs)          