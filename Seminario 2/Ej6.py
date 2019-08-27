#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 19:26:05 2018

@author: jose
"""

import numpy as np

# =============================================================================
# Ej6
# Pedir tres valores reales x1,x2,x3, obtener su máximo y su mínimo y mostrarlos por pantalla. (No
# usar la funcion max y min de python).
# =============================================================================

#Funcion que devuelve el mayor. (asumimos 3 valores)
def mayor(valores):
    h = valores[0] if valores[0] > valores[1] else valores[1]
    if valores[2] > h:
        h = valores[2]
    return h

#Funcion que devuelve el menor. (asumimos 3 valores)
def menor(valores):
    l = valores[0] if valores[0] < valores[1] else valores[1]
    if valores[2] < l:
        l = valores[2]
    return l

#Pedimos los valores
x1 = float(input("Inserte el primer numero: "))
x2 = float(input("Inserte el segundo numero: "))
x3 = float(input("Inserte el tercer numero: "))

#Sacamos el mayor
h = mayor(np.array([x1,x2,x3]))

#Sacamos el menor
l = menor(np.array([x1,x2,x3]))

#Mostramos el resultado
print("El mayor es: ",h)
print("El menor es: ",l)