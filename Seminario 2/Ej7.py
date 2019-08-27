#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 19:51:45 2018

@author: jose
"""

# =============================================================================
# Ej7
# Realizar un programa que pida el nombre de una persona, primer apellido, segundo apellido y
# que muestre por pantalla como sería el nombre completo en una sola línea. También mostrar el
# nombre completo pero al revés. Finalmente volver a descomponer el nombre completo en sus tres
# componentes y mostrarlos por pantalla.
# =============================================================================

#Pedimos los datos
nombre = input("Introduce tu nombre: ")
papellido = input("Introduce tu primer apellido: ")
sapellido = input("Introduce segundo apellido: ")

#Concatenamos en una sola cadena
completo = nombre+" "+papellido+" "+sapellido

#Mostramos el resultado
print(completo)

#Concatenamos el nombre en orden inverso
inv = sapellido+" "+papellido+" "+nombre

#Mostramos el resultado
print(inv)

#Mostramos por ultimo de nuevo los elementos por separado
print("Su nombre es",nombre)
print("Su primer apellido es",papellido)
print("Su segundo apellido es",sapellido)