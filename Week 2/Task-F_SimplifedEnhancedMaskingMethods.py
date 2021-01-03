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
#https://techtutorialsx.com/2018/06/02/python-opencv-converting-an-image-to-gray-scale/
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html
#https://evergreenllc2020.medium.com/fundamentals-of-image-thresholding-and-masking-6a89997ccca6

import numpy as np
import cv2

strImageFilename = r"C:\Users\Jamie Diep\Documents\frc2021\My images\1ftH1ftD0Angle0Brightness.jpg"

img = cv2.imread(strImageFilename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('Original',img)
cv2.imshow('GrayScale',gray)
cv2.imshow('Binary Image',thresh1)
cv2.imshow('Binary Inverse',thresh2)
cv2.imshow('Trunc',thresh3)
cv2.imshow('Tozero',thresh4)
cv2.imshow('Tozero inverse',thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows()

