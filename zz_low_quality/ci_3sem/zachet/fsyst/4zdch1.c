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
char DIRp[200];
printf(" vvedite nazvanie dirrectorii bez papok (primer ./ ili D:/cici/zachet/fsyst) ");
if (fgets(DIRp, 40, stdin))
 {
  DIRp[strcspn(DIRp, "\n")] = 0;
  printf("%s\n", DIRp);
 }
dp = opendir (DIRp);
if (dp != NULL)
 {
   while (ep = readdir (dp))
   {
   long int res = refindSize(ep->d_name);
    if (res != -1) {razmer += res;}
   }
  (void) closedir (dp);
 }
else {perror ("net dirrectorii");}

printf("BEC %d",razmer);
return 0;
 }

long int refindSize(char filename[])
{
   printf("%s\n", filename);
    FILE* fp = fopen(filename, "r");
    fseek(fp, 0, SEEK_END);
      long int res = ftell(fp);
      fclose(fp);
//    memset(filename,0,sizeof(filename));  больше не нужна но вдруг пригодится потом
    return res;
}
