import json

from model import lixeiras_pb2
from service import distancia
from service import lixeira as _l
from service import rota as _r


class LixeiraEsqueleto(object):

    def __init__(self):
        self.lixeiraService = _l.LixeiraService()

    def saveLixeira(self, argumentos):
        lixeira_json = argumentos[0]
        server_key = argumentos[1]
        l = json.loads(lixeira_json) #transforma a mensagem em JSON
        lixeira = lixeiras_pb2.Lixeira() #criar o objeto lixeira
        lixeira.id = int(l['id'])
        lixeira.localizacao = l['localizacao']
        lixeira.peso = float(l['peso'])

        if(self.lixeiraService.saveLixeira(lixeira, server_key)):
            return '1'
        else:
            return '0'

    def getLixeiras(self, argumentos):
        lixeiras = self.lixeiraService.getLixeiras()
        resposta = lixeiras.SerializeToString()
        return resposta

class DistanciaEsqueleto(object):

    def __init__(self):
        self.distanciaService = distancia.DistanciaService()

    def calcularDistancia(self, argumentos):
        localA = argumentos[0]
        localB = argumentos[1]
        resposta = str(self.distanciaService.calcularDistancia(localA, localB))
        return resposta

class RotaEsqueleto(object):

    def __init__(self):
        self.rotaService = _r.RotaService()

    def calcularRota(self, argumentos):
        origem = argumentos[0]
        destino = argumentos[1]
        lixeiras = argumentos[2:(len(argumentos))]
        listaLixeira = self.rotaService.calcularRota(origem, lixeiras, destino)
        resposta = listaLixeira.SerializeToString()
        return resposta