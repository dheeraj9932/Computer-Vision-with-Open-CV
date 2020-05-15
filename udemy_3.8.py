import cv2
import numpy as np

# If you're wondering why only two dimensions, well this is a grayscale image,
# if we doing a colored image, we'd use
# rectangle = np.zeros((300, 300, 3),np.uint8)

# Making a sqare
square_img = np.zeros((300, 300), np.uint8)
cv2.rectangle(square_img, (50, 50), (250, 250), 255, -69)
cv2.imshow("Square", square_img)
cv2.waitKey(0)

# Making a ellipse
ellipse_img = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse_img, (150, 150), (100,100), 45, 0, 180, 255, -1)
cv2.imshow("Ellipse", ellipse_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Shows only where they intersect
And = cv2.bitwise_and(square_img, ellipse_img)
cv2.imshow("AND", And)
cv2.waitKey(0)

# Shows where either square or ellipse is
bitwiseOr = cv2.bitwise_or(square_img, ellipse_img)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

# Shows where either exist by itself
bitwiseXor = cv2.bitwise_xor(square_img, ellipse_img)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

# Shows everything that isn't part of the square
bitwiseNot_sq = cv2.bitwise_not(square_img)
cv2.imshow("NOT - square", bitwiseNot_sq)
cv2.waitKey(0)

### Notice the last operation inverts the image totally

cv2.destroyAllWindows()

ellipse_img1 = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse_img1, (150, 150), (100, 50), 0, 0, 360, 255, -1)
#cv2.imshow("Ellipse", ellipse_img1)
#cv2.waitKey(0)

ellipse_img2 = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse_img2, (150, 150), (50, 5), 90, 0, 360, 255, -1)
#cv2.imshow("Ellipse", ellipse_img2)
#cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(ellipse_img1, ellipse_img2)
cv2.imshow("The Eye of Sauron", bitwiseXor)
cv2.waitKey(0)