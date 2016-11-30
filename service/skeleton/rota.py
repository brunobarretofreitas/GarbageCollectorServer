from service import rota as _r
from model import rotas_pb2

class RotaEsqueleto(object):

    def __init__(self):
        self.rotaService = _r.RotaService()

    def calcularRota(self, origem, lixeiras, destino):
        listaLixeira = self.rotaService.calcularRota(origem, lixeiras, destino)
        resposta = listaLixeira.SerializeToString()
        return resposta