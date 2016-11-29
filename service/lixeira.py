from db import lixeira as _l

class LixeiraService(object):

    def getLixeiras(self):
        lixeiraRepository = _l.LixeiraRepository()
        return lixeiraRepository.getLixeiras()