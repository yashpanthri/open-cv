import cv2 as cv
def rescaleFrame(frame, scale=0.75):
    pass # This function will rescale the frame to a given scale (default is 0.75)

    


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # Resize the frame to the new dimensions


############################################## PHOTO #######################################################################################


img = cv.imread('Photos/cat.jpg') # Read the image from the file

resized_image = rescaleFrame(img) # Rescale the image to 20% of its original size
cv.imshow('Cat', resized_image)




############################################## VIDEO #######################################################################################
## METHOD 1: Using a function to rescale the frame
capture = cv.VideoCapture('Videos/dog.mp4') # This will open the video file

while True:
    isTrue, frame = capture.read() # isTrue is a boolean that tells if the frame was read correctly and frame is the actual frame

    frame_resized = rescaleFrame(frame, scale=0.2) # Rescale the frame to 20% of its original size

    cv.imshow('Video', frame) # Show the frame in a window
    cv.imshow('Resized Video', frame_resized) # Show the resized frame in a window
    if cv.waitKey(20) & 0xFF == ord('d'): 
        break

capture.release() # Release the video capture object
cv.destroyAllWindows() # Close all OpenCV windows



## METHOD 2: Using change Res function(ONLY VALID FOR **LIVE VIDEO**)

def changeRes(width, height):
    def changeRes(frame):
        capture.set(3, width)  # Set the width of the frame
        capture.set(4, height)
    return changeRes