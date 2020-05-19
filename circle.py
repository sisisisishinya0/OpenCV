# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:30:36 2020

@author: 6752499
"""

import numpy as np
import cv2

img = np.zeros((630, 1200, 3), np.uint8)
cv2.circle(img, (451,134), 50, (255, 0,0), -1)
cv2.imwrite('C:\\Users\suzuk\program\img\circle_mask.jpg', img)
cv2.imshow('img1', img)

cv2.waitKey(0)
cv2.destroyAllWindows()