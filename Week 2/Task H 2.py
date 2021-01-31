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
# https://docs.opencv.org/4.5.0/d1/d32/tutorial_py_contour_properties.html

# 1 Aspect Ratio
# 2 Extent
# 3 Solidity
# 4 Equivalent Diameter
# 5 Orientation
# 6 Mask and Pixel Points
# 7 Maximum Value, Minimum Value and their locations
# 8 Mean Color or Mean Intensity
# 9 Extreme Points

from os import listdir
from os. path import isfile, join
import numpy as np
import cv2

colBgrBlue = (255, 0, 0)
colBgrGreen = (0 , 255, 0)
colBgrRed = (0, 0, 255)
colRgbYellow = (0, 255, 255)
colRgbPurple = (255, 102, 153)

# colors for HSV filtering
colHsvLowerGreen = (55, 220, 220)
colHsvUpperGreen = (65, 255, 255)

# fonts for displaying text
font = cv2.FONT_HERSHEY_SIMPLEX

#b = r"C:\Users\Jamie Diep\Documents\frc2021\My images"
intCounter = 0
strPathName = 'Vision2021-Curriculum/2017-pegsAtDistance/'
onlyfiles = [ f for f in listdir(strPathName) if isfile(join(strPathName,f))]
arrImageFiles=[]
flgExit = False
for n in range(0,len(onlyfiles)):
    arrImageFiles.append(onlyfiles[n])

while not(flgExit):
    bgrOriginal = cv2.imread(strPathName+arrImageFiles[intCounter])
    gray = cv2.cvtColor(bgrOriginal, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(bgrOriginal, cv2.COLOR_BGR2HSV)
    arrLowerColor = np.array([colHsvLowerGreen])
    arrUpperColor = np.array([colHsvUpperGreen]) 
    
    thresh = cv2.inRange(hsv, arrLowerColor,arrUpperColor)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    print('Found', len(contours), 'contours in this photo!')
    indiv = contours[0]
    print (indiv)
    #cv2.drawContours(bgrOriginal, [indiv], 0, (255,0,0), 2)

    #rect=cv2.minAreaRect(indiv)
    #box = cv2.boxPoints(rect)
    #box = np.int0(box)
    #cv2.drawContours(bgrOriginal,[box],0,(0,0,255),2)
    x, y, w, h =cv2.boundingRect(indiv)
    area = cv2.contourArea(indiv)
    aspect_ratio = float(w)/h
    rect_area = w*h
    extent = float(area)/rect_area
    hull = cv2.convexHull(indiv)
    hull_area = cv2.contourArea(hull)
    solidity = float(area)/hull_area
    area = cv2.contourArea(indiv)
    equi_diameter = np.sqrt(4*area/np.pi)
    (x,y),(MA,ma),angle = cv2.fitEllipse(indiv)
    leftmost = tuple(indiv[indiv[:,:,0].argmin()][0])
    rightmost = tuple(indiv[indiv[:,:,0].argmax()][0])
    topmost = tuple(indiv[indiv[:,:,1].argmin()][0])
    bottommost = tuple(indiv[indiv[:,:,1].argmax()][0])
    mask = np.zeros(gray.shape,np.uint8)
    #print('Matrix: ',mask)
    #print('end')
    cv2.drawContours(mask,[indiv],0,255,-1)
    pixelpoints = np.transpose(np.nonzero(mask))
    #print(pixelpoints)
    #cv2.imshow('mask', mask)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray,mask=mask)
    mean_val = cv2.mean(bgrOriginal,mask = mask)
    cv2.imshow('oi', bgrOriginal)

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
cv2.destroyAllWindows()