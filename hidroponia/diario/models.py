# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
    
	comentarios = models.TextField(default="(Amostragem feita automaticamente)")
	data_publicacao = models.DateTimeField(auto_now=True,editable=False)
	
	# Histórico de um dia de medições
	historico_medicoes = models.FileField(upload_to='historico/%Y/%m/%d',editable=True)

	# Foto do cultivo
	foto = models.FileField(upload_to='historico/%Y/%m/%d',editable=True)

	# Medições feitas no exato momento da criação do post
	ph = models.FloatField(editable=False,default=7.0)
	temp_agua = models.FloatField(editable=False,default=7.0)
	temp_ar = models.FloatField(editable=False,default=7.0)
	lux = models.FloatField(editable=False,default=7.0)

	def __str__(self):
		return self.comentarios


class Amostra(models.Model):
	data_amostragem = models.DateTimeField(auto_now=True,editable=False)
	
	ph = models.FloatField(editable=False)
	temp_agua = models.FloatField(editable=False)
	temp_ar = models.FloatField(editable=False)
	lux = models.FloatField(editable=False)
