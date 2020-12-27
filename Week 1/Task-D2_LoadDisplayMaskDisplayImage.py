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
a = r"C:\Users\lenie\Documents\frc2021\MyImages\RedLoading-030in-Down.jpg"

# load a color image using string
imgColor = cv2.imread(a,cv2.IMREAD_COLOR)

# display the color image to screen
cv2.imshow('Color Image',imgColor)

## convert to hsv
hsv = cv2.cvtColor(imgColor, cv2.COLOR_BGR2HSV)

# mask the image to only show yellow or green images
#mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))
mask = cv2.inRange(hsv, (60, 100, 100), (70, 255, 255))

# display the masked images to screen
cv2.imshow('Masked Image',mask)

# wait for user input to close
cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()
