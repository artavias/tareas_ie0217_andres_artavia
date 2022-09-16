#include <iostream>
#include <cmath>

using namespace std;

//Se define la clase funcion para evaluar la funcion y su derivada
class funcion
{
public:

    //El siguiente metodo de la clase retorna el valor al evaluar la funcion en un valor x
    float resolverEcuacion (float x)
    {
        return pow(x, 3) + 3*pow(x, 2) - 8*x + 12;
    }

     //El siguiente metodo de la clase retorna el valor al evaluar la derivada en un valor x
    float resolverDerivada ( float x)
    {
        return 3*pow(x, 2) + 6*x - 8;
    }
};

int main()
{
    funcion f;
    float a = f.resolverEcuacion(4);
    float b = f.resolverDerivada(4);

    cout<<a<<'\n'<<b<<endl;

    return 0;
}


