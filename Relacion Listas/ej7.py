#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:53:51 2018

@author: jose
"""
import numpy as np

# =============================================================================
# Ejercicio 7
# Escribe una funcion combinar(la,lb) que dadas dos listas devuelva una lista
# conteniendo los elementos de ambas listas ordenados de forma ascendente.
# =============================================================================

def combinar(la,lb):
    lr = []
    lr = la+lb
    lr.sort()
    
    return lr

#Rellenamos la lista con valores aleatorios.
l1 = []
for i in range(5):
    l1.append(np.random.randint(0,10))
    
l2 = []
for i in range(5):
    l2.append(np.random.randint(0,10))

#Calculamos la suma
nl = combinar(l1,l2)

#Mostramos el resultado
print('Lista 1: '+str(l1))
print('Lista 2: '+str(l2))
print('Lista compuesta y ordenada: '+str(nl))