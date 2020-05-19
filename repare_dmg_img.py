# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:45:56 2020

@author: 6752499
"""

import cv2
import numpy as np

try:
    img = cv2.imread('C:\\Users\suzuk\program\img\CirclesOnImage2.jpg')
    
    if img is None:
        print('ファイルを読み込めません')
        import sys
        sys.exit()

    msk = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, msk = cv2.threshold(msk, 240, 255, cv2.THRESH_BINARY)
        
    cv2.imwrite('C:\\Users\suzuk\program\img\mask2.jpg', msk)
    kernel = np.ones((3,3), np.uint8)
    msk = cv2.dilate(msk, kernel)
    cv2.imwrite('C:\\Users\suzuk\program\img\msk_dilated.jpg', msk)
    
    dst = img.copy()
    dst = cv2.inpaint(img, msk, 1, cv2.INPAINT_TELEA)
    
    cv2.imwrite('C:\\Users\suzuk\program\img\dst4.jpg', dst)
    cv2.imshow('dst', dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))