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

#print "Algoritmo de Escalonamento: FIFO (Fist in First out)"
#fifo = escalonadores.FIFO(processos)
#fifo.executar()  
  
#print "Algoritmo de Escalonamento: SJF (Shorted Job First)"
#sjf = escalonadores.SJF(processos) 
#sjf.executar()
  
#print "Algoritmo de Escalonamento: RR (Round Robin)" 
#rr = escalonadores.RR(processos)  
#Passar o timeslice
#rr.executar(10)
 
#print "Algoritmo de Escalonamento: Prioridades"  
#prioridades = escalonadores.PRIORIDADES(processos) 
#prioridades.executar() 