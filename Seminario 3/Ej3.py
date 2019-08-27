#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:02:28 2018

@author: jose
"""

# =============================================================================
# EJ3S3
# Escribe una función mayusculas_minusculas(palabra) que devuelva una cadena en la que las
# mayúsculas y las minúsculas estén al contrario.
# =============================================================================

#Funcion para cambiar mayusculas por minusculas
def mayusculas_minusculas(palabra):
    mayusculas = ord('A')
    minusculas = ord('a')
    dif = minusculas-mayusculas
    npalabra = ""
    
    for i in palabra:
        if(ord(i) < minusculas):  
            npalabra+=chr(ord(i)+dif)
        else:
            npalabra+=chr(ord(i)-dif)
    return npalabra

#Pedimos los datos de entrada
palabra = input("Inserte la palabra: ")

#Llamamos al metodo para cambiar la palabra
npalabra = mayusculas_minusculas(palabra)

#Mostramos el resultado
print("La nueva palabra es: "+ npalabra)