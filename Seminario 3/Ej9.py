#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 12:14:50 2018

@author: jose
"""

# =============================================================================
# EJ9S3
# Escribe una función elimina_vocales(palabra) que elimine todas las vocales que aparecen en
# la palabra.
# =============================================================================

def elimina_vocales(palabra):
    npalabra = ""
    letra = "aeiouAEIOU"
    for i in palabra:
        if i not in letra:
            npalabra+=i
    return npalabra

#Pedimos los valores por pantalla
palabra = input("Inserte la palabra donde quieres eliminar las vocales: ")

#Calculamos la nueva palabra
npalabra = elimina_vocales(palabra)

#Mostramos el resultado
print("La nueva palabra es " + npalabra)