#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:49:59 2019

@author: emmanuel
"""

import numpy as np
import cv2

# Crea una imagen en negro
img = np.zeros((512,512,3), np.uint8)

# Dibuja una línea horizontal verde con un grosor de 4 px
img = cv2.line(img,(0,255),(511,255),(0,255,0),4)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()