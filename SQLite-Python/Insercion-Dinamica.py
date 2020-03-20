#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 21:50:49 2019

@author: emmanuel
"""

import sqlite3
import time
import datetime
import random

# Conexión a la base de datos
conn = sqlite3.connect('tutorial1.db')
c = conn.cursor()

# Crear tabla 2
def create_table():
  c.execute("CREATE TABLE IF NOT EXISTS tabla2(unix REAL, fecha TEXT, palabraclave TEXT, valor REAL)")

def data_entry():
  c.execute("INSERT INTO tabla2 VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
  
  conn.commit()
  c.close()
  conn.close()

# Crear datos dinámicos
def dynamic_data_entry():

  unix = int(time.time())
  date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
  keyword = 'Python'
  value = random.randrange(0,10)

  c.execute("INSERT INTO tabla1 (unix, fecha, palabraclave, valor) VALUES (?, ?, ?, ?)",
        (unix, date, keyword, value))

  conn.commit()

for i in range(10):
  dynamic_data_entry()
  time.sleep(1)

c.close
conn.close()