#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:22:35 2019

@author: emmanuel
"""
# para hacer que un atributo o comportamiento sea privado

class Ejemplo():

    def publico(self):
        return "Soy un método público, a la vista de todo"
    def __privado(self):
        return "Soy un metodo privado, para ti no existo"

objeto = Ejemplo()

print(objeto.publico())

print(objeto.__privado())