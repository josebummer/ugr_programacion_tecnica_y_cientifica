#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 21:06:11 2018

@author: jose
"""

import numpy as np

# =============================================================================
# Ejercicio 10
# Escribe una funcion sumaAcumulada(numeros) a la que se le pase una lista
# de numeros y devuelva una lista en la que el elemento i-esimo se obtiene como
# la suma de los elementos de la lista entre las posiciones 0 e i. Por ejemplo,
# para [1,2,3] seria [1,3,6]
# =============================================================================

def sumaAcumulada(numeros):
    suma = 0
    l = []
    
    for n in numeros:
        suma+=n
        l.append(suma)
        
    return l

#Rellenamos la lista con valores aleatorios.
l = []
for i in range(3):
    l.append(np.random.randint(0,10))

#Calculamos la suma
nl = sumaAcumulada(l)

#Mostramos el resultado
print('La lista creada es '+str(l))
print('La nueva lista es '+str(nl))