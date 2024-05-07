/* ch05-catdir.с - Демонстрация opendir(), readdir(), closedir(). */
#include <stdio.h> /* для printf() и т.д. */
#include <errno.h> /* для errno */
#include <sys/types.h> /* для системных типов */
#include <dirent.h> /* для функций каталога */
char *myname;
int process(char *dir);
/* main --- перечисление аргументов каталога */
int main(int argc, char **argv)
{
int i;
int errs = 0;
myname = argv[0];
if (argc == 1)
errs = process("."); /* по умолчанию текущий каталог */
else
for (i = 1; i < argc; i++)
errs += process(argv[i]);
return (errs != 0);
}
int process(char *dir)
/*
process --- сделать что-то с каталогом, в данном случае,
вывести пары индекс/имя в стандартный вывод.
Возвращает 0, если все OK, иначе 1.
*/
{
DIR *dp;
struct dirent *ent;
if ((dp = opendir(dir)) == NULL) {
fprintf(stderr, "%s: %s: cannot open for reading: %s ",
myname, dir, strerror(errno));
return 1;
}
 errno = 0;
while ((ent = readdir(dp)) != NULL)
printf("%8ld %s ", ent->d_ino, ent->d_name);
if (errno != 0) {
fprintf(stderr, "%s: %s: reading directory entries: %s ",
myname, dir, strerror(errno));
return 1;
}
if (closedir(dp) != 0) {
fprintf(stderr, "%s: %s: closedir: %s ",
myname, dir, strerror(errno));
return 1;
}
return 0;
}
