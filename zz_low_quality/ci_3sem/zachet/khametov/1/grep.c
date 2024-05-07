#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{ 
int ahah=0,aha = 0;
char temp[100]="00";  
if(argc < 2) {printf("net stroki\n"); return 0;}
//while(1) {  должно постоянно работать вроде а потом получить сигнал на kill сынф  

/*
*grep, которая на стандартный поток ввода получает строки из канала и
*распечатывает те строки, в которых содержится подстрока '/etc'.        
*/
strcpy ( temp, argv);
for (int i = 3; i < argc;i++)
 {
 if (temp[i-3]=='/')
  {if (temp[i-2]=='e')
   {if (temp[i-1]=='t')
     if (temp[i]=='c') {aha=1;}
     
}}
 else {break;}  
 }
 
if (aha=1) {for (int i = 0; i<=sizeof(temp);i++)
    {printf("%c", temp[i]);} printf("\n");
           }

memset(temp, '0', sizeof(temp)); //чтобы новые строки от сына читать без ошибок
aha = 0; //в цикле бы имело смысл
    
    

//} конец несуществующего цикла 
return 0;
}