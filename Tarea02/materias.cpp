<<<<<<< HEAD
#include "materias.h"

using namespace std;

Materia ControlNotas::crear_materia(string nombre_de_materia){
    Materia a;
    a.nombre_materia=nombre_de_materia;
    return a;
};

Materia ControlNotas::insertar_tupla(string nombre, float nota, Materia mat){
    Record a;
    a.nombre_estudiante=nombre;
    a.nota_estudiante=nota;
    mat.estudiantes.push_back(a);
    return mat;
};

void ControlNotas::imprimir(Registro reg){
    list<Materia>:: iterator ptr;

    cout<<"##\t";
    for(ptr=reg.materias.begin(); ptr != reg.materias.end(); ++ptr){ 
        cout<< ptr->nombre_materia <<"\t";
    }
    cout<<"\n";

    list<Record>:: iterator pt;
    //pt=reg.materias.begin()->estudiantes.begin();
    for(pt=reg.materias.begin()->estudiantes.begin(); pt != reg.materias.begin()->estudiantes.end(); ++pt){
        cout<<pt->nombre_estudiante<<"\t"<<pt->nota_estudiante;
    }

    
};
=======
#include <iostream>
#include <iterator>
#include <list>

using namespace std;

int main()
{
    struct Record{
        string nombre_estudiante;
        float nota_estudiante;
    };

    class Materia{
        public:
            string nombre_materia;
            list<Record> estudiantes;
    };

    class Registro{
        public:
            list<Materia> materias;
    };

    class ControlNotas: public Record{
        public:
            Materia crear_materia(string nombre_de_materia){
                Materia a;
                a.nombre_materia=nombre_de_materia;
                return a;
            };
    
            Materia insertar_tupla(string nombre, float nota, Materia mat){
                Record a;
                a.nombre_estudiante=nombre;
                a.nota_estudiante=nota;
                mat.estudiantes.push_back(a);
                return mat;
            };
        
    };    
    return 0;
}
>>>>>>> Tarea02
