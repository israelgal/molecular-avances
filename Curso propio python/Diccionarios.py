# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:57:28 2019

@author: iisra
"""

diccionario={"Alemania":"Berlín","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}

print(diccionario["Alemania"]) #esto se hace para llamar a una clave guardada

print(diccionario)#Imprime todo el diccionario

diccionario["Italia"]="Lisboa"  #Para agregar otro dato al diccionario

print(diccionario)

diccionario["Italia"]="Roma" #Para cambiar una clave lo unico que se hace es sobreescribir

print(diccionario)

del diccionario["Reino Unido"] #Para borrar alguna clave

print(diccionario)

#Pueden agregarse valores de cualquier tipo a las claves
