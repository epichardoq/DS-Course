#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:41:43 2019

@author: emmanuel
"""

import numpy as np # Importamos numpy como el alias np
a = np.array([[8, 1, 4]])
b= np.array([[3, 7, 4]])
c= np.cross(a, b) # Producto vectorial
print(c)
d=np.outer(a, b) # Producto exterior
print(d)