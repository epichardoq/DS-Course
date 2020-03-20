#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:34:13 2019

@author: emmanuel
"""



import numpy as np
import cv2

# Crea una imagen en negro
img = np.zeros((512,512,3), np.uint8)

pts = np.array([[180,120],[330,120],[255,140]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()