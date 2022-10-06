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
