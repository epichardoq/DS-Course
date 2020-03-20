#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:04:01 2019

@author: emmanuel
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define el codec y crea el objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
       frame = cv2.flip(frame,0) #invierte el cuadro
       
       # escribe el cuadro invertido 
       out.write(frame)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) == ord('q'):
           break
    else:
        break

#Libera todo si la tarea ha terminado
cap.release()
out.release()
cv2.destroyAllWindows()