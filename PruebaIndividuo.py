from Individuo import Individuo
import matplotlib.pyplot as plt
import numpy as np
import cv2

def aver():
	individuo= Individuo()
	individuo.inicializar()
	individuo.pintar(individuo.getValues())

	plot , (a,b) = plt.subplots(1,2)
	a.imshow(individuo.imagen)
	imagen1 = cv2.imread('./azul.jpg')
	imagen2 = np.zeros((500,500,3), np.uint8)
	res = cv2.absdiff(individuo.imagen, imagen2)
	print(res.shape)
	aptitud = 0
	for i in range(imagen2.shape[0]):
		for j in range(imagen2.shape[1]):
			for k in range(imagen2.shape[2]):
				aptitud += res[i,j,k]
	print("suma: " ,aptitud)
	b.imshow(res)
	plt.show()

aver()