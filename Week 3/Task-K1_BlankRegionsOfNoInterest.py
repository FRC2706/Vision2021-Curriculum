# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task K - > Blank regions of no interest.  We have discussed the notion
# that there are areas of the image that will never contain information that we want
# our code to process.  Using online search engines find a way using OpenCV to
# modify a photo to contain black pixels in areas with no interest to our code

# Previous tasks can be copied here and modified, this should be a quick effort

# helpful links:
#http://www.learningaboutelectronics.com/Articles/Region-of-interest-in-an-image-Python-OpenCV.php

# Imports!
# Python - import modules of code as required (OpenCV here)
import numpy as np
import cv2


# Constants!
# colors for screen information
colBgrBlue = (255, 0, 0)
colBgrGreen = (0 , 255, 0)
colBgrRed = (0, 0, 255)
colRgbYellow = (0, 255, 255)
colRgbPurple = (255, 102, 153)

# colors for HSV filtering: green
colHsvLowerGreen = (55, 220, 220)
colHsvUpperGreen = (65, 255, 255)

# colors for HSV filtering: yellow
colHsvLowerYellow = (20, 200, 200)
colHsvUpperYellow = (40, 255, 255)

# define a string variable for the path to the file
strPathName = '2018-MergeAtWorlds/'
strImageFileName = '04615_raw.png'

# load a color image using the string and array
bgrOriginal = cv2.imread(strPathName + strImageFileName)
cv2.imshow('This is the original mask', bgrOriginal)

# blank out the top half of the image
# NOTE: the blank of the region is determined by the location of the camera
height, width= bgrOriginal.shape[:2]
print('heigh, width ', height, width)

ROI= np.array([[[0,height/2],[width,height/2],[width,height],[0,height]]], dtype= np.int32)
blank= np.zeros([height,width],dtype=np.uint8)
print("ROI shape", ROI.shape)

cv2.fillPoly(blank, ROI, 255)
#cv2.imshow('ROI ', blank)

region_of_interest_image= cv2.bitwise_and(bgrOriginal, bgrOriginal, mask=blank)
cv2.imshow('This is the interested image', region_of_interest_image)

# for test only
#a3 = np.array( [[[10,10],[100,10],[100,100],[10,100]]], dtype=np.int32 )
#im = np.zeros([240,320],dtype=np.uint8)
#cv2.fillPoly( im, a3, 255 )
#cv2.imshow('test',im)

# convert from BGR to HSV color
hsvOriginal = cv2.cvtColor(region_of_interest_image, cv2.COLOR_BGR2HSV)
    
# define a range of from upper to lower in HSV
arrLowerColor = np.array([colHsvLowerYellow], dtype='int32')
arrUpperColor = np.array([colHsvUpperYellow], dtype='int32') 
    
# threshold the HSV image to get only yellow color
mskBinary = cv2.inRange(hsvOriginal, arrLowerColor, arrUpperColor)

# create a full color mask
# Bitwise-AND binary mask and original image
mskColor = cv2.bitwise_and(bgrOriginal, bgrOriginal, mask=mskBinary)

# display the colour mask image to screen
#cv2.imshow('This is the Colour mask', mskColor)

# display the colour mask image to screen
cv2.imshow('This is the Colour mask', mskColor)

# wait for user input to move or close
while(True):
    ke = cv2.waitKeyEx(0)
    if ke == 113 or ke == 27:
        flgExit = True
        break
 
# cleanup and exit
cv2.destroyAllWindows()