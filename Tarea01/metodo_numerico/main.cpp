#include "newton_raphson.h"

using namespace std;


int main()
{
    //Se inicializan las variables
    float x = 0;
    float error = 0;
    newton a;

    printf("Este programa se encarga de calcular una aproximación a una raiz de la función x^3 + 4x^2 - 8\n");

    //Se escanean los datos que el usuario introduce y se asignan a las variables correspondientes
    printf("Ingrese el valor inicial de x y el error permitido\n");
    scanf("%f", &x);
    scanf("%f", &error);

    //Se imprime el resultado del metodo numerico
    printf("El resultado es %f" , a.newton_raphson(x, error));

    return 0;
}



