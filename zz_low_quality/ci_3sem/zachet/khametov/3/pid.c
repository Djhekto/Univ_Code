#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <fcntl.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>
// volatile int gd1 = 1,gd2 = 1;
void h_gd1 ( int sig ) {  };
void h_gd2 ( int sig ) {  };

int main(int argc, char const *argv[])
{
 int pfd[2];
 int i = 0, a = 0;
  if (pipe(pfd)){ printf("oshibka pipe\n"); exit(1);}

int vnuk1 = 0, vnuk2 = 0, sbln = 0;
sbln = fork();  //------------------- sbln
  if (sbln < 0 ) { printf("oshibka fork pri sozdanii sblna \n"); exit(1);}
  else 
   if (sbln == 0) 
    {// sbln norm => poluchaem pid
   int ded = getppid();
      if (ded < 0) { printf("ded propal \n"); exit(1);} 
vnuk1 = fork(); // B1
       if (vnuk1 < 0) {printf("oshibka fork pri sozdanii 1 vnyk\n"); kill( ded, SIGKILL); exit(1);}
       else 
        if (vnuk1 == 0)
        { 
	   signal (SIGTSTP, h_gd1);
	   close(pfd[1]);
          sbln = getppid(); 
       	 if (sbln < 0 ) 
       	  {printf("otec propal \n"); kill( vnuk1 , SIGKILL); exit(1);}
		
        a = read(pfd[0], &vnuk2, sizeof(vnuk2)); 		
		if (    a != sizeof(vnuk2)) { printf("oshibka chtenia pipe\n"); return 0; }
		printf("B1 %d O %d D %d V2 %d\n",getpid(),sbln,ded, vnuk2);
		close(pfd[0]);
		return 0; 
		}
vnuk2 = fork();
    if (vnuk2 < 0) {printf("oshibka fork  B2 \n"); kill( getppid() , SIGKILL); kill( vnuk1 , SIGKILL); exit(1);}
	else if (vnuk2 == 0){ 
		signal (SIGTSTP, h_gd1);
		sbln = getppid(); 
		if (sbln < 0 ) {printf("otec  propal \n"); kill( vnuk1 , SIGKILL); exit(1);}
		close(pfd[1]);
		close(pfd[0]);
		sleep(3);
			printf("B2 %d O %d D %d B1 %d\n",getpid(),sbln,ded, vnuk1);		  
			return 0; 
		}
	printf("O %d D %d B2 %d\n",getpid(),ded,vnuk2);
	waitpid(vnuk2,&i,0);
	close(pfd[0]);
	    a = write(pfd[1], &vnuk2, sizeof(vnuk2));
        if (a != sizeof(vnuk2)) { printf("oshibka \n"); exit(1);}
	waitpid(vnuk1,&i,0); 
	    a = write(pfd[1], &vnuk1, sizeof(vnuk1));
		if (a != sizeof(vnuk1)) { printf("oshibka \n"); exit(1);}
	    
        a = write(pfd[1], &vnuk2, sizeof(vnuk2));
		if (a != sizeof(vnuk2)) { printf("oshibka \n"); exit(1);}
	close (pfd[1]);
	return 0;
	}
waitpid(sbln,&i,0);
close(pfd[1]);
	
a = read(pfd[0], &vnuk1, sizeof(vnuk1));
if ( a != sizeof(vnuk1)) { printf("oshibka chtenia kanala\n"); return 0; }

a = read(pfd[0], &vnuk2, sizeof(vnuk2));
if ( a != sizeof(vnuk2)) { printf("oshibka chtenia kanala\n"); return 0; }

 printf("B1 %d B2 %d \n",vnuk1,vnuk2);
 close(pfd[2]);
return 0;
}
