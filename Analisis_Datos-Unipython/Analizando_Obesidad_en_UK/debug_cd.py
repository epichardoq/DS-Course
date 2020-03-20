#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 19:31:03 2019

@author: emmanuel
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.ExcelFile("obes-phys-acti-diet-eng-2017-tab.xlsx")

data_age = data.parse(u'Table 6', skiprows=7, skipfooter=15)
print(data_age)


#Para que el plotedo sea más sencillo cambiamos el indice a YEAR
data_age.drop("Unnamed: 1", axis=1, inplace=True)
data_age.dropna(inplace=True)
data_age.set_index('Year4', inplace=True)
print(data_age)

#Realizamos los gráficos
data_age.plot()
plt.show()