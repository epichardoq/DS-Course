#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:17:29 2019

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




#con matplotlib vamos hacer 3 graficas
# la primera son las 8 Areas al no UE
dfa = df.groupby("Area").sum()
dfa.head()
dfa["Perc_noUE"] = dfa["Leave"] / (dfa["Remain"] + dfa["Leave"]) * 100
dfa["Perc_siUE"] = dfa["Remain"] / (dfa["Remain"] + dfa["Leave"]) * 100
dfa.head(3)
top5_noUE = dfa[["Perc_noUE", "Perc_siUE"]].sort_values(by="Perc_noUE", ascending=False)[0:8]
top5_noUE.head()
plt1 = top5_noUE.plot(kind="bar")
plt1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# la segunda son las 8 Areas al si UE
top5_siUE = dfa[["Perc_noUE", "Perc_siUE"]].sort_values(by="Perc_noUE", ascending=False)[-8:]
top5_siUE.head()
plt2 = top5_siUE.plot(kind="bar")
plt2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# la tercera son las 8 Areas al si UE y las 8 areas al no UE
dfr = df.groupby("Region").sum()
dfr["Perc_noUE"] = dfr["Leave"] / (dfr["Remain"] + dfr["Leave"]) * 100
dfr["Perc_siUE"] = dfr["Remain"] / (dfr["Remain"] + dfr["Leave"]) * 100
dfr[["Perc_noUE", "Perc_siUE"]].sort_values(by="Perc_noUE", ascending=False).plot(kind="bar")