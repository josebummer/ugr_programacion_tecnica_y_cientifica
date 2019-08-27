#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 11:52:49 2018

@author: jose
"""

# =============================================================================
# Ej 4
# Realizar un programa para una caja de un supermercado que lea un precio desde el teclado y una
# cantidad entregada por el cliente (se supone que cantidad >= precio) y obtenga en la pantalla el
# numero mnimo de monedas de 1 euro, 50 centimos, 10 centimos y 1 centimo que se deben dar de
# cambio. Por ejemplo, si precio es 1.12 euros y cantidad es 5 euros, debe dar como resultado 3
# monedas de 1 euro, 1 moneda de 50 centimos, 3 monedas de 10 centimos y 8 monedas de 1
# centimo.
# =============================================================================

#Pedimos los datos

precio = float(input("Inserte el precio: "))
cantidad = float(input("Inserte cantidad: "))

#Calculamos el cambio
cambio = round(cantidad - precio,2)
cini = cambio

#Damos valores a las variables que vamos a utilizar para asegurar que los mensajes se muestran
# correctamente

euro = ccentimos = dcentimos = mcentimos = 0

#Calculamos el cambio minimo.
if(cambio >= 1):
    euro = cambio//1
    cambio = round(cambio%1,2)

if(cambio >= 0.5):
    ccentimos = cambio//0.5
    cambio = round(cambio%0.5,2)

if(cambio >= 0.1):
    dcentimos = cambio//0.1
    cambio = round(cambio%0.1,2)
    
if(cambio >= 0.01):
    mcentimos = cambio//0.01
    
print("El cambio que tenemos que dar es ",cini)
    
if(euro > 0):
    print("Necesitamos " + str(int(euro)) + " monedas de 1 euro")
    
if(ccentimos > 0):
    print("Necesitamos " + str(int(ccentimos)) + " monedas de 50 centimos")
    
if(dcentimos > 0):
    print("Necesitamos " + str(int(dcentimos)) + " monedas de 10 centimos")
    
if(mcentimos > 0):
    print("Necesitamos " + str(int(mcentimos)) + " monedas de 1 centimo")