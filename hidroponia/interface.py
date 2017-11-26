import time
import serial
import pygame
import pygame.camera

DIR_IMAGEM = "./media/camera.jpg"
DIR_LEITURA = "./interface/leitura.txt"
DIR_CONTROLE = "./interface/controlar.txt"

class Interface():

	camera = False
	serial = False
	
	def __init__(self):
		pygame.init()
		pygame.camera.init()
		camera_caminho = '/dev/video0'

		serial_caminho = '/dev/ttyACM0'
		
		try:
			self.cam = pygame.camera.Camera(camera_caminho,(640,480))
			self.cam.start()		
			print('camera iniciada com sucesso em %s' % (camera_caminho))		
			self.camera = True
		except:
			print('camera nao iniciada em %s' % (camera_caminho))
		
		try:
			self.ser = serial.Serial(serial_caminho,9600)
			self.ser.timeout = 1
			print('conexao iniciada em %s com sucesso' % (serial_caminho))
			self.serial = True
		except:
			print('conexao nao iniciada em %s' % (serial_caminho))

		self.rodar()		

	def rodar(self):
		while True:
			if (self.camera):
				self.tirar_foto()
			if (self.serial):			
				self.leitura_serial()
				self.controle()
			if (self.serial is not True and self.camera is not True):
				print('Nao ha nada a fazer\nSaindo...')
				exit()		

	def tirar_foto(self):
		print('tirando foto...')
		imagem = self.cam.get_image()
		pygame.image.save(imagem,DIR_IMAGEM)	

	def leitura_serial(self):
		print('--- Leitura ---')
		dados = []
		#self.ser.write("1011")
		while (True):
			dado = self.ser.read(size=1)
			if (dado == '\n'):
				dados.pop()
				dados = ''.join(dados)
				break
			else:
				dados.append(dado)
		
		print(dados)	
		arquivo = open(DIR_LEITURA,'w')

		print(dados.split(';'))

		if (len(dados.split(';')) is not 4):
			return

		ph = float(dados.split(';')[3])*(-7.6418e-03)+1.0864e1

		temp_agua = float(dados.split(';')[2])
		temp_agua = temp_agua*temp_agua*1.3847e-5 + temp_agua*1.4471e-2 + 1.0304e1

		temp_ar = float(dados.split(';')[1])
		temp_ar = temp_ar*temp_ar*1.4096e-5 + temp_ar*1.3919e-2 + 1.0361e1

		iluminancia = 10		
	
		print("ph:%.3f temp.agua: %.3f temp.ar: %.3f" % (ph,temp_agua,temp_ar))		
				
		arquivo.write("%.3f;%.3f;%.3f;%d" % (ph,temp_agua,temp_ar,iluminancia))
		arquivo.close()

	def controle(self):
		print('--- Controle ---')		
		'''
		[ph tempAgua tempAr lux]
		'''		
		leitura = open(DIR_LEITURA,'r')
		dadosLeitura = leitura.readline().split(';')
		leitura.close()
		
		'''
		[phSetPoint tempAguaSetPoint tempArSetPoint luxSetPoint]
		'''
		controle = open(DIR_CONTROLE,'r')
		dadosControle = controle.readline().split(';')
		controle.close()

		dadosControle.pop()

		comandoSerial = []
		
		if (len(dadosLeitura) is not 4):
			print(dadosLeitura)
			return

		histerese = 0.5
		# Se ph medido for < ph setpoint
		if (float(dadosLeitura[0]) < float(dadosControle[1]) - histerese):
			comandoSerial.append(0)
			comandoSerial.append(1)
			print('ph Muito acima')
		elif (float(dadosLeitura[0]) > float(dadosControle[1]) + histerese):
			comandoSerial.append(1)
			comandoSerial.append(0)
		else:
			comandoSerial.append(0)
			comandoSerial.append(0)

		histerese = 3.0
		# Se a temperatura da agua estiver quente
		if (float(dadosLeitura[1]) > float(dadosControle[2]) + histerese):
			comandoSerial.append(0)
		elif (float(dadosLeitura[2]) > float(dadosControle[3]) + histerese):
			comandoSerial.append(0)
		elif (float(dadosLeitura[1]) < float(dadosControle[2]) - histerese):
			comandoSerial.append(1)
		else:
			comandoSerial.append(0)
		
		histerese = 500
		# Se a iluminacao estiver fraca
		if (float(dadosLeitura[3]) > float(dadosControle[0]) + histerese):
			comandoSerial.append(0)
		elif (float(dadosLeitura[3]) < float(dadosControle[0]) - histerese):
			comandoSerial.append(1)
		else:
			comandoSerial.append(0)
					

		self.ser.write(''.join(str(v) for v in comandoSerial))
				

	def __del__(self): 
		if (self.camera is True):
			print("Desligando camera")
			self.cam.stop()
		if (self.serial is True):
			print('Desligando conexao serial')
			self.ser.close()

if __name__ == '__main__':
	interface = Interface()
	interface.rodar()
