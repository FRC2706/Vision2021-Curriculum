# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task P - > Math with Solve PNP function

# On the GIGMM trail we have used some simple math in the past, now let's look 
# at some complex math, or a specific function from OpenCV called SolvePNP

# to get there, lots of learning... but with sample code, here are some links

# https://docs.opencv.org/4.5.0/d9/db7/tutorial_py_table_of_contents_calib3d.html
# https://github.com/ligerbots/VisionServer/blob/master/utils/camera_calibration.py
# https://markhedleyjones.com/storage/checkerboards/Checkerboard-A4-25mm-10x7.pdf
# https://github.com/ligerbots/VisionServer/blob/master/data/calibration/chessboard_9x6.png

# start with Task G code, add some D5 and a little of G and H

# Imports!
# Python - import modules of code as required (OpenCV here)
import numpy as np
import cv2
from masking import maskByColor

# Constants!
# colors for screen information
colBgrBlue = (255, 0, 0)
colBgrGreen = (0 , 255, 0)
colBgrRed = (0, 0, 255)
colBgrYellow = (0, 255, 255)
colBgrPurple = (255, 102, 153)

colBgrWhite = (255, 255, 255)
colBgrBlack = (0, 0, 0)
colBgrGrey = (160, 160, 160)
colBgrOrange = (0, 128, 255)
colBgrTeal = (128, 128, 0)

colBgrApple = (0, 191, 17)
colBgrPacific = (193, 161,0)
colBgrAtlantis = (0, 217, 105)
colBgrCerise = (120, 0, 216)
colBgrJewel = (64, 109, 0)
colBgrFruit = (64, 155, 64)

# flags and multipliers for decision making
booChooser = True  # True is green and targets at distance, False is orange and cones for now
tupNewImageSize = (640, 480)

# colors for HSV filtering
if booChooser:
    colHsvLowerRange = (50, 100, 100) # green
    colHsvUpperRange = (90, 255, 255) # green
else:
    colHsvLowerRange = (10, 100, 100) # green try 50, 100, 100
    colHsvUpperRange = (15, 255, 255) # green try 90, 255, 255

# fonts for displaying text
font = cv2.FONT_HERSHEY_SIMPLEX

# define a string variable for the path to the file
if booChooser:
    strPathName = '2021-targetAtDistances/'
else:
    strPathName = '2021-conesAsMarkers/'

# define an array with the names of images 
arrImageFiles = []

# fill an array with the names of images 
if booChooser:
    arrImageFiles.append('2021-01-09-093303-01.png')
    arrImageFiles.append('2021-01-09-094009-10.png')
    arrImageFiles.append('2021-01-09-094029-11.png')
else:
    arrImageFiles.append('cone-01.png')
    arrImageFiles.append('cone-02.png')

# setup loop
flgExit = False
intCounter = 0
while not(flgExit):

    # print file to 
    print(arrImageFiles[intCounter])

    # load a color image using the string and array
    bgrOriginal = cv2.imread(strPathName + arrImageFiles[intCounter])

    # mask the image to only show yellow or green images
    hsvOriginal = cv2.cvtColor(bgrOriginal, cv2.COLOR_BGR2HSV)
    
    # define a range of from upper to lower in HSV
    arrLowerColor = np.array([colHsvLowerRange])
    arrUpperColor = np.array([colHsvUpperRange])

    # threshold the HSV image to get only green color
    mskBinary = maskByColor(hsvOriginal, arrLowerColor, arrUpperColor, 'kn')

    # display the binary masks image to screen
    #cv2.imshow('This is the Binary mask - Knoxville', mskBinary)

    # create a full color mask
    # Bitwise-AND binary mask and original image
    mskColor = cv2.bitwise_and(bgrOriginal, bgrOriginal, mask=mskBinary)
    mskExcluded = cv2.bitwise_and(bgrOriginal, bgrOriginal, mask=cv2.bitwise_not(mskBinary))

    # generate the array of Contours
    contours, hierarchy = cv2.findContours(mskBinary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # sort the array of Contours by area
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    print('Found', len(contours), 'contours in this photo!')

    # if there are no contours found
    if contours:
        indiv = contours[0]

        # draw the indiv contour on the color mask
        cv2.drawContours(mskColor, [indiv], 0, colBgrPurple, 3)

        # from this tutorial, do all the functions
        # https://docs.opencv.org/4.5.0/dd/d49/tutorial_py_contour_features.html

        # 1 Moments
        M = cv2.moments(indiv)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        # 2 Area
        area = cv2.contourArea(indiv)

        # 3 Permiter
        perimeter = cv2.arcLength(indiv,True)

        # 4 Approx
        epsilon = 0.1*cv2.arcLength(indiv,True)
        approx = cv2.approxPolyDP(indiv,epsilon,True)

        # 5 Convex Hull
        hull = cv2.convexHull(indiv)

        # 8 Minimum Enclosing Circle
        (mecx, mecy), radius = cv2.minEnclosingCircle(indiv)

        # 9 Extreme Points  
        leftmost = tuple(indiv[indiv[:,:,0].argmin()][0])
        rightmost = tuple(indiv[indiv[:,:,0].argmax()][0])
        topmost = tuple(indiv[indiv[:,:,1].argmin()][0])
        bottommost = tuple(indiv[indiv[:,:,1].argmax()][0])
       
        # draw circle at centroid of target on colour mask, and known distance to target as text
        cv2.circle(mskColor, (cx,cy), 4, colBgrPurple, -1)

        # draw the min eclosing circle
        center = (int(mecx),int(mecy))
        radius = int(radius)
        cv2.circle(mskColor,center,radius,colBgrCerise,2)

        # draw the extreme points
        cv2.circle(mskColor, leftmost, 4, colBgrGreen, -1)
        cv2.circle(mskColor, rightmost, 4, colBgrRed, -1)
        cv2.circle(mskColor, topmost, 4, colBgrWhite, -1)
        cv2.circle(mskColor, bottommost, 4, colBgrBlue, -1)
 
    # display the colour mask image to screen
    cv2.imshow('This is Task G', cv2.resize(mskColor, tupNewImageSize))
    cv2.imshow('This is Task G Excluded', cv2.resize(mskExcluded, tupNewImageSize))

    # wait for user input to move or close
    while(True):
        ke = cv2.waitKeyEx(0)
        if ke == 113 or ke == 27:
            flgExit = True
            break
        if ke == 105 or ke == 2490368:
            intCounter = intCounter - 1
            if intCounter < 0: 
                intCounter = len(arrImageFiles) - 1
            break
        if ke == 109 or ke == 2621440:
            intCounter = intCounter + 1
            if intCounter > len(arrImageFiles) - 1:
                intCounter = 0
            break

# cleanup and exit
cv2.destroyAllWindows()



