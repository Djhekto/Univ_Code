#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <dirent.h>
//
long int refindSize(char filename[]);
int main ()
 {

DIR *dp;
struct dirent *ep;
long int razmer = 0;
int i;
char DIRp[200];
//
printf("введите имя каталога (пример D:/ или ./) ");
    if (fgets(DIRp, 40, stdin))
    {
        DIRp[strcspn(DIRp, "\n")] = 0;
        printf("%s\n", DIRp);
    }
dp = opendir (DIRp);
//
if (dp != NULL)
 {
   while (ep = readdir (dp))
   {
//   printf("\n"); puts (ep->d_name);   //ВРЕМЕННАЯ СТРОКА
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

// чекаю работу фопен
    char filename1[200];
    scanf("\n%s", filename1);
printf("%s\n",filename1);
    FILE* fp = fopen(filename1, "r");
   if (fp == NULL) {printf("1");}


return 0;
 }

long int refindSize(char filename[])
{
    char filename1[200];
    int i = 0;
    filename1 [0] = '.'; filename1 [1] = '/';
    while (filename[i] !='\0') {
   // printf("1");
    filename1 [i+2] = (char)filename [i];
  //      printf("ВЕРНО:%c\n", filename1[i]);
    i++;
        } filename1[i+2]='\0';
   printf("%s\n", filename);  // ВРЕМЕННАЯ СТРОКА
    printf("%s\n", filename1);  // ВРЕМЕННАЯ СТРОКА
    FILE* fp = fopen(filename1, "r");
    fseek(fp, 0, SEEK_END);
      long int res = ftell(fp);
      fclose(fp);
//    memset(filename1,0,sizeof(filename1));  больше не нужна но вдруг пригодится потом
    return res;
}
