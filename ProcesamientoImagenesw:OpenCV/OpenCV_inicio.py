#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:06:36 2019

@author: emmanuel
"""

import numpy as np
import cv2

img = cv2.imread('58-aprenderpython.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k == 27: # wait for ESC key to exit
  cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
  cv2.imwrite('deepgray.jpg',img)
  cv2.destroyAllWindows()