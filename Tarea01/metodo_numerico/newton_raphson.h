#ifndef NEWTON_RAPHSON_H
#define NEWTON_RAPHSON_H

#include<stdio.h>
#include<cmath>
using namespace std;

//Se define la clase funcion para evaluar la funcion y su derivada
class evaluar
{
    public:

    float evaluarFuncion (float x);

    float evaluarDerivada (float x);

};

//Se declara la clase siguiente para calcular el valor siguiente en el metodo
class siguiente: public evaluar
{
    public:

    float calcular_siguiente (float x);
};

//Se declara la clase error para calcular el error del metodo
class error: public siguiente
{
    public:

    float calcular_error (float x);
};

//Se declara la clase newton para aplicar el algoritmo del metodo
class newton: public error
{
    public:

    float newton_raphson(float x_inicial, float error_permitido);
};



#endif // NEWTON_RAPHSON_H
