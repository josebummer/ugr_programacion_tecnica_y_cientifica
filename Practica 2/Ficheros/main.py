#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 04:55:27 2018

@author: jose
"""

import numpy as np  
import vrep
import sys
import time
import matplotlib.pyplot as plt  
import pandas as pd
from numpy.linalg import norm
from sklearn.svm import NuSVC

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
um_persona = 0.2

# =============================================================================
# Funcion que calcula la distancia de un punto a una recta
# =============================================================================
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

# =============================================================================
# Funcion para calcular los clusters dados unos puntos
# =============================================================================
def crearClusters(puntos):
    #Inicializamos los clusters vacios y inicializamos los puntos para
    # el primer cluster como el primer punto
    clusters = []
    puntosCluster = [puntos[0]]

    #Recorremos todos los puntos excepto el primero que ya lo hemos metido
    i = 1
    while i < len(puntos):
        
        #Comprobamos si el cluster ya esta lleno y si lo esta lo guardamos
        # como cluster y seguimos comporbando los demas puntos
        if (len(puntosCluster) >= nmin and len(puntosCluster) == nmax):
            clusters.append(puntosCluster.copy())
            puntosCluster.clear()
            puntosCluster.append(puntos[i])
            i += 1
            if i >= len(puntos):
                break
        
        #Comprobamos si el punto que estamos analizando tiene menor distancia
        # que lo marcado por el umbal, y si lo cumple se añade al cluster
        if norm(puntos[i].posicion()-puntosCluster[-1].posicion()) < umbral:
            puntosCluster.append(puntos[i])
        #Si no cumple la distancia y los puntos cumplen los requisitos, creamos
        # un nuevo cluster y seguimos con el siguiente punto
        elif len(puntosCluster) >= nmin:
            clusters.append(puntosCluster.copy())
            puntosCluster.clear()
            puntosCluster.append(puntos[i])
        #En otro caso limpiamos los puntos perdiendo de 1 a 2 puntos y seguimos
        # con los siguientes
        else:
            puntosCluster.clear()
            puntosCluster.append(puntos[i])
            
        i += 1
    
    #CUando terminemos de explorar todos los puntos comprobamos si tenemos un
    # cluster final valido y si lo tenemos lo añadimos a los clusters
    if len(puntosCluster) >= nmin:
        clusters.append(puntosCluster.copy())
    
    return clusters

# =============================================================================
# Funcion para crear las caracteristicas de permitro anchura y profundidad de
# los clusters
# =============================================================================
def crearCaracteristicas(clusters):
    caracteristicas = []
    
    #Recorremos todos los clusters
    for cluster in clusters:
        #Para cada cluster obtenemos el primer y el ultimo punto
        p0 = cluster[0].posicion()
        pn = cluster[-1].posicion()
            
        perimetro = 0.0
        profundidadm = 0.0
        #Recorremos todos los puntos para un cluster
        for j in range(len(cluster)-1):
            #Obtenemos el punto actual y el siguiente
            p = cluster[j].posicion()
            p1 = cluster[j+1].posicion()
            
            #Almacenamos en el perimetro la distancia entre estos dos puntos
            perimetro += norm(p1-p)
            #Comprobamos la profundidad de este punto a la recta para ver si
            # es la mayor profundidad
            if (j > 0 and profundidad(p0,pn,p) > profundidadm):
                profundidadm = profundidad(p0,pn,p)
        
        #Calculamos la anchura
        anchura = norm(pn-p0)
        #Guardamos las caracteristicas
        valores = (perimetro,profundidadm,anchura)
        caracteristicas.append(valores)
    indices = range(len(caracteristicas))
    #Finalmente se crea un DataFrame con las caracteristicas de cada cluster
    df = pd.DataFrame.from_records(caracteristicas, columns=columnas,index=indices)
    
    return df

# =============================================================================
# Funcion para predecir si es pierna o no
# =============================================================================
def calcularPrediccion(svclassifier,caracteristicas,clusters):
    #Calculamos la prediccion con el modelo creado de SVM
    y_pred = svclassifier.predict(caracteristicas)
    #print(y_pred)
        
    xPierna = []
    yPierna = []
    xNoPierna = []
    yNoPierna = []
    #Recorremos los clusters
    for i,c in enumerate(clusters):
        #Recorremos todos los puntos de cada cluster
        for p in c:
            #Si el cluster que estamos analizando es pierna, se añade este
            # punto a los valores de pierna
            if y_pred[i] == 1:
                xPierna.append(p.posicion()[0])
                yPierna.append(p.posicion()[1])
            #En caso contrario se añade a no pierna
            else:
                xNoPierna.append(p.posicion()[0])
                yNoPierna.append(p.posicion()[1])
    
    return xPierna,yPierna,xNoPierna,yNoPierna,y_pred

# =============================================================================
# Funcion que calula los centroides de los clusters
# =============================================================================
def calcularCentroides(clusters):
    centroides = []
    
    #Recorremos todos los clusters
    for c in clusters:
        #Obtenemos los valores x e y de los puntos para cada cluster
        xs = [p.posicion()[0] for p in c]
        ys = [p.posicion()[1] for p in c]
        #Calculamos el valor x e y del centroide 
        vx = sum(xs)/len(xs)
        vy = sum(ys)/len(ys)
        
        #Añadimos el centroide del cluster
        centroides.append(Punto(vx,vy))
        
    return centroides

# =============================================================================
# Funcion que calcula si dadas dos piernas, podemos decir que son de la misma
# persona o no
# =============================================================================
def calcularPersonas(y_pred,centroides):
    xCentro = []
    yCentro = []
    #Obtenemos los centroides de los cluster que consideramos personas
    n_centroides = [p for i,p in enumerate(centroides) if y_pred[i] == 1]
    
    #Recorremos loscentroides anteriormente calculados
    i = 0
    while i < len(n_centroides)-1:
        #Obtenemos el centroide actual
        p = n_centroides[i].posicion()
        #Obtenemos el centroide siguiente
        p1 = n_centroides[i+1].posicion()
        
        #Si la distancia entre estos centroides es menor de un umbral
        # establecido, se considera de la misma persona y se añade a los puntos
        # para poder pintarlo
        if norm(p1-p) < um_persona:
            xCentro.append((p[0]+p1[0])/2)
            yCentro.append((p[1]+p1[1])/2)
            i += 1
        i += 1
        
    return xCentro,yCentro


def correlation(dataset, threshold):
    col_corr = set() # Set of all the names of deleted columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if corr_matrix.iloc[i, j] >= threshold:
                colname = corr_matrix.columns[i] # getting the name of column
                col_corr.add(colname)
                if colname in dataset.columns:
                    del dataset[colname] # deleting the column from the dataset

    print(dataset)

#################################-FIN METODOS-#################################
###############################################################################    
###############################################################################
###############################################################################
#################################-CODIGO MAIN-#################################

#Creamos los nombres de las columnas
columnas = ['indice','perimetro','profundidad','anchura','Class']

#Cargamos los datos de los clusters de piernas
piernas = pd.read_csv('caracteristicasPiernas.dat',sep=' ',names=columnas,index_col=0)

#Cargamos los datos de los cluster de no piernas
noPiernas = pd.read_csv('caracteristicasNoPiernas.dat',sep=' ',names=columnas,index_col=0)

#JUntamos todos los datos en un mismo DataFrame
datos = pd.concat([piernas,noPiernas],ignore_index=True)

# Separamos las características de la etiqueta que nos dices a la clase que corresponde
X = datos.drop('Class', axis=1)
y = datos['Class'] 

#utilizamos un Kernel Gausiano de base radial 

svclassifier = NuSVC(kernel='rbf',nu=0.4,gamma=0.9)  
svclassifier.fit(X, y)

#Comenzamos con VREP

vrep.simxFinish(-1) #Terminar todas las conexiones
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) #Iniciar una nueva conexion en el puerto 19999 (direccion por defecto)
 
if clientID!=-1:
    print ('Conexion establecida')
 
else:
    sys.exit("Error: no se puede conectar") #Terminar este script
 
#Guardar la referencia de los motores
_, left_motor_handle=vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', vrep.simx_opmode_oneshot_wait)
_, right_motor_handle=vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', vrep.simx_opmode_oneshot_wait)
 
#Guardar la referencia de la camara
_, camhandle = vrep.simxGetObjectHandle(clientID, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)
 
#acceder a los datos del laser
_, datosLaserComp = vrep.simxGetStringSignal(clientID,'LaserData',vrep.simx_opmode_streaming)


velocidad = 0.35 #Variable para la velocidad de los motores
 
#Iniciar la camara y esperar un segundo para llenar el buffer
_, resolution, image = vrep.simxGetVisionSensorImage(clientID, camhandle, 0, vrep.simx_opmode_streaming)
time.sleep(1)

plt.axis([0, 4, -2, 2])

columnas = ['perimetro','profundidad','anchura']

#Comenzamos a recibir datos del sensor
while(True):
    puntosx=[] #listas para recibir las coordenadas x, y z de los puntos detectados por el laser
    puntosy=[]
    puntosz=[]
    returnCode, signalValue = vrep.simxGetStringSignal(clientID,'LaserData',vrep.simx_opmode_buffer) 
    time.sleep(1) #esperamos un tiempo para que el ciclo de lectura de datos no sea muy rápido
    datosLaser=vrep.simxUnpackFloats(signalValue)
    
    puntos = []    
    for indice in range(0,len(datosLaser),3):
        puntosx.append(datosLaser[indice+1])
        puntosy.append(datosLaser[indice+2])
        puntosz.append(datosLaser[indice])
        #Obtenemos los puntos del laser y los guardamos
        puntos.append(Punto(puntosx[-1],puntosy[-1]))

    #Creamos los clusters
    clusters = crearClusters(puntos)
    
    #Calculamos las caracteristicas
    caracteristicas = crearCaracteristicas(clusters)
    
    #Calculamos las predicciones
    if len(caracteristicas) > 0:
        xPierna,yPierna,xNoPierna,yNoPierna,y_pred = calcularPrediccion(svclassifier,caracteristicas,clusters)

        #Calculamos los centroides
        centroides = calcularCentroides(clusters)
        xCentro,yCentro = calcularPersonas(y_pred,centroides)

        #Dibujamos los resultados
        plt.clf() 
        if len(xCentro) > 0:
            plt.plot(xCentro,yCentro,'yo')
        plt.plot(xPierna, yPierna, 'r.')
        plt.plot(xNoPierna, yNoPierna, 'b.')
        plt.show()