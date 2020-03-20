#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:24:39 2019

@author: emmanuel
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('58-aprenderpython.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()