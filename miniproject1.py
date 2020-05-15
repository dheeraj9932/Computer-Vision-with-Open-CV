import cv2
import numpy as np

def sketch(image):
    flipped = cv2.flip(image,1)
    gray_image = cv2.cvtColor(flipped, cv2.COLOR_BGR2GRAY)
    gaussian_blur = cv2.GaussianBlur(gray_image,(5,5),0)
    canny = cv2.Canny(gaussian_blur, 30,100)
    ret, output=cv2.threshold(canny,70,255,cv2.THRESH_BINARY_INV)
    return output

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("livesketch", sketch(frame))
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()
