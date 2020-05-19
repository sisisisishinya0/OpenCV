# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:54:22 2020

@author: 6752499
"""

import cv2

try:
    img = cv2.imread('C:\\Users\suzuk\program\img\shinya.jpg')

    if img is None:
        print('読み込みできません')
        import sys
        sys.exit()
        
    SCALE1 = 0.5
    SCALE2 = 1.62
    height = img.shape[0]
    width = img.shape[1]
    
    dst = cv2.resize(img, (int(width*SCALE1),int(height*SCALE1)))
    cv2.imwrite('C:\\Users\suzuk\program\img\resize0.5.jpg', dst)
    cv2.imshow('dest1', dst)
    
    dst = cv2.resize(img, (int(width*SCALE2),int(height*SCALE2)))
    cv2.imwrite('C:\\Users\suzuk\program\img\resize1.62.jpg', dst)
    cv2.imshow('dest2', dst)
    
    dst = cv2.resize(img, (200,400))
    cv2.imwrite('C:\\Users\suzuk\program\img\resize400x200.jpg', dst)
    cv2.imshow('dest3', dst)
    
    dst = cv2.resize(img, (int(width*SCALE1),int(height*SCALE2)))
    cv2.imwrite('C:\\Users\suzuk\program\img\resize0.5x1.62.jpg', dst)
    cv2.imshow('dest4', dst)
    
    cv2.waitKey(0)
    cv2.desroyAllWindows()
    
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))

