import socket
import sys
from _thread import *

host = 'localhost'
port = 5500
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket criado")

try:
    welcome_socket.bind((host, port))
except socket.error:
    print("Error")
    sys.exit()

print("Socket atribuido")

welcome_socket.listen(10)

print("Socket pronto")

def clientthread(conn):
    welcome = "Welcome to the server. Type something"
    conn.send(welcome.encode())
    while True:
        data = conn.recv(1024)
        reply = "OK." + data.decode()
        if not data:
            break;
        print(reply)
        conn.sendall(data.encode())
    conn.close()



while True :
    clientsocket, address = welcome_socket.accept()
    print("Connected with" + address[0] + ":" + str(address[1]))
    start_new_thread(clientthread, (clientsocket ,))
welcome_socket.close()