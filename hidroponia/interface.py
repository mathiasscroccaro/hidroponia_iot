import time
import serial
import pygame
import pygame.camera

DIR_IMAGEM = "./media/camera.jpg"
DIR_LEITURA = "./interface/leitura.txt"
DIR_SETPOINT = "./interface/setpoint.txt"

pygame.init()
pygame.camera.init()
camera = pygame.camera.Camera('/dev/video0',(640,480))


try:
	camera.start()
	while True:

		try:
			ser = serial.Serial('/dev/ttyUSB0', 9600)
			ser.timeout = 1	
			ser.open()

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
			
			arquivo = open(DIR_LEITURA,'w')
			arquivo.write(dados.split(';'))
			arquivo.close()
		
		except:
			print("Nao foi possivel conectar via serial")

		

		print("Atualizando imagem em tempo real...")
		
		imagem = camera.get_image()
	
		pygame.image.save(imagem,DIR_IMAGEM)
		time.sleep(1)
except KeyboardInterrupt:
	print("Desligando camera")
	camera.stop()		
