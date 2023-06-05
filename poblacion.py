from Individuo import Individuo
import cv2
import time
class Poblacion:

    def __init__(self, size , widthImage, heigthImage):

        self.size = size
        self.widthImage = widthImage
        self.heigthImage = heigthImage


    def inicializar(self):

        poblacion = []

        for i in range(self.size):
            ind = Individuo(800, self.widthImage,self.heigthImage)
            ind.inicializar()
            ind.pintar(ind.getValues())
            poblacion.append(ind)

        self.poblacion = poblacion

