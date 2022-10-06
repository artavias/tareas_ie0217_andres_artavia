#ifndef MATERIAS_H
#define MATERIAS_H

#include <iostream>
#include <iterator>
#include <list>
#include <algorithm>

using namespace std;

//Declaracion del struct record
struct Record{
    string nombre_estudiante;
    float nota_estudiante;
};

//Declaracion de la clase Materia que contiene una lista del struct Record
class Materia{
    public:
        string nombre_materia;
        list<Record> estudiantes;
};

//Declaracion de Registro que contiene una lista de la clase Materia
class Registro: public Materia{
    public:
        list<Materia> materias;
};

//Declaracion de la clase control notas
class ControlNotas: public Registro{
    public:

        Materia crear_materia(string nombre_de_materia);

        Materia insertar_tupla(string nombre, float nota, Materia mat);

        void imprimir(Registro reg);
};


#endif // MATERIAS_H
