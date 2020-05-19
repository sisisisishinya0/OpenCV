# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:00:30 2020

@author: 6752499
"""

import cv2

try:
    capture = cv2.VideoCapture(0)

    while(True):
        ret, frame = capture.read()
        if ret == False:
            print('カメラから読み込みできませんでした')
            break
        
        cv2.imshow('f', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    capture.release()
    cv2.destroyAllWindows()
    
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
