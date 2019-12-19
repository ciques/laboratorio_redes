import socket
import thread
from time import sleep, time
import sys
import csv


def print_result_thread():
    file_name = 'mesure_'+ str(port) + '.csv'
    with open(file_name,'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        old_value = 0
        while True:
            value = valued_readed
            row = [0,0]
            row[0] = int(time())
            row[1] = value - old_value
            old_value = value
            writer.writerow(row)
            sleep(1)  


if len(sys.argv) is not 3:
    print("Argumentos passados estao invalidos. Use o comando:\n python server.py ipservidor porta_servidor")
    exit()

host = sys.argv[1]
port = int(sys.argv[2])

message = 'a'*640000
size = sys.getsizeof(message)
valued_readed = 0

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (host, port)

tcp.bind(orig)
tcp.listen(1)

thread.start_new_thread(print_result_thread,())

while True:
    con, cliente = tcp.accept()
    print 'Conectado por', cliente
    while True:
        msg = con.recv(size)
        print sys.getsizeof(message)
        if not msg: break
        valued_readed += sys.getsizeof(msg)
        sleep(1)
    print 'Finalizando conexao do cliente', cliente
    con.close()

