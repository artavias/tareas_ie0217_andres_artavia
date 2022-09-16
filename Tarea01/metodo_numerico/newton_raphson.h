#include <cmath>
#include <stdio.h>

using namespace std;

//Se define la clase funcion para evaluar la funcion y su derivada
class funcion
{
    public:

    //El siguiente metodo de la clase retorna el valor al evaluar la funcion en un valor x
    float evaluarFuncion (float x)
    {
        return pow(x, 3) + 4*pow(x, 2) - 10;
    }

     //El siguiente metodo de la clase retorna el valor al evaluar la derivada en un valor x
    float evaluarDerivada (float x)
    {
        return pow((3*x), 2) + 8*x;
    }

    //El siguiente metodo utiliza los metodos de funcion para calcular el siguiente valor de x
    float calcular_siguiente (float x)
    {
        return x - (evaluarFuncion(x)/evaluarDerivada(x));
    }


};


class error: public funcion
{
    public:

    float calcular_error (float x)
    {
        return abs(calcular_siguiente(x) - x);
    }
};

class newton: public error
{
    public:

    float newton_raphsone(float x)
    {
        int iterador = 0;
        float error = 0;
        float x1 = x;
        float x2 = 0;
        while(true)
        {
            x2 = calcular_siguiente(x1);
            iterador++;
            error = calcular_error(x1);
            if (error == 0)
            {
                break;
            }
            x1=x2;
        }
        return x2;
    }
};
