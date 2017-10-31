import time
import serial
import pygame
import pygame.camera

DIR_IMAGEM = "./media/camera.jpg"
DIR_LEITURA = "./interface/leitura.txt"
DIR_CONTROLE = "./interface/controle.txt"

class Interface():

	camera = False
	serial = False
	
	def __init__(self):
		pygame.init()
		pygame.camera.init()
		camera_caminho = '/dev/video0'

		serial_caminho = '/dev/ttyUSB0'
		
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
		self.ser.write("11")
			
		while (True):
			dado = self.ser.read(size=1)
			#dado = str(dado,"utf-8")
			if (dado == '\n'):
				dado.pop()
				dados = ''.join(dados)
				print(dados)
				break
			else:
				dados.append(dado)
		
		arquivo = open(DIR_LEITURA,'w')
		arquivo.write(dados)
		arquivo.close()

	def controle(self):
		pass		

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
