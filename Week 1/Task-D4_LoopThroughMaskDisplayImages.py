# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task D4 - > Loop through Mask Display Images

# Last task introduced loops, for this task lets store a bunch of images in an array and loop through them all with keyboard control

# Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html

# To help we have comments to prompt how to do this is below

# Imports!
# Python - import modules of code as required (OpenCV here)
import numpy as np
import cv2

# Constants!
# colors for screen information
colBgrBlue = (255, 0, 0)
colBgrGreen = (0 , 255, 0)
colBgrRed = (0, 0, 255)

# colors for HSV filtering
colHsvLowerGreen = (55, 220, 220)
colHsvUpperGreen = (65, 255, 255)

# define a string variable for the path to the file
strPathName = '2017-pegsAtDistance/'

# define and fill an array with the names of images 
arrImageFiles = []
arrImageFiles.append('01dinf-pegs-14hiin.jpg')
arrImageFiles.append('02dinf-pegs-14hiin.jpg')
arrImageFiles.append('03dinf-pegs-14hiin.jpg')
arrImageFiles.append('04dinf-pegs-14hiin.jpg')
arrImageFiles.append('05dinf-pegs-14hiin.jpg')
arrImageFiles.append('06dinf-pegs-14hiin.jpg')
arrImageFiles.append('07dinf-pegs-14hiin.jpg')
arrImageFiles.append('08dinf-pegs-14hiin.jpg')
arrImageFiles.append('09dinf-pegs-14hiin.jpg')
arrImageFiles.append('10dinf-pegs-14hiin.jpg')
arrImageFiles.append('11dinf-pegs-14hiin.jpg')
arrImageFiles.append('12dinf-pegs-14hiin.jpg')
arrImageFiles.append('13dinf-pegs-14hiin.jpg')
arrImageFiles.append('14dinf-pegs-14hiin.jpg')
arrImageFiles.append('15dinf-pegs-14hiin.jpg')
arrImageFiles.append('16dinf-pegs-14hiin.jpg')
arrImageFiles.append('17dinf-pegs-14hiin.jpg')
arrImageFiles.append('18dinf-pegs-14hiin.jpg')
arrImageFiles.append('19dinf-pegs-14hiin.jpg')
arrImageFiles.append('20dinf-pegs-14hiin.jpg')

# setup loop
flgExit = False
intCounter = 0
while not(flgExit):

    # load a color image using the string and array
    bgrOriginal = cv2.imread(strPathName + arrImageFiles[intCounter])
    cv2.imshow('original image', bgrOriginal)

    # mask the image to only show yellow or green images
    hsvOriginal = cv2.cvtColor(bgrOriginal, cv2.COLOR_BGR2HSV)
        
    # define a range of from upper to lower in HSV
    arrLowerColor = np.array([colHsvLowerGreen])
    arrUpperColor = np.array([colHsvUpperGreen]) 
    
    # threshold the HSV image to get only green color
    # NOTE: filtered color = white; others = black
    mskBinary = cv2.inRange(hsvOriginal, arrLowerColor, arrUpperColor)
    cv2.imshow('binary mask',mskBinary)

    # create a full color mask
    # Bitwise-AND binary mask and original image
    # NOTE: 1 = white; 0 = black;
    mskColor = cv2.bitwise_and(bgrOriginal, bgrOriginal, mask=mskBinary)

    # display the colour mask image to screen
    cv2.imshow('This is the Colour mask', mskColor)

    # wait for user input to move or close
    while(True):
        # stop the program until you input a key
        ke = cv2.waitKeyEx(0)
        # Key code is implementation specific and depends on used backend: QT/GTK/Win32
        # ke is the ASCII value of the key
        # for windows arrows,  Left: 2424832 Up: 2490368 Right: 2555904 Down: 2621440
        if ke == 113 or ke == 27:
            # exit at 'q' or 'esc'
            flgExit = True
            break
        if ke == 105 or ke == 2490368:
            # back loop at 'i' or upper arrow
            intCounter = intCounter - 1
            if intCounter < 0: 
                intCounter = len(arrImageFiles) - 1
            break
        if ke == 109 or ke == 2621440:
            # forward loop at 'm' or down arrow
            intCounter = intCounter + 1
            if intCounter > len(arrImageFiles) - 1:
                intCounter = 0
            break

# cleanup and exit
cv2.destroyAllWindows()
