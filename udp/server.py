import socket

host = "localhost"
port = 8000

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))

print(f"UDP Server started on {host}:{port}")

while True:
    data, addr = server.recvfrom(1024)
    message = data.decode()

    print(f"Client {addr} says: {message}")

    if message.lower() == 'exit':
        print("Client exited the chat.")
        break

    reply = input("You (server): ")
    server.sendto(reply.encode(), addr)

    if reply.lower() == 'exit':
        print("Exiting chat...")
        break

server.close()
print("Server closed.")
