# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 14:17:44 2020

@author: 6752499
"""

import cv2
import numpy as np

img = cv2.imread('C:\\Users\suzuk\program\img\LOVE.jpg')

try:
    if img is None:
        print('読み込みに失敗しました')
        import sys
        sys.exit()
    
    kernel = np.ones((3, 3), np.uint8)    
    dst = cv2.erode(img, kernel, iterations =50)
    cv2.imwrite('C:\\Users\suzuk\program\img\erode.jpg',dst)
    cv2.imshow('dst',dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))