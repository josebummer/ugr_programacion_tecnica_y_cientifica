#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 02:42:33 2018

@author: jose
"""

from numpy.linalg import norm
import numpy as np

class Punto:
    cont = 0
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        Punto.cont += 1
        
    def posicion(self):
        return np.array((self.x,self.y),dtype=np.float)
    
    def cuantos_puntos(self):
        return Punto.cont

nmax = 20
nmin = 3

umbral = 0.06

puntosPiernas = []
puntosNoPiernas = []
clustersPiernas = []
clustersNoPiernas = []

#Primero creamos los puntos correspondientes a las piernas.
fich = ['enPie','sentado']

for nombre in fich:
    for i in range(1,4):
        fichero = nombre+str(i)+'.dat'
        f = open(fichero,'r')
        lines = f.readlines()
        
        for line in lines:
            words = line.split(' ')
            if words[-1] == '\n':
                words.pop(-1)
            
            for j in range(2,len(words)-1,2):
                puntosPiernas.append(Punto(float(words[j]),float(words[j+1])))
        
#Ahora los puntos de no piernas
fich = ['cilindroMayor','cilindroMenor']

for nombre in fich:
    for i in range(1,4):
        fichero = nombre+str(i)+'.dat'
        f = open(fichero,'r')
        lines = f.readlines()
        
        for line in lines:
            words = line.split(' ')
            if words[-1] == '\n':
                words.pop(-1)
            
            for j in range(2,len(words)-1,2):
                puntosNoPiernas.append(Punto(float(words[j]),float(words[j+1])))      
        
#Creamos los clusters para piernas
puntosCluster = [puntosPiernas[0]]

i = 1
while i < len(puntosPiernas):    
    if (len(puntosCluster) >= nmin and len(puntosCluster) == nmax):
        clustersPiernas.append(puntosCluster.copy())
        puntosCluster.clear()
        puntosCluster.append(puntosPiernas[i])
        i += 1
        if i >= len(puntosPiernas):
            break
    
    if norm(puntosPiernas[i].posicion()-puntosCluster[-1].posicion()) < umbral:
        puntosCluster.append(puntosPiernas[i])
    elif len(puntosCluster) >= nmin:
        clustersPiernas.append(puntosCluster.copy())
        puntosCluster.clear()
        puntosCluster.append(puntosPiernas[i])
    else:
        puntosCluster.clear()
        puntosCluster.append(puntosPiernas[i])
    
    i += 1

if len(puntosCluster) >= nmin:
    clustersPiernas.append(puntosCluster.copy())

#Creamos los clusters para no piernas        
puntosCluster = [puntosNoPiernas[0]]

i = 1
while i < len(puntosNoPiernas):    
    if (len(puntosCluster) >= nmin and len(puntosCluster) == nmax):
        clustersNoPiernas.append(puntosCluster.copy())
        puntosCluster.clear()
        puntosCluster.append(puntosNoPiernas[i])
        i += 1
        if i >= len(puntosNoPiernas):
            break
    
    if norm(puntosNoPiernas[i].posicion()-puntosCluster[-1].posicion()) < umbral:
        puntosCluster.append(puntosNoPiernas[i])
    elif len(puntosCluster) >= nmin:
        clustersNoPiernas.append(puntosCluster.copy())
        puntosCluster.clear()
        puntosCluster.append(puntosNoPiernas[i])
    else:
        puntosCluster.clear()
        puntosCluster.append(puntosNoPiernas[i])
        
    i += 1
        
if len(puntosCluster) >= nmin:
    clustersNoPiernas.append(puntosCluster.copy()) 
    
#Escribimos los resultados en los ficheros de salida
f = open('clustersPiernas.dat','w')

for i,c in enumerate(clustersPiernas):
    f.write(str(i)+' '+str(len(c))+' ')
    
    for p in c:
        f.write(str(p.posicion()[0])+' '+str(p.posicion()[1]))
        f.write(' ')
    f.write('\n')
f.close()

f = open('clustersNoPiernas.dat','w')

for i,c in enumerate(clustersNoPiernas):
    f.write(str(i)+' '+str(len(c))+' ')
    
    for p in c:
        f.write(str(p.posicion()[0])+' '+str(p.posicion()[1]))
        f.write(' ')
    f.write('\n')
f.close()
    