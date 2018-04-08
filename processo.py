class Processo(object):
    tempos = []
    estado = None
    eventos = []


    def __init__(self, id, prioridade, tempos, estado, eventos):
        self.id = id
        self.prioridade = prioridade
        self.tempos = tempos
        self.estado = estado
        self.eventos = eventos
    def __str__(self):
        return "\n" + str(self.__dict__)
    def __repr__(self):
        return str(self) + "\n"
