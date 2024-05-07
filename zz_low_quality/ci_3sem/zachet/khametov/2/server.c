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
//Сервер узнаёт размер файла и передаёт его клиенту или сообщает, что файл не найден
char imya[1024]="0";
//как-то копируем в него полученное от клиента 
 
FILE* fp = imya(filename, "r");
int ras = ftell(fp);
fclose(fp);
memset(imya,'0',sizeof(imya));
//ras надо отправить клиенту

//
		write(connfd, sendBuff, strlen(sendBuff));
		close(connfd);
		sleep(1);
	}
}
