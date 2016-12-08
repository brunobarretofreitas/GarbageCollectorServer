from service import skeletons as _s
from model import message as _m

class Despachante(object):

    def getResposta(self, message):
        esqueleto = getattr(_s, message.objeto+"Esqueleto")()
        return getattr(esqueleto, message.metodo)(message)