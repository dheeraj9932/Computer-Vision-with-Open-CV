import cv2
import numpy as np

image = cv2.imread('images/someshapes.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, threshold = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('image', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours), np.shape(contours))

contours = sorted(contours, key=cv2.contourArea, reverse=False)
#contours = contours.pop(-1)
contours = contours[:-1]
print(contours)
print(len(contours), np.shape(contours))

for c in contours:
    accuracy = 0.01*cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, accuracy, True)
    print(len(approx))
    M = cv2.moments(c)
    cx = (int(M['m10'] / M['m00']) - 10)
    cy = (int(M['m01'] / M['m00']) + 10)
    #cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
    #cv2.imshow('image', image)
    #cv2.waitKey(0)
    cv2.destroyAllWindows()
    if len(approx) == 3:
        cv2.drawContours(image, [c], 0, (0, 255, 0), -1)
        cv2.putText(image,"triangle", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 100, 100), 2)
        cv2.imshow('image', image)
        cv2.waitKey()
    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(approx)
        if abs(w-h)>= 0.2*w or abs(w-h)>= 0.2*h :
            cv2.drawContours(image, [c], 0, (255, 0, 0), -1)
            cv2.putText(image, "rectangle", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 100, 100), 2)
            cv2.imshow('image', image)
            cv2.waitKey()
        else:
            cv2.drawContours(image, [c], 0, (0, 0, 255), -1)
            cv2.putText(image, "square", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 100, 100), 2)
            cv2.imshow('image', image)
            cv2.waitKey()
    elif 13 >= len(approx) >=10:
        cv2.drawContours(image, [c], 0, (255, 255, 0), -1)
        cv2.putText(image,"star", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 100, 100), 2)
        cv2.imshow('image', image)
        cv2.waitKey()
    else:
        cv2.drawContours(image, [c], 0, (100, 150, 200), -1)
        cv2.putText(image,"circle", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 100, 100), 2)
        cv2.imshow('image', image)
        cv2.waitKey()
"""
for i in range(len(contours)):
    if i == 0:
        pass
    else:
        accuracy = 0.01*cv2.arcLength(contours[i], True)
        approx = cv2.approxPolyDP(contours[i], accuracy, True)
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
        cv2.imshow('image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
"""