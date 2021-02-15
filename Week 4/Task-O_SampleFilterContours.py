# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task O - > Sample Filter Contours. 

# Over the weeks, we have explored ways to understand Contours visually and using
# OpenCV functions.  Now lets put these to work and really get down to the 
# challenge of finding FRC vision targets.  Basic idea is to loop through
# sorted contours keeping desired contous only.

# Significant contributions from Task D5 and H ...

# Imports!
# Python - import modules of code as required (OpenCV here)
import numpy as np
import cv2
import sys
from Task_O_SFC_drawAllAsIs import drawAllAsIs
from Task_O_SFC_displayUserInstructions import displayUserInstructions

# Constants!
# colors for screen information
colBgrBlue = (255, 0, 0)
colBgrGreen = (0 , 255, 0)
colBgrRed = (0, 0, 255)
colRgbYellow = (0, 255, 255)
colRgbPurple = (255, 102, 153)

colBgrWhite = (255, 255, 255)
colBgrBlack = (0, 0, 0)
colBgrGrey = (160, 160, 160)
colBgrOrange = (0, 128, 255)
colBgrTeal = (128, 128, 0)

# colors for HSV filtering
colHsvLowerGreen = (55, 220, 220)
colHsvUpperGreen = (65, 255, 255)

# define a string variable for the path to the file
strPathName = 'Week 4/'

# fonts for displaying text
font = cv2.FONT_HERSHEY_SIMPLEX

# define and fill an array with the names of images 
arrImageFiles = []
arrImageFiles.append('Task-O_small.png')
arrImageFiles.append('Task-O_medium.png')
arrImageFiles.append('Task-O_large.png')

# setup exit flag for loop ahead of instructions
flgExit = False

# instruct user on what to do
k = displayUserInstructions()

# show user instruction and check if they want to quit
if k == 27: 
    cv2.destroyAllWindows
    flgExit = True

# setup loop
intCounter = 0
while not(flgExit):

    # load a color image using the string and array
    bgrOriginal = cv2.imread(strPathName + arrImageFiles[intCounter])

    # mask the image to only show yellow or green images
    hsvOriginal = cv2.cvtColor(bgrOriginal, cv2.COLOR_BGR2HSV)
    
    # define a range of from upper to lower in HSV
    arrLowerColor = np.array([colHsvLowerGreen], dtype='int32')
    arrUpperColor = np.array([colHsvUpperGreen], dtype='int32') 
    
    # threshold the HSV image to get only green color
    mskBinary = cv2.inRange(hsvOriginal, arrLowerColor, arrUpperColor)

    # generate the array of Contours
    contours, hierarchy = cv2.findContours(mskBinary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print('Found', len(contours), 'contours in this photo!')

    # show the output of filtering by colour only, display all contours, identify first one, wait for user
    k = drawAllAsIs(bgrOriginal, mskBinary, contours)

    # process keypress from use on function
    if k == 113 or k == 27:
        flgExit = True
        break
    if k == 105:
        intCounter = intCounter - 1
        if intCounter < 0: 
            intCounter = len(arrImageFiles) - 1
    if k == 109:
        intCounter = intCounter + 1
        if intCounter > len(arrImageFiles) - 1:
            intCounter = 0

    # do next function here

# cleanup and exit
cv2.destroyAllWindows()


