#include <iostream>
#include <stdio.h>
#include "include/raylib.h"
#include <math.h>

using namespace std;

#define wWidth 2000
#define wHeight 1000
#define xStart wWidth-1400
#define yStart wHeight-400

int main()
{
double x, y, x_l,y_l,a,b;

int shagov;
double x_list[50000];
double y_list[50000];
double mashtab;
puts("--- atr xenona ---");
puts("vvedite: x0, y0, tochek ");
puts("(0.1; 0.1;  1000)");
scanf("%lf", &x); x_l = x;
scanf("%lf", &y); y_l = y;
scanf("%d", &shagov);
puts("vvedite mastab");
scanf("%lf", &mashtab);
puts("vvedite: a, b");
puts("1.4  0.3");
scanf("%lf", &a);
scanf("%lf", &b);
//
for (int i = 0; i < shagov; i++) {

y=b*x_l;
x=1+y_l-a*pow(x,2);
 //  printf("%d: %lf %lf \n",i+1,y,x);
x_list[i]=x_l;
y_list[i]=y_l;
x_l=x;
y_l=y;

                                  }
//
InitWindow(wWidth, wHeight, "zilli");
SetTargetFPS(30);
while (!WindowShouldClose())
    {
 BeginDrawing();
 ClearBackground(RAYWHITE);
DrawLine(0,yStart,wWidth,yStart,BLACK);
DrawLine(xStart,0,xStart,wHeight,BLACK);
/*
DrawLine(0,yStart+mashtab,wWidth,yStart+mashtab,GRAY);
DrawLine(0,yStart-mashtab,wWidth,yStart-mashtab,GRAY);
DrawLine(xStart+mashtab,0,xStart+mashtab,wHeight,GRAY);
DrawLine(xStart-mashtab,0,xStart-mashtab,wHeight,GRAY);
*/

int x1, y1;
for (int i = 1; i < shagov; i++)
     {
 x1 = (int)(xStart +(mashtab * x_list[i-1]));
 y1 = (int)(yStart -(mashtab * y_list[i-1]));
// DrawText("*", x2, y2, 10, BLUE);
    DrawCircle(x1,y1,3,RED);
     }


EndDrawing();
    }


    return 0;
}
