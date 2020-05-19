# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:06:25 2020

@author: 6752499
"""

import cv2

try:
    capture = cv2.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        
        if ret == False:
            print('カメラから映像を取得できませんでした。')
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dst = cv2.equalizeHist(gray)
        cv2.imshow('f', dst)
        
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

        