import socket
import time
import sys


if len(sys.argv) is not 3:
    print("Argumentos passados estao invalidos. Use o comando:\n python cliente.py ip_servidor porta_servidor")
    
    exit()
host = sys.argv[1]
port = int(sys.argv[2])

message = 'aasd'*64000  # ver aqui o que enviar

#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (host, port)

tcp.connect(dest)

while True:
    #tcp.send (','.join(message))
    tcp.send (message)

tcp.close()