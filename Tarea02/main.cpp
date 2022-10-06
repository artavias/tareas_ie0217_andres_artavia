#include "materias.h"
#include "materias.cpp"
#include <vector>

using namespace std;

int main(){
    ControlNotas a;
    Registro b;

    Materia Matematicas = a.crear_materia("Matematicas");
    Materia Ciencias = a.crear_materia("Ciencias");
    Materia Espanol = a.crear_materia("Espanol");
    Materia Historia = a.crear_materia("Historia");
    Materia EdFisica = a.crear_materia("EdFisica");

    int x = 0;
    vector<string> nombres;
    cout<<"Ingrese la cantidad de estudiantes: ";
    scanf("%d", &x);

    for(int i=0; i < x; i++){
        string nombre="";
        cout<<"Ingrese el nombre de la persona "<<i+1<<": "<<endl;
        cin>>nombre;
        nombres.push_back(nombre);
    };


    vector<string>:: iterator k;

    
    for(k = nombres.begin(); k != nombres.end(); ++k){
            float nota_m=0;
            cout<<"Ingrese la nota de "<<*k<<" en Matematicas: "<<"\n"<<endl;
            cin>>nota_m;
            Matematicas = a.insertar_tupla(*k, nota_m, Matematicas);

            float nota_c=0;
            cout<<"Ingrese la nota de "<<*k<<" en Ciencias: "<<"\n"<<endl;
            cin>>nota_c;
            Ciencias = a.insertar_tupla(*k, nota_c, Ciencias);

            float nota_e=0;
            cout<<"Ingrese la nota de "<<*k<<" en Espanol: "<<"\n"<<endl;
            cin>>nota_e;
            Espanol = a.insertar_tupla(*k, nota_e, Espanol);

            float nota_h=0;
            cout<<"Ingrese la nota de "<<*k<<" en Historia: "<<"\n"<<endl;
            cin>>nota_h;
            Historia = a.insertar_tupla(*k, nota_h, Historia);

            float nota_ed=0;
            cout<<"Ingrese la nota de "<<*k<<" en EdFisica: "<<"\n"<<endl;
            cin>>nota_ed;
            EdFisica = a.insertar_tupla(*k, nota_ed, EdFisica);
    };

    b.materias.push_back(Matematicas);
    b.materias.push_back(Ciencias);
    b.materias.push_back(Espanol);
    b.materias.push_back(Historia);
    b.materias.push_back(EdFisica);

    a.imprimir(b);

    return 0;
};