#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:32:05 2019

@author: emmanuel
"""


import numpy as np
import cv2

# Crea una imagen en negro
img = np.zeros((512,512,3), np.uint8)

img = cv2.ellipse(img,(255,105),(100,50),0,0,180,255,-1)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()