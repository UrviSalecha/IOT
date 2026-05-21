# q14 b) UDP receiver accepts byte streams decode each JPEG 
# converts it to grayscale and live display
import socket
import cv2
import numpy as np
socket_udp=socket.socket(socket.AF_NET,socket.SOCK_DGRAM)
socket_udp.bind(('127.0.0.1',5005))

while True:
    data,addr=socket_udp.recvfrom(65536) # receive data from sender
    nparr=np.frombuffer(data,np.uint8) # convert byte data to numpy array
    frame=cv2.imdecode(nparr,cv2.IMREAD_COLOR) # decode JPEG to image
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # convert to grayscale
    cv2.imshow('UDP Receiver',gray) # display the grayscale image
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
socket_udp.close() 

# UDP is preferred over TCP for real time video streaming because: 
# - Lower Latency 
# - Connectionless protocol
# - No congestion control 
# - real time can tolerate some kind of packet loss

# Visual artefact observed description: 
# - pixalated frames due to packet loss
# - some frames may appear blocky  