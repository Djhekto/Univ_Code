#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>

char* s_read (int fd, void *buf, int stroka);
int umnozc2 (char* chisl);

int main(int argc, char *argv[])
{
if(argc<2){fprintf(stderr,"ne doctatochno argumentov");}    
int fd = open(argv[1],O_RDWR,0); 
if(fd==-1){printf("fail ne otkrilsya\n"); return 1;}   
int strk = atoi(*argv);
//if ...? cto mozet slomatisya v atoi
char* temp[8];
char* chiclo = s_read(fd,temp,strk); 
int b = umnozc2 (chiclo);   
printf ("chislo v stroke %d umnoz na 2 = %d ",strk ,b);
return 0;    
}

char* s_read (int fd, void *buf, int stroka)
{ size_t amount=0; amount = stroka*8;
    char* temp = read(fd,buf+amount,buf+amount+8);
      if (temp==-1) {
    fprintf(stderr, "%s(%d) oshibka \n ",__FILE__,__LINE__); 
                    }
     
return temp;   
}

int umnozc2 (char* chisl)
{
/* mozno obrashat1sya k bykvam chisl po pravily
 chiclo*2 0->0 1->10  

   ili atoi(chisl) i umnoz 
  ne znau kakoi bydet bistree

vzyal pervi1
*/
int pere;
for (int i = 0; i < 8;i++)                            { // 
if (pere == 1) 
 {
 if      (chisl[i]=='1') {/**/}
 else if (chisl[i]=='0') {pere = 0; chisl[i]='1';}
 }
else if (pere == 0)
 {
  if      (chisl[i]=='0') {/**/}
  else if (chisl[i]=='1') {pere = 1; chisl[i]='0';} 
 }
                                                      } //
if (pere == 1) {printf("overflou");}
int a = atoi (chisl);
 return 0;  
}