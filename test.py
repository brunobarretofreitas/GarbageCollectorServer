from model import lixeiras_pb2
from model import rotas_pb2
import googlemaps
from util import config as _config
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

'''
request = '3;{"id":20, "localizacao":"123123,12300", "peso":900.0, "status_capacidade":0}**gPlb5AMBaXB3GSdjO5aUD1Ftp7L131YT'
"4;1**2**3**4**5**6**7**0"

mensagem = message.Mensagem(request)
despachante = dispatcher.Despachante()
resposta = despachante.getResposta(mensagem)

print resposta
'''
'''
config = _config.Config()
gmaps = googlemaps.Client(key=config.googlemaps_key)
resultado = gmaps.directions(origin="-3.765529,-38.637767", destination="-3.720905,-38.510949", waypoints="-3.756725,-38.627910|-3.739983,-38.593184", language="pt")

listaRota = rotas_pb2.ListaRota()

for leg in resultado["routes"][0]["legs"]:
    rota = listaRota.rota.add()
    rota.enderecoOrigem = leg["start_address"]
    rota.enderecoDestino = leg["end_address"]
    rota.tamanho = leg["distance"]["text"]
    for step in leg["steps"]:
        passo  = rota.passo.add()
        passo.instrucao = step["html_instructions"]
        passo.distancia = step["distance"]["text"]
        passo.tempo = step["duration"]["text"]

for r in listaRota.rota:
    print r.enderecoOrigem
    print r.enderecoDestino
    print r.tamanho
    for p in rota.passo:
        print p.instrucao
        print p.distancia
        print p.tempo
'''

request = "4;-3.765529,-38.637767**-3.720905,-38.510949**-3.756725,-38.627910**-3.739983,-38.593184"
mensagem = message.Mensagem(request)
despachante = dispatcher.Despachante()
resposta = despachante.getResposta(mensagem)

print resposta