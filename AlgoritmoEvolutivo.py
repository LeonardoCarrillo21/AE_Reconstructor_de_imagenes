
import cv2;
import numpy as np
from poblacion import Poblacion
from FitnessFunction import FitnessFunction
from Individuo import Individuo
from Seleccion import Seleccion
import random

#	PASOS DE LA EVOLUCION
# 1) Evaluar individuos
# 2) Seleccionar padres para cruza
# 3) Generar hijos (cruza)
# 4) Mutar a algunos
# 5) Evaluar hijos
# 6) Seleccionar miembros de la siguiente población

class AlgoritmoEvolutivo:
	
	def __init__(self, tam ):
																#	DECLARACIONES
		self.tam = tam									# cuantos elipses pintar
		nombreImagen='./goku.jpg'
		self.imagen = cv2.resize(cv2.imread(nombreImagen,0),(200,200))					# leer imagen
		self.objPoblacion= None									# declarar una poblacion


																#	INICIALIZACIONES
	def inicializar(self):
		#ancho, alto , colores= self.imagen.shape               	# separamos la imagen 
		alto, ancho = self.imagen.shape               	# separamos la imagen 
		objPoblacion = Poblacion(self.tam, ancho, alto)			# definimos la poblacion pero no la inicializamos
		
		objPoblacion.inicializar()								# iniicalizamos la poblacion
		#print("poblacion incializada")							# control
		self.objPoblacion = objPoblacion						# hacemos propia la poblacion

		self.seleccion = Seleccion()							# inicializamos la seleccion

		self.ff = FitnessFunction(self.imagen, ancho*alto)	# inicializamos la Funcion de aptitud
																# (imagen a comparar, dimensiones )
																	
																#	PARTE PRINCIPAL
	def evolucion(self):										# como vamos a evolucionar
		#print("Entrando a evolucion...")						# Control

		if self.objPoblacion is None:							# Control de problemas
 			print("iniciar la poblacion")						# Control
 			return												# Control

 																# 1) EVALUAR
 		# Mediante el metodo ff de la clase	
		poblacion = self.objPoblacion.poblacion					# guardamos una variable local de nuestra poblacion
		#print("tam Poblacion: " , len(poblacion))
		#print("Entrando a FF")
		aptitudes = [self.ff.evaluate(ind) 						# evaluamos cada individuo y guardamos un vector de aptitudes por individuo
 					for ind in poblacion]						# [aptitud, aptitud , ... ,aptitud]

 																# 2) SELECCIONAR
		k = int(len(poblacion)/2)										# la mitad de la poblacion
		if k%2 ==1:												# tomamos la mitad mayor 
 			k+=1
		indx = self.seleccion.selecciona(aptitudes,k)			# la mejor mitad [ ind, ind,ind ] - [ind, ind,ind]
 																# 3)CRUZA
		descendencia = []										# donde guardar los hijos
		#print("indx longitud: " , len(indx))
		#print("valor de k: ", k)
		for i in list(range(0,k-1,2)):							# recorremos la mitad mayor
			ip = indx[i]										# guardamos el indice padre
			im = indx[i+1]										# guardamos la indice madre
			papa = poblacion[ip]								# obtenemos el papa de la poblacion local
			mama = poblacion[im]								# obtenemos la mama de la poblacion local
			hijos = papa.cruza(mama)							# guardamos los cromosomas de la cruza [CR,CR]
			
			mama.pintar(hijos[1].cromosoma.elipses)				# la mama repinta su imagen hijos[0], -->hijos[1]<---
			descendencia.append(hijos[0])							# guardamos los cromosomas hijos
			descendencia.append(mama)							# guardamos los cromosomas hijos

 																# 4) MUTACION
		totalMutar = int(np.ceil(len(descendencia)*0.1))		# cuantos hijos son el 10% de la descendencia
		for i in range(totalMutar):								# por mutado
 			idx = random.choice(range(len(descendencia)))		# uno aleatorio
 			descendencia[idx].mutar()							# mutar
 																# 5) EVALAR HIJOS 
 																# 6) Seleccionar miembros de la sigueinte generacion
		for hijo in descendencia:								# se agregan lops hijos a la poblacion
 			poblacion.append(hijo)								#
		

		aptitudes = [self.ff.evaluate(ind)						# se evalua nuevamente la poblacion
				for ind in poblacion]						# con la FitenssFunction.evatuale()
																# elitismo
 																# se saca el indices de la mejor aptitud
		#idxMejor = np.argmax(aptitudes)							# indice de la mejor aptitud
		idxMejor = np.argmin(aptitudes)
		self.mejor=min(aptitudes)
		print("mejor: ", self.mejor)
		siguientePoblacion = []
		siguientePoblacion.append(poblacion[idxMejor])		# el mejor pasa directo
 																# seleccionamos a los miembros de
 																# la siguiente generacion
		
		idx = self.seleccion.selecciona(aptitudes,self.tam-1)	# obtenemos la mitad de los mejores de las aptiudes
		
		for i in idx:											# por indice agregamos a la poblacion los mejores 
 			siguientePoblacion.append(poblacion[i])
		
		self.objPoblacion.poblacion = siguientePoblacion		# actualizamos la poblacion de clase