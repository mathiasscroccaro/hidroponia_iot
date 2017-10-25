# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .forms import Formulario
import serial

def index(request):
	return redirect('/temporeal')

def temporeal(request):	

	dicionario = {'medidas':leituraSensores()}
	
	return render(request,'temporeal.html',dicionario)

def historico(request,ano=2017,mes=1,dia=1):
	posts = Post.objects.order_by('-data_publicacao')
	return render(request,'historico.html',{'posts':posts})

def cadastrar(request):
	if request.method == 'POST':
		form = Formulario(request.POST)
		if form.is_valid():
			novo_post = Post.objects.create(comentarios=form.cleaned_data['comentarios'])
			return redirect('/temporeal')
	else:
		form = Formulario()

	dicionario = {}
	dicionario['form'] = form	
	return render(request,'cadastrar.html',dicionario)

def leituraSensores():
		
	try:
		ser = serial.Serial('/dev/ttyUSB0', 9600)
		ser.timeout = 1	
		ser.open()
	except:
		print("Não foi possível conectar via serial")
		return []

	dados = []

	ser.write("requisicao")

	while (True):
		dado = ser.read(size=1)
		dado = str(dado,"utf-8")

		if (dado == '\n'):
			dados = int(''.join(dados))
			print(dados)
			break
		else:
			dados.append(dado)

	ser.close()

	return dados.split(',')
