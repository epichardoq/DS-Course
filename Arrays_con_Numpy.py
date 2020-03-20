#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:47:49 2019

@author: emmanuel
"""

#ndarray.ndim –> Proporciona el número de dimensiones de nuestro array.
#ndarray.dtype –> Es un objeto que describe el tipo de elementos del array.
#ndarray.shape –> Devuelve la dimensión del array, es decir, una tupla de 
#   enteros indicando el tamaño del array en cada dimensión. Para una matriz 
#   de n filas y m columnas obtendremos (n,m).
#ndarray.data –> El buffer contiene los elementos actuales del array.
#ndarray.itemsize –> devuelve el tamaño del array en bytes.
#ndarray.size –> Es el número total de elementos del array.

import numpy as np # Importamos numpy como el alias np
miArray = np.arange(10) # Creamos un array de 0 a 9 separados de uno en uno
print(type(miArray))
numdim= miArray.ndim
dim=miArray.shape
tam= miArray.size
byte=miArray.itemsize
