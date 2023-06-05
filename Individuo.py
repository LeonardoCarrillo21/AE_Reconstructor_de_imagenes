import numpy as np
from elipse import Elipse
from Cromosoma import Cromosoma as Cr
import cv2
import random


class Individuo:

	def __init__(self, maxElipses=1000, widthImage=500,heigthImage=500):

		self.maxElipses = maxElipses
		self.widthImage = widthImage
		self.heigthImage = heigthImage
		self.cromosoma = Cr(self.maxElipses,self.widthImage,self.heigthImage)
		self.imagen = np.zeros((self.widthImage,self.heigthImage,3), np.uint8)  


	def  inicializar(self):
		self.cromosoma.inicializa()


	
		
	def pintar(self,vector):
		
		# esta linea de codigo rehace la imagen a una imagen blanca, 
		# sin embargo, lo que queremos es sobreponer las figuras sobre la anterior
		# para obtener un resultado mas cercano al que nos interesa,
		# con las figuras anteriores tambien

		self.imagen = np.zeros((self.widthImage,self.heigthImage,3), np.uint8)
		
		
		for elipse in vector:
			
			centro,radios,anguloRotacion,anguloInicio,anguloFinal,color,grosor = elipse.getValues()
			cv2.ellipse(self.imagen,
				centro,
				radios,
				anguloRotacion,
				anguloInicio,
				anguloFinal,
				color,
				grosor)
	def pintar2(self,centro,radios,anguloRotacion,anguloInicio,anguloFinal,color,grosor ):
		
		
		cv2.ellipse(self.imagen,
			centro,
			radios,
			anguloRotacion,
			anguloInicio,
			anguloFinal,
			color,
			grosor)

	def cruza(self, madre):
		papa = Individuo(self.maxElipses,self.widthImage,self.heigthImage)
		papa.inicializar()
		mama = Individuo(self.maxElipses,self.widthImage,self.heigthImage)
		mama.inicializar()
		hijos = []
		hijos =  self.cromosoma.cruzar(madre)
		
		papa.cromosoma = hijos[0]
		mama.cromosoma = hijos[1]
		
		papa.pintar(hijos[0].elipses)
		mama.pintar(hijos[1].elipses) 
		return [papa,mama]


	def mutar(self):
		#print("mutando")
		centro,radios,anguloRotacion,anguloInicio,anguloFinal,color,grosor = self.cromosoma.mutar()
		self.pintar2(centro,radios,anguloRotacion,anguloInicio,anguloFinal,color,grosor)
	def showIndividuo(self):

		cv2.imshow("Individuo : ",self.imagen)
		cv2.waitKey(0)

	def getValues(self):
		return self.cromosoma.getValues()

	def __str__():

		cad = ""
		cad += self.cromosoma.str()
		return cad