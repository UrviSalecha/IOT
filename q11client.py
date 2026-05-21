# Q11 TCP Client sends user_typed messages and receives broadcast messages from other 
# clients using two threads one sending and one receiving

import socket
import threading

HOST = "0.0.0.0"
PORT = 12346

username = input("Choose your username: ")
# TCP code q11client.py refer 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try: # exceptional exception handling 
            message = client.recv(1024).decode()
            if message == "USERNAME":
                client.send(username.encode())
            else:
                print(message)
        except:
            print("Disconnected from server.")
            client.close()
            break

def send_messages():
    while True:
        message = f"{username}: {input()}"
        client.send(message.encode())

threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
