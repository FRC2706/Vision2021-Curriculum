# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task F - > Simplified and/or Enhanced Masking.  The basic range based mask you
# used in step D is a pure "range" based filter.  There are different methods out there, 
# mostly based on what is called "Chroma-Key" or perhaps more widely called
# "Green-Screening" for television and movies.

# Consider this explanation of green screen:
# - https://en.wikipedia.org/wiki/Chroma_key

# Then look at (and try out on your computer) these teams vision and masking code:
# - https://github.com/frc1418/2016-vision/blob/master/imgproc/findGreen.py
# - https://github.com/Knoxville-FRC-alliance/Vision-2018-Python/blob/master/visionPi.py
# - https://github.com/Knoxville-FRC-alliance/Vision-2018-Python/blob/master/vision.py
# - https://github.com/team3997/ChickenVision/blob/master/ChickenVision.py

# The idea is to experiment with a few lines of their code and use it with your own python files.  
# Objective is to pick a method to use for making our mask.

# Post a few favourie links and code snippets into a python copy of this file, then push to github.
# Imports!
# Python - import modules of code as required (OpenCV here)
import numpy as np
import cv2

# define a string variable for the path to the file
a = r"C:\Users\lenie\Documents\frc2021\MyImages\RedLoading-030in-Down.jpg"

# Load the image
img = cv2.imread(a)
cv2.imshow('orig', img)


# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img_gray', img_gray)
# Threshold the image to produce a binary image
ret, thresh = cv2.threshold(img_gray,60,255,0)
# Find the contours
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Draw the contours 
cv2.drawContours(img, contours, -1, (255,0,0), 2)
# Display the image
cv2.imshow('a1',img)


# wait for user input to close
cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()


