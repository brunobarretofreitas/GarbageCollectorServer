from model import constants as _constants
from service.skeleton import distancia as _dist_esqueleto


class Despachante(object):
    def __init__(self):
        self.resposta = ''
        self.mensagem = None

    def getResposta(self, message):
        if (message.servico == _constants.Servicos.CALCULAR_DISTANCIA.value):
            esqueleto = _dist_esqueleto.DistanciaEsqueleto()
            locais = message.conteudo
            self.resposta = esqueleto.calcularDistancia(localA=locais[0], localB=locais[1])

        return self.resposta