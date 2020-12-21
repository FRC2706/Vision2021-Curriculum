# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task D2 - > Load Display Mask Display Image

# Using Python and OpenCV, write a small bit of code to load an image and display it on your screen.  Then mask it to green or yellow and display that.

# Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html

# To help we have comments to prompt how to do this is below

# Imports!
# Python - import modules of code as required (OpenCV here)

# define a string variable for the path to the file

# load a color image using string

# display the color image to screen

# mask the image to only show yellow or green images

# display the masked images to screen

# wait for user input to close

# cleanup and exit

import numpy as np
import cv2

str_path_name = 'Week 1/'
img_1_name = 'Vision_Basketball_Targets.png'

img_1_input = cv2.imread(str_path_name + img_1_name)

cv2.imshow('origonal image',img_1_input)

img_1_in_hsv = cv2.cvtColor(img_1_input,cv2.COLOR_BGR2HSV)

low_green = np.array([20,100,100])
high_green = np.array([120,255,255])

img_1_binary_mask = cv2.inRange(img_1_in_hsv, low_green, high_green)


cv2.imshow('masked image',img_1_binary_mask)

cv2.waitKey(0)

cv2.destroyAllWindows()
