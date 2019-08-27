#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:48:47 2018

@author: jose
"""

# =============================================================================
# EJ5S3
# Escribe una función num_vocales(palabra) que devuelva el número de vocales que aparece
# en la palabra.
# =============================================================================

#Funcion que cuenta el numero de vocales en una palabra
def num_vocales(palabra):
    contador = 0
    for i in palabra:
        if i in ("aeiouAEIOU"):
            contador+=1
    return contador

#Pedimos los valores por pantalla
palabra = input("Inserte la palabra donde quieres saber las vocales: ")

#Calculamos el numero llamando a la funcion
veces = num_vocales(palabra)

#Mostramos el resultado
print("La palabra "+ palabra + " tiene " + str(veces) + " vocales")
