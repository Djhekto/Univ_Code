# include <stdio.h>
int main( )
{
FILE *testfile ;
char c ;
printf( "demo of fgetc" ) ;
testfile = fopen ( "000.txt", "r" ) ;
 if ( testfile == NULL ) {printf ( "\nCould not open file test.txt" ) ;return 1;}
printf( "file is present and is being read \n" ) ;
while ( 1 ) {
 c = fgetc ( testfile ) ;
  if ( c == EOF ) break ;
 printf ( "%c", c ) ;
            }
printf("Closing the file") ;
fclose ( testfile ) ;
return 0;
}
