#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:46:21 2018

@author: jose
"""

# =============================================================================
# EJ1S3
# Escribe una función contar_letras(palabra, letra) que devuelva el número de veces que
# aparece una letra en una palabra.
# =============================================================================

#Funcion que cuenta el numero de veces que esta una letra en una palabra
def contar_letras(palabra, letra):
    contador = 0
    for i in palabra:
        if(letra == i):
            contador += 1
    return contador

#Pedimos los valores por pantalla
palabra = input("Inserte la palabra donde quieres buscar la letra: ")
letra = input("Inserte la letra a buscar: ")

#Calculamos el numero llamando a la funcion
veces = contar_letras(palabra,letra)

#Mostramos el resultado
print("La palabra "+ palabra + " tiene " + str(veces) + " veces la letra " + letra)