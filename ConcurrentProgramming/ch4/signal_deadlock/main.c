#include <pthread.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void handler(int sig)
{
    pthread_mutex_lock(&mutex);
    printf("received signal %d\n", sig);
    pthread_mutex_unlock(&mutex);
}

int main(int argc, char *argv[])
{
    pid_t pid = getpid();
    printf("pid = %d\n", pid);
    fflush(stdout);

    signal(SIGUSR1, handler);

    pthread_mutex_lock(&mutex);

    while (1)
    {
        sleep(1);
        printf("sleep\n");
        fflush(stdout);
    }

    pthread_mutex_unlock(&mutex);

    return 0;
}