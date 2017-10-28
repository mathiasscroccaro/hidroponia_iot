from .models import Post,Amostragem

def amostragem():
	Amostragem.objects.create(ph=leituraSensores()[0],temp_agua=leituraSensores()[1],temp_ar=leituraSensores()[2],lux=leituraSensores()[3])

def postagem():
	Post.objects.create(ph=leituraSensores()[0],temp_agua=leituraSensores()[1],temp_ar=leituraSensores()[2],lux=leituraSensores()[3])	

def leituraSensores():

	arquivo = "../interface/leitura.txt" 

	try:
		arq_sensores = open(arquivo,'r')	
		leitura = arq_sensores.readline().split(';')
		arq_sensores.close()
	except:
		print("Não foi possível abrir o arquivo %s" % (arquivo))
		leitura = [0,0,0,0]	

	return leitura
	
	#try:
	#	ser = serial.Serial('/dev/ttyUSB0', 9600)
	#	ser.timeout = 1	
	#	ser.open()
	#except:
	#	print("Não foi possível conectar via serial")
	#	return [0,0,0,0]

	#dados = []

	#ser.write("requisicao")

	#while (True):
	#	dado = ser.read(size=1)
	#	dado = str(dado,"utf-8")

	#	if (dado == '\n'):
	#		dados = int(''.join(dados))
	#		print(dados)
	#		break
	#	else:
	#		dados.append(dado)

	#ser.close()

	#return dados.split(',')
