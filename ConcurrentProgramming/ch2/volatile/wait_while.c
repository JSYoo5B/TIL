void wait_while_0_normal(int *p) {
    while (*p == 0) {
    }
}

void wait_while_0_volatile(volatile int *p) {
    while (*p == 0) {
    }
}