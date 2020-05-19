# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 16:47:05 2020

@author: 6752499
"""
 
import cv2

try:
    img1 = cv2.imread('C:\\Users\suzuk\program\img\shinya.jpg')
    img2 = cv2.imread('C:\\Users\suzuk\program\img\hana.jpg')
    
    if img1 is None or img2 is None:
        print('ファイルを読み込めません')
        import sys
        sys.exit()
        
    dst = cv2.add(img1, img2)
    cv2.imwrite('C:\\Users\suzuk\program\img\add.jpg', dst)
    cv2.imshow('dst', dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
