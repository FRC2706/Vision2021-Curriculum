import numpy as np
import cv2

path_name = 'Week 1/'
#Bgr
#col_Blue = (255, 0, 0)
#col_Green = (0 , 255, 0)
#col_Red = (0, 0, 255)

colHsvLowerGreen = (40, 100, 50)
colHsvUpperGreen = (50, 150, 200)

cap = cv2.VideoCapture(path_name + 'Vision_green_target1.mp4')


#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
#cap.set(cv2.CAP_PROP_EXPOSURE, -8)
    
while(True):
    ret, Original = cap.read()

    cv2.imshow('This is the original image', Original)

    hsvOriginal = cv2.cvtColor(Original, cv2.COLOR_BGR2HSV)

    arrLowerColor = np.array([colHsvLowerGreen])
    arrUpperColor = np.array([colHsvUpperGreen]) 

    mskBinary = cv2.inRange(hsvOriginal, arrLowerColor, arrUpperColor)

    mskColor = cv2.bitwise_and(Original, Original, mask=mskBinary)

    cv2.imshow('This is the Binary mask', mskBinary)
    cv2.imshow('This is the Colour mask', mskColor)

    keys = cv2.waitKey(1) & 0xFF
    if keys == ord('q') or keys == 27:
        break

cap.release()
cv2.destroyAllWindows()
