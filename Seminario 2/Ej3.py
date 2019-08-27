#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 11:41:28 2018

@author: jose
"""

# =============================================================================
# Ej 3
# Realizar un programa que lea una cantidad de horas, minutos y segundos con valores arbitrarios,
# y los transforme en una expresion de tiempo convencional en la que los minutos y segundos dentro
# del rango [0,59]. Por ejemplo, dadas 10 horas, 119 minutos y 280 segundos, debera dar como
# resultado 12 horas, 3 minutos y 40 segundos.
# =============================================================================

#Pedimos los valores

horas = int(input("Inserte las horas: "))
minutos = int(input("Inserte los minutos: "))
segundos = int(input("Inserte los segundos: "))

#Calculamos los restos y los valores

if(segundos > 59):
    coc = segundos//60
    rest = segundos%60
    minutos +=coc
    segundos = rest
    
if(minutos > 59):
    coc = minutos//60
    rest = minutos%60
    horas += coc
    minutos = rest
    
print("El valor real es: " + str(horas) + "h " + str(minutos) + "m " + str(segundos) + "s")