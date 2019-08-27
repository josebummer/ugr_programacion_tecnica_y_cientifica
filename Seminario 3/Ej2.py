#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:55:03 2018

@author: jose
"""

# =============================================================================
# EJ2S3
# Escribe una función eliminar_letras(palabra, letra) que devuelva una versión de palabra que
# no contiene el carácter letra.
# =============================================================================

def eliminar_letras(palabra, letra):
    npalabra = ""
    for i in palabra:
        if(letra != i):
            npalabra+=i
    return npalabra

#Pedimos los valores por pantalla
palabra = input("Inserte la palabra donde quieres eliminar la letra: ")
letra = input("Inserte la letra a elimiar: ")

#Calculamos la nueva palabra
npalabra = eliminar_letras(palabra,letra)

#Mostramos el resultado
print("La nueva palabra es " + npalabra)