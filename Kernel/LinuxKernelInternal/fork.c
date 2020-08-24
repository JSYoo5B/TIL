#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int g = 2;

int main(int argc, char* argv[])
{
	pid_t pid;
	int l = 3;
	int exit_status;

	printf("%s (%d): Parent g=%d, l=%d\n", argv[0], getpid(), g, l);

	if((pid=fork())<0){
		perror("fork error");
		exit(1);
	} else if(pid == 0) {
		g++;
		l++;
	} else {
		pid = wait(&exit_status);
	}

	printf("%s (%d): g=%d, l=%d\n", argv[0], getpid(), g, l);

	return 0;
}
