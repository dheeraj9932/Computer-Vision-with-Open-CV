import cv2
import numpy as np


image = cv2.imread('images/gradient.jpg',0)
cv2.imshow('Original', image)
cv2.waitKey()


#values below 127 goes to 0(black), everything above goes to 255(white)
ret, thresh1 = cv2.threshold(image, 127,255,cv2.THRESH_BINARY)
cv2.imshow('1 threshold binary', thresh1)
cv2.waitKey()

#values below 127 go to 255 and values above 127 goes to zero
ret, thresh2 = cv2.threshold(image, 127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('2 threshold binary inverse', thresh2)
cv2.waitKey()

#values below 127 are truncated at 127
ret, thresh3 = cv2.threshold(image, 127,255,cv2.THRESH_TRUNC)
cv2.imshow('3 threshold truncated', thresh3)
cv2.waitKey()

#values below 127 go to 0 and above 127 are unchanged
ret, thresh4 = cv2.threshold(image, 127,255,cv2.THRESH_TOZERO)
cv2.imshow('3 threshold tozero', thresh4)
cv2.waitKey()

#reverse of above
ret, thresh5 = cv2.threshold(image, 127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('3 threshold tozero_inverse', thresh5)
cv2.waitKey()
