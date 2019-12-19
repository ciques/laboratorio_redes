import socket
import thread
from time import sleep, time
import sys
import csv


def log_writer():
    file_name = 'log_txt_'+ str(port) + '.txt'
    with open(file_name,'w') as the_file:
        the_file.write('Hello\n')
        old_value = 0
        while True:
            value = message_size
            line = str(time()) + ' - ' + str(value - old_value)
            print line
            old_value = value
            the_file.write(line + '\n')
            sleep(1)  

    print 'Finalizando thread'
    thread.exit()


if len(sys.argv) is not 3:
    print("Argumentos passados estao invalidos. Use o comando:\n python server.py ipservidor porta_servidor")
    exit()

host = sys.argv[1]
port = int(sys.argv[2])

message = 'a'*64000
size = sys.getsizeof(message)
message_size = 0

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (host, port)

tcp.bind(orig)
tcp.listen(1)

thread.start_new_thread(log_writer,())

while True:
    con, cliente = tcp.accept()
    print 'Conectado por', cliente
    while True:
        msg = con.recv(size)
        if not msg: break
        message_size += sys.getsizeof(msg)
    print 'Finalizando conexao do cliente', cliente
    con.close()

