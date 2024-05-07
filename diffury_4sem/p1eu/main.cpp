#include <iostream>
#include "include/raylib.h"
#include <math.h>
#include <stdio.h>

using namespace std;

#define wWidth 2000
#define wHeight 1000
#define xStart wWidth-1400
#define yStart wHeight-400


using namespace std;

int main()
{
double x, y, x_l, y_l, shag;
int shagov;
double t=0;
double x_list[5001];
double y_list[5001];
double mashtab;
puts("--- euler ---");
puts("vvedite: x0, y0, shag , shagov(<5000), mashtab ");
puts("(-0.1; 0.1; 0.01; 2000; 300)");
scanf("%lf", &x);
scanf("%lf", &y);
scanf("%lf", &shag);
scanf("%d", &shagov);
scanf("%lf", &mashtab);

double w, delta, gamma;
puts("vvedite: w, delta, gamma (1; 0.25; 0.3) ");
scanf("%lf", &w);
scanf("%lf", &delta);
scanf("%lf", &gamma);

x_l = x_list[0] = x;
y_l = y_list[0] = y;
double t_w;
//
for (int i = 0; i < shagov; i++) {
     t+=shag;
     t_w = t*w;
     y += shag * (x_l - (pow(x_l,3)) - (delta*y_l) + (gamma * cos(t_w)));
     x += shag * y_l;
     x_l = x_list[i+1] = x;
     y_l = y_list[i+1] = y;
//     printf("%d: %lf %lf \n",i+1,y,x);

                                  }
//

InitWindow(wWidth, wHeight, "euler v2");
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
