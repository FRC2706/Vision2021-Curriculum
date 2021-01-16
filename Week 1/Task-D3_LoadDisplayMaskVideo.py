# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task D3 - > Load Display Mask Display Video

# Using Python and OpenCV, write a small bit of code to load an image from a webcam and display it on your screen.  
# Then mask it to green or yellow and display that. 
#  Keep looping to make a video. 
#  Find some green or yellow object in your house to practice on.

# Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html

# To help we have comments to prompt how to do this is below

# Imports!
# Python - import modules of code as required (OpenCV here)
import numpy as np
import cv2

#define color constants using BGR
colBgrBlue = (255, 0, 0)
colBgrGreen = (0, 255, 0)
colBgrRed = (0, 0, 255)

# define the camera
# Create a video capture object
cap = cv2.VideoCapture(0)

#NOTE: use some retroTapeGreen to test
# setup loop
while(True):

    # Capture frame-by-frame --> frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # mask the image to only show yellow or green images
 
    # covert BGR to HSV
    imgImageInHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define a range of green in HSV
    lower_green = np.array([55,220,220])
    upper_green = np.array([65,255,255])
    # threshold the HSV image to get only green color
    imgImageBinaryMask = cv2.inRange(imgImageInHSV, lower_green, upper_green)
    # perform bit-wise and operation to get the green color as white and other colors as black
    mskColor = cv2.bitwise_and(frame, frame, mask=imgImageBinaryMask)

    # Display the resulting frame
    cv2.imshow('original',frame)
    cv2.imshow('color mask',imgImageBinaryMask)
    cv2.imshow('binary mask',mskColor)
    #cv2.imshow('frame', imgImageInHSV)
    
    # check for user input to exit loop and if not return to top of loop
    # Get out of the loop condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()