import cv2 as cv
import numpy as np


blank = np.zeros((500, 500, 3), dtype='uint8')  # Create a blank image of size 500x500 with 3 color channels
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[:] = 0, 255, 0  # Paint the image green
cv.imshow('Green', blank)
blank[200:300, 300:400] = 255, 0, 0  # Paint a rectangle in the center blue
cv.imshow('Blue Rectangle', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=2)  # Draw a filled green ; Can use rectangle thickness = cv.FILLED or thickness=-1
cv.rectangle(blank, (0,0), (blank.shape[0]//2, blank.shape[1]//2), (0, 255, 0), thickness=cv.FILLED)  # Draw a filled green rectangle in the top left corner
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255, 255, 0), thickness=-1)  # Draw a filled yellow circle in the center
cv.imshow('Circle', blank)
# 4. Draw a line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 255), thickness=3)  # Draw a purple diagonal line from top left to bottom right
cv.imshow('Line', blank)
# 5. Write text
cv.putText(blank, 'Hello, OpenCV!', (10, 400), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), thickness=2)  # Write yellow text at the bottom left corner
cv.imshow('Text', blank)


img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)
