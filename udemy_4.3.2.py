import cv2
import numpy as np

def sketch(image):
    flipped = cv2.flip(image, 1)
    gray = cv2.cvtColor(flipped, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 100, 255, 0)
    canny = cv2.Canny(thresh, 50, 200)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    n = len(contours) - 1
    contours = sorted(contours, key=cv2.contourArea, reverse=False)[:n]
    for c in contours:
        hull = cv2.convexHull(c)
        cv2.drawContours(canny, [hull], 0, (0, 255, 0), 2)
        #cv2.imshow('Convex Hull', canny)
    return canny

cap = cv2.VideoCapture(0)
cv2.waitKey(1000)

while True:
    ret, frame = cap.read()
    cv2.imshow("livesketch", sketch(frame))
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()