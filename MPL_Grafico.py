#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 19:29:12 2019

@author: emmanuel
"""

import matplotlib.pyplot as plt

import numpy as np # Importamos numpy como el alias np

a = np.linspace(0,20,50)

b= np.sin(a)

plt.plot(a, b, 'k--', linewidth = 2) 