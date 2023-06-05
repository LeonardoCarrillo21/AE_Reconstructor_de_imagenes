from AlgoritmoEvolutivo import AlgoritmoEvolutivo
import matplotlib.pyplot as plt
import cv2
import threading
import time
import numpy as np
import os
from datetime import datetime
#Hacemos uso de la clase Algortimo Evolutivo

   
def algoritmo():
    ae = AlgoritmoEvolutivo(300)
    ae.inicializar()
    i=0
    hoy = datetime.now()
    nombreCarpeta = ''+str(hoy.year)+'-'+str(hoy.month)+'-'+str(hoy.day)+'_'+str(hoy.hour)+' '+str(hoy.minute) 
    os.mkdir(nombreCarpeta)

    while(True):

        print("generacion: " , i)
        ae.evolucion()
        if(i%200==0):
            nombre='./'+nombreCarpeta+'/generacion '+str(i)+''+'.jpg'
            cv2.imwrite(nombre,cv2.cvtColor(ae.objPoblacion.poblacion[0].imagen,cv2.COLOR_BGR2GRAY))       
        i+=1
        if(ae.mejor<1000):
            break;
        
algoritmo = threading.Thread(target=algoritmo,name="trabajador")
algoritmo.start()