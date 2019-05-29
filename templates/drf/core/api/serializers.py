# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Ramal
from .models import Setor
from .models import Funcionario
from .models import SetorFuncionarioRamal
from .models import RamalAdmin

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = ('id', 'set_nome', 'set_sigla', 'set_id_superior', 'set_ativo', 'set_tipo')        


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('id', 'matricula', 'pes_nome', 'funcao', 'setor')                

class RamalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ramal
        fields = ('id', 'numero', 'tipo', 'visivel', 'setor_id')

class SetorFuncionarioRamalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetorFuncionarioRamal
        fields = ('set_id', 'pessoa', 'set_nome', 'pes_nome', 'numero', 'tipo')

class RamalAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = RamalAdmin
        fields = ('id', 'numero', 'tipo', 'visivel', 'setor_id', 'set_nome')        