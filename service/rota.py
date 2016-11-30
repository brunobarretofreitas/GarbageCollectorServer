import googlemaps
from util import config as _c
from model import rotas_pb2

class RotaService(object):

    def __init__(self):
        config = _c.Config()
        self.gmaps = googlemaps.Client(key=config.googlemaps_key)

    def calcularRota(self, origem, lixeiras, destino): #origem(lat, long), lixeiras(list), destino(lat,long)
        w = ''
        for l in lixeiras:
            w += l + "|"

        tamanho = len(w)
        waypoints = w[0:(tamanho-1)]
        resultado = self.gmaps.directions(origin=origem, destination=destino,
                                     waypoints=waypoints, language="pt")

        listaRota = rotas_pb2.ListaRota()

        for leg in resultado["routes"][0]["legs"]:
            rota = listaRota.rota.add()
            rota.enderecoOrigem = leg["start_address"]
            rota.enderecoDestino = leg["end_address"]
            rota.tamanho = leg["distance"]["text"]
            for step in leg["steps"]:
                passo = rota.passo.add()
                passo.instrucao = step["html_instructions"]
                passo.distancia = step["distance"]["text"]
                passo.tempo = step["duration"]["text"]

        return listaRota