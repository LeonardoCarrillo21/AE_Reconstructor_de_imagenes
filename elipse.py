

import numpy as np

class Elipse:

	def __init__(self, centerCoordenates, axesLength, anguloRotacion=0,color= (255,124,222)):

		self.centerCoordenates = centerCoordenates#(1,1)
		self.axesLength = axesLength #(5,6)
		self.anguloRotacion = anguloRotacion #0
		self.startAngle = 0
		self.endAngle= 360
		self.color =  color #(255,0,0) azul
		self.grosor = -1 #llenar la forma con el color 
		#lineType = opcional limite de la elipse
		# shift = opcional tipo de ñlimite de la elipse 
		#valor de retorno devulve una imagen

	def getValues(self):
		'''print(self.centerCoordenates)
								print(self.axesLength)
								print(self.anguloRotacion)
								print(self.startAngle)
								print(self.endAngle)
								print(self.color)
								print(self.grosor)'''
		return self.centerCoordenates,self.axesLength,self.anguloRotacion,self.startAngle,self.endAngle,self.color,self.grosor


	def __str__(self):

		cad = ""
		cad += "\nCoordenadas Centrales: " + self.centerCoordenates
		cad += "\nlongitud de los redios : " + self.axesLength
		cad += "\nangulo de anguloRotacion: " + self.anguloRotacion
		cad += "\ncolor: " + self.color

		return cad