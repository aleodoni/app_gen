# -*- coding: utf-8 -*-

from django.db import models
from psycopg2 import DataError

#------------------------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------------------------
class Setor(models.Model):
	class Meta:
		verbose_name_plural = 'Setores'
		managed = False
		db_table = "v_setor"

	id = models.IntegerField(primary_key=True, db_column='set_id')
	set_nome = models.CharField(max_length=500)
	set_sigla = models.CharField(max_length=100)
	set_id_superior = models.IntegerField(blank=True, null=True)
	set_ativo = models.BooleanField()
	set_tipo = models.CharField(max_length=1)

	def __unicode__(self):
		return self.set_nome

	def __str__(self):
		return self.set_nome    

#------------------------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------------------------
class Funcionario(models.Model):
    class Meta:
        managed = False
        db_table = "v_cmcfuncionarios"

    id = models.IntegerField(primary_key=True, db_column='pessoa')
    matricula = models.IntegerField()
    pes_nome = models.CharField(max_length=500)
    funcao = models.IntegerField(blank=True, null=True)
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING)    		
#------------------------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------------------------
class Ramal(models.Model):
    
    numero = models.CharField(max_length=4) # número do ramal
    tipo = models.CharField(max_length=1) # 0 - nenhum, 1 - geral, 2 - recepção, 3 - chefia
    visivel = models.BooleanField(default=True) # se o ramal aparece ou não na list
    setor_id = models.IntegerField() # referencia o setor do ramal

    class Meta:
        verbose_name_plural = "Ramais"
#------------------------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------------------------
class SetorFuncionarioRamal(models.Model):
    class Meta:
        managed = False
        db_table = "v_setor_funcionario"
        unique_together = (( 'set_id', 'pessoa'),)

    set_id = models.IntegerField(primary_key=True)
    pessoa = models.IntegerField()
    set_nome = models.CharField(max_length=500)
    pes_nome = models.CharField(max_length=500)
    numero = models.CharField(max_length=500)
    tipo = models.CharField(max_length=1)

#------------------------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------------------------
class RamalAdmin(models.Model):
    class Meta:
        managed = False
        db_table = "v_ramal_admin"

    id = models.IntegerField(primary_key=True)
    numero = models.CharField(max_length=4)
    tipo = models.CharField(max_length=1)
    visivel = models.BooleanField(default=True)
    setor_id = models.IntegerField()
    set_nome = models.CharField(max_length=500)