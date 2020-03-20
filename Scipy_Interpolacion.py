#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:00:37 2019

@author: emmanuel
"""

import scipy as sp

from scipy import interpolate

import matplotlib.pyplot as plt

#array

x = sp.linspace(0,3,10)

# generamos datos experimentales de ejemplo)

y = sp.exp(-x/3.0)

# Interpol

interpolacion = interpolate.interp1d(x, y)

# array con mas puntos en el mismo intervalo

x2 = sp.linspace(0,3,1000)

# Evaluamos x2 en la interpolacion

y2 = interpolacion(x2)

plt.figure

plt.plot(x, y, 'ok')

plt.plot(x2, y2, '-c')

plt.legend(('Datos conocidos', 'Datos experimentales interpolados'))

plt.show()