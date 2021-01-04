# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task D5 - > Introduction to Contours and Distance Calculations

# Last task we looped through images with keyboard control, this time we will complicate life by introducing parts of Task G and H to measure distance from camera to a vision target

# You can find answers to complete this task in the following links 
# -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html
# -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html#contours-getting-started
# -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html#contour-area
# -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html#a-straight-bounding-rectangle
# -> https://docs.wpilib.org/en/stable/docs/software/vision-processing/introduction/identifying-and-processing-the-targets.html?highlight=distance#measurements

# To help we have comments to prompt how to do this is below

# Imports!
# Python - import modules of code as required (OpenCV here)

# define a string variable for the path to the file

# define and fill an array with the names of images 

# setup loop

# load a color image using the string and array

# mask the image to only show yellow or green images

# generate the array of Contours

# sort the array of Contours by area

# draw circle at centroid of target on colour mask, and known distance to target as text

# calculate the vision distance to the target, assumed to be largest contour

# display the colour mask image to screen

# wait for user input to move or close

# cleanup and exit

