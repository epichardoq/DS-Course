#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:06:17 2019

@author: emmanuel
"""

class Coche():

    ruedas=4

    def desplazamiento(self):
        print("El coche se esta desplazando sobre 4 ruedas")

class Moto():

    ruedas=2

    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")

miVehiculo=Coche()

print("Mi coche tiene ", miVehiculo.ruedas, " ruedas")

miVehiculo.desplazamiento()

print("---------------Segundo objeto---------------")

miVehiculo2=Moto()

print("Mi moto tiene ", miVehiculo2.ruedas, " ruedas")

miVehiculo2.desplazamiento()