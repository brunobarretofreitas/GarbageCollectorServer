import json

from model import lixeiras_pb2
from model import mensagem_pb2
from service import distancia
from service import lixeira as _l
from service import rota as _r


class LixeiraEsqueleto(object):

    def __init__(self):
        self.lixeiraService = _l.LixeiraService()

    def getLixeiras(self, mensagem):
        lixeiras = self.lixeiraService.getLixeiras()
        resposta = mensagem_pb2.Mensagem()
        resposta.tipo = 1
        resposta.id = mensagem.id
        resposta.objeto = mensagem.objeto
        resposta.metodo = mensagem.metodo
        resposta.argumentos.append(lixeiras.SerializeToString())

        return resposta

    def atualizarStatusColeta(self, mensagem):
        status_coleta = mensagem.argumentos[0]
        id_lixeiras_list = mensagem.argumentos[1:len(mensagem.argumentos)]
        resposta = mensagem_pb2.Mensagem()
        resposta.tipo = 1
        resposta.id = mensagem.id
        resposta.objeto = mensagem.objeto
        resposta.metodo = mensagem.metodo

        if(self.lixeiraService.atualizarStatusColeta(id_lixeiras_list, status_coleta)):
            resposta.argumentos.append('1')
            return resposta
        else:
            resposta.argumentos.append('0')
            return resposta

class DistanciaEsqueleto(object):

    def __init__(self):
        self.distanciaService = distancia.DistanciaService()

    def calcularDistancia(self, mensagem):
        localA = mensagem.argumentos[0]
        localB = mensagem.argumentos[1]

        resposta = mensagem_pb2.Mensagem()
        resposta.tipo = 1
        resposta.id = mensagem.id
        resposta.objeto = mensagem.objeto
        resposta.metodo = mensagem.metodo
        resposta.argumentos.append(str(self.distanciaService.calcularDistancia(localA, localB)))

        return resposta

class RotaEsqueleto(object):

    def __init__(self):
        self.rotaService = _r.RotaService()

    def calcularRota(self, mensagem):
        origem = mensagem.argumentos[0]
        destino = mensagem.argumentos[1]
        lixeiras = mensagem.argumentos[2:(len(mensagem.argumentos))]
        listaRota = self.rotaService.calcularRota(origem, lixeiras, destino)
        resposta = mensagem_pb2.Mensagem()

        resposta.tipo = 1
        resposta.id = mensagem.id
        resposta.objeto = mensagem.objeto
        resposta.metodo = mensagem.metodo
        resposta.argumentos.append(listaRota.SerializeToString())

        return resposta
