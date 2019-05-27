# -*- coding: utf-8 -*-

from factory.django import DjangoModelFactory
from factory import SubFactory
from datetime import datetime

from .models import Ramal

#--------------------------------------------------------------------------------------
# Factory Ramal
#--------------------------------------------------------------------------------------
class RamalFactory(DjangoModelFactory):
	class Meta:
		model = Ramal
	id = 1
	setor_id = 172
	numero = 4812
	tipo = '0'
	visivel = True