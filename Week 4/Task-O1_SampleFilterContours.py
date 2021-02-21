# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task O - > Argument passing and Folder management. 

# We are going to continue towards our objective of a tool for season kickoff
# This pseudo file will allow us to pass instructions to our code from the
# command line about what folders to use and eventually other desired options.

# imports
import numpy as np
import cv2
import os
import sys

# input folder of interest
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
dirName = sys.argv[1]
suffixName = sys.argv[2]

print('dirName ', dirName)
# read file names
fileNames = os.listdir(dirName)
#print('fileNames ', fileNames)

# filter file names
arrImageFiles = []

for filename in os.listdir(dirName):
    if filename.endswith(suffixName):
        arrImageFiles.append(filename)

print('number of files: ', len(arrImageFiles))


#command line example
# #python Task-O1_SampleFilterContours.py ../2018-MergeAtWorlds .png