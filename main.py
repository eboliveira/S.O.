# -*- coding: utf-8 -*-
import sys
import processo

if len(sys.argv)  != 2:
    print("Modo de uso: python main.py <arquivos contendo informações dos processos>")
    exit(1)
arq = open(sys.argv[1], 'r')
process = []
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
    process.append(
        processo.Processo(
                            idProcesso,
                            prioridade,
                            (tempo_chegada,tam,None), #None = tempo de inicio
                            "parado", #estado inicial é parado
                            eventos
                            )
    )
    texto = arq.readline()  #pula pra proxima linha

print(process)