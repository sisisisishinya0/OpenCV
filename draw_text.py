# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:25:36 2020

@author: 6752499
"""

import cv2
import sys

try:
    img = cv2.imread('C:\\Users\suzuk\program\img\shinya.jpg')
    
    if img is None:
        print('ファイルを読み込めません')
        import sys
        sys.exit()
        
    cv2.circle(img, (50, 50), 40, (0, 255, 0), 2)
    cv2.circle(img, (150, 150), 80, (255, 255, 0), 6, cv2.LINE_8)
    cv2.circle(img, (200, 200), 50, (0, 255, 255), -1, cv2.LINE_8)  
    cv2.putText(img, 'Hello OpenCV', (300, 300), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, (255, 255, 255), 6, cv2.LINE_AA)  
    
    
    cv2.imwrite('C:\\Users\suzuk\program\img\puttext3.jpg', img)
    
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
