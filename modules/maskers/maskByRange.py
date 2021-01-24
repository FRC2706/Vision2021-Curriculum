import cv2

def maskByRange(hsvImage, colHsvLower, colHsvUpper):
    print('mbr-recd', colHsvLower, 'h', colHsvUpper)
    return cv2.inRange(hsvImage, colHsvLower, colHsvUpper)