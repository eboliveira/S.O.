# -*- coding: utf-8 -*-
def formatarProcessos(arq,processo):    #formata uma lista de processos em uma lista de objetos
    processos = []
    texto = arq.readline()
    while texto:    #enquanto houver linhas para ler
        texto = texto.strip('\n')   #retira a quebra de linha
        content = texto.split(' ')  #passa para um vetor retirando o token " "
        idProcesso = content[0]
        tam = content[1]
        prioridade = content[2]
        tempo_chegada = content[3]
        eventos = []
        for i in range(4, len(content)):
            eventos.append(content[i])
        processos.append(
            processo.Processo(
                                idProcesso,
                                prioridade,
                                {"chegada" : int(tempo_chegada), "inicio" : None}, #None = tempo de inicio
                                int(tam),
                                "parado", #estado inicial é parado
                                eventos
                                )
        )
        texto = arq.readline()  #pula pra proxima linha
    return processos

def formatarProcessosRR(arq,processo):    #formata uma lista de processos em uma lista de objetos
    processos = []
    texto = arq.readline()
    while texto:    #enquanto houver linhas para ler
        texto = texto.strip('\n')   #retira a quebra de linha
        content = texto.split(' ')  #passa para um vetor retirando o token " "
        idProcesso = content[0]
        tam = content[1]
        quantum = content[1]
        prioridade = content[2]
        tempo_chegada = content[3]
        eventos = []
        for i in range(4, len(content)):
            eventos.append(content[i])
        processos.append(
            processo.Processo(
                                idProcesso,
                                prioridade,
                                {"chegada" : int(tempo_chegada), "inicio" : None}, #None = tempo de inicio
                                int(tam),int(quantum),
                                "parado", #estado inicial é parado
                                eventos
                                )
        )
        texto = arq.readline()  #pula pra proxima linha
    return processos
