#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:55:48 2018

@author: jose
"""

# =============================================================================
# EJ6S3
# Escribe una función vocales(palabra) que devuelva las vocales que aparecen en la palabra.
# =============================================================================

#Funcion que devuelve una cadena con las vocales que aparecen en una palabra
def vocales(palabra):
    vocales = ""
    
    if "a" in palabra or "A" in palabra:
        vocales+="a "
    if "e" in palabra or "E" in palabra:
        vocales+="e "
    if "i" in palabra or "I" in palabra:
        vocales+="i "
    if "o" in palabra or "O" in palabra:
        vocales+="o "
    if "u" in palabra or "U" in palabra:
        vocales+="u "
        
    return vocales

#Pedimos los valores por pantalla
palabra = input("Inserte la palabra donde quieres saber las vocales: ")

#Llamamos a la funcion para saber las vocales de la palabra
vc = vocales(palabra)

#Mostramos el resultado
print("La palabra "+ palabra + " tiene " + vc + " vocales")
    