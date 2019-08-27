#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 03:48:16 2018

@author: jose
"""

import numpy as np
from numpy.linalg import norm

def profundidad(A, B, P):
    #Comprobamos que el punto no corresponda a los extremos del segmento.
    if all(A==P) or all(B==P):
        return 0

    #Calculamos el angulo entre AB y AP, si es mayor de 90 grados retornamos la distancia enre A y P
    elif np.arccos(np.dot((P-A)/norm(P-A), (B-A)/norm(B-A))) > np.pi/2:
        return norm(P-A)

    #Calculamos el angulo entre AB y BP, si es mayor de 90 grados retornamos la distancia enre B y P.
    elif np.arccos(np.dot((P-B)/norm(P-B), (A-B)/norm(A-B))) > np.pi/2:
        return norm(P-B)

    #Como ambos angulos son menores o iguales a 90º sabemos que podemos hacer una proyección ortogonal del punto.
    return norm(np.cross(B-A, A-P))/norm(B-A)
    

#Calculamos y guardamos las caracteristicas de los clustersPiernas
f = open('clustersPiernas.dat','r')
fw = open('caracteristicasPiernas.dat','w')
lines = f.readlines()
        
for i,line in enumerate(lines):
    cluster = line.split(' ')
    if cluster[-1] == '\n':
        cluster.pop(-1)
    fw.write(str(i)+' ')
    p0 = np.array((cluster[2],cluster[3]),dtype=np.float)
    pn = np.array((cluster[-2],cluster[-1]),dtype=np.float)
        
    perimetro = 0.0
    profundidadm = 0.0
    for j in range(2,len(cluster)-3,2):
        p = np.array((cluster[j],cluster[j+1]),dtype=np.float)
        p1 = np.array((cluster[j+2],cluster[j+3]),dtype=np.float)
        
        perimetro += norm(p1-p)
        if (j > 2 and profundidad(p0,pn,p) > profundidadm):
            profundidadm = profundidad(p0,pn,p)
        
    fw.write(str(perimetro)+' ')
    fw.write(str(profundidadm)+' ')
    anchura = norm(pn-p0) 
    fw.write(str(anchura)+' ')
    fw.write('1\n')
fw.close()
f.close()


#Calculamos y guardamos las caracteristicas de los clustersNoPiernas
f = open('clustersNoPiernas.dat','r')
fw = open('caracteristicasNoPiernas.dat','w')
lines = f.readlines()
        
for i,line in enumerate(lines):
    cluster = line.split(' ')
    if cluster[-1] == '\n':
        cluster.pop(-1)
    fw.write(str(i)+' ')
    p0 = np.array((cluster[2],cluster[3]),dtype=np.float)
    pn = np.array((cluster[-2],cluster[-1]),dtype=np.float)
        
    perimetro = 0.0
    profundidadm = 0.0
    for j in range(2,len(cluster)-3,2):
        p = np.array((cluster[j],cluster[j+1]),dtype=np.float)
        p1 = np.array((cluster[j+2],cluster[j+3]),dtype=np.float)
        
        perimetro += norm(p1-p)
        if (j > 2 and profundidad(p0,pn,p) > profundidadm):
            profundidadm = profundidad(p0,pn,p)
        
    fw.write(str(perimetro)+' ')
    fw.write(str(profundidadm)+' ')
    anchura = norm(pn-p0) 
    fw.write(str(anchura)+' ')
    fw.write('0\n')
fw.close()
f.close()