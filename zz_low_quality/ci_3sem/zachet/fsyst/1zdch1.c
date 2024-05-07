#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <dirent.h>
//
long int refindSize(char* file[]);
int main (void)
 {
system("chcp 1251");
system("cls");
DIR *dp;
struct dirent *ep;
long int razmer = 0;
int i;
char DIRp[200];
//
printf("введите имя каталога (пример D:/) ");
    if (fgets(DIRp, 40, stdin))
    {
        DIRp[strcspn(DIRp, "\n")] = 0;
        printf("%39s\n", DIRp);
    }
dp = opendir (DIRp);
//
if (dp != NULL)
 {
   while (ep = readdir (dp))
   {
   puts (ep->d_name);   //ВРЕМЕННАЯ СТРОКА
   long int res = refindSize(ep->d_name);
 if (res != -1) {razmer += res; printf("AAAAAAAAAAAAAAAAAAAAAAAA");}
   }
   (void) closedir (dp);
 }
else
 {perror ("нет такой дирректории");}
//

//
printf("ВЕС %d",razmer);
return 0;
 }

long int refindSize(char* filename[])  //ПО УКАЗАТЕЛЮ ХОЧУ ПОПАСТЬ НА НАЗВАНИЕ НО ВОЗВРАЩАЕТ НЕ ТОЛЬКО НАЗВАНИЕ
{
int pop = strlen(filename); // временно
    printf("ВЕРНУЛО: %39s  %d \n", filename, pop);  // ВРЕМЕННАЯ СТРОКА
    FILE* fp = fopen(filename, "r");
    fseek(fp, 0L, SEEK_END);
      long int res = ftell(fp);
      fclose(fp);
    return res;
}
