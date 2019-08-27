#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:27:55 2018

@author: jose
"""

import numpy as np

# =============================================================================
# Ejercicio 4
# Escribe una función numerosPares(numero) que devuelva los numeros pares que hay
# en una lista y la suma de estos elementos
# =============================================================================

#Funcion que devuelve los numeros pares que hay en una lista y la suma de
#estos elementos
def numerosPares(numeros):
    pares = 0
    suma = 0
    
    for n in numeros:
        if n%2 == 0:
            pares += 1
            suma += n
        
    return pares,suma

#Rellenamos la lista con valores aleatorios.
l = []
for i in range(20):
    l.append(np.random.randint(0,10))

#Calculamos la suma
pares,suma = numerosPares(l)

#Mostramos el resultado
print('El numero total de pares es '+str(pares))
print('La suma de estos números es '+str(suma))