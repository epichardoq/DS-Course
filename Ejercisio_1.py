#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:30:29 2019

@author: emmanuel
"""

#Ejercicio Python #01: Define una función llamada menorque() que nos devuelva 
#en pantalla el número menor entre dos enteros. Define una salida de texto en 
#caso de que.

def menorque(a, b):
    if a > b:
        print ("El menor es b")
    elif b > a:
        print ("El menor es a")
    else: 
        print ("Ambos son iguales")

menorque(5,2)