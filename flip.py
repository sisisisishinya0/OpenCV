# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:43:56 2020

@author: 6752499
"""

import cv2

try:
    img = cv2.imread('C:\\Users\suzuk\program\img\shinya.jpg')
    
    if img is None:
        print('ファイルを読み込みできません')
        import sys
        sys.exit()
        
    dst = cv2.flip(img, 0)
    cv2.imwrite('C:\\Users\suzuk\program\img\flip0.jpg', dst)
    cv2.imshow('dst1', dst)
    
    dst = cv2.flip(img, 1)
    cv2.imwrite('C:\\Users\suzuk\program\img\flip1.jpg', dst)
    cv2.imshow('dst2', dst)
    
    dst = cv2.flip(img, -1)
    cv2.imwrite('C:\\Users\suzuk\program\img\flip-1.jpg', dst)
    cv2.imshow('dst3', dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
