#include "materias.h"
#include <iomanip>
using namespace std;

//La siguiente funcion toma como paramtero el nombre de la materia y retorna una clase materia con el mismo nombre
Materia ControlNotas::crear_materia(string nombre_de_materia){
    Materia a;
    a.nombre_materia=nombre_de_materia;
    return a;
};

//La siguiente funcion inserta el nombre y la nota del estudiante en la materia y retorna la materia
Materia ControlNotas::insertar_tupla(string nombre, float nota, Materia mat){
    Record a;
    a.nombre_estudiante=nombre;
    a.nota_estudiante=nota;
    mat.estudiantes.push_back(a);
    return mat;
};

//La siguiente funcion se encarga de imrpimir todas las materias y las notas de cada estudiante de una clase Registro
void ControlNotas::imprimir(Registro reg){
    list<Materia>:: iterator ptr;

    cout<<"##\t"<<setw(15);
    for(ptr=reg.materias.begin(); ptr != reg.materias.end(); ++ptr){ 
        cout<< ptr->nombre_materia <<setw(15);
    }
    cout<<"\n";

    int x = reg.materias.size();
    int y = reg.materias.begin()->estudiantes.size();

    list<Record>:: iterator pt;
    list<Materia>:: iterator pt_m;
    list<Record>:: iterator pt_r;
    
    pt = reg.materias.begin()->estudiantes.begin();
    for(int j = 0; j < y; j++){
        advance(pt, j);
        for (int i = 0; i< x; i++)
        {
            if(i==0){
                pt_m = reg.materias.begin();
                cout<<"\n## "<<pt->nombre_estudiante<<setw(15);
                pt_r = pt_m->estudiantes.begin();
                advance(pt_r, j);
                cout<<pt_r->nota_estudiante<<setw(15);
            }
            else{
                pt_m = reg.materias.begin();
                advance(pt_m, i);
                pt_r = pt_m->estudiantes.begin();
                advance(pt_r, j);
                cout<<pt_r->nota_estudiante<<setw(15);
            }

        }
    }

    
};
