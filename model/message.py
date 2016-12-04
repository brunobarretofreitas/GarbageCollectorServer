class Mensagem(object):

    def __init__(self, request):
        parametros = request.split(';')
        self.object = parametros[0]
        self.method = parametros[1]
        arg = parametros[2]
        self.arguments = arg.split('**')

    def toString(self):
        msg = ''+self.object+";"+self.method+";"
        for arg in self.arguments:
            msg += arg + "**"

        tamanho = len(msg)
        msg = msg[0:tamanho-2]
        return msg