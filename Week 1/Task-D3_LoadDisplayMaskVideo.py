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

# define the camera
# Create a video capture object
cap = cv2.VideoCapture(0)

# setup loop
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # mask the image to only show yellow or green images
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #colorHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    colorRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB )

    # Display the resulting frame
    cv2.imshow('frame',colorRGB)
    
    # check for user input to exit loop and if not return to top of loop
    # Get out of the loop condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()