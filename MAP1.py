#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 17:04:41 2019

@author: emmanuel
"""

#map(función, iterable)

lista = [2,4,8,10]
listaCuadrada = map(lambda x: x**2, lista)
print(listaCuadrada)