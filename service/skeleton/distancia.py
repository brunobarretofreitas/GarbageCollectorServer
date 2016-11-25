from service import distancia

class DistanciaEsqueleto(object):

    def __init__(self):
        self.distanciaService = distancia.DistanciaService()

    def calcularDistancia(self, localA, localB):
        resposta = str(self.distanciaService.calcularDistancia(localA, localB))
        return resposta