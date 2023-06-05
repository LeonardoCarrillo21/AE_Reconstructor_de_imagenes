import numpy as np
import random
class Seleccion:

    def selecciona(self, aptitudes, k=2):                           # aptitudes, cuantos elementos seran seleccionados
        #print("--selecion--")

        vector = []

        

        aptitudes2 = aptitudes.copy()

        

        aptitudes2.sort()

        

        for i in range(k):

            indice = aptitudes.index(aptitudes2[0])

            vector.append(indice)

            aptitudes2.remove(aptitudes2[0])

            aptitudes[indice]=0
            
        return vector                                               # retorna indices [ 28,45,52,8,74] 