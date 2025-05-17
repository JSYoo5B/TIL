#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void *thread_func(void *arg) {
    pthread_detach(pthread_self());
    for (int i = 0; i < 5; i++) {
        printf("i = %d\n", i);
        sleep(1);
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    pthread_t th;
    if (pthread_create(&th, NULL, thread_func, NULL) != 0) {
        perror("pthread_create");
        return -1;
    }

    sleep(7);

    return 0;
}