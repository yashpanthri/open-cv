import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

##### Method of blurring #####

##Averaging
average = cv.blur(img, (3, 3))  # Apply averaging filter with a kernel size of 7x7
cv.imshow('Averaging', average)

##Gaussian Blurring
gaussian = cv.GaussianBlur(img, (7,7), 0)  # Apply Gaussian blur with a kernel size of 7x7
cv.imshow('Gaussian', gaussian)

##Median Blurring
median = cv.medianBlur(img, 3)  # Takes a kernel size of 3 and takes median of the pixels in that kernel around a pixel
cv.imshow('Median', median)

##Bilateral Blurring
bilateral = cv.bilateralFilter(img, 5, 15, 15) #cv.bilateralFilter(img, d, sigmaColor, sigmaSpace)
#sigmaColor means how much the color values within a pixel neighborhood will be mixed
#sigmaSpace means how much the spatial distance between pixels will be mixed
#d means diameter of the pixel neighborhood
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)