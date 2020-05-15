import cv2
import numpy as np

def sketch(image):
    flipped = cv2.flip(image,1)
    gray_image = cv2.cvtColor(flipped, cv2.COLOR_BGR2GRAY)
    gaussian_blur = cv2.GaussianBlur(gray_image,(5,5),0)
    canny = cv2.Canny(gaussian_blur, 30,150)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    x = np.zeros((image.shape[0],image.shape[1],1), np.uint8)
    output= cv2.drawContours(x, contours, -1, (255,255,255), 3)
    return output

camera_port = 0
#cap = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("livesketch", sketch(frame))
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()
