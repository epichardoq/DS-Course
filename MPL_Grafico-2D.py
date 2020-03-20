#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:32:32 2019

@author: emmanuel
"""

import numpy as np

import matplotlib.pyplot as plt

plt.figure()

x = np.arange(-5, 5, 0.01)

y = np.arange(-5, 5, 0.01)

X, Y = np.meshgrid(x, y)

# Definimos cos (x^3 + y^2)

fxy = np.cos(X**3+Y**2)

plt.imshow(fxy);

plt.colorbar();

plt.show()