import psycopg2

class ConnectionFactory(object):

    def __init__(self):
        self.host='localhost'
        self.database='garbage'
        self.user='postgres'
        self.password='postgres'

    def getConnection(self):
        con = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        return con
