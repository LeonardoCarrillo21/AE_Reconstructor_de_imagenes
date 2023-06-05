
from elipse import Elipse
import random
import numpy as np


class Cromosoma:

	
	def __init__(self, tamElipses,widthImage,heigthImage):

		self.tamElipses = tamElipses
		self.widthImage = widthImage
		self.heigthImage = heigthImage
		self.elipses = []

	def inicializa(self):
		elipses = []
		
		for i in range(self.tamElipses):
			centroElipse = (random.randrange(self.widthImage), random.randrange(self.heigthImage))
			axeslength = (random.randint(1,10),random.randint(1,10))
			color = (random.randrange(255),random.randrange(255),random.randrange(255))
			anguloRotacion = random.randrange(360)
			elipse = Elipse(centroElipse,axeslength,anguloRotacion,color) 
			elipses.append(elipse)
		self.elipses = elipses

	def mutar(self):

		modificar = random.choice(range(len(self.elipses)))
		self.elipses[modificar] = Elipse(
			(random.randrange(self.widthImage), random.randrange(self.heigthImage)),
			(random.randint(1,10),random.randint(1,10)),
			random.randrange(360),
			(random.randrange(255),random.randrange(255),random.randrange(255))
			)
		return self.elipses[modificar].getValues()

	def cruzar(self,madre):

		papa=self.elipses.copy()
		mama= madre.cromosoma.elipses.copy()
		cromosomaPapa = Cromosoma(self.tamElipses,self.widthImage, self.heigthImage)
		cromosomaMama = Cromosoma(self.tamElipses,self.widthImage, self.heigthImage)
		
		cps1 = int(np.floor((self.tamElipses-1)/3)) # punto de corte 1
		cps2 = 2*cps1 #punto de corte 2

		#se cruza de la manera padre-madre-padre
		h1 = papa[0:cps1]
		h1.extend(mama[cps1:cps2])
		h1.extend(papa[cps2:])

		#se cruza de la manera mama-papa-mama
		h2 = mama[0:cps1]
		h2.extend(papa[cps1:cps2])
		h2.extend(mama[cps2:])

		cromosomaPapa.elipses = h1
		cromosomaMama.elipses = h2

		return[cromosomaPapa,cromosomaMama]


	def getValues(self):
			
		return self.elipses

	def __str__():
		pass