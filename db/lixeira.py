import connection as con
from model import lixeiras_pb2

class LixeiraRepository(object):

    def __init__(self):
        connectionFactory = con.ConnectionFactory()
        self.connection = connectionFactory.getConnection()

    def saveLixeira(self, lixeira):
        cursor = self.connection.cursor()
        sql = "insert into lixeira(id,localizacao,peso,status_coleta, status_capacidade) values(%s, %s, %s, %s, %s)"

        data = (lixeira.id, lixeira.localizacao, lixeira.peso, 1, 1)
        cursor.execute(sql, data)
        self.connection.commit()
        self.closeConnection()

    def updateLixeira(self, lixeira):
        cursor = self.connection.cursor()
        sql = "update lixeira set(localizacao, peso, status_capacidade) = (%s, %s, %s) where id = %s"
        data = (lixeira.localizacao, lixeira.peso, lixeira.status_capacidade, lixeira.id)
        cursor.execute(sql, data)
        self.connection.commit()
        self.closeConnection()

    def updateStatusColeta(self, lixeira):
        cursor = self.connection.cursor()
        sql = "update lixeira set(status_coleta) = (%s) where id = %s"
        data = (lixeira.status_coleta, lixeira.id)
        cursor.execute(sql, data)
        self.connection.commit()
        self.closeConnection()

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

        self.closeConnection()
        return listaLixeira

    def lixeiraExists(self, lixeira):
        cursor = self.connection.cursor()
        sql = "select * from lixeira where id = %s"
        data = ([lixeira.id])
        cursor.execute(sql, data)
        lixeira = cursor.fetchall()
        if(len(lixeira) > 0):
            return True
        else:
            return False

    def closeConnection(self):
        self.connection.close()