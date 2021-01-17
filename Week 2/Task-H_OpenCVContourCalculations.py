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

import numpy as np
import cv2
strImageFilename = r"C:\Users\Jamie Diep\Documents\frc2021\My images\1ftH1ftD0Angle0Brightness.jpg"
im = cv2.imread(strImageFilename)
cv2.putText(im,'1ftH 1ftD 0Angle 0Brightness',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im, contours, -1, (255,0,0), 2)
cv2.imshow('Contour on image',im)
cv2.drawContours(imgray, contours, -1, (255,0,0), 2)
cv2.imshow('Countour on grayscale',imgray)
cnt = contours[0]
M = cv2.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
area = cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt,True)
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
print( 'Moments:',M )
print('Centroid: ',cx, cy)
print('Area', area)
print('Perimeter', perimeter)
print('Approximate: ', approx)
#create hull array for convex hull points
hull = []
# calculate points for each contour
for i in range(len(contours)):
    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
for i in range(len(contours)):
    color_contours = (0, 255, 0) # green - color for contours
    color = (255, 0, 0) # blue - color for convex hull
    # draw ith contour
    cv2.drawContours(drawing, contours, i, color_contours, 2, 8, hierarchy)
    # draw ith convex hull object
    cv2.drawContours(drawing, hull, i, color, 2, 8)
    cv2.imshow('Convex Hull',drawing)

for i in range(len(contours)):
    (x,y),radius = cv2.minEnclosingCircle(contours[i])
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(im,center,radius,(0,255,0),2)
    cv2.imshow('Contour Features', im)

ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(im,ellipse,(242,223,151),2)
cv2.imshow('Contour Features', im)

for i in range(len(contours)):
    rows,cols = im.shape[:2]
    [vx,vy,x,y] = cv2.fitLine(contours[i], cv2.DIST_L2,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    cv2.line(im,(cols-1,righty),(0,lefty),(133,31,84),2)
    cv2.imshow('Contour Features', im)

cv2.waitKey(0)
cv2.destroyAllWindows()