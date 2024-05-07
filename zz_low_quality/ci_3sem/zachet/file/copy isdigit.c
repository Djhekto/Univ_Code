#include <stdio.h>
#include <ctype.h>

int main ()
{

    // Use the isdigit() function to check the character is digit or not. */
    if (isdigit ( 'P' ) == 0)  //check 'P' is digit
    {
        printf (" \n The given character 'P' is not digit'. ");
    }
    else
    {
        printf ("\n The given character 'P' is a digit. ");
    }


    if (isdigit ( '3' ) == 0)  //check for '3'
    {
        printf (" \n The given character '3' is not digit'. ");
    }
    else
    {
        printf ("\n The given character '3' is a digit. ");
    }


    if (isdigit ( '!' ) == 0)  //check for '!' character
    {
        printf (" \n The given character '!' is not digit'. ");
    }
    else
    {
        printf ("\n The given character '!' is a digit. ");
    }


    if (isdigit ( '$4' ) == 0)  //check for '44'
    {
        printf (" \n The given character '$4' is not digit'. ");
    }
    else
    {
        printf ("\n The given character '$4' is a digit. ");
    }


    if (isdigit ( '0' ) == 0)  //check for '0'
    {
        printf (" \n The given character '0' is not a digit. ");
    }
    else
    {
        printf ("\n The given character '0' is a digit. ");
    }

    return 0;
}
