int n_sum(int num, ...) {
    int n, i, s = 0;

    for (i = 0; i < num; i++) {
        if (i == 0) {
            __asm__ ("mov %%esi, %0": "=r" (n));
        } else if (i == 1) {
            __asm__ ("mov %%edx, %0": "=r" (n));
        } else if (i == 2) {
            __asm__ ("mov %%ecx, %0": "=r" (n));
        } else if (i == 3) {
            __asm__ ("mov %%r8d, %0": "=r" (n));
        } else if (i == 4) {
            __asm__ ("mov %%r9d, %0": "=r" (n));
        } else {
            n = *(&n + 6 + (i - 5) * 2);
        }

        s += n;
    }

    return s;
}