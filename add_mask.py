# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 22:11:02 2020

@author: 6752499
"""

import cv2
import numpy as np

try:
    img1 = cv2.imread('C:\\Users\suzuk\program\img\shinya.jpg')
    img2 = cv2.imread('C:\\Users\suzuk\program\img\hana.jpg')
    img3 = cv2.imread('C:\\Users\suzuk\program\img\hana3.jpg')
    
    if img1 is None or img2  is None or img3 is None:
        print('ファイルを読み込めません')
        import sys
        sys.exit()
    
    height = img1.shape[0]
    width = img1.shape[1]

    img_mask = np.zeros((height, width), np.uint8)
    img_mask[:,:] = [0]
    img_mask[height//4:height*3//4, width//4:width*3//4] = [255]

    dst = cv2.add(img1, img2, mask = img_mask)
    cv2.imwrite('C:\\Users\suzuk\program\img\addMask1.jpg', dst)
    cv2.imshow('dst1', dst)

    dst = cv2.add(img1, img2, dst = img1, mask = img_mask)
    cv2.imwrite('C:\\Users\suzuk\program\img\addMask2.jpg', dst)
    cv2.imshow('dst2', dst)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
