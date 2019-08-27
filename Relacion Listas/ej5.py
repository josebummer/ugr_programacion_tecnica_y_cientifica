#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:33:46 2018

@author: jose
"""

import numpy as np

# =============================================================================
# Ejercicio 5
# Escribe una funcion maximo(numeros) que devielva el elemento mas grande de
# una lista
# =============================================================================

#Funcion que devuelve el elemento mas grande de una lista
def maximo(numeros):
    maximo = numeros[0]
    
    for n in numeros:
        if n > maximo:
            maximo = n
    
    #return np.max(numeros)
    return maximo

#Rellenamos la lista con valores aleatorios.
l = []
for i in range(20):
    l.append(np.random.randint(0,10))

#Calculamos la suma
maximo = maximo(l)

#Mostramos el resultado
print('El numero mas grande de esta lista es '+str(maximo))