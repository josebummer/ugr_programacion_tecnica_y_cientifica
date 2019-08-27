#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:25:32 2018

@author: jose
"""

import numpy as np

# =============================================================================
# Ejercicio 3
# Escribe una función numeroPares(numeros) que contabilice la cantidad
# de números pares que hay en una lista
# =============================================================================

#Funcion que devuelve el numero de números pares que tiene una lista.
def numerosPares(numeros):
    pares = 0
    
    for n in numeros:
        pares = pares+1 if n%2 == 0 else pares
        
    return pares


#Rellenamos la lista con valores aleatorios.
l = []
for i in range(20):
    l.append(np.random.randint(0,10))

#Calculamos la suma
suma = numerosPares(l)

#Mostramos el resultado
print('El numero total de pares es '+str(suma))