import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')

B,G,R = image[10,50]
print (str(B)+" "+str(G)+" "+str(R))
print(image.shape)

gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
B= gray_img[10,50]
print (str(B))
print(gray_img.shape)

#cv2.imshow('show',gray_img)
#cv2.waitKey()
#cv2.destroyAllWindows()
'''''
hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
cv2.imshow('hsv_image',hsv_image)
cv2.imshow('hue',hsv_image[:,:,0])
cv2.imshow('sat',hsv_image[:,:,1])
cv2.imshow('val',hsv_image[:,:,2])
cv2.waitKey()
cv2.destroyAllWindows()

h,s,v = cv2.split(hsv_image)
cv2.imshow("hue2",h)
cv2.imshow("sat2",s)
cv2.imshow("val2",v)
cv2.waitKey()
cv2.destroyAllWindows()
'''''


b,g,r = cv2.split(image)
'''''
cv2.imshow('image',image)
cv2.imshow('b',image[:,:,0])
cv2.imshow('g',image[:,:,1])
cv2.imshow('r',image[:,:,2])
cv2.waitKey()
cv2.destroyAllWindows()

b,g,r = cv2.split(image)
cv2.imshow("r2",r)
cv2.imshow("g2",g)
cv2.imshow("b2",b)
'''
'''''
merged_image1 = cv2.merge([b,g,r])
merged_image2 = cv2.merge([g,r,b])
merged_image3 = cv2.merge([r,g,b])
merged_image4 = cv2.merge([b,r,g])
merged_image5 = cv2.merge([g,b,r])
merged_image6 = cv2.merge([r,b,g])

cv2.imshow("merged1",merged_image1)
cv2.imshow("merged2",merged_image2)
cv2.imshow("merged3",merged_image3)
cv2.imshow("merged4",merged_image4)
cv2.imshow("merged5",merged_image5)
cv2.imshow("merged6",merged_image6)

cv2.waitKey()
cv2.destroyAllWindows()

'''''
B, G, R = cv2.split(image)

# Let's create a matrix of zeros
# with dimensions of the image h x w
zeros = np.zeros(image.shape[:2], dtype = "uint8")

#den = np.identity([10,10], dtype= "str")
#print (iden)

cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

print(image.shape[1:3])



cv2.waitKey(0)
cv2.destroyAllWindows()