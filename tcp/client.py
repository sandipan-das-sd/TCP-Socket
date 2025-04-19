import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="localhost"
port=8000
client.connect((host,port))
print("connected to server")
while True:
    messge=input("You (client): ")
    client.send(messge.encode())
    if messge.lower() == 'exit':
        break
    data=client.recv(1024).decode()
    print("data from server:",data)
client.close()
print("Connection closed")
print("Client closed")
