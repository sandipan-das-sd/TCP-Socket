import socket

host = "localhost"
port = 8000

# Create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Connected to UDP server at {host}:{port}")

while True:
    message = input("You (client): ")
    client.sendto(message.encode(), (host, port))

    if message.lower() == 'exit':
        break

    data, addr = client.recvfrom(1024)
    print("Server:", data.decode())

    if data.decode().lower() == 'exit':
        break

client.close()
print("Client closed.")
