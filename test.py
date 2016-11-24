from model import lixeiras_pb2
import googlemaps
import service.distancia as distanciaService

gmaps = googlemaps.Client(key="AIzaSyDcyoiTWB9E-9-bgdk1jhjIqxS_xDKc0Ls")
resposta = gmaps.distance_matrix("-3.765529,-38.637767", "-3.765981,-38.635758")
distancia = (resposta['rows'][0]['elements'][0]['distance']['value'] * 1.0)/1000
print distancia