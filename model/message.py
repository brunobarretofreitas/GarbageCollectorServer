class Mensagem(object):

    def __init__(self, request):
        self.servico = request.split(';')[0]
        request = request.split(';')[1]
        self.conteudo = request.split('**')