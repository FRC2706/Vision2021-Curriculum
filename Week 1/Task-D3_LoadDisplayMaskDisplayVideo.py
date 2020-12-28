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
    cv2.imshow('frame2',frame)
    cv2.imshow('frame3',frame)
    cv2.imshow('frame1',frame)
    cv2.imshow('frame4',frame)
    cv2.imshow('frame5',frame)
    cv2.imshow('frame6',frame)
    cv2.imshow('frame',gray)
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
