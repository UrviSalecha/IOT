# OpenCV+ UDP : Real time Video Frame Streaming 
# a) UDP sender -> captures frames from a webcam using OpenCV encodes each frame as JPEG byte buffer
#  and transmits it via UDP socket

import socket
import cv2

socket_udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
cap=cv2.VideoCapture(0) # Video capture using the given command in question 
# check locally if opened 

while True:
    ret,frame=cap.read()
    if not ret:
        break
    # encoding
    encoded= cv2.imencode('.jpeg',frame)[1].tobytes()
    # send
    socket_udp.sendto(encoded,('127.0.0.1',5005))
    cap.release()
    socket_udp.close()
