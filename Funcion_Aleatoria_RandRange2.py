#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:08:29 2019

@author: emmanuel
"""

import random
# Rango simple 0 <= r < 6
print (random.randrange(6)), (random.randrange(6))
# Rango más complejo 1 <= r < 7
print (random.randrange(1,7)), (random.randrange(1,7))
# Rango realmente complejo de números pares entre 2 y 36
print (random.randrange(2,37,2))
# Números impares del 1 al 35
print(random.randrange(1,36,2))