import cv2

def BilateralFilter(image):
    image=cv2.imread(image)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    return cv2.bilateralFilter(image,9,75,75)