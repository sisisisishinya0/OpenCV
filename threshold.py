# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:16:35 2020

@author: 6752499
"""

import cv2

try:
    img = cv2.imread('C:\\Users\suzuk\program\img\shinya.jpg', cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print('ファイルを見込みません')
        import sys
        sys.exit()
        
    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_BINARY)
    cv2.imwrite('C:\\Users\suzuk\program\img\threshold_THRESH_BIARY.jpg', dst)
    cv2.imshow('dst', dst)
    
    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_BINARY_INV)
    cv2.imwrite('C:\\Users\suzuk\program\img\threshold_THRESH_BIARY_INV.jpg', dst)
    cv2.imshow('dst2', dst)
    
    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_TRUNC)
    cv2.imwrite('C:\\Users\suzuk\program\img\threshold_THRESH_TRUNC.jpg', dst)
    cv2.imshow('dst3', dst)
    
    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_TOZERO)
    cv2.imwrite('C:\\Users\suzuk\program\img\threshold_THRESH_TOZERO.jpg', dst)
    cv2.imshow('dst4', dst)
    
    ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_TOZERO_INV)
    cv2.imwrite('C:\\Users\suzuk\program\img\threshold_THRESH_TOZERO_INV.jpg', dst)
    cv2.imshow('dst5', dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))

    