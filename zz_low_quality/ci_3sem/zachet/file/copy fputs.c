#include<stdio.h>
#include<stdlib.h>
int main()
{
char input[200];
printf("enter \n");
scanf("%[^\n]s",input);
FILE *destfile;
destfile = fopen("000.txt", "w");
 if(destfile == NULL){ printf("Error opening file\n"); exit(1);}
 while( gets(input) != EOF ) {fputs(input, destfile);}
fclose(destfile);
return 0;
}
// CLOMANO
