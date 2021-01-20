# This is a pseudo code file for Merge Robotics, 2021, Game Changers

# This is task F - > Simplified and/or Enhanced Masking.  The basic range based mask you
# used in step D is a pure "range" based filter.  There are different methods out there, 
# mostly based on what is called "Chroma-Key" or perhaps more widely called
# "Green-Screening" for television and movies.

# Consider this explanation of green screen:
# - https://en.wikipedia.org/wiki/Chroma_key

# Then look at (and try out on your computer) these teams vision and masking code:
# - https://github.com/frc1418/2016-vision/blob/master/imgproc/findGreen.py
# - https://github.com/Knoxville-FRC-alliance/Vision-2018-Python/blob/master/visionPi.py
# - https://github.com/Knoxville-FRC-alliance/Vision-2018-Python/blob/master/vision.py
# - https://github.com/team3997/ChickenVision/blob/master/ChickenVision.py

# The idea is to experiment with a few lines of their code and use it with your own python files.  
# Objective is to pick a method to use for making our mask.

# Post a few favourie links and code snippets into a python copy of this file, then push to github.
#*
def threshold_range(im, lo, hi):
    unused, t1 = cv2.threshold(im, lo, 255, type=cv2.THRESH_BINARY)
    unused, t2 = cv2.threshold(im, hi, 255, type=cv2.THRESH_BINARY_INV)
    return cv2.bitwise_and(t1, t2)

#no pictures for 34-54, 10
img = cv2.imread('RealFullField/79.jpg')
cv2.imshow('image', img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)
a, b = 2, 1
h = threshold_range(h, 63, 105)
s = threshold_range(s, 7, 255)
v = threshold_range(v, 67, 242)
#cv2.imshow('s', s)
combined = cv2.bitwise_and(h, cv2.bitwise_and(s,v))
#img2 = combined.copy()
contours, v = cv2.findContours(combined, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
