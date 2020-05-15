import numpy as np
import cv2 as cv

###########read_Stuff###########read_Stuff###########read_Stuff###########read_Stuff###########read_Stuff###########read_Stuff###########read_Stuff
inputvar = cv.imread('./images/input.jpg')
cv.imshow('input',inputvar)
cv.waitKey()
cv.destroyAllWindows()

############image_data############image_data############image_data############image_data############image_data############image_data############image_data
k = inputvar.shape
print(k)
print(inputvar.shape)
print(inputvar.size)

print ('Height of Image: '+ str(inputvar.shape[0])+ ' pixels')
print ('Width of Image: '+ str(inputvar.shape[1])+ ' pixels')

##########write##########write##########write##########write##########write##########write##########write##########write##########write##########write
cv.imwrite('./images/0000110.jpg',inputvar)
cv.imwrite('louvre.png',inputvar)
cv.imwrite('louvre.jpg',inputvar)




