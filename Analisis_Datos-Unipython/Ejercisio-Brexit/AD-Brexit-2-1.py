#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:09:24 2019

@author: emmanuel
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# Obtenemos el ingreso medio por área / condado (están en la misma columna, pero la fusión posterior lo arreglará)
salarios_archivo = "/Users/emmanuel/Documents/curso_python/Analisis_Datos-Unipython/Ejercisio-Brexit/Table_3_13_14.xlsx" #no olvides poner donde tienes el #archivo
salarios = pd.read_excel(io=salarios_archivo, sheet_name='Table_3_13_14', header=10, usecols=('A,U'), skiprows=[11, 12, 13],)
salarios.dropna(how='all', inplace=True)
salarios.rename(index=str, columns={salarios.columns[0]: "Region", salarios.columns[1]: "median_income"}, inplace=True)
salarios.set_index("Region", inplace=True)
salarios.head(5)
# Los datos de ingresos tienen espacios en blanco para combinar no coincide, limpiamos los espacios en blanco
salarios.index = salarios.index.str.strip()
# Perdemos 2 regiones, aceptando que por ahora
[i for i in votes_region.index if i not in salarios.index]

# Combinar los conjuntos de datos de votos e ingresos en los índices de su condado
votes_and_income = votes_region.merge(salarios, left_index=True, right_index=True, how='left')
votes_and_income.drop_duplicates(subset="Remain", keep="first", inplace=True)
votes_and_income = votes_and_income[votes_and_income["median_income"] > 0] # clean 2 NANs
votes_and_income
# No se puede reutilizar el método anterior de showplot, así que ajustaremos el código aquí
# Tuve que agregar FuncFormatter también porque el eje x tiene valores de voto mucho mayores, porque medimos
# Regiones (= más grande) en lugar de áreas (= más pequeñas) aquí
factor = "median_income"
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1,1,1)
ax.scatter(votes_and_income["votes"], votes_and_income[factor], s=100, c='r', marker="o", label="media_ingresos_salariales")
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda y, pos: ('%2d')%(y*1e-3)))
# muestra un punto y el nombre del condado
for i, txt in enumerate(votes_and_income.index):
  ax.annotate(txt, (votes_and_income["votes"][i], votes_and_income[factor][i]),
  horizontalalignment='right', verticalalignment='top',
    bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=0.2'))
plt.legend(loc='upper left');
plt.xlabel("votos en 1000s (< 0 = noUE / > 0 = siUE)")
plt.ylabel("media_ingresos_salariales")
plt.axvline(x=0)
plt.axhline(y=votes_and_income[factor].mean()) # linea horizontal en la media de los datos
plt.show()
fig.savefig(factor+".png")