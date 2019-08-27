#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 18:41:39 2018

@author: jose
"""

import numpy as np
from time import time

# =============================================================================
# Ejercicio 1
# Escribe una función sumNumLista(numeros) que sume todos los números de una
# lista. Compara el tiempo entre usar o no range.
# =============================================================================

#Funcion que dada una lista, devuelve la suma de los valores de la lista.
def sumNumLista(numeros):
    suma = 0
    
    for n in numeros:
        suma += n
        
    return suma

def sumNumListaRange(numeros):
    suma = 0
    
    for i in range(len(numeros)):
        suma += numeros[i]
        
    return suma

#Rellenamos la lista con valores aleatorios.
l = []
for i in range(20):
    l.append(np.random.randint(0,10))

#Calculamos la suma
start_time = time()
for i in range(100000):
    suma = sumNumLista(l)
elapsed_time = time() - start_time

start_time2 = time()
for i in range(100000):
    suma = sumNumListaRange(l)
elapsed_time2 = time() - start_time2

#Mostramos el resultado
print('La suma total de los elementos es '+str(suma))
print("El proceso sin range ha tardado: "+str(elapsed_time))
print("El proceso con range ha tardado: "+str(elapsed_time2))
