#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 17:20:06 2019

@author: emmanuel
"""

#filter(función, iterable) crea una lista nueva a partir de los elementos para 
#los cuales ‘función’ devuelve ‘True’

lista = [1,2,3,4,5,6]
nuevaLista = list(filter(lambda x: x % 3 == 0, lista)) # 'list()' convierte el iterable
print(nuevaLista)                                      #  generado por 'filter' en una lista