USUARIO = 0     #define usuario como 0
SISTEMA = 1     #define sistema como 1
class Processo(object):
    
    tempos = {}
    estado = None
    eventos = []
    tipo = None

    def __init__(self, Id, prioridade, tempos, tam, estado, eventos):
        self.id = Id
        self.prioridade = prioridade
        self.tempos = tempos
        self.estado = estado
        self.eventos = eventos
        self.tamanho = tam
        self.tipo = USUARIO

    def __str__(self):      #funcao de print de um objeto
        return "\n" + str(self.__dict__)

    def __repr__(self):     #funcao de print de uma lista de objetos
        return str(self) + "\n"

    def __getitem__(self, tup):     #recebe como parametro uma tupla que contem o nome do atributo e posicao; retorna o objeto
        nome, posi = tup
        return self.__getattribute__(nome)[posi]

class Sistema(Processo):

    def __init__(self):
        self.tipo = SISTEMA

    def exec_IO(self, processo, tempo_exec):
        if len(processo.eventos):
            print "Evento de IO do processo ID = {} executado no tempo: {}".format(processo.id, tempo_exec)
            processo.eventos.pop(0)
        
  
