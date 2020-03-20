#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:23:03 2019

@author: emmanuel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#matplotlib inline
census_data = {"age" : "r21ewrttableks102ewladv1_tcm77-290566.xls",
"unemployment" : "r21ewrttableks601ewladv1_tcm77-290745.xls",
"education" : "r21ewrttableks501ewladv1_tcm77-290734.xls",
"outside_uk" : "r21ewrttableqs203ewladv1_tcm77-290919.xls",}

votes_org = pd.read_csv("/Users/emmanuel/Documents/curso_python/Analisis_Datos-Unipython/Ejercisio-Brexit/EU-referendum-result-data.csv", usecols=["Area_Code", "Region", "Remain", "Leave"] ) #no olvides poner donde tienes el #archivo
votes_org.rename(index=str, inplace=True, columns={"Area_Code": "Area code", }) # same col name for merge
votes_org["votes"] = votes_org["Remain"] - votes_org["Leave"]
votes = votes_org[["Area code", "votes"]]
votes.head(2)
edad = pd.read_excel(io=census_data["age"], sheet_name='KS102EW_Numbers', header=10, usecols=('A,W'), skiprows=[11,12,13])
edad.dropna(how='all', inplace=True)
edad.rename(index=str, inplace=True, columns={"Median age": "median_age", })
edad = edad[["Area code", "median_age"]]
edad.head(2)
desempleo = pd.read_excel(io=census_data["unemployment"], sheet_name='KS601EW_Numbers', header=10, usecols=('A,E,I'), skiprows=[11,12,13])
desempleo.dropna(how='all', inplace=True)
desempleo["perc_unemployed"] = desempleo[desempleo.columns[2]] / desempleo[desempleo.columns[1]]
desempleo = desempleo[["Area code", "perc_unemployed"]]
desempleo.head(2)
educacion = pd.read_excel(io=census_data["education"], sheet_name='KS501EW_Numbers', header=10, usecols=('A,E,J,K'), skiprows=[11,12,13])
educacion.dropna(how='all', inplace=True)
educacion["perc_high_education"] = (educacion[educacion.columns[2]] + educacion[educacion.columns[3]]) / educacion[educacion.columns[1]]
educacion = educacion[["Area code", "perc_high_education"]]
educacion.head(2)
fuera_uk = pd.read_excel(io=census_data["outside_uk"], sheet_name='QS203EW_Numbers', header=10, usecols=('A,E,G'), skiprows=[11,12,13])
fuera_uk.dropna(how='all', inplace=True)
fuera_uk.columns[2]
fuera_uk["perc_born_outside_uk"] = (fuera_uk[fuera_uk.columns[1]] - fuera_uk[fuera_uk.columns[2]]) / fuera_uk[fuera_uk.columns[1]]
fuera_uk = fuera_uk[["Area code", "perc_born_outside_uk"]]
fuera_uk.head(2)
data = votes.merge(edad, on='Area code').merge(desempleo, on='Area code').merge(educacion, on='Area code').merge(fuera_uk, on='Area code')
data.head(5)
100 - ((len(votes) - len(data)) / len(votes)*100)
#hacemos una funcion para plotear
def showplot(data, factor,factor2):
  fig = plt.figure(figsize=(6, 6))
  ax = fig.add_subplot(1,1,1)
  ax.scatter(data["votes"], data[factor], s=20, c='r', marker="o", label=factor2)
  plt.legend(loc='upper left');
  plt.xlabel("votos (< 0 = noUE / > 0 = siUE)")
  plt.ylabel(factor2)
  plt.axvline(x=0)
  plt.axhline(y=data[factor].mean())# linea horizontal en la media de los datos
  plt.show()
  fig.savefig(factor+".png")

showplot(data, "median_age", "media_edad")
showplot(data, "perc_unemployed", "%_desempleados")
showplot(data, "perc_high_education", "%_alta_educacion")
showplot(data, "perc_born_outside_uk","%_nacidos_fuera_UK" )
votes_region = votes_org.groupby("Region").sum()
votes_region.head(2)
len(votes_region)