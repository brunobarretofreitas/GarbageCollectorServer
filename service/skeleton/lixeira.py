from service import lixeira as _l
from model import lixeiras_pb2

class LixeiraEsqueleto(object):

    def __init__(self):
        self.lixeiraService = _l.LixeiraService()

    def getLixeiras(self):
        lixeiras = self.lixeiraService.getLixeiras()
        resposta = lixeiras.SerializeToString()
        return resposta