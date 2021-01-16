

import numpy as np
import cv2

# define a string variable for the path to the file
strPathName = "Week 0/"
#strImageFileName = './pictures/RetroTape.jpg'
strImageFileName = 'img04.jpg'
#strImageFileName = '2016-stonghold-high-tower-goal.png'

# load a color image using string
imgImageInput = cv2.imread(strPathName + strImageFileName)

# display the color image to screen
cv2.imshow('This is the original image',imgImageInput)

#
imHSV = cv2.cvtColor(imgImageInput, cv2.COLOR_BGR2HSV)


ret, thresh = cv2.threshold(imHSV, 127, 255, 0)
contours, hierarchy = cv2.findContours(imHSV, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv.drawContours(thresh, contours, -1, (0,255,0), 3)

#cnt = contours[4]
#cv2.drawContours(thresh, [cnt], 0, (0,255,0), 3)