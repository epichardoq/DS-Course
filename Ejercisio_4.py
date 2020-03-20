#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:45:40 2019

@author: emmanuel
"""

#Define una función que nos devuelva True si al darle una vocal mayúscula nos 
#devuelva False, mientras que si es minúscula sea True.

def es_vocal (x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return False
es_vocal (e)