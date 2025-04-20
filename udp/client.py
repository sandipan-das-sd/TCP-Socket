import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8000)
print("Connected to server")

while True:
    # Receive message from server
    server_msg, _ = client.recvfrom(1024)
    print("Server:", server_msg.decode())

    # Send message to server
    message = input("You (client): ")
    client.sendto(message.encode(), server_address)
