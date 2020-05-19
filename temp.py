# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:04:53 2020

@author: 6752499
"""

list = ['a','b','c','d','e']
list[:] = ['C','D','E']
print(list[:])

import numpy as np
img = np.zeros((400,400,3),np.uint8)
print(img)

img[:,:]=[255,0,0]
print(img)