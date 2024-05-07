#include <stdio.h>
#include <math.h>

#define A 0.0
#define B 31.41592653589793//pi*10

double f(double x) {  return 1.57 * (fabs(sin(x)));}//pi/2 * |sin|  ->  f(k*pi) = k*pi

int main ()
{
    int segnum = 200000000;
    int i;
    double otvet = 0.0;
    double x_l, x_r, x_mid;//точка (слева, справа, центр) на интервале
    double h = (B - A) / (double) segnum;// шаг
    {
        for (i = 0; i < segnum; i++)
        {
            x_l =   A + h * (double) i;
            x_mid = A + h * (double) (i + 0.5);
            x_r =   A + h * (double) (i + 1);
            otvet +=  h/6.0 * (f(x_l) + 4.0 * f(x_mid) + f(x_r));
        }
    }
    printf("%.20f  ~~ pi*10\n", otvet);
    return 0;
}