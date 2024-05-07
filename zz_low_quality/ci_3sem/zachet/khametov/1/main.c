#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <fcntl.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>
 volatile int gd1 = 1;
void h_gd1 ( int sig ) { gd1 = 0; };

int main(int argc, char const *argv[])
{
int pfd[2];
int i = 0, a = 0;
char imya[200]="0";
if(argc < 2){printf("ne vveli imya\n");}
if (pipe(pfd)){ printf("oshibka pipe\n"); exit(1);}

int sbln = 0;
sbln = fork();  //------------------- sbln
  if (sbln < 0 ) { printf("oshibka fork pri sozdanii sblna \n"); exit(1);}
  else 
   if (sbln == 0)
   {
/*
*2-х родственных процессов. Первый процесс читает файл
*imya файла передаётся в параметрах функции main каждую чётную строку этого файла передаёт через не
*именованный канал второму процессу (запрещается файл сохранять в оперативной памяти), этот
*процесс запускает программу grep
*/       
strcpy ( imya, argv);
for (int i = 0; i < argc; i++) { printf("imya = %s\n", imya[i]);}
FILE* fp = fopen(imya, "r");
if(fp == NULL){ printf("net faila\n", argv[1]);}
fgets(pfd,100,fp);

// тут как-то надо запустить grep.exe еще и сигнал ему потом подать на закрытие 
// fseek что-бы разные строки отправлять в grep

   }
fclose(fp);
close(pfd[1])
return 0;
}
