import cv2
import numpy as np

# Create a black image
image = np.zeros((512,512,3), np.uint8)

# Can we make this in black and white?
image_bw = np.zeros((512,512), np.uint8)

cv2.imshow("Black Rectangle (Color)", image)
cv2.imshow("Black Rectangle (B&W)", image_bw)

cv2.waitKey(0)
cv2.destroyAllWindows()
#################################################################

# Draw a diagonal blue line of thickness of 5 pixels
image = np.zeros((512,512,3), np.uint8)
cv2.line(image, (0,0), (511,511), (255,255,255), 20)
cv2.line(image, (0,512),(512,0),(255,255,255),20)
cv2.imshow("white cross", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
#################################################################
# Draw a Rectangle in
image = np.zeros((512,512,3), np.uint8)

cv2.rectangle(image, (200,200), (400,450), (255,255,255), 5)
cv2.rectangle(image, (100,100), (300,250), (255,255,255), -1)
cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
##################################################################

#circles
#cv2.cirlce(image, center, radius, color, fill)

image = np.zeros((512,512,3), np.uint8)
cv2.circle(image, (150, 150), 100, (0,255,255), 5)
cv2.circle(image, (350, 350), 100, (15,75,50), -1)
cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
##################################################################

#polygons

image = np.zeros((512,512,3), np.uint8)

# Let's define four points
pts1 = np.array( [[10,50], [400,50], [90,200], [50,500]], np.int32)
pts2 = np.array( [[500,50], [500,500], [60,480], [400,400]], np.int32)

# Let's now reshape our points in form  required by polylines
pts1 = pts1.reshape((-1,1,2))
pts2 = pts2.reshape((-1,1,2))

cv2.polylines(image, [pts1], True, (0,0,255), 3)
cv2.polylines(image, [pts2], True, (0,0,255), 3)
cv2.imshow("Polygon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#####################################################################
'''
cv2.putText(image, 'Text to Display', bottom left starting point, Font, Font Size, Color, Thickness)

FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN
FONT_HERSHEY_DUPLEX,FONT_HERSHEY_COMPLEX
FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL
FONT_HERSHEY_SCRIPT_SIMPLEX
FONT_HERSHEY_SCRIPT_COMPLEX
'''
image = np.zeros((512,512,3), np.uint8)

cv2.putText(image, 'Hello World!', (75,290), cv2.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3)
cv2.imshow("Hello World!", image)
cv2.waitKey(0)
cv2.destroyAllWindows()















