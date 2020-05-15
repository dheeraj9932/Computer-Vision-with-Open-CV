#Scaling, re-sizing and interpolations
#Re-sizing is very easy using the cv2.resize function, it's arguments are:

#cv2.resize(image, dsize(output image size), x scale, y scale, interpolation)

import cv2
import numpy as np
# load our input image
image = cv2.imread('images/input.jpg')
# Let's make our image 3/4 of it's original size
image_scaled = cv2.resize(image, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)
image_scaled2= cv2.resize(image_scaled,None,fx=10,fy=10,interpolation=cv2.INTER_LANCZOS4)
image_scaled3= cv2.resize(image_scaled,None,fx=10,fy=10,interpolation=cv2.INTER_LINEAR)
image_scaled4= cv2.resize(image_scaled,None,fx=10,fy=10,interpolation=cv2.INTER_CUBIC)
image_scaled5= cv2.resize(image_scaled,None,fx=10,fy=10,interpolation=cv2.INTER_NEAREST)
cv2.imshow('Scaling - LANCZOS4 Interpolation', image_scaled2)
cv2.imshow('Scaling - Linear Interpolation', image_scaled3)
cv2.imshow('Scaling - CUBIC Interpolation', image_scaled4)
cv2.imshow('Scaling - NEAREST Interpolation', image_scaled5)
cv2.waitKey()


# Let's double the size of our image
img_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation', img_scaled)
cv2.waitKey()
# Let's skew the re-sizing by setting exact dimensions
img_scaled = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Size', img_scaled)
cv2.waitKey()
cv2.destroyAllWindows()
