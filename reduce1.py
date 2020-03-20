#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 17:50:38 2019

@author: emmanuel
"""
#reduce(función, iterable) aplica dos argumentos a los elementos en el 
#iterable, de izquierda a derecha de forma acumulativa

from functools import reduce  # Esto es necesario si se está usando Python 3

lista = [2,4,6,8]
a = reduce(lambda x,y: x-y, lista)
print(a)