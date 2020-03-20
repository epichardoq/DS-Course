#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:12:57 2019

@author: emmanuel
"""

from raices import raices, raizCuadrada

A = float(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = float(input("Ingrese el coeficiente de la variable lineal\n"))
C = float(input("Ingrese el término independiente\n"))
r1 = 0
r2 = 0

r1,r2 = raices(A,B,C) # Llamado a la función sin el prefijo del módulo

print(f"La primera raiz es: {r1}") 
print(f"La segunda raiz es: {r2}")
