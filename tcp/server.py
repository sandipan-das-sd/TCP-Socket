import socket

host = "localhost"
port = 8000

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print("Waiting for connection...")
conn, addr = server.accept()
print("Server connected to", addr)

# Communication loop
while True:
    try:
        data = conn.recv(1024).decode()
        if not data:
            print("Client disconnected.")
            break

        print("Client:", data)

        message = input("You (server): ")
        conn.send(message.encode())

        if message.lower() == 'exit':
            print("Exiting chat...")
            break

    except Exception as e:
        print("Error:", e)
        break

# Close connections
conn.close()
server.close()
print("Connection closed.")
print("Server shut down.")
