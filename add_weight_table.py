# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:11:11 2020

@author: 6752499
"""

import cv2
import math
import numpy as np

try:
    def create_cos(rows, cols):
        weight = np.zeros((row, cols, 3), np.uint8)
        center = (row/2, cols/2)
        radius = math.sqrt(center[0]**2 + center[1]**2)

        for r in range(rows):
            for c in range(cols):
                #distance from center
                distance = math.sqrt((center[0] - r) **2 + (center[1] - c)**2)
                
                #radius=π, current radian
                radian = (distance / radius) * math.pi
                
                #cosΘ, normalie -1.0~1.0 to 0~1.0
                Y = (math.cos(radian) + 1.0) / 2.0
                weight[r, c] = [Y, Y, Y]
                
        return weight
    
    img1 = cv2.imread('C:\\Users\suzuk\program\img\shinya.jpg').astype（np.uint8) / 255
    img2 = cv2.imread('C:\\Users\suzuk\program\img\hana.jpg').astype(np.uint8) / 255
    
    if img1 is None or img2 is None:
        print('ファイルを読み込めません')
        import sys
        sys.exit()

    row, cols = img1.shape[:2]
    
    weight = create_cos(rows, cols)
    i_weight = 1.0 - weight
    
    int_src1 = cv2.multiply(img1, weight)
    int_src2 = cv2.multiply(img2, i_weight)
    
    dst = cv2.add(int_src1, int_src2)
    
    cv2.imwrite('C:\\Users\suzuk\program\img\int_src1.jpg', int_src1 * 255)
    cv2.imwrite('C:\\Users\suzuk\program\img\int_src2.jpg', int_src2 * 255)
    cv2.imwrite('C:\\Users\suzuk\program\img\dst.jpg', dst * 255)
    #cv2.imshow('int_src1', int_src1)
    #cv2.imshow('int_src2', int_src2)
    #cv2.imshow('dst', dst)
    
    cv2.imshow('ins_src1', (int_src1 * 255).astype(np.uint8))
    cv2.imshow('ins_src2', (int_src2 * 255).astype(np.uint8))
    cv2.imshow('dst', (dst * 255).astype(np.uint8))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
