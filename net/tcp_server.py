import socket
from threading import Thread
from model import message
from net import dispatcher
from model import mensagem_pb2
from model import lixeiras_pb2

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):
    def __init__(self, ip, port, conn):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn
        print "[+] New server socket thread started for " + ip + ":" + str(port)

    def run(self):
        request = self.getRequest()
        mensagem = mensagem_pb2.Mensagem()
        mensagem.ParseFromString(request)

        despachante = dispatcher.Despachante()
        resposta = despachante.getResposta(mensagem)

        self.sendReply(resposta.SerializeToString())

    def getRequest(self):
        request = self.conn.recv(2048) #mensagem recebida
        return str(request)

    def sendReply(self, response):
        self.conn.send(response)
        self.conn.close()

TCP_IP = 'localhost'
TCP_PORT = 2068
BUFFER_SIZE = 1024

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    print len(threads)
    tcpServer.listen(5)
    (conn, (ip, port)) = tcpServer.accept()
    print "Cliente conectado"
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)