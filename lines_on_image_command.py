# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:08:53 2020

@author: 6752499
"""

import cv2
import sys

try:
    if(len(sys.argv) !=2):
        print('引数に読み込む画像を指定する必要があります')
        sys.exit()
        
    img = cv2.imread(sys.argv[1])
    
    if img is None:
        print('ファイルを読み込めません')
        import sys
        sys.exit()
        
    cv2.line(img, (50, 50), (200, 50), (255, 0, 0))
    
    cv2.line(img, (50, 100), (200, 100), (0, 255, 0), 5)
    
    cv2.imwrite('C:\\Users\suzuk\program\img\LinesOnImage1.jpg', img)
    
    cv2.imshow('img', img)
    cv2.waitKet(0)
    cv2.destroyAllWindows()

except:
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
