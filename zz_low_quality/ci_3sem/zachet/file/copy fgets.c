#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int main(void)
{
long a;
char buf[1024]; // use 1KiB just to be sure
int success; // flag for successful conversion

do
{
printf("enter a number: ");
if (!fgets(buf, 1024, stdin))
{
// reading input failed:
return 1;
}

// have some input, convert it to integer:
char *endptr;

errno = 0; // reset error number
a = strtol(buf, &endptr, 10);
if (errno == ERANGE)
{
printf("Sorry, this number is too small or too large.\n");
success = 0;
}
else if (endptr == buf)
{
// no character was read
success = 0;
}
else if (*endptr && *endptr != '\n')
{
// *endptr is neither end of string nor newline,
// so we didn't convert the *whole* input
success = 0;
}
else
{
success = 1;
}
} while (!success); // repeat until we got a valid number

printf("You entered %ld.\n", a);
}
