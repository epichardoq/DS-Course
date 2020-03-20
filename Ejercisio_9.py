#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 18:21:58 2019

@author: emmanuel
"""

#  Imprime en pantalla la hora y fecha actual.
import datetime
now = datetime.datetime.now()
print ("La fecha y hora actual es : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))