#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	pid_t pid;
	int exit_status;

	if((pid=fork())<0){
		perror("fork error");
		exit(1);
	} else if(pid == 0) {
		printf("%s (%d): Before exec\n", argv[0], getpid());
		execl("./fork", "fork", (char *)0);
		printf("%s (%d): After exec\n", argv[0], getpid());
	} else {
		pid = wait(&exit_status);
	}

	printf("%s (%d): Parent\n", argv[0], getpid());
	return 0;
}
