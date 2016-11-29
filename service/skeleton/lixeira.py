from service import lixeira as _l
from model import lixeiras_pb2
import json

class LixeiraEsqueleto(object):

    def __init__(self):
        self.lixeiraService = _l.LixeiraService()

    def saveLixeira(self, lixeira_json, server_key):
        l = json.loads(lixeira_json) #transforma a mensagem em JSON
        lixeira = lixeiras_pb2.Lixeira() #criar o objeto lixeira
        lixeira.id = int(l['id'])
        lixeira.localizacao = l['localizacao']
        lixeira.peso = float(l['peso'])

        if(self.lixeiraService.saveLixeira(lixeira, server_key)):
            return '1'
        else:
            return '0'

    def getLixeiras(self):
        lixeiras = self.lixeiraService.getLixeiras()
        resposta = lixeiras.SerializeToString()
        return resposta