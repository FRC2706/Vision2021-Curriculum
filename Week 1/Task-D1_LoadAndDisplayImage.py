import numpy as np
import cv2

str_path_name = 'Week 1/'
img_1_name = 'Vision_Basketball_Targets.png'

img_1_input = cv2.imread(str_path_name + img_1_name)
print('img_1_imput')

cv2.imshow('image window name',img_1_input)

cv2.waitKey(0)

cv2.destroyAllWindows()

print('hello')