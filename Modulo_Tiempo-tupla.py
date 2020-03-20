#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:02:59 2019

@author: emmanuel
"""
import time
t = time.localtime() # Establecemos nuestra tupla, la cual será obtenida por localtime.

print ("time.asctime(t): %s " % time.asctime(t))