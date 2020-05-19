# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:52:01 2020

@author: 6752499
"""

import cv2

img = cv2.imread('C:\\Users\suzuk\program\img\shinya.jpg')

try:
    if img is None:
        print('読み込みに失敗しました')
        import sys
        sys.exit()
        
    dst = cv2.GaussianBlur(img,(13,13), 80, 10)
    cv2.imwrite('C:\\Users\suzuk\program\img\gaussianblur1.jpg',dst)
    cv2.imshow('dst1',dst)
    
    dst = cv2.GaussianBlur(img, (31, 31), 80 ,3)
    cv2.imwrite('C:\\Users\suzuk\program\img\gaussianblur2.jpg',dst)
    cv2.imshow('dst2',dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
