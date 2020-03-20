#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:43:55 2019

@author: emmanuel
"""

import cv2
# cargamos 2 imagenes
img1 = cv2.imread('dst.png')
img2 = cv2.imread('aprenderpython.png')
# Yo quiero poner el logo en el corner izquierdo y por eso creo un ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
# Ahora creo una máscara de logotipo y hago su máscara inversa también
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 250, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# Ahora pongo oscura el área de logotipo en ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
# Tome solamente la región del logotipo de la imagen del logotipo
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
# Ponga el logotipo en ROI y modifique la imagen principal
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('res',roi )
cv2.waitKey(0)
cv2.destroyAllWindows()