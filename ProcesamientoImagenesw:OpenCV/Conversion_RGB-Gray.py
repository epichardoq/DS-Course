#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 22:43:08 2019

@author: emmanuel
"""

import cv2

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

print (flags)
