# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task N - > Sample Filter Contours. 

# Over the weeks, we have explored ways to understand Contours visual and using
# OpenCV functions.  Now lets put these to work and really get down to the 
# challenge of finding FRC vision targets.  Basic idea is to loop through
# sorted contours keeping desired contours only

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
strImageFileName = '02456_raw.png'

# load a color image using the string and array
bgrOriginal = cv2.imread(strPathName + strImageFileName)
cv2.imshow('This is the original mask', bgrOriginal)

# convert from BGR to HSV color
hsvOriginal = cv2.cvtColor(bgrOriginal, cv2.COLOR_BGR2HSV)
    
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

# generate the array of Contours
contours, hierarchy = cv2.findContours(mskBinary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# sort the array of Contours by area
contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
print('Found', len(contours), 'contours in this photo!')
indiv = contours[0]
#print (indiv)

# display the colour mask image to screen
cv2.imshow('This is the Colour mask', mskColor)

selected_contours = []
# loop through the sorted contours
for i in range(0, len(contours)):
    indiv_contour = contours[i]
 
    # area > areaTreshod = 10
    # other features?
    indiv_area = cv2.contourArea(indiv_contour)
    print(indiv_area)
    if indiv_area > 20:
        selected_contours.append(indiv_contour)
        
    #todo: put the criteria for the desired contour here
    # moment
    # cv2.moments(indiv_contour)
    # extreme values
    #    leftmost = tuple(indiv_contour[indiv_contour[:,:,0].argmin()][0])
    #    rightmost = tuple(indiv_contour[indiv_contour[:,:,0].argmax()][0])
    #    topmost = tuple(indiv_contour[indiv_contour[:,:,1].argmin()][0])
    #    bottommost = tuple(indiv_contour[indiv_contour[:,:,1].argmax()][0])

print('number of desired contours', len(selected_contours))
# wait for user input to move or close
while(True):
    ke = cv2.waitKeyEx(0)
    if ke == 113 or ke == 27:
        flgExit = True
        break
 
# cleanup and exit
cv2.destroyAllWindows()