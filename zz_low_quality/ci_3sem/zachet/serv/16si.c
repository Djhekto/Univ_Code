#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>

#define WINT 0
#define SUM 1

int max_count=0;
int ssn=WINT;
int count_z=0;
int count_l=0;

void end_func(int sig, siginfo_t *info, void *pointer){
   printf("\nThe end %d\n", max_count);
   exit(0);
}
/*
int main () {   
   struct sigaction end_action;
   end_action.sa_sigaction=end_func;
// sigemptyset(&end_action.sa_mask);
   sigaction(SIGINT, &end_action, NULL);

   while(1){
      printf ("Hello summer %d\n", count_l);
      sleep (1);
      }
   return 0;
} */