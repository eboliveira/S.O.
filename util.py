# -*- coding: utf-8 -*-

def formatarProcessos(arq,processo):
    processos = []
    texto = arq.readline()
    while texto:    #enquanto houver linhas para ler
        texto = texto.strip('\n')   #retira a quebra de linha
        content = texto.split(' ')  #passa para um vetor com um token de ' '
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
                                [int(tempo_chegada),int(tam),None], #None = tempo de inicio
                                "parado", #estado inicial é parado
                                eventos
                                )
        )
        texto = arq.readline()  #pula pra proxima linha
    return processos
