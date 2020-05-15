#!/usr/bin/env python
# coding: utf-8

# # Circle Detection - Hough Cirlces
# 
# **cv2.HoughCircles**(image, method, dp, MinDist, param1, param2, minRadius, MaxRadius)
# 
# 
# - Method - currently only cv2.HOUGH_GRADIENT available
# - dp - Inverse ratio of accumulator resolution
# - MinDist - the minimum distance between the center of detected circles
# - param1 - Gradient value used in the edge detection
# - param2 - Accumulator threshold for the HOUGH_GRADIENT method (lower allows more circles to be detected (false positives))
# - minRadius - limits the smallest circle to this size (via radius)
# - MaxRadius - similarly sets the limit for the largest circles
# 
# 

# In[ ]:


import cv2
import numpy as np
from numpy import interp
#import cv2.cv as cv

image = cv2.imread('images/bottlecaps.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 35, param1=50, param2=30, minRadius=0, maxRadius=45)
#circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 20, 45)
#circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1, 10)
print(len(circles[0]))
circles = np.uint16(np.around(circles))

k=0
for i in circles[0,:]:
    k += 1
    # draw the outer circle
    cv2.circle(image,(i[0], i[1]), i[2], (255, 0, 0), 2)
    cv2.putText(image, str(k), (i[0], i[1]), cv2.FONT_HERSHEY_COMPLEX,0.8, (0, 0, 0), 2)
    # draw the center of the circle
    cv2.circle(image, (i[0], i[1]), 2, (0, 255, 0), 5)

p = abs(len(circles[0])-74)
print(p)
z = interp(p,[0,74],[100,0])
print(z)
cv2.imshow('detected circles, total detected ' + str(len(circles[0])) + ' with accuracy of ' + str(z) + "%", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




