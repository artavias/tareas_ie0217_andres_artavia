#ifndef NEWTON_RAPHSON_H
#define NEWTON_RAPHSON_H

#include<stdio.h>
#include<cmath>
#include<iostream>
using namespace std;

//Se define la clase funcion para evaluar la funcion y su derivada y calcular el siguiente x mediante la formula del metodo
class evaluar
{
    public:

    float evaluarFuncion (float x);

    float evaluarDerivada (float x);

};

class siguiente
{
    public:

    float calcular_siguiente (float x);
};


class error: public evaluar
{
    public:

    float calcular_error (float x);
};

class newton: public error
{
    public:

    float newton_raphson(float x_inicial, float error_permitido);
};



#endif // NEWTON_RAPHSON_H
