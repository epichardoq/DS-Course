#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:38:49 2019

@author: emmanuel
"""

import pandas as pd

# Read the file
data = pd.read_csv("/Users/emmanuel/Documents/curso_python/Analisis_Datos-Unipython/Trabajando_Big-Data-Files/Stats19-Data1979-2004/Accidents7904.csv", low_memory=False)
# Output the number of rows
print("Total rows: {0}".format(len(data)))
# See which headers are available
print(list(data))