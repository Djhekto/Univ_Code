#include <iostream>
#include <stdio.h>
#include "include/raylib.h"
#include <math.h>

using namespace std;

#define wWidth 2000
#define wHeight 1000
#define xStart wWidth-1600
#define yStart wHeight-400

int main()
{
double x, y, shag,x_l,y_l,a,b;
//double f1;
int shagov;
double x_list[50000];
double y_list[50000];
double mashtab;
puts("--- zuli ---");
//puts("vvedite: x0, y0, shag , shagov(<5000), mashtab ");
//puts("(0; 0;  100)");
//scanf("%lf", &x); x_l = x;
//scanf("%lf", &y); y_l = y;
//scanf("%lf", &shag);
//scanf("%d", &shagov);
puts("vvedite mastab");
scanf("%lf", &mashtab);
shagov = mashtab;
shag = 1/mashtab;
puts("vvedite: a, b");
puts("0.2; -0.1");
scanf("%lf", &a);
scanf("%lf", &b);
double x_k = -1.5;
double y_k = -1.5;
long int chet=0;
int i = 0;
//
while(x_k<1.5)
{
 while (y_k<1.5)
 {
  x_l = x_k;
  y_l = y_k;
   while (i < 1000)
    {
    x = x_l*x_l - y_l*y_l + a;
    y = 2*x_l*y_l + b;
     if (x>10000) {i = 999;}
     if ( x==x_l ) {
            if (y==y_l) {
                             x_list[chet] = x_k;
                             y_list[chet] = y_k;
                             chet++; i = 999;
                        }
                   }
     x_l = x;
     y_l = y;
     i++;
    }
   y_k+= shag;
   i=0;
  }
x_k += shag;
y_k = -1.5;
//printf("%d %f ",cik,x_k);
printf("%f ",x_k);
}
/*
for (int ciko=0; ciko<chet; ciko++  )
 {
   printf(" %lf %lf \n",x_list[ciko],y_list[ciko]);
 }
*/

InitWindow(wWidth, wHeight, "zilli");
SetTargetFPS(30);
while (!WindowShouldClose())
    {
 BeginDrawing();
 ClearBackground(RAYWHITE);
DrawLine(0,yStart,wWidth,yStart,BLACK);
DrawLine(xStart,0,xStart,wHeight,BLACK);

DrawLine(0,yStart+mashtab,wWidth,yStart+mashtab,GRAY);
DrawLine(0,yStart-mashtab,wWidth,yStart-mashtab,GRAY);
DrawLine(xStart+mashtab,0,xStart+mashtab,wHeight,GRAY);
DrawLine(xStart-mashtab,0,xStart-mashtab,wHeight,GRAY);


int x1, y1;
for (int i = 1; i < chet; i++)
     {
 x1 = (int)(xStart +(mashtab * x_list[i-1]));
 y1 = (int)(yStart -(mashtab * y_list[i-1]));
// DrawText("*", x2, y2, 10, BLUE);
    DrawCircle(x1,y1,1,RED);
     }


EndDrawing();
    }
return 0;
}
