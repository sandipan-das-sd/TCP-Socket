import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8000))
print("Connected to server")

while True:
    
    server_msg = client.recv(1024).decode()
    if not server_msg:
        print("Server disconnected.")
        break
    print("Server:", server_msg)

    # Send message to server
    message = input("You (client): ")
    client.send(message.encode())

client.close()
