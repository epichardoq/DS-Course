#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:02:02 2019

@author: emmanuel
"""

import pandas as pd

# Read the file
data = pd.read_csv("/Users/emmanuel/Documents/curso_python/Analisis_Datos-Unipython/Trabajando_Big-Data-Files/Stats19-Data1979-2004/Accidents7904.csv", low_memory=False)

# Accidents which happened on a Sunday
accidents_sunday = data[data.Day_of_Week == 1]
print("Accidents which happened on a Sunday: {0}".format(
 len(accidents_sunday)))

#Accidents which happened on a Sunday, &amp;gt; 20 
accidents_sunday_twenty_cars= data[(data.Day_of_Week == 1) & (data.Number_of_Vehicles >= 20)]
print("Accidents which happened on a Sunday involving >= 20 cars: {0}".format(len(accidents_sunday_twenty_cars)))

#Accidents which happened on a Sunday, &amp;gt; 20 cars, in the rain
accidents_sunday_twenty_cars_rain = data[(data.Day_of_Week == 1) & (data.Number_of_Vehicles >= 20) & (data.Weather_Conditions == 2)]
print("Accidents which happened on a Sunday involving >= 20 cars in the rain: {0}".format (len(accidents_sunday_twenty_cars_rain)))

# Accidents in London on a Sunday
london_data = data[(data['Police_Force'] == 1) & (data.Day_of_Week == 1)]
print("\nAccidents in London from 1979-2004 on a Sunday: {0}".format(len(london_data)))

# Save to Excel
writer= pd.ExcelWriter ('London_Sundays.xlsx', engine='xlsxwriter') 
london_data.to_excel (writer, 'Sheet1')
writer.save()
