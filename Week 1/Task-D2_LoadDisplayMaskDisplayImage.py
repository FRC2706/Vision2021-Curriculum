# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task D2 - > Load Display Mask Display Image

# Using Python and OpenCV, write a small bit of code to load an image and display it on your screen.  Then mask it to green or yellow and display that.

# Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html

# To help we have comments to prompt how to do this is below

# Imports!
# Python - import modules of code as required (OpenCV here)
import numpy as np
import cv2

# define a string variable for the path to the file
strPathName = 'Week 1/'
strImageFilename = '2016-stonghold-high-tower-goal.png'

# load a color image using string
bgrOriginal = cv2.imread(strPathName + strImageFilename)

# display the color image to screen
cv2.imshow('This is the original image', bgrOriginal)

# mask the image to only show yellow or green images
# Convert RGB(BGR) to HSV
hsvOriginal = cv2.cvtColor(bgrOriginal, cv2.COLOR_BGR2HSV)
# define a range of green in HSV
colLowerGreen = np.array([55,220,220])
colUpperGreen = np.array([65,255,255]) 
# threshold the HSV image to get only green color
mskBinary = cv2.inRange(hsvOriginal, colLowerGreen, colUpperGreen)
# create a full color mask


# display the masked images to screen
cv2.imshow('This is the Binary mask', mskBinary)

# wait for user input to close
cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()
