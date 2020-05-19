# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:55:34 2020

@author: 6752499
"""

import cv2

try:
    img = cv2.imread('C:\\Users\suzuk\program\img\canny.jpg')
    
    if img is None:
        print('読み込みに失敗しました')
        import sys
        sys.exit()
    
    dst = cv2.bitwise_not(img)
    cv2.imwrite('C:\\Users\suzuk\program\img\bitwisenot2.jpg', dst)
    
    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))

    