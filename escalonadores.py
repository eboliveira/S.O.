import operator
class Escalonadores(object):

    lista_espera = []
    ordem = []

    def __init__(self, processos):
        self.processos = processos
    def ordenar(self):
        pass
    def executar(self, processo):
        pass

    

class FIFO(Escalonadores):

    def __init__(self, processos):
        super(FIFO,self).__init__(processos)
    def ordenar(self):
        self.ordem = sorted(self.processos, key = operator.itemgetter(['tempos',1]) ) #ordena por ordem de chegada 
    def __str__(self):
        return "\n" + str(self.__dict__)
    def __repr__(self):
        return str(self) + "\n"
    # def executar(self, processos):


