class Processo(object):
    
    def __init__(self, id, prioridade, tempos):
        self.id = id
        self.prioridade = prioridade
        self.tempos = tempos
    def printProcesso(self):
        print("Id: %d - Prioridade: %d Tempo 1: %d", self.id, self.prioridade)


#MAIN#

processo_exemplo = Processo(1,1,{10,10,10})
print(processo_exemplo.id)
