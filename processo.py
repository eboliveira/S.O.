class Processo(object):

    tempos = {}
    estado = None
    eventos = []

    def __init__(self, Id, prioridade, tempos, tam, estado, eventos):
        self.id = Id
        self.prioridade = prioridade
        self.tempos = tempos
        self.estado = estado
        self.eventos = eventos
        self.tamanho = tam
    def __str__(self):      #funcao de print de um objeto
        return "\n" + str(self.__dict__)
    def __repr__(self):     #funcao de print de uma lista de objetos
        return str(self) + "\n"
    def __getitem__(self, tup):     #recebe como parametro uma tupla que contem o nome do atributo e posicao; retorna o objeto
        nome, posi = tup
        return self.__getattribute__(nome)[posi]