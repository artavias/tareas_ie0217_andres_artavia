#include "newton_raphson.h"

using namespace std;

int main()
{
    float x = 0;
    float error = 0;
    newton a;

    printf("Ingrese el valor inicial de x y el error permitido\n");

    scanf("%f", &x);
    scanf("%f", &error);

    printf("El resultado es %f" , a.newton_raphson(x, error));

    return 0;
}



