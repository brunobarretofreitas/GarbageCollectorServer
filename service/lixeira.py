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

    def atualizarStatusColeta(self, id_lixeiras_list, status_coleta):
        lixeiraRepository = _l.LixeiraRepository()
        lixeiras = lixeiraRepository.getLixeiras().lixeira
        flag = False
        for id in id_lixeiras_list:
            flag = False
            id = int(id.rstrip())
            for lixeira in lixeiras:
                if lixeira.id == id:
                    flag = True
                    lixeira.status_coleta = int(status_coleta)
                    config = _c.Config()
                    lixeiraRepository = _l.LixeiraRepository()
                    lixeiraRepository.updateStatusColeta(lixeira)
                    lixeiras.remove(lixeira)
                    break
            if not flag:
                break
            else:
                flag = True

        return flag