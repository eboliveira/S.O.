# -*- coding: utf-8 -*-
import sys
import processo
import escalonadores
import util

if len(sys.argv)  != 2:
    print("ERROR: Modo de uso: python main.py <arquivos contendo informações dos processos>")
    exit(1)
arq = open(sys.argv[1], 'r')
processos = util.formatarProcessos(arq,processo)
# print processos
#fifo = escalonadores.FIFO(processos)
#fifo.executar()  
 
#sjf = escalonadores.SJF(processos) 
#sjf.executar()
 
rr = escalonadores.RR(processos)  
#Passar o timeslice
rr.executar(10)
