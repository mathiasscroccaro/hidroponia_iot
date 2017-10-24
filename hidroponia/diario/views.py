# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Visualização do temporeal.")

def historico(request,ano=2017,mes=1,dia=1):
	return HttpResponse(str(dia) + "/" + str(mes) + "/" + str(ano))
