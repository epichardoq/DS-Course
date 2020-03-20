#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:00:10 2019

@author: emmanuel
"""

import pandas as pd
#importamos los datos yo me lo he bajado de esta web:
#https://www.electoralcommission.org.uk/find-information-by-subject/elections-and-referendums/upcoming-elections-and-referendums/eu-referendum/electorate-and-count-information
df = pd.read_csv("/Users/emmanuel/Documents/curso_python/Analisis_Datos-Unipython/Ejercisio-Brexit/EU-referendum-result-data.csv")
# vamos a sumar quien esta a favor de la UE y quien no
noUE = df["Leave"].sum()
siUE = df["Remain"].sum()
print("no UE: {} votantes | si UE {} votantes".format(noUE, siUE))
#calculamos los porcentajes
porcennoUE=noUE / (siUE + noUE) *100
porcensiUE=siUE / (noUE + siUE) *100
print("Porcentage del no a UE: {} y del si a UE {}".format(porcennoUE, porcensiUE))
#calculamos el censo, porcentage de votantes y rechazados
censo = df['Electorate'].sum();
porcenvotantes = (noUE + siUE) / censo * 100; 
rechazados = df.Rejected_Ballots.sum();
print("El censo es: {}, el procentage de votantes es {} y el numero de rechazados es {}".format(censo, porcenvotantes, rechazados))

