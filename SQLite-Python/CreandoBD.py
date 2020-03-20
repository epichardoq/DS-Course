#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:31:54 2019

@author: emmanuel
"""

import sqlite3

conn = sqlite3.connect('tutorial1.db')
c= conn.cursor()

#Crear una tabla
def create_table():
 c.execute("CREATE TABLE IF NOT EXISTS tabla1(unix REAL, fecha TEXT, palabraclave TEXT, valor REAL)")
 
#Insertar Valores
def data_entry():
  c.execute("INSERT INTO tabla1 VALUES(1452549219,'2018-02-12 16:50:39','Python',6)")

  conn.commit()
  c.close()
  conn.close()

create_table()
data_entry()
