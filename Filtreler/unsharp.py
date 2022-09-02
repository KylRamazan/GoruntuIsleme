import cv2

def UnsharpFilter(image):
    image=cv2.imread(image)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    return cv2.addWeighted(image,1.5,cv2.GaussianBlur(image,(0,0),2.0),-0.5,0,image)