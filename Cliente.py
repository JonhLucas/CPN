import socket
import sys


try:
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Falha na conexao")
    sys.exit()

print("socket criado")

host = "www.google.com"
#host = "localhost"
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("hostname pode estar errado")
    sys.ext();

print("IP address: " + remote_ip)

new_socket.connect((remote_ip, port))

message = "GET / HTTP/1.1\r\n\r\n"

try:
    new_socket.sendall(message.encode())
except socket.error:
    print("erro ao enviar")
    sys.exit()

print("enviado com sucesso")

reply = new_socket.recv(4096)

print(reply.decode())

new_socket.close()

#new_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#new_cliente.connect(("localhost", 5500))
#msg = new_cliente.recv(1024)
#print(msg.decode("utf-8"))