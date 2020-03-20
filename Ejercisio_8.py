#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 18:13:24 2019

@author: emmanuel
"""

#Define una función que permita multiplicar los números de una lista y sumar 
#sus resultados.

def multip (lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    print (multiplicacion)
multip([4,2,6])