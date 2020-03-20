#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:34:12 2019

@author: emmanuel
"""

from utiles.clases import Estudiante # Se importa la clase 'Estudiante'
from utiles.funciones import proms # Se importa la función 'proms'

N = int(input("Ingrese la cantidad de estudiantes\n"))
grupo = [ Estudiante() for x in range(0,N) ]
promed = 0.0
promia = 0.0

for i in grupo:
  i.nombre = input("Ingrese el nombre del estudiante (min. 1 caracter)\n")
  i.edad = int(input("Ingrese la edad de %s\n" % i.nombre))
  i.indice = float(input("Ingrese el I.A de %s (entre 1 y 10)\n" % i.nombre))

PROMEDIOS = proms(grupo, N)

print("El promedio de las edades es: %s" % PROMEDIOS[0])
print("El promedio de los I.A. es: %s" % PROMEDIOS[1])