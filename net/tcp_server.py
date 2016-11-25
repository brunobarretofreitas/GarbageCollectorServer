import socket
from threading import Thread
from model import message
from net import dispatcher

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "[+] New server socket thread started for " + ip + ":" + str(port)

    def run(self):
        while True:
            request = conn.recv(2048) #mensagem recebida
            mensagem = message.Mensagem(request)
            despachante = dispatcher.Despachante()
            resposta = despachante.getResposta(mensagem)
            conn.send(resposta)


# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = 'localhost'
TCP_PORT = 2009
BUFFER_SIZE = 1024  # Usually 1024, but we need quick response

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpServer.listen(4)
    (conn, (ip, port)) = tcpServer.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()