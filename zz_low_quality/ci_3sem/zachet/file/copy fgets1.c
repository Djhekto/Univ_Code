# include <stdio.h>
int main( )
{
FILE *sourcefile ;
char newdata[50] ;
printf( "Opening  file 000.txt " ) ;
sourcefile = fopen( "000.txt", "r" ) ;
 if ( sourcefile== NULL ) { printf( "Could not open file test.txt" ) ;return 1;}
printf( "Reading 000.txt \n" ) ;
while( fgets ( newdata, 50, sourcefile ) != NULL )
 printf( "%s" , newdata ) ;
fclose(sourcefile) ;
return 0;
}
