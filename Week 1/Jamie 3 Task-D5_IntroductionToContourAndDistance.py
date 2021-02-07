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
colHsvLowerGreen = (5, 50, 50)
colHsvUpperGreen = (15, 255, 255)

# fonts for displaying text
font = cv2.FONT_HERSHEY_SIMPLEX

#b = r"C:\Users\Jamie Diep\Documents\frc2021\My images"
intCounter = 0
strPathName = 'OrangePylons/'
onlyfiles = [ f for f in listdir(strPathName) if isfile(join(strPathName,f))]
arrImageFiles=[]
flgExit = False
for n in range(0,len(onlyfiles)):
    arrImageFiles.append(onlyfiles[n])

while not(flgExit):
    bgrOriginal = cv2.imread(strPathName+arrImageFiles[intCounter])
    hsv = cv2.cvtColor(bgrOriginal, cv2.COLOR_BGR2HSV)
    arrLowerColor = np.array([colHsvLowerGreen])
    arrUpperColor = np.array([colHsvUpperGreen]) 
    
    thresh = cv2.inRange(hsv, arrLowerColor,arrUpperColor)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    #print('Found', len(contours), 'contours in this photo!')
    indiv = contours[0]
    #print (indiv)
    cv2.drawContours(bgrOriginal, [indiv], 0, (255,0,0), 2)

    #rect=cv2.minAreaRect(indiv)
    #box = cv2.boxPoints(rect)
    #box = np.int0(box)
    ix, iy, iw, ih =cv2.boundingRect(indiv)
    #cv2.drawContours(bgrOriginal,[box],0,(0,0,255),2)
    cv2.imshow('oi', bgrOriginal)
    print('Image height: ',ih)
    #print(rect)
    #width=(rect[1][0])
    #print(width)
    #height=(rect[1][1])
    #print(height)
    #focalpoint=5.2
    #RealDistance = (RealHeight*Focal length)/PixelHeight
    CalculatedDistance = (14*145.8857)/ih
    print('Calculated distance: ', CalculatedDistance)

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