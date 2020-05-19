# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:26:36 2020

@author: 6752499
"""

import cv2

try:
    img = cv2.imread('C:\\Users\suzuk\program\img\shinya.jpg')
    msk = cv2.imread('C:\\Users\suzuk\program\img\circle_mask.jpg', cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print('ファイルを読み込めません')
        import sys
        sys.exit()
        
    dst = cv2.inpaint(img, msk, 1, cv2.INPAINT_TELEA)
    
    cv2.imwrite('C:\\Users\suzuk\program\img\dst3.jpg', dst)
    cv2.imshow('dst', dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
