#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:13:02 2019

@author: emmanuel
"""

import numpy as np # Importamos numpy como el alias np
g=np.matrix( [[3,4,-9], [7,4,-5] ,[1,3,9]] )
print(g)
b=np.matrix( [[-9], [-5] ,[9]] )
print(b)
c=g*b
print(c)
bt=b.T #traspuestas
print(bt)
bh=b.H #traspuestas y conjudaga
print(bh)
gi=g.I #inversa
print(gi)
detgi=np.linalg.det(gi) #calculo del determinante
tragi=np.trace(gi) #calculo de la traza