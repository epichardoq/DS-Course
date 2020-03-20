#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:38:55 2019

@author: emmanuel
"""

#Define una función llamada num_max_min() que nos devuelva en pantalla el 
#número mayor y menor entre 3 diferentes enteros. En caso de que todos sean 
#iguales imprime en pantalla un mensaje indicándolo.

def num_max_min(a, b, c):
    if a > b and a > c:
        print ("El mayor es", a, "y el menor", c) 
    elif b > a and b > c:
        print ("El mayor es", b, "y el menor", c)
    elif c > a and c > b:
        print ("El mayor es", c, "y el menor", b)
    else:
        print ("Son iguales")
num_max_min(4,2,1)