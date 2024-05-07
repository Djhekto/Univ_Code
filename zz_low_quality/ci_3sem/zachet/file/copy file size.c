// C program to find the size of file
#include <stdio.h>

long int findSize(char mfile[])
{
    // opening the file in read mode
    FILE* fp = fopen(mfile, "r");
    // checking if the file exist or not
    if (fp == NULL)  {
        printf("File Not Found!\n");
        return -1;    }
    fseek(fp, 0L, SEEK_END);
    // calculating the size of the file
    long int res = ftell(fp);
    // closing the file
    fclose(fp);
return res;
}
// Driver code
int main()
{
    char mfile[] = { "1.c" };
    long int res = findSize(mfile);
    if (res != -1)
        printf("Size of the file is %ld bytes \n", res);
    return 0;
}
