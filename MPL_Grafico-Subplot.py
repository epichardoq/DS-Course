#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:23:51 2019

@author: emmanuel
"""

import matplotlib.pyplot as plt

import numpy as np # Importamos numpy como el alias np

a = np.linspace(0,20,50)

b= np.sin(a)

plt.figure()

# plot 1

plt.subplot(2,2,1)

plt.plot(a, b,'r')

# Segunda grafica

plt.subplot(2,2,2)

plt.plot(a+2, b*25,'g')

# Tercera grafica

plt.subplot(2,2,3)

plt.plot(b, a,'b')

# Cuarta grafica

plt.subplot(2,2,4)

plt.plot(a, b,'k')

# Mostramos en pantalla

plt.show()