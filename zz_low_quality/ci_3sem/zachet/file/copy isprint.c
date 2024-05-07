#include <stdio.h>
#include <conio.h>
#include <ctype.h>
int main ()
{
    // declaration of the character type variables
    int ch1 = 'b';
    int ch2 = '@';
    int ch3 = ' ';
    int ch4 = '%';
    int ch5 = '\n';
    int ch6 = '\t';

    /* use isprint () function to check the printable character. */
    if ( isprint (ch1) )
    {
        printf (" '%c' is a printable character. \n", ch1);
    }
    else
    {
        printf ("'%c' is not a printable character. \n", ch1);
    }


    if ( isprint (ch2) )
    {
        printf (" '%c' is a printable character. \n", ch2);
    }
    else
    {
        printf ("'%c' is not a printable character. \n", ch2);
    }


    if ( isprint (ch3) )
    {
        printf (" '%c' is a printable character. \n", ch3);
    }
    else
    {
        printf ("'%c' is not a printable character. \n", ch3);
    }


    if ( isprint (ch4) )
    {
        printf (" '%c' is a printable character. \n", ch4);
    }
    else
    {
        printf ("'%c' is not a printable character. \n", ch4);
    }

    if ( isprint (ch5) )
    {
        printf (" '%c' is a printable character. \n", ch5);
    }
    else
    {
        printf ("'%c' is not a printable character. \n", ch5);
    }

    if ( isprint (ch6) )
    {
        printf (" '%c' is a printable character. \n", ch6);
    }
    else
    {
        printf ("'%c' is not a printable character. \n", ch6);
    }

    return 0;
}
