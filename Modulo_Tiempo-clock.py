#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:47:20 2019

@author: emmanuel
"""

import time

def procedure():
 time.sleep(2.5)

# Proceso de impresión con time.clock
 t0 = time.process_time()
 procedure()
 print (time.process_time(), "segundos del proceso time")

# Proceso de impresión en Windows
t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")