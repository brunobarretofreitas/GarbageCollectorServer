import connection as con
from model import lixeiras_pb2

class LixeiraRepository(object):

    def __init__(self):
        connectionFactory = con.ConnectionFactory()
        self.connection = connectionFactory.getConnection()

    def getLixeiras(self):
        sql = "select * from lixeira"
        cur = self.connection.cursor()
        cur.execute(sql)
        lixeiras = cur.fetchall()
        listaLixeira = lixeiras_pb2.ListaLixeira()
        for l in lixeiras:
            lixeira = listaLixeira.lixeira.add()
            lixeira.id = int(l[0])
            lixeira.localizacao = l[1]
            lixeira.peso = float(l[2])
            lixeira.status_coleta = l[3]
            lixeira.status_capacidade = l[4]

        return listaLixeira

    def closeConnection(self):
        self.connection.close()