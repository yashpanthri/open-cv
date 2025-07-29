import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('cats', img)

blank = np.zeros(img.shape, dtype = 'uint8')  # Create a blank image with the same height and width as the original image, but only one channel (grayscale)
cv.imshow('Blank', blank)

# Convert the original image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


## Method of detecting contours: Canny Edge Detection
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)  # Apply Gaussian blur to the image
cv.imshow('Blur', blur)  # Show the blurred image
canny = cv.Canny(blur,125,175)
cv.imshow('Canny', canny)



# ##Method of detecting contours: Thresholding
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)  # Apply binary thresholding to the image ret: the threshold value, thresh: the thresholded image
# # ret is the threshold value used, which is returned by the function. It is the value that was used to separate the pixel values into two classes: those below the threshold and those above it.
# cv.imshow('Threshold', thresh)  # Show the thresholded image




contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)  # Find contours in the image
#cv.RETR_LIST retrieves all contours without establishing any hierarchy, cv.RETER_EXTERNAL returns only external contours of hierarchy , cv.RETER_TREE gives all contours in hierarchial system.
# cv.CHAIN_APPROX_NONE (returns all points of a line) returns all the points of the contour, cv.CHAIN_APPROX_SIMPLE (returns just end points of a line) compresses horizontal, vertical, and diagonal segments and leaves only their end points.
print(f'{len(contours)} contours found!')  # Print the number of contours found

cv.drawContours(blank, contours, -1, (0, 255,255), 1)  # Draw all contours on the blank image, -1 means draw all contours, (0, 255, 0) is the color of the contour (green), thickness=2 is the thickness of the contour line
cv.imshow('Contours Drawn', blank)  # Show the image with contours drawn

cv.waitKey(0)