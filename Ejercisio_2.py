#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:36:33 2019

@author: emmanuel
"""

#Define una función llamada num_max() que nos devuelva en pantalla el número 
#mayor entre 4 diferentes enteros. No definas ningún valor a imprimir en caso 
#de que ambos números sean iguales.

def num_max (a, b, c):
    if a > b and a > c:
        print (a)
    elif b > a and b > c:
        print (b)
    elif c > a and c > b:
        print (c)
    else:
        print ("Son iguales")
num_max(1,2,3)