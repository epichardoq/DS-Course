#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:34:38 2019

@author: emmanuel
"""

def proms(A, q):
  '''	Función:
    Calcula los promedios de las edades e indices  
    academicos y los almacena en un arreglo.
  '''
  pred = sum(i.edad for i in A)/q
  pria = sum(i.indice for i in A)/q
  S = [pred, pria]
  return S