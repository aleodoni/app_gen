# -*- coding: utf-8 -*-

from django.test import TestCase, Client, RequestFactory
from django.db import IntegrityError, DataError
from django.core.exceptions import ValidationError
from django.conf import settings

from ..factories import RamalFactory

#--------------------------------------------------------------------------------------
# Testes model Ramal
#--------------------------------------------------------------------------------------
class RamalModelTest(TestCase):

    def test_ramal_factory_ok(self):
        ramal = RamalFactory.create()
        self.assertEqual(ramal.id, 1)

    def test_ramal_factory_setor_vazio(self):
        with self.assertRaises(IntegrityError):
            ramal = RamalFactory.create(setor_id=None)

    def test_ramal_factory_numero_vazio(self):
        with self.assertRaises(IntegrityError):
            ramal = RamalFactory.create(numero=None)            

    def test_ramal_factory_numero_maior_4_digitos(self):
        if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.postgresql':
            with self.assertRaises(DataError):
                ramal = RamalFactory.create(numero='12345')            
                ramal.full_clean()
        else:
            with self.assertRaises(ValidationError):
                ramal = RamalFactory.create(numero='12345')            
                ramal.full_clean()

    def test_ramal_factory_tipo_vazio(self):
        with self.assertRaises(IntegrityError):
            ramal = RamalFactory.create(tipo=None)

    def test_ramal_factory_visivel_branco(self):
        with self.assertRaises(IntegrityError):
            ramal = RamalFactory.create(visivel=None)
