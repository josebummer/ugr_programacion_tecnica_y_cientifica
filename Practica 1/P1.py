#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 22:55:20 2018

@author: jose
"""

import csv
import numpy as np
from bs4 import BeautifulSoup
from collections import defaultdict
import matplotlib.pyplot as plt

# =============================================================================
# Funcion para limpiar un fichero csv y dejar solo los datos que nos interesan
# =============================================================================
def limpiaFichero(n):
    name = n+".csv"
    
    #Abrimos el fichero
    ficheroInicial=open(name,"r", encoding="windows-1250")

    #Leemos el contenido
    cadenaPob=ficheroInicial.read()
    
    #Cerramos el fichero de entrada
    ficheroInicial.close()

    #Nos quedamos con los datos que nos interesan
    primero=cadenaPob.find("Total Nacional")
    ultimo=cadenaPob.find("Notas")
    
    #Recortamos la cadena completa cojiendo los datos que nos interesan
    cadenaFinal=cadenaPob[primero:ultimo]
    
    #Creamos la cabecera a nuestro gusto
    cabecera="Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011;H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010"
    
    name = n+"Final.csv"
    
    #Abrimos el fichero de salida
    ficheroFinal=open(name, "w",encoding="windows-1250")
    
    #Escribimos el resultado
    ficheroFinal.write(cabecera+'\n'+cadenaFinal)
    
    #Cerramos el fichero
    ficheroFinal.close()
 
# =============================================================================
# Funcion para leer un fichero csv
# Devuelve el contenido del mismo
# =============================================================================
def readFich(n):
    name = n+".csv"
    #Abrimos el fichero de entrada
    with open(name, encoding="windows-1250") as csvarchivo:
        #Obtenemos el iterador al archivo
        entrada = csv.reader(csvarchivo, delimiter=';')
        res = []
        #Lo recorremos y por cada una de los registros lo añadimos a la lista que devolvemos
        for reg in entrada:
            #Esta comprobacion la realizo porque vi que metía una ultima columna vacia
            if(reg[-1]):
                res.append(reg)
            else:
                res.append(reg[:-1])
    
    return res

# =============================================================================
# Funcion para el ejercicio 1
# Calcula la variacion absoluta y relativa del total de los datos
# Devuelve una matriz con el resultado
# =============================================================================
def vabsYvrel(datos):
    #Cojo solo los datos que me interesan, en mi caso los correspondientes a los datos totales
    d = [e[:9] for e in datos]
    #Elimino la cabecera
    d.pop(0)
        
    #Creo la nueva cabecera
    cabecera=["Provincia","2017","2016","2015","2014","2013","2012","2011","2017","2016","2015","2014","2013","2012","2011"]
    
    #Guardo las etiquetas de cada una de las filas
    l = [[e[0]] for e in d]
    #Creo un numpy array para realizar todos los calculos mas eficientemente, eliminando
    # la etiqueta que ya la he almacenado en el paso anterior
    d = np.array(d)[:,1:].astype(np.float)
    
    desp = d.shape[1]-1
    #Creo un numpy array lleno de 0, que lo ire rellenando y sera el objeto que se devuelva
    res = np.zeros((d.shape[0],(desp)*2))
    #Por cada uno de los elementos, se calcula la variacion relativa y absoluta
    # para esos valores y se almacenan en el arraya resultante
    for i in range(d.shape[1]-1):
        res[:,i] = d[:,i]-d[:,i+1]
        res[:,i+d.shape[1]-1] = (d[:,i]-d[:,i+1])/d[:,i+1]*100
    
    #Añadimos de nuevo las etiquetas y la cabecera al resultado final
    res = np.hstack((l,res))
    res = np.vstack((cabecera,res))

    return res

# =============================================================================
# Funcion para el ejercicio 4
# Como la funcion anterior calcula la variabilidad absoluta y relativa, pero en este
# caso tanto del total como por cada sexo
# Devuelve un numpy array con el resultado calculado
# =============================================================================
def vabsYvrelSex(datos):
    #Hago una copia para no modificar lo que nos pasan
    d = datos.copy()
        
    #Creo la nueva cabecera
    cabecera=["Comunidad","T2017","T2016","T2015","T2014","T2013","T2012","T2011","T2017","T2016","T2015","T2014","T2013","T2012","T2011"]
    cabecera.extend(["H2017","H2016","H2015","H2014","H2013","H2012","H2011","H2017","H2016","H2015","H2014","H2013","H2012","H2011"])
    cabecera.extend(["M2017","M2016","M2015","M2014","M2013","M2012","M2011","M2017","M2016","M2015","M2014","M2013","M2012","M2011"])
    #Elimino la cabecera
    d = d[1:,:]
    
    #Guardo todas las etiquetas y creo un np.array con todos los datos restantes
    l = [[e[0]] for e in d]
    d = np.array(d)[:,1:].astype(np.float)
    
    desp = 7
    #Creo en np.array que voy a devolver como resultado
    res = np.zeros((d.shape[0],desp*6))
    # Recorriendo unicamente los primeros 7 elementos que son lo que se corresponden
    # con los totales, calculo tanto éstos como por cada uno de los sexos y lo
    # añado al array resultado
    for i in range(desp):
        res[:,i] = d[:,i]-d[:,i+1]
        res[:,i+desp] = (d[:,i]-d[:,i+1])/d[:,i+1]*100
        
        res[:,i+desp*2] = d[:,i+desp+1]-d[:,i+desp+2]
        res[:,i+desp*3] = (d[:,i+desp+1]-d[:,i+desp+2])/d[:,i+desp+2]*100
        
        res[:,i+desp*4] = d[:,i+desp*2+2]-d[:,i+desp*2+3]
        res[:,i+desp*5] = (d[:,i+desp*2+2]-d[:,i+desp*2+3])/d[:,i+desp*2+3]*100
    
    #Añado la cabecera y las etiquetas
    res = np.hstack((l,res))
    res = np.vstack((cabecera,res))

    return res

# =============================================================================
# Funcion que crea un fichero css con el estilo que va a tener la tabla resultante
# =============================================================================
def createCSS():
    fileEstilo=open("estilo.css","w")

    estilo="""  table, th, td {
                    border-collapse: collapse;    
                    border:1px solid black;
                    font-family: Arial, Helvetica, sans-serif;
                    padding: 8px;
                    
                }  """
    
    fileEstilo.write(estilo)
    fileEstilo.close()

# =============================================================================
# Funcion que crea un HTM resultante con los datos que se le pasa como parámetro
# y haciendo unas determinadas tablas o graficas dependiendo del propio
# ejercicio para el que lo estemos ejecutando
# =============================================================================
def exportToHTML(data,fich,plot=None,ej1=False,ej2=False,ej3=False,ej4=False,ej5=False):
    name = fich+".htm"
    f = open(name,'w')

    if ej1:
        paginaPob = """<!DOCTYPE html><html>
        <head><title>Variabilidad Absoluta y relativa</title>
        <link rel="stylesheet" href="estilo.css">
        <meta charset="UTF-8"></head>
        <body><h1>Ej1-Variabilidad Absoluta y relativa</h1>"""
    elif ej2:
        paginaPob = """<!DOCTYPE html><html>
        <head><title>Valores por comunidades</title>
        <link rel="stylesheet" href="estilo.css">
        <meta charset="UTF-8"></head>
        <body><h1>Ej2- Valores por comunidades y sexos</h1>"""
    elif ej4:
        paginaPob = """<!DOCTYPE html><html>
        <head><title>Variabilidad Absoluta y relativa Comunidades</title>
        <link rel="stylesheet" href="estilo.css">
        <meta charset="UTF-8"></head>
        <body><h1>Ej4-Variabilidad Absoluta y relativa Comunidades</h1>"""
    
    cabecera=data[0]
    
    poblacion=data[1:]
    
    paginaPob+= "<p><table>"
    if ej1 or ej4 or ej5:
        
        paginaPob += "<tr>"
        
        paginaPob+="<th></th>"
        paginaPob+="<th colspan='7'>Variablidad Absoluta</th>"
        paginaPob+="<th colspan='7'>Variablidad Relativa</th>"
        if ej5:
            paginaPob+="<th colspan='7'>Variablidad Absoluta</th>"
            paginaPob+="<th colspan='7'>Variablidad Relativa</th>"
            paginaPob+="<th colspan='7'>Variablidad Absoluta</th>"
            paginaPob+="<th colspan='7'>Variablidad Relativa</th>"
        
        paginaPob+="</tr>"
    paginaPob += "<tr>"
    
    for nomColumna in cabecera:
        paginaPob+="<th>%s</th>" % (nomColumna)
    
    paginaPob+="</tr>"
    
    for reg in poblacion:
        paginaPob+="<tr><td>%s</td>" % (reg[0])
        for i,v in enumerate(reg):
            if i != 0:
                if ej2 or ej3:
                    paginaPob+="<td>{}</td>".format(int(float(v)))
                elif i < 8 or (i > 14 and i < 22) or (i > 28 and i < 35):
                    paginaPob+="<td>{}</td>".format(int(float(v)))
                else:
                    paginaPob+="<td>{}</td>".format(round(float(v),2))
        paginaPob+="</tr>"
        
    
    paginaPob+="</table></p>"
    
    if ej3 or ej5:
        paginaPob += "<img src='"+plot+"' alt='Grafico'/>"
        
    paginaPob += "</body></html>"
    
    f.write(paginaPob)
    f.close()
    
# =============================================================================
# Funcion para el ejercicio 2
# Esta funcion crea y devuelve un diccionario que contiene como clave el numero
# que hace referencia a la comunidad y como valor el nombre de la misma
# =============================================================================
def createAutonomas(n):
    name = n+".htm"
    #Abro el fichero htm donde estan los datos
    with open(name, encoding="windows-1250") as htmarchivo:
        #Obtengo el iterador al fichero
        entrada = BeautifulSoup(htmarchivo, 'html.parser')
        #Obtengo la tabla dentro del htm que es lo que nos interesa
        table = entrada.table

        #Creo el diccionario
        dict1 = defaultdict(str)
        #Por cada elemento tr de la tabla, obtenemos sus td y los almacenamos
        #en el diccionario como se puede ver en el codigo
        for tr in table.findAll('tr'):
            if(len(tr.findAll('td')) > 1):
                el = tr.findAll('td')
                if el[0].string and el[1].string:
                    dict1[el[0].string.strip()] = el[1].string.strip()
        
    return dict1

# =============================================================================
# Funcion para el ejercicio 2
# Crea y devuelve un diccionario con la relacion entre cada una de las provincias
# con su comunidad autonoma, donde la clave es el codigo de la provincia y el
# valor el codigo de la comunidad autonoma
# =============================================================================
def createProvAuto(n):
    name = n+".htm"
    #Abro el fichero htm donde estan los datos
    with open(name, encoding="windows-1250") as htmarchivo:
        #Obtengo el iterador al fichero
        entrada = BeautifulSoup(htmarchivo, 'html.parser')
        #Obtengo la tabla dentro del htm que es lo que nos interesa
        table = entrada.table

        #Creo el diccionario
        dict1 = defaultdict(str)
        #Por cada elemento tr de la tabla, obtenemos sus td y los almacenamos
        #en el diccionario como se puede ver en el codigo
        for tr in table.findAll('tr'):
            if(len(tr.findAll('td')) > 1):
                el = tr.findAll('td')
                if el[2].string and el[0].string:
                    dict1[el[2].string.strip()] = el[0].string.strip()
        
    return dict1

# =============================================================================
# Funcion para el ejercicio 2
# Devuelve un numpy donde tenemos todos los datos de las comunidades autonomas
# tanto totales como por sexos
# =============================================================================
def valoresAutonomas(datos,dictAuto,dictProvAuto):
    #Hago una copia de los datos para no modificarlos
    d = datos.copy()
    #Guardo las etiquetas de las comunidades para luego añadirlos a la tabla resultante
    nl = [[e[0]+' '+e[1]] for e in dictAuto.items()]
    #Guardo las claves de las comunidades autonomas para usarlas despues en comparaciones
    nlk = [e[0] for e in dictAuto.items()]
    
    #Creo la cabecera
    cabecera=d[0]
    cabecera[0] = "Comunidad"
    #Elimino la cabecera de los datos
    d.pop(0)
    #Guardo los valores Totales Nacionales ya que esos no varian
    total = d[0]
    #Y los elimino de lso datos
    d.pop(0)
    #Guardo las etiquetas de los datos y creo el np.array solo con los datos numericos
    l = [[e[0]] for e in d]
    d = np.array(d)[:,1:].astype(np.float)
    
    #Creo el array de salida
    res = np.zeros((len(dictAuto),d.shape[1]))
    #Recorro la matriz de datos por filas
    for i in range(len(d)):
        #Obtengo la key de la comunidad de la fila actual
        k = l[i][0][:2]
        #Busco a que comunidad pertenece esta provincia
        elem = dictProvAuto.get(k)
        #Obtengo la posicion de la comunidad en el array resultante
        pos = nlk.index(elem)
        #Sumo el valor de la fila de la provincia al de la comunidad
        res[pos] += d[i]
    
    #Añado las nuevas etiquetas de las comunidades, el total que ya teniamos
    # y la cabecera
    res = np.hstack((nl,res))
    res = np.vstack((total,res))
    res = np.vstack((cabecera,res))

    return res

# =============================================================================
# Funcion para el ejercicio 3
# Funcion que devuelve un top10 de comunidades con mayor poblacion media
# desde 2010 a 2017
# =============================================================================
def top10(data):
    #Elimino la cabecera y los totales nacionales
    d = data[2:,:]
        
    #Guardo las etiquetas y creo un np array solo con los datos numericos
    l = [[e[0]] for e in d]
    d = np.array(d)[:,1:].astype(np.float)
    
    #Creo el array resultado
    res = np.zeros((d.shape[0],3))
    #Para cada una de las filas, sumo todos los valores totales y hago la media
    res[:,0] = [sum(e[:8])/8 for e in d]
    #Guardo el valor de los hombre en 2017 (para grafico)
    res[:,1] = d[:,8]
    #Guardo el valor de las mujeres el 2017 (para grafico)
    res[:,2] = d[:,16]        
        
    #Añado las etiquetas y ordeno el array
    res = np.hstack((l,res))
    res = np.array(sorted(res,key=lambda x: float(x[1]), reverse=True))
    
    #Devuelvo las 10 mejores
    return res[:10,:]

# =============================================================================
# Funcion para el ejercicio 3
# Crea un grafico mostrando para las 10 comunidades autonomas con mas poblacion
# media desde 2010 a 2017 el numero de hombres y mujeres en 2017
# =============================================================================
def getplotBar(data): 
    #Obtengo los hombre y las mujeres para ese año
    h = [e[2].astype(np.float) for e in data]
    m = [e[3].astype(np.float) for e in data]
    #Guardo las etiquetas
    st = [e[0] for e in data]
    
    #Creo el grafico de barras y lo guardo en un fichero externo
    X = np.arange(10)
    
    plt.figure("barras",figsize=(20, 15))
    plt.bar(X + 0.00, h, color = "r", width = 0.25,label='hombres')
    plt.bar(X + 0.25, m, color = "b", width = 0.25,label='mujeres')
    plt.legend(loc="upper right")
    plt.xticks(X+0.2, st)
    
    plt.savefig('barrasej3.png')
    
    plt.close()
    
    return "barrasej3.png"

# =============================================================================
# Funcion para el ejercicio 5
# Dibuja un grafico de lineas con la progresion de la poblacion desde 2010
# hasta 2017 para las 10 mejores comunidades autonomas en poblacion media
# =============================================================================
def getplotLines(data):
    
    #Guardo cada uno de los datos para cada una de las comunidades
    lista = [e[2:].astype(np.float) for e in data]
    #Creo las etiquetas
    st = ["2017","2016","2015","2014","2013","2012","2011","2010"]
    labels = [e[0] for e in data]
    
    #Creo el grafico y lo guardo en un fichero
    X = np.arange(8)

    plt.figure("lineal",figsize=(20, 15))
    for e in lista:
        plt.plot(e)   # Dibuja el gráfico
    plt.title("Poblacion por años")   # Establece el título del gráfico
    plt.xlabel("Año")   # Establece el título del eje x
    plt.ylabel("Poblacion")   # Establece el título del eje y
    plt.legend(labels,loc="upper right")
    plt.xticks(X, st )
    
    plt.savefig('linesej5.png')
    
    plt.close()
    
    return 'linesej5.png'
    
# =============================================================================
# Funcion para el ejercicio 5
# Crea un top 10 de las comunidades autonomas como la funcion anterior pero
# ahora devuelve todos los datos totales y no únicamente los de hombres y mujeres en 2017
# =============================================================================
def top10Max(data):
    #Me quedo con los datos que me interesan para los calculos
    d = data[2:,:9]
        
    #Guardo las etiquetas y creo el np array solo con los datos numericos
    l = [[e[0]] for e in d]
    d = np.array(d)[:,1:].astype(np.float)
    
    #Creo el resultado
    res = np.zeros((d.shape[0],d.shape[1]+1))
    #Calculo la media para todas las filas
    res[:,0] = [sum(e[:8])/8 for e in d]
    #Añado el resto de elementos
    res[:,1:] = d[:]        
        
    #Añado las etiquetas y ordeno el array
    res = np.hstack((l,res))
    res = np.array(sorted(res,key=lambda x: float(x[1]), reverse=True))
    
    #Devuelvo los 10 primeros
    return res[:10,:]
    
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################
    
# =============================================================================
# R1. La variación de la población por provincias desde el año 2011 a 2017 en términos absolutos y
# relativos generando una página web 1 (fichero variacionProvincias.htm)
# =============================================================================
    
fich = "poblacionProvinciasHM2010-17"

limpiaFichero(fich)

datos = readFich(fich+"Final")

ej1 = vabsYvrel(datos)

createCSS()
exportToHTML(ej1,"variacionProvincias",ej1=True)

# =============================================================================
# R2. Usando el listado de comunidades autónomas que podemos obtener de los datos de entrada, así
# como de las provincias de cada comunidad autónoma, generar una página web 2 (fichero
# poblacionComAutonomas.htm) con una tabla con los valores de población de cada comunidad
# autónoma en cada año de 2010 a 2017 indicando también los valores desagregados por sexos
# =============================================================================

dictAuto = createAutonomas("comunidadesAutonomas")
dictProvAuto = createProvAuto("comunidadAutonoma-Provincia")

ej2 = valoresAutonomas(datos,dictAuto,dictProvAuto)

createCSS()
exportToHTML(ej2,"poblacionComAutonomas",ej2=True)

# =============================================================================
# R3. Para las 10 comunidades con más población media de 2010 a 2017, generar un gráfico de
# columnas que indique la población de hombres y mujeres en el año 2017, salvar el gráfico a fichero
# e incorporarlo a la página web 2 del punto R2.
# =============================================================================

newd = top10(ej2)

plot = getplotBar(newd)

createCSS()
exportToHTML(ej2,"poblacionComAutonomas",plot,ej2=True,ej3=True)

# =============================================================================
# R4. Generar una página web 3 (fichero variacionComAutonomas.htm) con una tabla con la
# variación de población por comunidades autónomas desde el año 2011 a 2017, indicando variación
# absoluta, relativa y desagregando dicha información por sexos, es decir, variación absoluta
# (hombres, mujeres) y relativa (hombres, mujeres).
# =============================================================================

ej4 = vabsYvrelSex(ej2)

createCSS()
exportToHTML(ej4,"variacionComAutonomas",ej4=True)

# =============================================================================
# R5. Para las 10 comunidades elegidas en el punto R3 generar un gráfico de líneas que refleje la
# evolución de la población total de cada comunidad autónoma desde el año 2010 a 2017, salvar el
# gráfico a fichero e incorporarlo a la página web 3 del punto R4.
# =============================================================================

ej5 = top10Max(ej2)

plot = getplotLines(ej5)

createCSS()
exportToHTML(ej4,"variacionComAutonomas",plot,ej4=True, ej5=True)