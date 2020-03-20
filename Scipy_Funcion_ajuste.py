#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:31:52 2019

@author: emmanuel
"""

import numpy as np # Importamos numpy como el alias np

import scipy as sp # Importamos scipy como el alias sp

from scipy.optimize import curve_fit # Importamos curve_fit de scipy.optimize

import scipy as sp # Importamos scipy como el alias sp

import matplotlib.pyplot as plt # Importamos matplotlib.pyplot como el alias plt.

def mi_funcion(x, a, b, c, d):

  return a*sp.exp(-b*x**2/(2*d**2)) + c * x

# Añadimos ruido

x = sp.linspace(0, 5,40)

y = mi_funcion(x, 2.5, 1.3, 0.5,1)

def ruido(x,y,k):

  yn = y + k * sp.random.normal(size = len(x))

  return yn

# Ajustamos los datos experimentales a nuestra funcion y los almacenamos

coeficientes_optimizados, covarianza_estimada = curve_fit(mi_funcion, x, y)

# Mostramos los coeficientes calculados

print ("Coeficientes optimizados:", coeficientes_optimizados)

print ("Covarianza estimada:", covarianza_estimada)

# Creamos la figura

plt.figure()

# Dibujamos los datos ruido

plt.plot(x,y,'ro', label = 'Experimental')

# mantenemos la figura



results=mi_funcion(x,coeficientes_optimizados[0],coeficientes_optimizados[1],coeficientes_optimizados[2], coeficientes_optimizados[3])

plt.plot(x,results, label = 'Ajuste')

plt.legend()

plt.xlabel('Tiempo (h)')

plt.ylabel('Ventas del supermercado en pescado x100 ($)')

plt.show()