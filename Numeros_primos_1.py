#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:45:04 2019

@author: emmanuel
"""

numero= int(input("¿Qué número quieres saber si es primo? "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
    print("divisor:", n)

if contador > 0 :
  print("El número no es primo" )
else:
  print("El número es primo")