#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:55:43 2019

@author: emmanuel
"""
# Ejemplo para el cálculo integral siguiente de 0 a infinito.
import scipy as sp
from scipy import integrate
def integral_1(limite_inferior, limite_superior, mostrar_resultados):
  # funcion e^(-x)
  exponencial_decreciente = lambda x: sp.exp(-x)
  # resultados por pantalla
  if mostrar_resultados == True:
    print ('La integral entre %2.2f y %2.2f es '% (limite_inferior, limite_superior))
    print(integrate.quad(exponencial_decreciente,limite_inferior,limite_superior))
  # Los devuelvo
  return integrate.quad(exponencial_decreciente ,limite_inferior,limite_superior)

integral_1(limite_inferior = 0, limite_superior = sp.inf, mostrar_resultados = True)