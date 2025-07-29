import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')  

b, g, r = cv.split(img)  # Split the image into its blue, green, and red channels

cv.imshow('Blue', b) #Blue channel
cv.imshow('Green', g) #Green channel
cv.imshow('Red', r) #Red channel

blue = cv.merge([b, blank, blank])  # Create a blue image by merging the blue channel with blank channels
green = cv.merge([blank, g, blank])  # Create a green image by merging the green channel with blank channels
red = cv.merge([blank, blank, r])  # Create a red image by merging the red channel with blank channels

cv.imshow('Blue Image', blue)  # Show the blue image
cv.imshow('Green Image', green)  # Show the green image
cv.imshow('Red Image', red)  # Show the red image

#Printing the shape of the image and its channels
print('Image shape:', img.shape)  # Print the shape of the original image
print('Blue channel shape:', b.shape)  # Print the shape of the blue channel
print('Green channel shape:', g.shape)  # Print the shape of the green channel
print('Red channel shape:', r.shape)  # Print the shape of the red channel

merged = cv.merge([b,g,r])  # Merge the blue, green, and red channels back into a single image
cv.imshow('Merged Image', merged)  # Show the merged image

cv.waitKey(0)
