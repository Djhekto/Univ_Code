#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <time.h>

#define strok 4

int main(int argc, char *argv[])
{
	int listenfd = 0, connfd = 0;
	struct sockaddr_in serv_addr;
	char sendBuff[1025];
	time_t ticks;
	listenfd = socket(AF_INET, SOCK_STREAM, 0);
	memset(&serv_addr, '0', sizeof(serv_addr));
	memset(sendBuff, '0', sizeof(sendBuff));
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
	serv_addr.sin_port = htons(5000);
	bind(listenfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
	listen(listenfd, 10);

	while(1)
	{
		connfd = accept(listenfd, (struct sockaddr*)NULL, NULL);
		ticks = time(NULL);
//

char* imya ="key.txt"; //файл известен и кол-во строк в нем  (хотя в таком случае я и имена заранее знаю поэтому двойной цикл снизу получится бессмысленный (так как тогда вместе с именами я знаю их строки), если получится)
FILE* fp = fopen(imya, "r");
  //ichem формат: «имя_клиента:ключ1\n»
    
char temp[200]="0";
for (int i = 0; i<strok ;i++) {while (temp!='\n')  // тут будем по букве сравнивать пришедшее со строками файла пооочередно
 {
    //чтобы попасть на нужную строку буду искать \n i раз
int ii = i;
while (ii!=0) {ii--; /* ... */  }    
    //ушел сдавать
 }
}
//
		write(connfd, sendBuff, strlen(sendBuff));
		close(connfd);
		sleep(1);
	}
return 0;
}
