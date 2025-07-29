import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Cat', img)

#Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur the image
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=1) # Make bright/foreground areas thicker. Every pixel is replaced by the maximum value in its neighborhood, so white/bright blobs grow outward by the structuring-element’s radius.
cv.imshow('Dilated', dilated)


#Eroding the image
eroded = cv.erode(dilated, (3,3), iterations=1) # Make bright/foreground areas thinner. Every pixel is replaced by the minimum value in its neighborhood, so white/bright blobs shrink inward by the structuring-element’s radius.
cv.imshow('Eroded', eroded)

#Resize the image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA) # Resize the image to destination size of 500x500 pixels(NOTE: Use cv.INTER_AREA for shrinking images, cv.INTER_LINEAR or cv.INTER_CUBIC for enlarging images)
#resize = cv.resize(image matrix, (width, height), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)


#Cropping the image
cropped = img[50:200, 200:400] # Crop the image from row 50 to 200 and column 200 to 400 img[start_row:end_row, start_col:end_col]
cv.imshow('Cropped', cropped)

# Wait for a key press and close all windows
cv.waitKey(0)