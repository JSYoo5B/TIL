#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define THREAD_COUNT	20

int counter = 0;
pthread_mutex_t mut = PTHREAD_MUTEX_INITIALIZER;

void *some_func(void *arg)
{
    if (pthread_mutex_lock(&mut) != 0)
    {
        perror("pthread_mutex_lock");
        exit(-1);
    }

    counter += 1;

    if (pthread_mutex_unlock(&mut) != 0)
    {
        perror("pthread_mutex_unlock");
        exit(-1);
    }

    return NULL;
}

int main(int argc, char *argv[])
{
    pthread_t th[THREAD_COUNT];
    for (int i = 0; i < THREAD_COUNT; i++)
    {
        if (pthread_create(&th[i], NULL, some_func, NULL) != 0)
        {
            perror("pthread_create");
            return -1;
        }
    }

    for (int i = 0; i < THREAD_COUNT; i++)
    {
        if (pthread_join(th[i], NULL) != 0)
        {
            perror("pthread_join");
            return -1;
        }
    }

    if (pthread_mutex_destroy(&mut) != 0)
    {
        perror("pthread_mutex_destroy");
        return -1;
    }

    printf("counter = %d, expected = %d\n", counter, THREAD_COUNT);

    return 0;
}