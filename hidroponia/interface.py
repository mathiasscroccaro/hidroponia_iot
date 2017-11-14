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

		serial_caminho = '/dev/ttyS3'
		
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
		dados = []
		#self.ser.write("00")
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
		arquivo.write(dados)
		arquivo.close()

	def controle(self):
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
		
		histerese = 0.5
		# Se ph medido for < ph setpoint
		if (dadosLeitura[0] < dadosControle[0] - histerese):
			comandoSerial.append(0)
			comandoSerial.append(1)
			print('ph Muito acima')
		elif (dadosLeitura[0] > dadosControle[0] + histerese):
			comandoSerial.append(1)
			comandoSerial.append(0)
		else:
			comandoSerial.append(0)
			comandoSerial.append(0)
	
		histerese = 3.0
		# Se a temperatura da água estiver quente
		if (dadosLeitura[1] > dadosControle[1] + histerese):
			comandoSerial.append(0)
		elif (dadosLeitura[2] > dadosControle[2] + histerese):
			comandoSerial.append(0)
		elif (dadosLeitura[1] < dadosControle[1] - histerese):
			comandoSerial.append(1)
		else:
			comandoSerial.append(0)
		
		histerese = 500
		# Se a iluminação estiver fraca
		if (dadosLeitura[3] > dadosControle[3] + histerese):
			comandoSerial.append(0)
		elif (dadosLeitura[3] < dadosControle[3] - histerese):
			comandoSerial.append(1)
		else:
			comandoSerial.append(0)
		
		enviar = ""

		for i in comandoSerial:
			enviar += str(i) + ';'

		enviar.pop()
			
		self.ser.write(enviar)
				

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
