#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:22:53 2019

@author: emmanuel
"""

class Coche():                                                      #Clase, la primera es mayuscula siempre

    ruedas=4                                                        #Atributo

    def desplazamiento(self):                                       #Funcion (Def), se diferencia de una funcion escribiendo (self), ello son los objetos de la clase
        print("El coche se esta desplazando sobre 4 ruedas")

miVehiculo=Coche()                                                  #Clase lista de objetos
                                                                    #Después del “=” le estamos especificando a que clase pertenece el objeto que acabamos de crear.
print("Mi coche tiene ", miVehiculo.ruedas, " ruedas")              #Para mostrar atributos: miObjeto.atributo

miVehiculo.desplazamiento()                                         #Para mostrar métodos: miObjeto.metodo()