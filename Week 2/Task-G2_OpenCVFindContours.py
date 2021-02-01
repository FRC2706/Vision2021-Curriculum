# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task G - > Find Contours.  This is a seemingly simple command. But is where the real math begins.  
# The command basically converts the masked image into arrays of coordinates that we do math on.  Make sure
# you can do this in your code.  You need to end up with a set of contours!  If you print them to the console
# you will see pages and pages of coordinates go by.  Do that at least once.

# useful links
# https://docs.opencv.org/4.5.0/d4/d73/tutorial_py_contours_begin.html


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):

    # Capture frame-by-frame --> frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    cv2.imshow("Original gray", imgray)
    cv2.imshow("Thresh binary", thresh)

    ret, binaryThreshInv = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("Thresh binary inverse", binaryThreshInv)

    ret, ThreshTrunc = cv2.threshold(imgray, 127, 255, cv2.THRESH_TRUNC)
    cv2.imshow("Thresh truncate", ThreshTrunc)

    ret, ThreshToZero = cv2.threshold(imgray, 127, 255, cv2.THRESH_TOZERO)
    cv2.imshow("Thresh to zero", ThreshToZero)

    ret, ThreshToZeroInv = cv2.threshold(imgray, 127, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow("Thresh to zero inverse", ThreshToZeroInv)
    
    # check for user input to exit loop and if not return to top of loop
    # Get out of the loop condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()