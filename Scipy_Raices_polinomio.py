#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:02:37 2019

@author: emmanuel
"""

import scipy as sp
import matplotlib.pyplot as plt
# Creamos un polinomio
polinomio = [4.3,9,.6,-1]# polinomio = 4.3 x^3 + 9 x^2 + 0.6 x - 1
# array
x = sp.arange(-4,2,.05)
#&amp;amp;nbsp; Evaluamos el polinomio en x mediante polyval.
y = sp.polyval(polinomio,x)
# Calculamos las raices del polinomio 
raices = sp.roots(polinomio)
# Evaluamos el polinomio en las raices
s = sp.polyval(polinomio,raices)
# Las presentamos en pantalla
print ("Las raices son %2.2f, %2.2f, %2.2f. " % (raices[0], raices[1], raices[2]))
# Creamos la figura
plt.figure
# Dibujamos
plt.plot(x,y,'-', label = 'y(x)')
# Fibujamos en la figura anterior

# Dibujamos
plt.plot(raices.real,s.real,'ro', label = 'Raices')
# Etiquetas 
plt.xlabel('x')
plt.ylabel('y')
plt.title(u'Raices de un polinomio de x^3')
# Leyenda
plt.legend()
# Mostramos la figura en pantalla
plt.show()