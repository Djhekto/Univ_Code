#include <stdio.h>
#include <stdlib.h>

int main()
{
FILE *fap;
fap  = fopen ("chisla.txt", "w");
        int i;
        char fn[50];
        char str[] = "https://bit.ly/3kGX1Ne\n";
        fap = fopen("chisla.txt", "w");
        for (i = 0; str[i] != '\n'; i++)
        {
            fputc(str[i], fap);
        }

fclose (fap);

   char ch, file_name[25];
   FILE *fp;

   printf("Enter name of a file you wish to see\n");
   gets(file_name);

   fp = fopen(file_name, "r"); // read mode

   if (fp == NULL)
   {
      perror("Error while opening the file.\n");
      exit(EXIT_FAILURE);
   }

   printf("The contents of %s file are:\n", file_name);

   while((ch = fgetc(fp)) != EOF)
      printf("%c", ch);

   fclose(fp);
return 0;
}
