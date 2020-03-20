#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:31:54 2019

@author: emmanuel
"""

import random

regalos = ['Hojas', 'Almohadas', 'iPhone', 'Cocina', 'Puerta',

'Tablet', 'Llavero', 'Zapatos', 'Automovil', 'Bolso']

for serie in range(3):

print ('\nserie:', serie + 1)

random.seed(0)

for sorteo in range(6):

regalo = regalos[random.randint(0, 9)]

print('Sorteo', sorteo + 1, ':', regalo)