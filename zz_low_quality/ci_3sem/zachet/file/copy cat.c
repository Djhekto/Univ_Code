#include <stdio.h>
/* cat: конкатенация файлов, версия 1 */
main(int argc, char *argv[])
{
 FILE *fp;
 void filecopy(FILE *, FILE *);
 if (argc == 1) /* нет аргументов; копируется стандартный ввод */
 filecopy(stdin, stdout);
 else
 while (--argc > 0)
 if ((fp = fopen(*++argv, "r")) == NULL) {
 printf("cat: не могу открыть файл %s\n", *argv);
 return 1;
 } else {
 filecopy(fp, stdout);
 fclose(fp);
 }
 return 0;
}
/* filecopy: копирует файл ifp в файл ofp */
void filecopy(FILE *ifp, FILE *ofp)
{
 int c;
 while ((c = getc(ifp)) != EOF)
 putc(c, ofp);
}
