#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 12:05:43 2018

@author: jose
"""

# =============================================================================
# EJ7S3
# Escribe una función mayusculas(palabra) que devuelva la palabra pasada a mayúsculas.
# =============================================================================

def mayusculas(palabra):
    mayusculas = ord('A')
    minusculas = ord('a')
    dif = minusculas - mayusculas
    npalabra = ""
    
    for i in palabra:
        if ord(i) < minusculas:
            npalabra+=i            
        else:
            npalabra+=chr(ord(i)-dif)
    return npalabra

#Pedimos los valores por pantalla
palabra = input("Inserte la palabra: ")

#Llamamos a la funcion para saber las vocales de la palabra
m = mayusculas(palabra)

#Mostramos el resultado
print("La palabra "+ palabra + " es mayusculas es " + m)