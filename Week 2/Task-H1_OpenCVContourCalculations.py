

# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task H - > OpenCV "Contour Calculations."  Not sure if it is clear by now, 
# but OpenCV can do a lot of things, we need to understand what it offers to complete 
# our vision code.  For a given single contour, (meaning it was imaged and masked and 
# converted to a coordinate array), you need to be able to use a number of OpenCV functions.
# Please experiment with the following, easiest is to simply draw them back to a blank image
# or on top of original.

# --> moments, contour area, contour perimeter, contour approximation, bounding rectangles, 
# minimum enclosing circle, fitting elipse, fitting line, etc.

# useful links
# https://docs.opencv.org/4.5.0/dd/d49/tutorial_py_contour_features.html
# https://docs.opencv.org/4.5.0/d1/d32/tutorial_py_contour_properties.html

# Imports!
# Python - import modules of code as required (OpenCV here)
import numpy as np
import cv2
import time

# Constants!
# colors for screen information
colBgrBlue = (255, 0, 0)
colBgrGreen = (0 , 255, 0)
colBgrRed = (0, 0, 255)
colBgrPurple = (153,102,255)

colRgbYellow = (0, 255, 255)
colRgbPurple = (255, 102, 153)
colRgbGreen = (0,255,0)
colRgbRed = (255,0,0)

# colors for HSV filtering: green
colHsvLowerGreen = (55, 220, 220)
colHsvUpperGreen = (65, 255, 255)

# colors for HSV filtering: yellow
colHsvLowerYellow = (20, 200, 200)
colHsvUpperYellow = (40, 255, 255)

# colors for HSV filtering: purple
colHsvLowerPurple = (255, 98, 150)
colHsvUpperPurple = (255, 105, 155)

# define the camera
cap = cv2.VideoCapture(0)

# setup loop
while(True):

    # load a color image from camera
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == False:
        print("getting frame failed")

    #print(len(frame[0])) #640
    #print(len(frame)) #480

    # Our operations on the frame come here
    # change color image to gray image, to be processed with threshold
    imGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # display the color image to screen
    cv2.imshow('This is the original gray image', imGray)

    # find the contours
    ret, thresh_binary = cv2.threshold(imGray, 127,255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # draw all contours
    cv2.drawContours(frame, contours, -1, colBgrGreen, 1)
    cv2.imshow('all contours with THRESH_BINARY',frame)

    # only leave the green contours
    frameHsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #cv2.imshow('frameHsv',frameHsv)
    # define a range of green in HSV
    colLowerGreen = np.array(colHsvLowerGreen)
    colUpperGreen = np.array(colHsvUpperGreen) 
    # threshold the HSV image to get only green color
    mskBinary = cv2.inRange(frameHsv, colLowerGreen, colUpperGreen)
    #cv2.imshow('binary', mskBinary)
    # create a full color mask
    # Bitwise-AND binary mask and original image
    mskColor = cv2.bitwise_and(frame, frame, mask=mskBinary)
    cv2.imshow('the contours only', mskColor)

    # test with threshold types
    # note cv2.THRESH_BINARY = 0
    ret, thresh = cv2.threshold(imGray, 127, 255, 0)
    #cv2.imshow('1. THRESH_BINARY', thresh)

    ret, thresh_binary_inv = cv2.threshold(imGray, 127,255, cv2.THRESH_BINARY_INV)
    #cv2.imshow('2. THRESH_BINARY_INV',thresh_binary_inv)
    ret, thresh_toZero = cv2.threshold(imGray, 127,255, cv2.THRESH_TOZERO)
    #cv2.imshow('3. THRESH_TOZERO',thresh_toZero)
    ret, thresh_toZero_inv = cv2.threshold(imGray, 127,255, cv2.THRESH_TOZERO_INV)
    #cv2.imshow('4. This is THRESH_TOZERO_INV',thresh_toZero_inv)

    # sort the array of Contours by area
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    #print('Found', len(contours), 'contours in this photo!')
    #print (indiv)
    indiv = contours[0]
    indiv1 = contours[1]
    indiv2 = contours[2]
    indiv3 = contours[3]
    indiv4 = contours[4]
    
    # draw the centroid

    # bounding rectangle
    x,y,w,h = cv2.boundingRect(indiv1)
    cv2.rectangle(mskColor,(x,y),(x+w,y+h),colBgrRed,3)
    
    # minimum enclosing circle
    (x,y),radius = cv2.minEnclosingCircle(indiv2)
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(mskColor,center,radius,colBgrPurple,3)
    
    # fitting ellipse
    ellipse = cv2.fitEllipse(indiv3)
    cv2.ellipse(mskColor,ellipse,colBgrBlue,3)

    #get the hull of the contour
    hull = cv2.convexHull(indiv4)
    cv2.drawContours(mskColor, [hull], 0,colBgrRed,3)

    cv2.imshow('contour features', mskColor)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# cleanup and exit
cv2.destroyAllWindows()