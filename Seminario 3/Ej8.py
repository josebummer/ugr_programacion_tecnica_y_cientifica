#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 12:11:02 2018

@author: jose
"""

# =============================================================================
# EJ8S3
# Escribe una función inicio_fin_vocal(palabra) que determine si una palabra empieza y acaba
# con una vocal.
# =============================================================================

def inicio_fin_vocal(palabra):
    if palabra[0] in "aeiouAEIOU" and palabra[len(palabra)-1] in "aeiouAEIOU":
        return True
    else:
        return False
    
#Pedimos los valores por pantalla
palabra = input("Inserte la palabra: ")

#Llamamos a la funcion para saber si empieza y termina en vocal
com_fin = inicio_fin_vocal(palabra)

#Mostramos el resultado
if(com_fin):
    print("La palabra " + palabra + " comienza y termina con vocal")
else:
    print("La palabra " + palabra + " no comienza y termina con vocal")