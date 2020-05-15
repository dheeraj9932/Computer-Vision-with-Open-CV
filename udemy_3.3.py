#Rotations
#cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y, angle of rotation, scale)

import cv2
import numpy as np
image = cv2.imread('images/input.jpg')
height, width = image.shape[:2]
# Divide by two to rotate the image around its centre
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 30, .5)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()
print(rotation_matrix)

#method2-but only rptates in 90 degrees increments

img = cv2.imread('images/input.jpg')
rotated_image = cv2.transpose(img)
cv2.imshow('Rotated Image - Method 2', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

# Let's now to a horizontal flip.
flipped = cv2.flip(image, 0)
cv2.imshow('Horizontal Flip', flipped)
cv2.waitKey()
cv2.destroyAllWindows()