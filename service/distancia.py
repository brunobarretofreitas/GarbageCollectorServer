import googlemaps
import googlemaps.distance_matrix as gm_distance
import util.Config as config

class DistanciaService(object):

    def __init__(self):
        self.gmaps = googlemaps.Client(key=config.googlemaps_key)

    def calcularDistancia(self, localA, localB):
        response = self.gmaps.distance_matrix(localA, localB)
        distancia = (response['rows'][0]['elements'][0]['distance']['value'] * 1.0)/1000
        return distancia
    