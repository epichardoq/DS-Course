#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:38:17 2019

@author: emmanuel
"""

import time

localtime = time.asctime( time.localtime(time.time()) )
print ("Actual hora local :", localtime)