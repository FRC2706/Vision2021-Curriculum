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
intCounter = 0
strPathName = 'Vision2021-Curriculum/2017-pegsAtDistance/'
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

    mask = 

    
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