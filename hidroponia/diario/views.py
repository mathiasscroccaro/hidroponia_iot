# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post

def index(request):
	return redirect('/temporeal')

def temporeal(request):
	return render(request,'temporeal.html',{})

def historico(request,ano=2017,mes=1,dia=1):
	posts = Post.objects.order_by('-data_publicacao')
	return render(request,'historico.html',{'posts':posts})
	#return HttpResponse(str(dia) + "/" + str(mes) + "/" + str(ano))
