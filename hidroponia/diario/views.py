# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .models import Amostra
from .forms import BuscarForm
from .forms import Formulario
from .cron import leituraSensores
import matplotlib.pyplot as plt
import matplotlib
import serial

def index(request):
	return redirect('/temporeal')

def temporeal(request):	

	medidas = leituraSensores()

	dicionario = {'medidas':medidas}
	
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

def buscar(request,busca=None):
	if request.method == 'POST':
		form = BuscarForm(request.POST)
		if form.is_valid():
			inicial = form.cleaned_data['data_inicial']
			final = form.cleaned_data['data_final']
			dados = Amostra.objects.filter(data_amostragem__range=(inicial,final))
			gerarGrafico(dados)
			return redirect('/media/buscar.png')
	else:
		form = BuscarForm()

	dicionario = {}
	dicionario['form'] = form	
	return render(request,'buscar.html',dicionario)

def gerarGrafico(dados):
	
	### FIX <- corrigir timezone
	matplotlib.use("qt4agg")

	ph = []
	temp_agua = []
	temp_ar = []
	lux = []
	data = []

	for dado in dados:
		data.append(dado.data_amostragem)
		ph.append(dado.ph)
		temp_agua.append(dado.temp_agua)
		temp_ar.append(dado.temp_ar)
		lux.append(dado.lux)

	f, (ax1,ax2,ax3,ax4) = plt.subplots(4,sharex=True)
	
	ax1.plot(ph)
	ax1.set_title('Ph')
	ax2.plot(temp_agua)
	ax2.set_title('Temperatura agua')
	ax3.plot(temp_ar)
	ax3.set_title('Temperatura ar')
	ax4.plot(lux)
	ax4.set_title('Iluminância')

	plt.xticks(rotation='vertical')
	
	f.subplots_adjust(hspace=0.3)
	plt.xlabel('Tempo')
	f.savefig('./media/buscar.png')
	plt.close('all')

#def leituraSensores():
#		
#	try:
#		ser = serial.Serial('/dev/ttyUSB0', 9600)
#		ser.timeout = 1	
#		ser.open()
#	except:
#		print("Não foi possível conectar via serial")
#		return []
#
#	dados = []
#
#	ser.write("requisicao")
#
#	while (True):
#		dado = ser.read(size=1)
#		dado = str(dado,"utf-8")
#
#		if (dado == '\n'):
#			dados = int(''.join(dados))
#			print(dados)
#			break
#		else:
#			dados.append(dado)
#
#	ser.close()
#
#	return dados.split(',')
