#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:05:41 2019

@author: emmanuel
"""

import raices	# Importa el módulo 'raices'

A = float(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = float(input("Ingrese el coeficiente de la variable lineal\n"))
C = float(input("Ingrese el término independiente\n"))
r1 = 0
r2 = 0

r1,r2 = raices.raices(A,B,C) # Llamado a la función 'raices' del módulo 'raices'

print(f"La primera raíz es: {r1}") 
print(f"La segunda raíz es: {r2}")