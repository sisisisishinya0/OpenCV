# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 00:13:53 2020

@author: 6752499
"""


import cv2
import numpy as np

try:
    img1 = cv2.imread('C:\\Users\suzuk\program\img\shinya.jpg')
    img2 = cv2.imread('C:\\Users\suzuk\program\img\hana.jpg')
    
    if img1 is None or img2 is None:
        print('ファイルを読み込めません')
        import sys
        sys.exit()
    
    img3 = cv2.bitwise_not(img1)
    
    dst = cv2.addWeighted(img1, 1, img2, 1, -50)
    cv2.imwrite('C:\\Users\suzuk\program\img\blend0307.jpg', dst)
    cv2.imshow('dst1', dst)

    dst = cv2.addWeighted(img1, 0.6, img2, 0.4, 0.0)
    cv2.imwrite('C:\\Users\suzuk\program\img\blend0604.jpg', dst)
    cv2.imshow('dst2', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
