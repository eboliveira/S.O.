# -*- coding: utf-8 -*-
import sys
import processo
import escalonadores
import util

if len(sys.argv)  != 2:
    print("Modo de uso: python main.py <arquivos contendo informações dos processos>")
    exit(1)
arq = open(sys.argv[1], 'r')
processos = util.formatarProcessos(arq,processo)
fifo = escalonadores.FIFO(processos)
fifo.ordenar()
print(fifo.ordem)