#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 11:21:09 2018

@author: jose
"""

#Importamos los paquetes necesarios
import math
import numpy as np

# =============================================================================
# Ej2
# Dados tres números x1, x2, x3, calcular la desviación típica respecto a su media aritmética.
# =============================================================================

#Funcion para calcular la media (asumimos que vienen 3 valores)
def media(valores):
    return (valores[0]+valores[1]+valores[2])/3

#Funcion para calcular la desviacion tipica. (asumimos que tenemos 3 valores)
def desviacion_tipica(valores):
    m = media(valores)
    
    div = (valores[0]-m)**2
    div += (valores[1]-m)**2
    div += (valores[2]-m)**2
    div /= 3
    
    return math.sqrt(div)

# Pedimos los distintos valores

x1 = float(input("Ingrese el primer numero: "))
x2 = float(input("Ingrese el segundo numero: "))
x3 = float(input("Ingrese el tercer numero: "))

#Calculamos la desviacio tipica

desv = desviacion_tipica(np.array([x1,x2,x3]))

#Mostramos el resultado

print("La desviacion tipica de " + str(x1) + " " + str(x2) + " " + str(x3) + " es: " + str(desv))