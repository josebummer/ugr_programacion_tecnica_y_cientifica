#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:18:59 2018

@author: jose
"""

# =============================================================================
# EJ4S3
# Escribe una función buscar(palabra, sub) que devuelva la posición en la que se puede
# encontrar sub dentro de palabra o -1 en caso de que no esté.
# =============================================================================

def buscar(palabra,sub):
    j = i = 0
    encontrado = False
    comienzo = -1
    
    #Recorremos la palabra
    while i < len(palabra) and not encontrado:
        #Vemos si el elemeneto de la palabra coincide con el inicio de la subcadena
        if palabra[i] == sub[j]:
            if j == 0:
                comienzo = i
            elif j == len(sub)-1:
                encontrado = True
            j+=1
        #Comprueba si el elemento de la palabra es igual que al de la subcadena pero
        # asumiendo que ya hemos comenzado.
        else:
            j = 0
            comienzo = -1

        i+=1
    
    #Si no hemos terminado de recorrer la subcadena, error
    if j < len(sub):
        return -1
    #En otro caso devolvermos el resultado
    else:
        return comienzo

#Pedimos los datos por pantalla
palabra = input("Inserte la palabra: ")
sub = input("Inserte la subcadena a buscar en la palabra: ")

#Buscamos si la subcadena existe
pos = buscar(palabra,sub)

#Mostramos el resultado
if(pos >= 0):
    print("La subcadena comienza en la posicion "+str(pos))
else:
    print("La subcadena no existe en la palabra")