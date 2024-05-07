#include <iostream>
#include <stdio.h>
#include "include/raylib.h"
#include <math.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

#define wWidth 2000
#define wHeight 1000
#define xStart wWidth-1400
#define yStart wHeight-400

int main()
{
double x_list[50000]; //otobraz
double y_list[50000];
double x_list_p[1000]; //kuda popalo
double y_list_p[1000];
double a,b,temp;  //param
double mashtab;
int nomer=0;     //nomer yacheiky
puts("--- cepno-rek ---");
/*
puts("vvedite: x0, y0 ");
puts("(0.1; 0.1;  100)");
scanf("%lf", &x_list[0]);
scanf("%lf", &y_list[0]);
*/
x_list[0]=0.9; y_list[0]=-0.5; /**/
//puts("vvedite mastab");
//scanf("%lf", &mashtab);
puts("vvedite: a, b");
puts("0.3  0.2");
scanf("%lf", &a);
scanf("%lf", &b);
//printf("%lf",x_list[0]);
double ya_dlin, xniz, yniz, xvv, yvv;
puts("dlinna yacheiki");
scanf("%lf", &ya_dlin);
/*
puts("koordinati niznego ugla");
puts("1.5 1.5");
scanf("%lf", &xniz);
scanf("%lf", &yniz);
puts("koordinati verhnego ugla");
puts("1.5 1.5");
scanf("%lf", &xvv);
scanf("%lf", &yvv);
if (xvv<xniz) {return 1;}
if (yvv<yniz) {return 1;}
//подгон размера xvv yvv
double temp1, temp2;
while(temp1<xvv)
  {
  temp1+=ya_dlin;
  }
while(temp2<yvv)
  {
  temp2+=ya_dlin;
  }
xvv=temp1; yvv=temp2;
*/
yniz=xniz=-1.5;
xvv=yvv=1.5;
int nomertemp;
double tempx,tempy;
tempx = xniz;
tempy = yvv;
srand (time(NULL));
int chet = 1;
//
while (tempy > yniz)
{
  while (tempx < xvv)
    {
for (int i = 0; i <= 100; i++) //цикл рандома
  {
x_list [i] = rand() % 500;
x_list [i] = tempx + x_list[i]/1000;
y_list [i] = rand() % 500;
y_list [i] = tempy - y_list[i]/1000;
//printf("%lf  %lf\n",x_list[i],y_list[i]);

  }
for (int i = 0; i <= 100; i++) //цикл отображ
  {
y_list[i] =  2*x_list[i]*y_list[i] + b;
x_list[i] = x_list[i]*x_list[i] - y_list[i]*y_list[i] + a;
  }
for (int i = 1; i <= 100; i++) //цикл номеров
  {
nomer = (int)(  floor((  fabs(1.5 - y_list[i])  /ya_dlin))  *6
              + (floor(abs(-1.5-x_list[i])/ya_dlin)+1))  ;
if (x_list[i]< -1.5 || x_list[i]>1.5) {}
 else {
        if (y_list[i]< -1.5 || y_list[i]>1.5) {}
    else {
if (y_list[i] == yniz)   {nomer-=(abs(xvv-xniz)/ya_dlin);}
if (nomer != nomertemp)    { printf("%d -> %d  |",chet,nomer);}
                               // printf("%lf  %lf\n",x_list[i],y_list[i]); }
nomertemp = nomer;
        }  }
  }

    tempx += ya_dlin;
    chet++;
   }
  tempy-=ya_dlin;
  tempx =xniz;
}
//

//
return 0;
}
