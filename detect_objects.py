# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:02:36 2020

@author: 6752499
"""

import cv2

try:
    img = cv2.imread('C:\\Users\suzuk\program\img\shinya.jpg')
    
    if img is None:
        print('ファイルを読み込めません')
        import sys
        sys.exit()
        
    cascade = cv2.CascadeClassifier(r'C:\\Users\suzuk\program\data\haarcascade_frontalface_alt.xml')
    facerect = cascade.detectMultiScale(img)
    
    if len(facerect) > 0:
        for rect in facerect:
            print(rect)
            print(rect[0:2])
            x,y = rect[0:2]
            cv2.circle(img, (x,y), 4, (255,255,0), 2)
            cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=2)
            
    else:
        print('no face')
        
    cv2.imwrite('C:\\Users\suzuk\program\img\dobj.jpg', img)
    cv2.imshow('img', img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print('Error:', sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
