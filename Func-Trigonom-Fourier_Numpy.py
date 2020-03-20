#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:50:52 2019

@author: emmanuel
"""

import numpy as np # Importamos numpy como el alias np
x=np.linspace(0,1,100)
y=np.sin(x)
print (np.fft.fft(y))