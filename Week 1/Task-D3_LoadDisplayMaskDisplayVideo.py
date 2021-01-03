import numpy as np
import cv2

path_name = 'Week 1/'
intCameraNumber = 1

colRgbBlue = (255, 0, 0)
colRgbGreen = (0 , 255, 0)
colRgbRed = (0, 0, 255)

if intCameraNumber == 0:
    colHsvLowerGreen = (45, 30, 127)
    colHsvUpperGreen = (85, 255, 255)
elif intCameraNumber == 1:
    colHsvLowerGreen = (40, 100, 50)
    colHsvUpperGreen = (50, 150, 200)

cap = cv2.VideoCapture(path_name + 'Vision_green_target1.mp4')

if intCameraNumber == 0:
    pass
elif intCameraNumber == 1:
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
    cap.set(cv2.CAP_PROP_EXPOSURE, -8)
    
while(True):
    ret, bgrOriginal = cap.read()

    cv2.imshow('This is the original image', bgrOriginal)

    hsvOriginal = cv2.cvtColor(bgrOriginal, cv2.COLOR_BGR2HSV)

    arrLowerColor = np.array([colHsvLowerGreen])
    arrUpperColor = np.array([colHsvUpperGreen]) 

    mskBinary = cv2.inRange(hsvOriginal, arrLowerColor, arrUpperColor)

    mskColor = cv2.bitwise_and(bgrOriginal, bgrOriginal, mask=mskBinary)

    cv2.imshow('This is the Binary mask', mskBinary)
    cv2.imshow('This is the Colour mask', mskColor)

    keys = cv2.waitKey(1) & 0xFF
    if keys == ord('q') or keys == 27:
        break

cap.release()
cv2.destroyAllWindows()
