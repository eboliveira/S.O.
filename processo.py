class Processo(object):

    tempos = []
    estado = None
    eventos = []

    def __init__(self, Id, prioridade, tempos, estado, eventos):
        self.id = Id
        self.prioridade = prioridade
        self.tempos = tempos
        self.estado = estado
        self.eventos = eventos
    def __str__(self):
        return "\n" + str(self.__dict__)
    def __repr__(self):
        return str(self) + "\n"
    def __getitem__(self, tup):
        nome, posi = tup
        return self.__getattribute__(nome)[posi]