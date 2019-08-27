#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:03:27 2018

@author: jose
"""

# =============================================================================
# Ejercicio 8
# La transpuesta de una matriz se obtiene intercambiando filas y columa.
# Escribe una funcion que devuelva la traspuesta de una matriz
# =============================================================================

def transpuesta(m):
    l2 = []

    for i in range(len(m[0])):
        col = []
        for j in range(len(m)):
            col.append(m[j][i])
        l2.append(col)
    return l2
    
l = [[1,2,3,10],[4,5,6,11],[7,8,9,12]]

tras = transpuesta(l)

print(l)
print(tras)