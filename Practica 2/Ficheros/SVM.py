#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 04:55:27 2018

@author: jose
"""

import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.svm import NuSVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np

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

test_p = float(input('Introduce el porcentaje de test (0-1): '))
#dividimos en conjunto de entrenamiento y de prueba de forma aleatoria
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_p, random_state=50,stratify=y)

#utilizamos un Kernel Gausiano de base radial 
nus = np.arange(0.1,1.0,0.1)
gammas = np.arange(0.1,1.0,0.1)
# =============================================================================
# nus = [0.4]
# gammas = [0.9]
# =============================================================================
max_value = 0.0
best_nu = 0.0
best_gamma = 0.0

for nu in nus:
    for gamma in gammas:
        
        print("NU = %f\n GAMMA = %f\n" % (nu,gamma))
        
        svclassifier = NuSVC(nu=nu,gamma=gamma,kernel='rbf')  
        svclassifier.fit(X_train, y_train)
        
        # Con el clasificador obtenido hacemos la predicción sobre el conjunto de test incial
        
        y_pred = svclassifier.predict(X_test)
        
        acc_test=accuracy_score(y_test, y_pred)
        
        print("Acc_test: (TP+TN)/(T+P)  %0.2f" % acc_test)
        
        
        print("Matriz de confusión Filas: predicción Columnas: clases verdaderas")
        
        print(confusion_matrix(y_test, y_pred))
        
        '''
        La precisión mide la capacidad del clasificador en no etiquetar como positivo un ejemplo que es negativo.
        El recall mide la capacidad del clasificador para encontrar todos los ejemplos positivos.
        '''
        
        print("Precision= TP / (TP + FP), Recall= TP / (TP + FN)")
        print("f1-score es la media entre precisión y recall")
        print(classification_report(y_test, y_pred))
        
        palabras = classification_report(y_test, y_pred).split(' ') 
        
        value = float(palabras[-8])
        
        #realizando validación cruzada 5-cross validation, si hay 150 muestras
        #entonces está usandos 30 muestras de ejemplo cada vez y eso lo realiza 5 veces
        
        svclassifier2 = NuSVC(nu=nu,gamma=gamma,kernel='rbf')
        
        scores = cross_val_score(svclassifier2, X, y, cv=5,n_jobs=4,scoring='roc_auc')
        
        # exactitud media con intervalo de confianza del 95%
        print("Accuracy 5-cross validation: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
        
        value += scores.mean() 
        
        #para obligar a un porcentaje de test con cross validation
        
        cv = StratifiedShuffleSplit(n_splits=5, test_size=test_p, random_state=0)
        
        scores = cross_val_score(svclassifier2, X, y, cv=cv,n_jobs=4,scoring='roc_auc')
        
        # exactitud media con intervalo de confianza del 95%
        print("Accuracy 5-cross validation (test %0.2f): %0.2f (+/- %0.2f)" % (test_p, scores.mean(), scores.std() * 2))
        
        value += scores.mean()
        
        value /= 3
        
        if(value > max_value):
            best_nu = nu
            best_gamma = gamma
            max_value = value
print('nu= %f , gamma = %f' % (best_nu,best_gamma))