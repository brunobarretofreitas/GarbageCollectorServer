import socket
from threading import Thread
from model import message
from net import dispatcher

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
            mensagem = message.Mensagem(request)
            despachante = dispatcher.Despachante()
            tmensagem = despachante.getResposta(mensagem)
            resposta = mensagem.arguments
            print resposta
            self.sendReply(resposta)

    def getRequest(self):
        request = self.conn.recv(2048).decode('UTF-8') #mensagem recebida
        return request

    def sendReply(self, response):
        self.conn.send(response)
        self.conn.close()

TCP_IP = 'localhost'
TCP_PORT = 2055
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