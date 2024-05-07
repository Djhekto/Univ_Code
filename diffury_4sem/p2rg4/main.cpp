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
double x, y, x_l, y_l, shag;
//double f1;
int shagov;
double t=0;
double x_list[5001];
double y_list[5001];
double mashtab;
double k1,k2,k3,k4;
puts("---  rk4  ---");
puts("vvedite: x0, y0, shag , shagov(<5000), mashtab ");
puts("(-0.1; 0.1; 0.01; 2000; 300)");
scanf("%lf", &x); x_l = x;
scanf("%lf", &y); y_l = y;
scanf("%lf", &shag);   double shag2 = shag/2;
scanf("%d", &shagov);
scanf("%lf", &mashtab);
double w, delta, gamma;
puts("vvedite: w, delta, gamma (1; 0.25; 0.3) ");
scanf("%lf", &w);
scanf("%lf", &delta);
scanf("%lf", &gamma);
double t_w;
//
for (int i = 0; i <= shagov; i++) {
    x_list[i] = x;
    y_list[i] = y;
    t+=shag;
    t_w = t*w;
 k1 = x_l - (pow(x_l,3)) - (delta*y_l) + (gamma * cos(t_w));
 k2 = x_l+shag2 - (pow((x_l+shag2),3)) - (delta*y_l+shag2*k1) + (gamma * cos(t_w));
 k3 = x_l+shag2 - (pow((x_l+shag2),3)) - (delta*y_l+shag2*k2) + (gamma * cos(t_w));
 k4 = x_l+shag - (pow((x_l+shag),3)) - (delta*y_l+shag*k3) + (gamma * cos(t_w));
/**/ y = y_l + (shag * (k1+2*k2+2*k3+k4)/6);
 k1 = y_l;
 k2 = y_l + shag2*k1;
 k3 = y_l + shag2*k2;
 k4 = y_l + shag*k3;
/**/ x = x_l + (shag * (k1+2*k2+2*k3+k4)/6);
    y_l = y;
    x_l = x;
//   printf("%d: %lf %lf \n",i+1,y,x);
                                  }
//
InitWindow(wWidth, wHeight, "runge kutt");
SetTargetFPS(30);
while (!WindowShouldClose())
    {
 BeginDrawing();
 ClearBackground(RAYWHITE);
DrawLine(0,yStart,wWidth,yStart,BLACK);
DrawLine(xStart,0,xStart,wHeight,BLACK);

int x1, x2, y1, y2;
for (int i = 1; i <= shagov; i++)
     {
 x1 = (int)(xStart +(mashtab * x_list[i-1]));
 x2 = (int)(xStart +(mashtab * x_list[i]));
 y1 = (int)(yStart -(mashtab * y_list[i-1]));
 y2 = (int)(yStart -(mashtab * y_list[i]));
// DrawText("*", x2, y2, 10, BLUE);
    DrawLine(x1,y1,x2,y2,RED);
     }


EndDrawing();
    }
//
CloseWindow();
return 0;
 }
