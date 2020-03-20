#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:38:56 2019

@author: emmanuel
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.ExcelFile("obes-phys-acti-diet-eng-2017-tab.xlsx")

print(data.sheet_names)

data_age = data.parse(u'Table 6', skiprows=7, skipfooter=15)
print(data_age)


#Para que el plotedo sea más sencillo cambiamos el indice a YEAR y limpiamos datos
# Elimina la columna "extra" y vacía
data_age.drop("Unnamed: 1", axis=1, inplace=True)
# Limpia las celdas vacías
data_age.dropna(inplace=True)
# Year como punto de origen
data_age.set_index('Year4', inplace=True)
print(data_age)


#Realizamos los gráficos
data_age.plot()
plt.title("Indíce de obesidad por orden de edad", fontsize = 10)
plt.show()

#Representamos de nuevo, pero eliminando el número Total
data_age_minus_total= data_age.drop('All persons5', axis=1)
#Ploteemos lo que tenemos ahora
data_age_minus_total.plot()
plt.title("Indíce de obesidad por orden de edad", fontsize = 10)
plt.show()
plt.close()

# Representamos children vs adults
data_age['Under 16'].plot(label="Under 16")
data_age['35 to 44'].plot(label="35 to 44")
plt.legend(loc="upper right")
plt.title("Indíce de obesidad Niños vs Adultos", fontsize = 10)
plt.show()
plt.close()

# Pero, ¿qué hay sobre el futuro?
# Ajuste de Curvas e Interpolación Polinomial
kids_values= data_age['Under 16'].values
x_axis = range(len(kids_values))
# Interpolación Polinomial de Grado 
poly_degree= 7
curve_fit = np.polyfit(x_axis, kids_values, poly_degree)
poly_interp = np.poly1d(curve_fit)
poly_fit_values = []
for i in range(len(x_axis)):
     poly_fit_values.append(poly_interp(i))
#Representamos los datos
plt.title("Predicción de obesidad en niños menores > 16 años", fontsize = 10)
plt.plot(x_axis, poly_fit_values, "-r", label = "Fitted")
plt.plot(x_axis, kids_values, "-b", label = "Orig")
plt.legend(loc="upper right")
