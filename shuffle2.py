# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 01:49:56 2020

@author: 6752499
"""


roi_target = [0, 1, 2, 3]
counter = 60
    
while(True):
    for i in range(0, 4):
        print(i, roi_target[i])
            
        counter -= 1
        if counter <= 0:
            counter = 60
            for i in range(0, 4):
                roi_target[i] += 1
                if roi_target[i] == 4:
                    roi_target[i] = 0
                    
                    