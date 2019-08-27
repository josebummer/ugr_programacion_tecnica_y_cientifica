#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 12:22:48 2018

@author: jose
"""

# =============================================================================
# EJ10S3
# Escribe una función es_inversa(palabra1, palabra2) que determine si una palabra es la
# misma que la otra pero con los caracteres en orden inverso. Por ejemplo 'absd' y 'dsba'.
# =============================================================================

def es_inversa(palabra1, palabra2):
    j = len(palabra2)-1
    
    if len(palabra1) != len(palabra2):
        return False
    
    for i in palabra1:
        if i != palabra2[j]:
            return False
        j-=1
        
    return True

#Pedimos los valores por pantalla
palabra1 = input("Inserte la primera palabra: ")
palabra2 = input("Inserte la segunda palabra: ")

#Calculamos el numero llamando a la funcion
inversa = es_inversa(palabra1,palabra2)

#Mostramos el resultado
if inversa:
    print("Las palabras son inversas entre sí")
else:
    print("Las palabras no son inversas entre sí")