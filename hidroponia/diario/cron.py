from .models import Post,Amostra
import os

def amostragem():
	leitura = leituraSensores(arquivo = '/home/mathias/hidroponia_iot/hidroponia/interface/leitura.txt')
	Amostra.objects.create(ph=leitura[0],temp_agua=leitura[1],temp_ar=leitura[2],lux=leitura[3])

def postagem():
	Post.objects.create(ph=leituraSensores()[0],temp_agua=leituraSensores()[1],temp_ar=leituraSensores()[2],lux=leituraSensores()[3],foto='camera.png')	

def leituraSensores(arquivo = './interface/leitura.txt'):

	try:
		arq_sensores = open(arquivo,'r')	
		leitura = arq_sensores.readline().split(';')
		arq_sensores.close()
	except:
		print("Nao foi possivel abrir o arquivo %s" % (arquivo))
		leitura = [6,6,6,6]	

	return leitura
	
