from AlgoritmoEvolutivo import AlgoritmoEvolutivo
import matplotlib.pyplot as plt
import cv2
import threading
import time
import numpy as np

fig = plt.figure("nueva ventana")
	
def algoritmo():
	ae = AlgoritmoEvolutivo(10)
	ae.inicializar()
	for i in range(3):
		print("generacion: " , i+1)
		ae.evolucion()
		plt.imshow(cv2.cvtColor(ae.mejor.imagen,cv2.COLOR_BGR2RGB),cmap=None)
		

algoritmo = threading.Thread(target=algoritmo,name="trabajador")
algoritmo.start()
plt.show()