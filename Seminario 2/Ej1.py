#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 10:45:26 2018

@author: jose
"""

# =============================================================================
# EJ1
# Calcular precio de un vehículo suponiendo que tenemos que pedir como datos de entrada los
# siguientes: precio bruto del vehículo, porcentaje de ganancia del vendedor, IVA a aplicar.
# El precio base se calcula incrementando el precio bruto con el porcentaje de ganancia.
# El precio final será el precio base incrementado con el porcentaje de IVA.
# =============================================================================

#Funcion para aplicar un porcentaje a un numero
# El porcentaje debe estar entre 0 y 100

def aplicar_porcentaje(valor,porcentaje):
    return (valor*(porcentaje/100+1))

#Pedimos los datos por pantalla.

bruto = float(input("Inserte el precio bruto del vehiculo: "))
porcentaje = int(input("Inserte el procentaje de ganancia del vendedor (0-100): "))
iva = int(input("Inserte el IVA a aplicar (0-100): "))

# Calculmos el precio base.

base = aplicar_porcentaje(bruto,porcentaje)

#Calculamos el precio final

final = aplicar_porcentaje(base,iva)

# Mostramos el resultado

print("El resultado final del vehiculo es",final)
    