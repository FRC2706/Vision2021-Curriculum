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
strImageFilename = r"C:\Users\Jamie Diep\Documents\frc2021\My images\1ftH1ftD0Angle0Brightness.jpg"
# load a color image using string
img = cv2.imread(strImageFilename)
# display the color image to screen
cv2.imshow('Color Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# mask the image to only show yellow or green images
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))
# display the masked images to screen
cv2.imshow('Masked image',mask)
# wait for user input to close
cv2.waitKey(0)
# cleanup and exit
cv2.destroyAllWindows()
