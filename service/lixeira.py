from db import lixeira as _l
from util import config as _c

class LixeiraService(object):

    def saveLixeira(self, lixeira, chave):
        config = _c.Config()
        if(chave == config.server_key):
            lixeiraRepository = _l.LixeiraRepository()
            if (lixeiraRepository.lixeiraExists(lixeira)):
                lixeiraRepository.updateLixeira(lixeira)
            else:
                lixeiraRepository.saveLixeira(lixeira)

            return True
        else:
            return False

    def getLixeiras(self):
        lixeiraRepository = _l.LixeiraRepository()
        return lixeiraRepository.getLixeiras()