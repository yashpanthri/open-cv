import cv2 as cv
import matplotlib.pyplot as plt
# Read the image
img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

#Convert BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Convert BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#Conver BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab', lab)  

plt.imshow(img) # Display the image using matplotlib
plt.show() # Show the matplotlib window

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)  # Show the RGB image in an OpenCV window

plt.imshow(rgb) # Display the RGB image using matplotlib
plt.show() # Show the matplotlib window

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)  # Convert HSV back to BGR
cv.imshow('HSV to BGR', hsv_bgr)  # Show the converted image

lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)  # Convert L*a*b back to BGR
cv.imshow('Lab to BGR', lab_bgr)  # Show the converted image  



### There is no direct way to convert grayscale to hsv. First convert grayscale to BGR, then to HSV!!###



cv.waitKey(0) # Wait for a key press to close the OpenCV windows