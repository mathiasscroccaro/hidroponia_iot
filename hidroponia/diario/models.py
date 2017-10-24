# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
    
	titulo = models.CharField(max_length=200)
	comentarios = models.TextField()
	data_publicacao = models.DateTimeField(default=datetime.datetime.now())
	
	historico_ph = models.FileField(upload_to='historico/%Y/%m/%d/ph')
	historico_lux = models.FileField(upload_to='historico/%Y/%m/%d/lux')
	historico_temp_agua = models.FileField(upload_to='historico/%Y/%m/%d/temp_agua')
	historico_temp_ar = models.FileField(upload_to='historico/%Y/%m/%d/temp_ar')

	def get_data(self,tipo):
		if (tipo == 1):
			return 1
		if (tipo == 2):
			return 2
		if (tipo == 3):
			return 3
		if (tipo == 4):
			return 4
	
	def __str__(self):
		return self.titulo

