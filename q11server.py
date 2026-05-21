#Build multi client TCP chat system using sockets and multi threading
# TCP server multiple clients concurrently using threads each client connect separate thread any incoming message from one client to all other connected clients
import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []

print("Group Chat Server started...")

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            usernames.remove(username)
            broadcast(f"{username} left the chat.".encode())
            break

def receive_connections():
    while True:
        client, addr = server.accept()
        print(f"Connected with {addr}")

        client.send(b"USERNAME")
        username = client.recv(1024).decode()

        usernames.append(username)
        clients.append(client)

        print(f"Username is {username}")
        broadcast(f"{username} joined the chat!".encode())

        client.send(b"Connected to the server.")
        threading.Thread(target=handle_client, args=(client,)).start()

receive_connections()