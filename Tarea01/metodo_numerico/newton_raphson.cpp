#include "newton_raphson.h"

using namespace std;




//El siguiente metodo de la clase retorna el valor al evaluar la funcion en un valor x
float evaluar::evaluarFuncion (float x)
{
    return pow(x, 3) + 4*pow(x, 2) - 10;
}

//El siguiente metodo de la clase retorna el valor al evaluar la derivada en un valor x
float evaluar::evaluarDerivada (float x)
{
    return pow((3*x), 2) + 8*x;
}

//El siguiente metodo utiliza los metodos de funcion para calcular el siguiente valor de x
float evaluar::calcular_siguiente (float x)
{
    return x - (evaluarFuncion(x)/evaluarDerivada(x));
}






float error::calcular_error (float x)
{
    return abs(calcular_siguiente(x) - x);
}



float newton::newton_raphson(float x_inicial, float error_permitido)
{
    int iterador = 0;
    float error = 0;
    float x1 = x_inicial;
    float x_siguiente = 0;
    while(true)
    {
        x_siguiente = calcular_siguiente(x1);
        iterador++;
        error = calcular_error(x1);
        x1=x_siguiente;
        printf("Iteracion: %i  Resultado: %f\n" ,iterador, x1);
        if (error <= error_permitido)
        {
            break;
        }

    }
    return x1;
}




