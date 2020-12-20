# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task D1 - > Load and Display Images

# Using Python and OpenCV, write a small bit of code to load an image and display it on your screen.

# Recommeded starting points 
#    -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html

# To help we have comments to prompt how to do this is below

# Imports!
# Python - import modules of code as required (OpenCV here)
import numpy as numpy
import cv2

# define a string variable for the path to the file
a = r"C:\Users\lenie\Documents\frc2021\MyImages\RedLoading-030in-Down.jpg"
print(a)

# load a color image using string
#img = cv2.imread(a,cv2.IMREAD_COLOR)
imgColor = cv2.imread(a,cv2.IMREAD_COLOR)
imgGrayscale = cv2.imread(a,cv2.IMREAD_GRAYSCALE)


# display the color image to screen
cv2.imshow('Color Image',imgColor)
cv2.imshow('Grayscale Image',imgGrayscale)

# wait for user input to close
cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()

