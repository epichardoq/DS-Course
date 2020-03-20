#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:41:24 2019

@author: emmanuel
"""

from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

import numpy as np

fig = plt.figure()

ax = Axes3D(fig)

X = np.arange(-4, 4, .3)

Y = np.arange(-4, 4, .3)

X, Y = np.meshgrid(X, Y)

R = np.sqrt(X**2 + Y**2)

Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet')