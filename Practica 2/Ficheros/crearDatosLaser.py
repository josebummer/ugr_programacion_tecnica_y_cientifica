# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

"""
    Vrep y OpenCV en Python

    @author: Jose Antonio Ruiz Millan
"""
import vrep
import sys
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt


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

name = input('¿Que nombre quieres ponerle al fichero de datos? ')
clock = int(input('¿Cada cuantos segundos quieres medir el laser? '))
itera = int(input('¿Cuantas iteraciones como maximo? '))

f = open(name,'w') 
for i in range(itera):
    puntosx=[] #listas para recibir las coordenadas x, y z de los puntos detectados por el laser
    puntosy=[]
    puntosz=[]
    returnCode, signalValue = vrep.simxGetStringSignal(clientID,'LaserData',vrep.simx_opmode_buffer) 
    time.sleep(clock) #esperamos un tiempo para que el ciclo de lectura de datos no sea muy rápido
    datosLaser=vrep.simxUnpackFloats(signalValue)
    
    f.write(str(i)+' ')
    f.write(str(int(len(datosLaser)/3))+' ')
    for indice in range(0,len(datosLaser),3):
        puntosx.append(datosLaser[indice+1])
        puntosy.append(datosLaser[indice+2])
        puntosz.append(datosLaser[indice])
        f.write(str(puntosx[-1])+' '+str(puntosy[-1])+' ')
    f.write('\n')
    
    print('Medida '+str(i))

f.close()