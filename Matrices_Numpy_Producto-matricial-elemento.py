#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:30:01 2019

@author: emmanuel
"""

import numpy as np # Importamos numpy como el alias np
a = np.array([[8, 2], [8, 4]])
b=np.dot(a,a)
print(b)
c=a*a
print(c)
d=np.multiply(a, a)
print(d)