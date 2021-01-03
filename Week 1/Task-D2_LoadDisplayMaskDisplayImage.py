import numpy as np
import cv2

str_path_name = 'Week 1/'
img_1_name = 'Vision_Basketball_Targets.png'
img_2_name = 'Vision_RGB_colors.png'

img_1_input = cv2.imread(str_path_name + img_1_name)
img_2_input = cv2.imread(str_path_name + img_2_name)

cv2.imshow('origonal image 1',img_1_input)
cv2.imshow('origonal image 2',img_2_input)

img_1_in_hsv = cv2.cvtColor(img_1_input,cv2.COLOR_BGR2HSV)
img_2_in_hsv = cv2.cvtColor(img_2_input,cv2.COLOR_BGR2HSV)

low_green_1 = np.array([20,100,100])
high_green_1 = np.array([120,255,255])

low_green_2 = np.array([20,100,100])
high_green_2 = np.array([80,200,200])

img_1_binary_mask = cv2.inRange(img_1_in_hsv, low_green_1, high_green_1)
img_2_binary_mask = cv2.inRange(img_2_in_hsv, low_green_2, high_green_2)


cv2.imshow('masked image 1',img_1_binary_mask)
cv2.imshow('masked image 2',img_2_binary_mask)

cv2.waitKey(0)

cv2.destroyAllWindows()
