#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 15:11:02 2019

@author: emmanuel
"""

import numpy as np 
import cv2 
# Load an color image in grayscale 
img = cv2.imread('ejemplo1.jpg',0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)