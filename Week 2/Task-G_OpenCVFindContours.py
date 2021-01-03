# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task G - > Find Contours.  This is a seemingly simple command. But is where the real math begins.  
# The command basically converts the masked image into arrays of coordinates that we do math on.  Make sure
# you can do this in your code.  You need to end up with a set of contours!  If you print them to the console
# you will see pages and pages of coordinates go by.  Do that at least once.

# useful links
# https://docs.opencv.org/4.5.0/d4/d73/tutorial_py_contours_begin.html

import numpy as np
import cv2
strImageFilename = r"C:\Users\Jamie Diep\Documents\frc2021\My images\1ftH1ftD0Angle0Brightness.jpg"
im = cv2.imread(strImageFilename)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im, contours, -1, (255,0,0), 2)
cv2.imshow('Contour on image',im)
cv2.drawContours(imgray, contours, -1, (255,0,0), 2)
cv2.imshow('Countour on grayscale',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()