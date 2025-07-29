import cv2 as cv
import numpy as np

img = cv.imread ('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')  
cv.imshow('Blank', blank)  

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)  # Create a circular mask
cv.imshow('Mask', circle)  # Show the mask
rectangle = cv.rectangle( blank.copy(), (30,30), (370,370), 255, -1 )# As the image is grayscale, we can use single color parameter that is 255
weird_shape = cv.bitwise_and(rectangle, circle)  # Perform bitwise AND operation
cv.imshow('Weird Shape', weird_shape)  # Show the weird shape

masked = cv.bitwise_and(img, img, mask = weird_shape)  # image & image = image and then apply mask
# mask tells which part of the image to keep
cv.imshow('Masked Image', masked)  # Show the masked image

cv.waitKey(0)












########################################################################################################################################################################################################################################################################


# import cv2 as cv
# import numpy as np

# img = cv.imread ('Photos/cats.jpg')
# cv.imshow('Cats', img)

# blank = np.zeros(img.shape, dtype='uint8')  
# cv.imshow('Blank', blank)  

# mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, (255,255,255), -1)  # Create a circular mask
# cv.imshow('Mask', mask)  # Show the mask
# print('Mask shape:', mask.shape)  # Print the shape of the mask
# print('Image shape:', img.shape)  # Print the shape of the image

# masked = cv.bitwise_and(img, blank)
# cv.imshow('Masked Image', masked)  # Show the masked image

# cv.waitKey(0)