#include <netinet/in.h>
#include <stdio.h>
#include <sys/socket.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int sockfd,clientfd;
    //creating a socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    char message[] = "hello world";

    //check if the socket opens
    if(sockfd == -1){
        perror("socket failed");
        return 1;
    }

    //create the binding
    struct sockaddr_in server_addr;

    //bind
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(8080);

    if(bind(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0){
        perror("bind error");
        return -1;
    }

    if(listen(sockfd, 1) < 0 ){
        perror("listen");
        return 1;
    }

    printf("server is listening on port 8080....\n");

    clientfd = accept(sockfd, NULL, NULL);
    if (clientfd < 0){
        perror("client error");
        return 1;
    }

    write(clientfd, message, strlen(message));

    //close the sockets
    // close(sockfd);
    // close(clientfd);

    return EXIT_SUCCESS;
}
