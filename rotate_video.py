# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 23:53:00 2020

@author: 6752499
"""


import cv2

try:
    capture = cv2.VideoCapture(0)
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    center = (width//2, height//2)
    degree = 0.0
    
    while(True):
        ret, frame = capture.read()
        if ret == False:
            print('カメラから映像を取得できませんでした。')
            break
        affin_trans = cv2.getRotationMatrix2D(center, degree, 1.0)
        dst = cv2.warpAffine(frame, affin_trans, (width, height))
        degree += 1.0
        
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

                    