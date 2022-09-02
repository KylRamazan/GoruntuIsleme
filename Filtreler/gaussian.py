import cv2,consts
import matplotlib.pyplot as plt

def GaussianFilter(image):
    image=cv2.imread(image)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    return cv2.cvtColor(cv2.GaussianBlur(image,(consts.figure_size,consts.figure_size),0),cv2.COLOR_HSV2RGB)