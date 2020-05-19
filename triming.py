# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:31:44 2020

@author: 6752499
"""

import cv2

try:
    img = cv2.imread('C:\\Users\suzuk\program\img\shinya.jpg')
    if  img is None:
        print('読み込みできません')
        import sys
        sys.exit()
        
    height = img.shape[0]
    width = img.shape[1]
    
    dst = img[40:height, 40:width]
    cv2.imwrite('C:\\Users\suzuk\program\img\triming.jpg', dst)
    
    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
