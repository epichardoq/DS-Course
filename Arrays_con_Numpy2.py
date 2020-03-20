#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:01:15 2019

@author: emmanuel
"""
#identity(n,dtype) –>Devuelve la matriz identidad, es decir, uma matriz 
#   cuadrada nula excepto en su diagonal principal que es unitaria. n es el 
#   número de filas (y columnas) que tendrá la matriz y dtype es el tipo de dato. 
#ones(shape,dtype) –>Crea un array de 1 compuesto de shape elementos.
#zeros(shape, dtype) –>Crea un array de 0 compuesto de “shape” elementos”.
#linspace(start,stop,num,endpoint=True,retstep=False) –>Crea un array con valor
#   inicial start,valor final stop y num elementos.
#empty(shape, dtype) –>Crea un array de ceros compuesto de “shape” elementos” 
#   sin entradas.
#meshgrid(x,y) –>Genera una malla a partir de dos los arrays x, y.
#eye(N, M, k, dtype) –>Crea un array bidimensional con unos en la diagonal k y 
#   ceros en el resto. Es similar a identity. Todos los argumentos son opcionales.
#   N es el número de filas, M el de columnas y k es el índice de la diagonal. 
#   Cuando k=0 nos referimos a la diagonal principal y por tanto eye es similar 
#   a identity.
#arange([start,]stop[,step,],dtype=None) –>Crea un array con valores distanciados 
#   step entre el valor inicial star y el valor final stop. Si no se establece 
#   step python establecerá uno por defecto.

import numpy as np # Importamos numpy como el alias np
g=np.zeros( (3,4) )
print(g)
k=np.linspace( 1, 4, 9 )
print(k)
X,Y=np.meshgrid([1,2,3],[7,9,34])
print(X)
print(Y)