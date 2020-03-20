#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:56:06 2019

@author: emmanuel
"""

def raizCuadrada(i):  # Función que calcula la raíz cuadrada de un número
  return i**(1/2)

def raices(A,B,C):  # Función que calcula las raíces de un polinomio cuadrático
  return ((-B+raizCuadrada(B**2-(4*A*C)))/(2*A)),((-B-raizCuadrada(B**2-(4*A*C)))/(2*A))