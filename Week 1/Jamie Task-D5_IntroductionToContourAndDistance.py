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
b = 'Vision2021-Curriculum/2017-pegsAtDistance/'
onlyfiles = [ f for f in listdir(b) if isfile(join(b,f))]
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0,len(onlyfiles)):
    images[n] = cv2.imread( join(b,onlyfiles[n]))
    hsv = cv2.cvtColor(images[n], cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (60, 100, 100), (70, 255,255))
    cv2.imshow('image',images[n])
    cv2.imshow('Masked image',mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()