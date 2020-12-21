# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task D1 - > Load and Display Images

# Using Python and OpenCV, write a small bit of code to load an image and display it on your screen.

# Recommeded starting points 
#    -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html

# To help we have comments to prompt how to do this is below

import numpy as np
import cv2

str_path_name = 'Week 1/'
img_1_name = 'Vision_Basketball_Targets.png'

img_1_input = cv2.imread(str_path_name + img_1_name)
print('img_1_imput')

cv2.imshow('image window name',img_1_input)

cv2.waitKey(0)

cv2.destroyAllWindows()

print('hello')