#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 20:36:32 2019

@author: emmanuel
"""

import time

t = (2018, 3, 28, 17, 3, 38, 1, 48, 0) # Damos un valor a la tupla con una fecha
 secs = time.mktime( t ) #Definimos nuestro método
 print ("time.mktime(t) : %f" % secs) # Imprimimos el método en segundos

# Convertimos nuevamente nuestro código a una cadena de texto
 print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))