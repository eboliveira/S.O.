# -*- coding: utf-8 -*-
import operator
class Escalonadores(object):

    lista_espera = []   #lista de espera da execucao
    ordem = []  #ordem de execucao
    tempos = {"execucao" : 0, "espera" : 0}


    def __init__(self, processos):
        self.processos = processos
    def ordenar(self):
        pass
    def executar(self, processo):
        pass
    def exec_IO(self, evento):
        pass

    

class FIFO(Escalonadores):

    def __init__(self, processos):
        super(FIFO,self).__init__(processos) #herança da classe pai
    def ordenar(self):
        self.ordem = sorted(self.processos, key = operator.itemgetter(["tempos","chegada"]) ) #ordena por ordem de chegada 
    def __str__(self):  #função de print de um objeto
        return "\n" + str(self.__dict__) 
    def __repr__(self): #função de print de uma lista de objetos
        return str(self) + "\n" 
    def executar(self): #função principal, executa os processos na ordem fifo
        self.ordenar()
        for i in range(len(self.ordem)):
            if self.tempos["execucao"] < self.ordem[i].tempos["chegada"]:   #verifica se não tinha outro processo executando
                dif = self.ordem[i].tempos["chegada"] - self.tempos["execucao"] #
                self.tempos["espera"] = self.tempos["espera"] + dif             #Se nao tinha outro processo executando, adiciona ao tempo de espera, o tempo em que o programa está ocioso
                self.tempos["execucao"] = self.ordem[i].tempos["chegada"]       #
            self.ordem[i].estado = "executando" #seta o estado do precesso como executando
            self.ordem[i].tempos["inicio"] = self.tempos["execucao"]    #seta o tempo de inicio de execucao do processo
            if self.ordem[i].tempos["chegada"] < self.tempos["execucao"]:   #verifica se ele esperou pra ser executado
                dif = self.tempos["execucao"] - self.ordem[i].tempos["chegada"]
                self.tempos["espera"] = self.tempos["espera"] + dif
            for j in range(len(self.ordem[i].eventos)): #execucao dos I/O
                self.exec_IO(self.ordem[i].eventos[j])
            
            print("{} - {} # Processo {}".format(self.tempos["execucao"], (self.tempos["execucao"]+self.ordem[i].tamanho), self.ordem[i].id))
            self.tempos["execucao"] =self.tempos["execucao"] + self.ordem[i].tamanho 
            self.ordem[i].estado = "terminado"  #seta o estado do processo como terminado
        print("\nTempo total de execução: {}ns".format(self.tempos["execucao"]))
        print("Tempo total de espera: {}ns".format(self.tempos["espera"]))
        print("Tempo médio de espera: {}ns".format((float(self.tempos["espera"]) / float(len(self.ordem)))))