from model import lixeiras_pb2
import googlemaps
import service.distancia
from net import dispatcher
from model import message

request = "1;-3.765529,-38.637767**-3.765981,-38.635758"
mensagem = message.Mensagem(request)
despachante = dispatcher.Despachante()
print despachante.getResposta(mensagem)