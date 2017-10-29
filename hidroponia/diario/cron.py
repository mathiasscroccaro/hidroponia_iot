from .models import Post,Amostra

def amostragem():
	Amostra.objects.create(ph=leituraSensores()[0],temp_agua=leituraSensores()[1],temp_ar=leituraSensores()[2],lux=leituraSensores()[3])

def postagem():
	Post.objects.create(ph=leituraSensores()[0],temp_agua=leituraSensores()[1],temp_ar=leituraSensores()[2],lux=leituraSensores()[3],foto='camera.png')	

def leituraSensores():

	arquivo = "/home/mathias/interface_web/hidroponia/interface/leitura.txt" 

	try:
		arq_sensores = open(arquivo,'r')	
		leitura = arq_sensores.readline().split(';')
		arq_sensores.close()
	except:
		print("Nao foi possivel abrir o arquivo %s" % (arquivo))
		leitura = [6,6,6,6]	

	return leitura
	
	#try:
	#	ser = serial.Serial('/dev/ttyUSB0', 9600)
	#	ser.timeout = 1	
	#	ser.open()
	#except:
	#	print("Nao foi possivel conectar via serial")
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
