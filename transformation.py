import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

#Translation
def translate(img,x,y):
    trans_mat = np.float32([[1,0,x],[0,1,y]]) # Create a translation matrix
    dimensions =(img.shape[1], img.shape[0]) # Get the dimensions of the image in the form (width, height) tuple
    return cv.warpAffine(img, trans_mat, dimensions) # Apply the translation matrix to the image

# -x and -y will move the image to the left and up respectively
# +x and +y will move the image to the right and down respectively

translated_img = translate(img, 100, 100) # Translate the image by 100 pixels to the right and down
cv.imshow('Translated Image', translated_img)



# Roataion
def rotate(img, angle,rot_point = None):
    (height, width) = img.shape[:2]
    if rot_point is None:
        rot_point = (width//2, height//2) # If no rotation point is given, use the center of the image as the rotation point

    dimensions = (width, height) # Get the dimensions of the image in the form (width, height) tuple
    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0) # Create a rotation matrix with the given angle and rotation point
    return cv.warpAffine(img, rot_mat, dimensions) # Apply the rotation matrix to the image

rotated_img = rotate(img, 45) # Rotate the image by 45 degrees counter-clockwise
#For clockwise rotation, use a negative angle like -45 degrees
cv.imshow('Rotated Image', rotated_img)
rotated_rotated_img = rotate(rotated_img, 45) # Rotate the image by 45 degrees clockwise
cv.imshow('Rotated Rotated Image', rotated_rotated_img) # By rotating the image twice, the image will include the black triangles that are created by the first use of rotated!


#Resizing
def resize_image(img, w, h):
    return cv.resize(img, (w, h), interpolation=cv.INTER_CUBIC) # Resize the image to the given width and height

resized_img = resize_image(img, 500, 500) # Resize the image to 500x500 pixels
cv.imshow('Resized Image', resized_img)


#Flipping
def flip_image(img, flip_code):
    return cv.flip(img, flip_code) # Flip the image horizontally or vertically based on the flip code = 0(vertical), 1(horizontal), -1(both)
flipped_img = flip_image(img, 1) # Flip the image horizontally
cv.imshow('Flipped Image', flipped_img)


#Cropping
def crop_image(img, start_row, end_row, start_col, end_col):
    return img[start_row:end_row, start_col:end_col] # Crop the image from the given start and end rows and columns

cropped_img = crop_image(img, 50, 200, 200, 400) # Crop the image from row 50 to 200 and column 200 to 400
cv.imshow('Cropped Image', cropped_img)

cv.waitKey(0)
