# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 00:28:48 2020

@author: 6752499
"""

import cv2
import numpy as np

try:
    img1 = cv2.imread('C:\\Users\suzuk\program\img\shinya.jpg')
    img2 = cv2.imread('C:\\Users\suzuk\program\img\hana.jpg')
    img3 = cv2.imread('C:\\Users\suzuk\program\img\circle3.jpg')
    
    if img1 is None or img2 is None or img3 is None:
        print('ファイルを読み込めません')
        import sys
        sys.exit()
        
    dst = cv2.bitwise_or(img1, img2)
    cv2.imwrite('C:\\Users\suzuk\program\img\or.jpg', dst)
    cv2.imshow('dst1', dst)

    
    img_mask = cv2.resize(img3, img1.shape[1::-1])
    dst = cv2.bitwise_or(img_mask, img1, img_mask, img1)
    cv2.imwrite('C:\\Users\suzuk\program\img\orMask.jpg', dst)
    cv2.imshow('dst2', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
