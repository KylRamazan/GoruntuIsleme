import cv2

def Gray(image):
    return cv2.cvtColor(cv2.imread(image),cv2.COLOR_BGR2GRAY)