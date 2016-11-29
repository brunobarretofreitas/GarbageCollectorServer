from service.skeleton import distancia as _dist_esqueleto
from service.skeleton import lixeira as _lix
from enum import Enum

class Despachante(object):

    def getResposta(self, message):
        resposta = None
        if (message.servico == Servicos.CALCULAR_DISTANCIA.value):
            esqueleto = _dist_esqueleto.DistanciaEsqueleto()
            locais = message.conteudo
            resposta = esqueleto.calcularDistancia(localA=locais[0], localB=locais[1])

        elif(message.servico == Servicos.GET_LIXEIRAS.value):
            esqueleto = _lix.LixeiraEsqueleto()
            resposta = esqueleto.getLixeiras()

        elif(message.servico == Servicos.SAVE_LIXEIRA.value):
            esqueleto = _lix.LixeiraEsqueleto()
            lixeira_json = message.conteudo[0]
            server_key = message.conteudo[1]
            if(esqueleto.saveLixeira(lixeira_json, server_key)):
                resposta = '1'
            else:
                resposta = '0'

        return resposta

class Servicos(Enum):
    CALCULAR_DISTANCIA = '1'
    GET_LIXEIRAS = '2'
    SAVE_LIXEIRA = '3'
    ALTERAR_STATUS_COLETA = '4'