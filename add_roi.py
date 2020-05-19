# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:42:57 2020

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
    
    dst = img1.copy()
    
    height = img1.shape[0]
    width = img1.shape[1]

    img1_roi = img1[height//4:height*3//4, width//4:width*3//4]
    img2_roi = img2[height//4:height*3//4, width//4:width*3//4]
    dst_roi = dst[height//4:height*3//4, width//4:width*3//4]
    
    cv2.add(img1_roi, img2_roi, dst_roi)
    cv2.imwrite('C:\\Users\suzuk\program\img\dst.jpg', dst)
    cv2.imshow('dst', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
