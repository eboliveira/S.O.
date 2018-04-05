#ifndef processos_H
#define processos_H
#include <iostream>
class Processo
{
private:
	int id;
	int prioridade;
	int estado;
	int Chegada;
	int *eventosES;

public:

    Processo();
    virtual ~Processo();
    int getId();
    int getPrioridade;
    int getEstado;
    int getChegada;
    int getEvento;

    void setID(int);
    void setPrioridade(int);
    void setEstado(int);
    void setChegada(int);
    int setEvento;
};

#endif // processo_H
