#ifndef MATERIAS_H
#define MATERIAS_H

#include <iostream>
#include <iterator>
#include <list>
#include <algorithm>

using namespace std;

struct Record{
    string nombre_estudiante;
    float nota_estudiante;
};

class Materia{
    public:
        string nombre_materia;
        list<Record> estudiantes;
};

class Registro: public Materia{
    public:
        list<Materia> materias;
};


class ControlNotas: public Registro{
    public:

        Materia crear_materia(string nombre_de_materia);

        Materia insertar_tupla(string nombre, float nota, Materia mat);

        void imprimir(Registro reg);
};


#endif // MATERIAS_H
