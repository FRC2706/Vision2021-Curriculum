# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task D3 - > Load Display Mask Display Video

# Using Python and OpenCV, write a small bit of code to load an image from a webcam and display it on your screen.  Then mask it to green or yellow and display that.  Keep looping to make a video.  Find some green or yellow object in your house to practice on.

# Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html

# To help we have comments to prompt how to do this is below

# Imports!
# Python - import modules of code as required (OpenCV here)
import numpy as np
import cv2
# define the camera
cap = cv2.VideoCapture(0)

# setup loop
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    
    #Show Binary Thresh image with contour
    ret,thresh1 = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(thresh1, contours, -1, (255,0,255), 2)
    cv2.imshow('Binary',thresh1)

    #Show Gray image
    cv2.imshow('Gray Image', gray)
    
    #Show Canny
    edge = cv2.Canny(gray,35,100)
    cv2.imshow('Canny edge', edge)
    
    #Show Binary Inverse Thresh image
    ret,thresh2 = cv2.threshold(frame,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('Binary inversion',thresh2)

    #Show Trunc Thresh image
    ret,thresh3 = cv2.threshold(frame,127,255,cv2.THRESH_TRUNC)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(thresh3, contours, -1, (235,193,148), 2)
    cv2.imshow('Trunc',thresh3)

    #Show ToZero Thresh image
    ret,thresh4 = cv2.threshold(frame,127,255,cv2.THRESH_TOZERO)
    cv2.imshow('ToZero',thresh4)

    #Show ToZero inversion image
    ret,thresh5 = cv2.threshold(frame,127,255,cv2.THRESH_TOZERO_INV)
    cv2.imshow('ToZero inversion',thresh5)

    #Show Original Image with Contour
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (72,34,159), 2)
    cv2.imshow('Original',frame)

    #Exit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# load a color image from camera

# display the color image to screen

# mask the image to only show yellow or green images

# display the masked images to screen

# check for user input to exit loop and if not return to top of loop

# cleanup and exit
