#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:40:53 2018

@author: jose
"""

import numpy as np

# =============================================================================
# Ejercicio 6
# Dada una matriz representada como una lista, escribe una funcion dims(lista)
# que devuelva sus dimensiones
# =============================================================================

def dims(lista):
    col = len(lista[0])
    
    fil = len(lista)
    
    return fil,col

#Rellenamos la lista con valores aleatorios.
l = []
for i in range(4):
    fil = []
    for j in range(5):
        fil.append(np.random.randint(0,10))
    l.append(fil)

#Calculamos la suma
fil,col = dims(l)

#Mostramos el resultado
print('La dimension de la matriz es '+str(fil)+'*'+str(col)+' = '+str(fil*col)+' elementos')
    