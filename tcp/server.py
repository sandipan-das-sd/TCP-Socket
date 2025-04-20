import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8000))
server.listen(1)  
print("Waiting for connection...")

conn, addr = server.accept()
print("Connected to client:", addr)

# Server sends first message
conn.send("Welcome to the server!".encode())

while True:
    # Receive message from client
    data = conn.recv(1024).decode()
    if not data:
        print("Client disconnected.")
        break
    print("Client:", data)

    # Send message to client
    message = input("You (server): ")
    conn.send(message.encode())

conn.close()
server.close()
