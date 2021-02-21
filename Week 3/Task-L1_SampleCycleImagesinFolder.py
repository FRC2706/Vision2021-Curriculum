# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task L - > Sample and Cycle Images in Folder. 
# We are going to continue towards our objective of a vision tool
# This pseudo file is a reasonable attempt at cycling through a folder and 
# displaying all the images (png or jpg only, our decision) navigating with up/down
# arrow keys, and exiting with esc key or q.

# imports
import numpy as np
import cv2
import os

# select folder of interest
dirName = '../2017-pegsAtDistance/'

# read file names
fileNames = os.listdir(dirName)
print('fileNames ', fileNames)

# filter file names
arrImageFiles = []

for filename in os.listdir(dirName):
    if filename.endswith(".jpg"):
        arrImageFiles.append(filename)

if len(arrImageFiles) > 0 :
    # set index of files
    intCounter = 0

    # begin loop
    flgExit = False
    while not(flgExit):

        ## read file
        bgrOriginal = cv2.imread(dirName + arrImageFiles[intCounter])

        ## display files
        cv2.imshow(arrImageFiles[intCounter], bgrOriginal)

        ## wait for user input
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
    ## end of loop
else :
    print('no file is found')

# cleanup and end of file
cv2.destroyAllWindows()

