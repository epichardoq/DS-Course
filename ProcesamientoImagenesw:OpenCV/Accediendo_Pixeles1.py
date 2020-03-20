#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:43:36 2019

@author: emmanuel
"""

import cv2
import numpy as np
img = cv2.imread('trump.jpg')


# accessing RED value
img.item(10,10,2)
# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()