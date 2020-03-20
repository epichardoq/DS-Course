#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 18:01:01 2019

@author: emmanuel
"""
#Define una función que permita imprimir un mensaje en base a los valores 
#tomados de una lista para comprobar si todos los de la lista son mayores o 
#menores de edad.


def mayor_menor_edad (lista):
    for i in lista:
        if i > 18:
            print ("Es mayor de edad")
        elif i == 18:
            print ("Apenas tiene la mayoría de edad")
        else:
            print ("Es menor de edad")
mayor_menor_edad([18,21,8,19,5,4,3,8,2,3])