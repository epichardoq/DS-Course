#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:24:28 2019

@author: emmanuel
"""

# Actualización de datos
import sqlite3

conn = sqlite3.connect('tutorial1.db')
c = conn.cursor()
 
def actualizar_y_borrar():

# Vamos a cambiar todos los valores menores de 5 por 2018
  c.execute('UPDATE tabla1 SET valor = 2018 WHERE valor < 5')
  conn.commit()
# Borrar todos los valores que son iguales a 2018
  #c.execute('DELETE FROM tabla1 WHERE valor = 2018')
  #conn.commit()

  c.execute('SELECT * FROM tabla1')
  data = c.fetchall()
  [print(row) for row in data]
 
actualizar_y_borrar()