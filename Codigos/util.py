# -*- coding: utf-8 -*-
def formatarProcessos(arq,processo):    #formata uma lista de processos em uma lista de objetos
    processos = []
    texto = arq.readline()
    while texto:    #enquanto houver linhas para ler
        texto = texto.strip('\n')   #retira a quebra de linha
        content = texto.split(' ')  #passa para um vetor retirando o token " "
        idProcesso = content[0]
        tam = int(content[1])
        prioridade = content[2]
        tempo_chegada = content[3]
        eventos = []
        j = 0
        for i in range(4, len(content)):
            eventos.append(int(content[i]))
            if eventos[j] > tam-1:
                print "ERROR: Evento de IO fora do tempo do processo"
                exit(1)
            j+=1
        eventos.sort()
        processos.append(
            processo.Processo(
                                idProcesso,
                                prioridade,
                                {"chegada" : int(tempo_chegada), "inicio" : None, "executado" : 0}, #None = tempo de inicio
                                tam,
                                "parado", #estado inicial é parado
                                eventos
                                )
        )
        texto = arq.readline()  #pula pra proxima linha
    return processos

