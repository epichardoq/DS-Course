#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:05:46 2019

@author: emmanuel
"""

import cv2

img1 = cv2.imread('python-log.png')
img2 = cv2.imread('pirata.png')
img3=img1[1:268,1:501,:]

dst = cv2.addWeighted(img3,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
cv2.imwrite('dst.png',dst)
cv2.waitKey(0)

cv2.destroyAllWindows()