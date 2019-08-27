#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:32:27 2018

@author: jose
"""

# =============================================================================
# Ejercicio 9
# Escribe una funcion factores_primos(num) que devuelva una lista con la
# descomposcion en factores primos de num
# =============================================================================

#Funcion que devuelve si un numero es primo
def es_primo(num):
    i = 2
    
    while i <= num//2:
        if num%i == 0:
            return False
        
        i+=1
        
    return True

#Funcion que devuelve el siguiente numero primo empezando desde num
def next_primo(num):
    n = num+1
    while not es_primo(n):
        n+=1
        
    return n

def factores_primos(num):
    fp = []
    div = 2
    
    while num != 1:
        if num%div == 0:
            fp.append(div)
            num //= div
            div = 2
        else:
            div = next_primo(div)
            
    return fp

#Pedimos los datos por pantalla.
n = int(input('Inserte un numero:'))

#Calculamos su descomposicion en factores primos
fp = factores_primos(n)

#Mostramos los resultados
print('La descomposicion en factores primos del numero '+str(n)+' esta formada por '+str(fp))

    