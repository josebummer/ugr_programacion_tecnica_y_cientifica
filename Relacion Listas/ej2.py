#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 18:58:57 2018

@author: jose
"""

import numpy as np

# =============================================================================
# Ejercicio 2
# Escribe una función contarNumerosImpares(numeros) que contabilice la cantidad
# de números impares que hay en una lista
# =============================================================================

#Funcion que devuelve el numero de números impares que tiene una lista.
def contarNumerosImpares(numeros):
    impares = 0
    
    for n in numeros:
        impares = impares+1 if n%2 != 0 else impares
        
    return impares


#Rellenamos la lista con valores aleatorios.
l = []
for i in range(20):
    l.append(np.random.randint(0,10))

#Calculamos la suma
suma = contarNumerosImpares(l)

#Mostramos el resultado
print('El numero total de impares es '+str(suma))
