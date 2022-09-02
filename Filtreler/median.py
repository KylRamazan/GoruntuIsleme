import cv2,consts
from matplotlib import pyplot as plt

def MedianFilter(image):
    image=cv2.imread(image)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    return cv2.cvtColor(cv2.medianBlur(image,consts.figure_size),cv2.COLOR_HSV2RGB)