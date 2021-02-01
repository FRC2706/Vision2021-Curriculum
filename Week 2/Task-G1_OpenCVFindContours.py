# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task G - > Find Contours.  This is a seemingly simple command. But is where the real math begins.  
# The command basically converts the masked image into arrays of coordinates that we do math on.  Make sure
# you can do this in your code.  You need to end up with a set of contours!  If you print them to the console
# you will see pages and pages of coordinates go by.  Do that at least once.

# useful links
# https://docs.opencv.org/4.5.0/d4/d73/tutorial_py_contours_begin.html


import numpy as np
import cv2

colRgbYellow = (0, 255, 255)
colRgbPurple = (255, 102, 153)
colRgbGreen = (0,255,0)

colBgrPurple = (153, 102, 255)

colHsvLowerGreen = (55, 220, 220)
colHsvUpperGreen = (65, 255, 255)
colHsvPurple = (100, 240, 255)

cap = cv2.VideoCapture(0)

#ret, thresh = cv2.threshold(imHSV, 127, 255, 0)
#contours, hierarchy = cv2.findContours(imHSV, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv.drawContours(thresh, contours, -1, (0,255,0), 3)

while(True):

    # Capture frame-by-frame --> frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, threshBinary = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("Original color", frame)
    #cv2.imshow("Original gray", imgray)
    #cv2.imshow("Thresh binary", threshBinary)

    # Find contours
    contours, hierarchy = cv2.findContours(threshBinary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame, contours, -1, colRgbGreen, 1)
    #cv2.imshow('rgb contours', frame)

    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  #  cv2.drawContours(hsvFrame, contours, -1, (60,240,240), 3)
    #cv2.imshow("hsv Contours", hsvFrame)

    # define a range of from upper to lower in HSV
    arrLowerColor = np.array([colHsvLowerGreen])
    arrUpperColor = np.array([colHsvUpperGreen]) 

    # threshold the HSV image to get only green color
    mskBinary = cv2.inRange(hsvFrame, arrLowerColor, arrUpperColor)

    # Bitwise-AND binary mask and original image
    mskColor = cv2.bitwise_and(frame, hsvFrame, mask=mskBinary)
    #cv2.imshow("Filtered Contours", mskColor)

    # Find the contour of the max area
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    indiv_1 = contours[3]
    indiv_2 = contours[2]

    #bounding rect
    x,y,w,h = cv2.boundingRect(indiv_1)
    cv2.rectangle(mskColor,(x,y),(x+w,y+h),(0,0,255),3)
    

    # filing an ellipse
    ellipse = cv2.fitEllipse(indiv_2)
    cv2.ellipse(mskColor,ellipse,(255,0,0),3)

    cv2.imshow("contours + rectangle + ellipse", mskColor)


















    #contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 
    # covert BGR to HSV
    imgImageInHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define a range of green in HSV
    lower_green = np.array([55,220,220])
    upper_green = np.array([65,255,255])
    # threshold the HSV image to get only green color
    imgImageBinaryMask = cv2.inRange(imgImageInHSV, lower_green, upper_green)
    # perform bit-wise and operation to get the green color as white and other colors as black
    mskColor = cv2.bitwise_and(frame, frame, mask=imgImageBinaryMask)

    # Display the resulting frame
    #cv2.imshow('original',frame)
    #cv2.imshow('color mask',imgImageBinaryMask)
    #cv2.imshow('binary mask',mskColor)
    #cv2.imshow('frame', imgImageInHSV)
    
    # check for user input to exit loop and if not return to top of loop
    # Get out of the loop condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()