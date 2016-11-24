from model import lixeiras_pb2
import googlemaps
import service.distancia

distanciaService = service.distancia.DistanciaService()
print(distanciaService.calcularDistancia("-3.765529,-38.637767", "-3.765981,-38.635758"))