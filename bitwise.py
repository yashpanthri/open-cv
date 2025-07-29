import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype = 'uint8')  # Create a blank image of size 400x400 pixels
rectangle = cv.rectangle( blank.copy(), (30,30), (370,370), 255, -1 )# As the image is grayscale, we can use single color parameter that is 255
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1) 
cv.imshow('Rectangle', rectangle)  # Show the rectangle
cv.imshow('Circle', circle)  # Show the circle 

# Bitwise Operations
#Bitwise AND --> Intersecting region
bitwise_and = cv.bitwise_and(rectangle, circle)  # Perform bitwise AND operation
cv.imshow('Bitwise AND', bitwise_and)  # Result is intersection or common area of rectangle and circle

#Bitwise OR --> Intersecting and non-intersecting region
bitwise_or = cv.bitwise_or(rectangle,circle) # Union or superimposition of rectangle and circle
cv.imshow('Bitwise OR', bitwise_or)  # Show the result of bitwise OR operation

#Bitwise XOR --> Non-intersecting region
bitwise_xor = cv.bitwise_xor(rectangle, circle) # A-B U B-A
cv.imshow('Bitwise XOR', bitwise_xor)  # Show the result of bitwise XOR operation (exclusive OR)

#Bitwise NOT --> Inversion of the image
bitwise_not = cv.bitwise_not(rectangle) # Inverts the binary image
cv.imshow("Bitwise NOT", bitwise_not) # Show the result of bitwise NOT operation

cv.waitKey(0)