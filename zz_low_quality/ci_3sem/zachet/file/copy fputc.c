#include <stdio.h>
int main()
 {
char ch;
FILE *source;
FILE *destination;
if (source = fopen("000.txt", "r"))
 { ch = getc(source); destination = fopen("001.txt", "w+");
while (ch != EOF)
 { fputc(ch, destination); ch = getc(source); }
fclose(source);
fclose(destination);
return 0;
 }
return 1;
 }
