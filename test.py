from model import lixeiras_pb2
import googlemaps
import service.distancia
from net import dispatcher
from model import message
import psycopg2
from db import lixeira
'''
lixeira = lixeiras_pb2.Lixeira()
lixeira.id = 10
lixeira.localizacao = "-3.765529,-38.637767"
lixeira.peso = 200.0
lixeira.status_coleta = 1
lixeira.status_capacidade = 1

l = lixeira.SerializeToString()
request = "2;" + l
print request


#request = "1;-3.765529,-38.637767**-3.765981,-38.635758"
mensagem = message.Mensagem(request)
print mensagem.servico
print mensagem.conteudo
print mensagem.conteudo[0]

print mensagem.conteudo[0] == l


#FUNCIONAAAAAAA POOOOOOOORA BIIIIIRL
#despachante = dispatcher.Despachante()
#print despachante.getResposta(mensagem)
'''
'''
con = psycopg2.connect(host='localhost', database='garbage', user='postgres', password='postgres')
cur = con.cursor()
cur.execute('select * from lixeira')
ver = cur.fetchone()
'''

'''
request = "2;"
mensagem = message.Mensagem(request)
despachante = dispatcher.Despachante()
resposta = despachante.getResposta(mensagem)
print resposta

print "Transformando em objeto..."

lista = lixeiras_pb2.ListaLixeira()
lista.ParseFromString(resposta)

print lista
'''


request = '3;{"id":20, "localizacao":"123123,12300", "peso":900.0, "status_capacidade":0}**gPlb5AMBaXB3GSdjO5aUD1Ftp7L131YT'
"4;1**2**3**4**5**6**7**0"

mensagem = message.Mensagem(request)
despachante = dispatcher.Despachante()
resposta = despachante.getResposta(mensagem)

print resposta