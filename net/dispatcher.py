from model import constants as _constants
from service.skeleton import distancia as _dist_esqueleto
from service.skeleton import lixeira as _lix

class Despachante(object):

    def getResposta(self, message):
        resposta = None
        if (message.servico == _constants.Servicos.CALCULAR_DISTANCIA.value):
            esqueleto = _dist_esqueleto.DistanciaEsqueleto()
            locais = message.conteudo
            resposta = esqueleto.calcularDistancia(localA=locais[0], localB=locais[1])

        elif(message.servico == _constants.Servicos.GET_LIXEIRAS.value):
            esqueleto = _lix.LixeiraEsqueleto()
            resposta = esqueleto.getLixeiras()

        return resposta