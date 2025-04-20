import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 8000))
print("Waiting for connection...")

while True:
    # Receive message from client
    data, addr = server.recvfrom(1024)
    print("Client:", data.decode())

    # Send message to client
    message = input("You (server): ")
    server.sendto(message.encode(), addr)


