import cv2 as cv

############################################## IMAGE #######################################################################################

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)




############################################## VIDEO #######################################################################################
capture = cv.VideoCapture('Videos/dog.mp4') # This will open the video file

while True:
    isTrue, frame = capture.read() # isTrue is a boolean that tells if the frame was read correctly and frame is the actual frame
    cv.imshow('Video', frame) # Show the frame in a window
    if cv.waitKey(20) & 0xFF == ord('d'): 
        break

capture.release() # Release the video capture object
cv.destroyAllWindows() # Close all OpenCV windows

