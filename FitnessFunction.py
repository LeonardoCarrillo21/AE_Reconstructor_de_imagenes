import numpy as np
import cv2

class FitnessFunction:

    def __init__(self, resultado, pixeles):
        #TARGET es el resultado a encontrar
        self.target = resultado
        self.pixeles = pixeles

    def evaluate(self, ind):
        aEvaluar = cv2.cvtColor(ind.imagen, cv2.COLOR_BGR2GRAY)
        diferencia = cv2.absdiff(self.target,aEvaluar)
        aptitud = np.sum(diferencia)
        #for i in range(diferencia.shape[0]):
        #    for j in range(diferencia.shape[1]):
        #        for k in range(diferencia.shape[2]):
        #            aptitud += diferencia[i,j,k]

       # for i in range(diferencia.shape[0]):
        #    for j in range(diferencia.shape[1]):
         #       aptitud += diferencia[i,j]
        
        return aptitud  