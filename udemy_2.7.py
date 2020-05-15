import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('images/input.jpg')

# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
histogram1 = cv2.calcHist([image], [2], None, [256], [0, 256])
histogram2 = cv2.calcHist([image], [2], None, [256], [0, 256])
histogram3 = cv2.calcHist([image], [2], None, [256], [0, 256])

plt.plot(histogram1); plt.plot(histogram2); plt.plot(histogram3);
plt.show()

plt.hist(image[0].ravel(), 256, [0, 256])
plt.hist(image[1].ravel(), 256, [0, 256])
plt.hist(image[2].ravel(), 256, [0, 256])
plt.show()

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram2, color=col)
    plt.xlim([0, 256])


"""
#educational purposes
    print(str(i))
    print(col)
    E= (enumerate(color))
    print(list(E))
    print([image])

    k=[(1,2,3,(12,23,13)),(4,5,6),(7,8,9)]
    print(list(enumerate(k)))
"""
plt.show()