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
strImgPath = "2016-stonghold-high-tower-goal.png"
# load a color image using string
imgImageInput = cv2.imread(strPathName+strImgPath)
# display the color image to screen
cv2.imshow("Original Image",imgImageInput)
# mask the image to only show yellow or green images

# display the masked images to screen

# wait for user input to close

# cleanup and exit

