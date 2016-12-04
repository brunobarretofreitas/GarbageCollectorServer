from service import skeletons as _s
from model import message as _m

class Despachante(object):

    def getResposta(self, message):
        esqueleto = getattr(_s, message.object+"Esqueleto")()
        resposta = getattr(esqueleto, message.method)(message.arguments)
        message.arguments = resposta
        return message

'''
request = "0;1;Distancia;calcularDistancia;-3.865905,-38.579406**-4.968011,-39.006793"
m = _m.Mensagem(request)
despachante = Despachante()
m = despachante.getResposta(m)
print m.arguments
print m.type
'''