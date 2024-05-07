/*реализуйте следующую схему порождения процессов: О->С->В1, О->С->В2 сын распечатывает свой
pid, pid отца, pid своего второго сына. Внук распечатывает свой pid, pid своего отца, pid деда и pid
своего брата. Отец распечатывает pid-ы всех внуков. Предусмотреть обработку всех возможных
ошибочных ситуаций. Разрешается использовать 1 неименованный канал и механизм сигналов.*/ 
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <fcntl.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>
 volatile int gd1 = 1,gd2 = 1;
void handler_gd1 ( int sig ) { gd1 = 0; };
void handler_gd2 ( int sig ) { gd2 = 0; };

int main(int argc, char const *argv[])
{
 int pfd[2];
 int i = 0, e = 0;
  if (pipe(pfd)){ printf("Ошибка pipe\n"); exit(1);}

int gdson1 = 0, gdson2 = 0, son = 0;
son = fork();  //------------------- son
  if (son < 0 ) { printf("oshibka fork pri sozdanii son \n"); exit(1);}
  else 
   if (son == 0) 
    {// son norm => poluchaem pid
   int grandpa = getppid();
      if (grandpa < 0) { printf("Дед пропал \n"); exit(1);} 
gdson1 = fork(); // B1
       if (gdson1 < 0) {printf("oshibka fork pri sozdanii 1 vnyk\n"); kill( grandpa, SIGKILL); exit(1);}
       else 
        if (gdson1 == 0)
        { //жду отца и брата 
	   signal (SIGTSTP, handler_gd1);
	   close(pfd[1]);
	              //printf(" Жду брата \n ");
          son = getppid(); 
       	 if (son < 0 ) 
       	  {printf("Отец пропал \n"); kill( gdson1 , SIGKILL); exit(1);}
		
        e = read(pfd[0], &gdson2, sizeof(gdson2)); 			// читаю pid брата
		if ( e != sizeof(gdson2)) { printf("Ошибка чтения канала\n"); return 0; }
		printf("%d %d %d %d\n",getpid(),son,grandpa, gdson2);
		close(pfd[0]);
		return 0; 
		}
gdson2 = fork();
    if (gdson2 < 0) {printf("Ошибка fork сын 2-ой внук \n"); kill( getppid() , SIGKILL); kill( gdson1 , SIGKILL); exit(1);}
	else if (gdson2 == 0){ //2-ой сын , а это его дед grandpa  // pid, pid своего отца, pid деда и pid своего брата
		signal (SIGTSTP, handler_gd1);
		son = getppid(); 
		if (son < 0 ) {printf("Отец пропал \n"); kill( gdson1 , SIGKILL); exit(1);}
//жду отца
		close(pfd[1]);
		close(pfd[0]);
		sleep(3);
// printf("Я сын 2 \n");
			printf("%d %d %d %d\n",getpid(),son,grandpa, gdson1);		
		// читаю pid брата 
		// печатаю
		// закрываю пайп  
			return 0; 
		}
        //printf("Отец, жду детей \n");
	printf("%d %d %d\n",getpid(),grandpa,gdson2);
	//kill (gdson2,SIGTSTP);
	// жду 2-го сына 
	waitpid(gdson2,&i,0);
	close(pfd[0]);
	    e = write(pfd[1], &gdson2, sizeof(gdson2));
        if (e != sizeof(gdson2)) { printf("Ошибка \n"); exit(1);}
	waitpid(gdson1,&i,0);	// жду 1-го сына 
	    e = write(pfd[1], &gdson1, sizeof(gdson1));
		if (e != sizeof(gdson1)) { printf("Ошибка \n"); exit(1);}
	    
        e = write(pfd[1], &gdson2, sizeof(gdson2));
		if (e != sizeof(gdson2)) { printf("Ошибка \n"); exit(1);}
	close (pfd[1]);
	return 0;
	}
//printf("Жду сына \n");
waitpid(son,&i,0);
close(pfd[1]);
	
e = read(pfd[0], &gdson1, sizeof(gdson1));
if ( e != sizeof(gdson1)) { printf("Ошибка чтения канала\n"); return 0; }

e = read(pfd[0], &gdson2, sizeof(gdson2));
if ( e != sizeof(gdson2)) { printf("Ошибка чтения канала\n"); return 0; }

 printf("%d %d \n",gdson1,gdson2);
 close(pfd[2]);
return 0;
}
