# Canny edge detection to the received frame before rendering
# specify 2 threshold values you would use and why

import cv2 
import numpy as np

def canny_edge_detection(frame):
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    edges=cv2.Canny(blur,50,150)
    return edges

# Commonly used threshold values for canny edge detection 
# 50: to detect strong edges
# 150: to supress weak edages and reduce noise 
# subjective and modified as per input image characteristics and desired output  