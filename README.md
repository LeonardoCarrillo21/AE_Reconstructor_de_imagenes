# Algoritmo Evolutivo Reconstructor de Imagenes
algortmo evolutivo recontrucción de imagenes  a escala de grises 

## Contenido
- [Descripcion](#descripcion)
- [Carcateristicas](#caracteristicas)
- [Video Muestra](#video)
- [Requisitos](#requisitos)
- [Instalación](#instalacion)
- [Uso](#uso)

## Descrpcion <a name="descripcion"></a>
Programa en python que reconstruye imagenes en escala de grises, recibiendo como entrada la imagen original, de la que generará, 300 imagenes con figuras geometricas aleatorias para convinarlas y generar nuevas, mediante las cuales, llegara a reconstruir la imagen original a travez de el paso de generaciones que se recombinan iterativamente.

## Capturas<a name="video"></a>


<hr>

## Caracteristicas <a name="caracteristicas"></a>
  - lenguaje Python
  - imagenes en escala de grises
  - se genera una carpeta con las imagenes mas aptas de cada 200 generaciones.

### Algoritmo Evolutivo
  1. Inicialización de la poblacion (300 individuos).
  2. Evaluacion de la aptitud (diferencia media de los valores con la imagen original).
  3. Selección de individuos (los 150 mas parecidos).
  4. Operadores Geneticos (variacion de 1 de las figuras geometricas) en una pequeña parte de la poblacion.
  5. Creacion de una nueva generación (150 imagenes nuevas convinadas con las 150 mas aptas).
  6. Convergencia repetir los pasos 2 a 5 hasta un minimo parecido o maximo de iteraciones o repeticiones.
  7. Seleccion de la mejor solucion (el individuo mas apto).

## Requisitos <a name="requisitos"></a>
- un equipo de computo de medios recursos (intel core i5 y 8 Gb Ram recomendado).

## Instalacion <a name="instalacion"></a>
- python
- modulo cv2

## Uso <a name="uso"></a>
1. Se modifica el codigo para la imagen de entrada
2. se ejecuta el comando "python test.py" en terminal
