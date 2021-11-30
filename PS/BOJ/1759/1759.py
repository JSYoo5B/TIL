#!/usr/bin/env python3

from itertools import combinations

if __name__ == '__main__':
    pwd_len, letter_cnt = map(int, input().split())
    letters = list(input().split())
    letters.sort()

    combs = combinations(letters, pwd_len)
    for passwd in combs:
        vowel_cnt = 0
        vowel_cnt += passwd.count('a')
        vowel_cnt += passwd.count('e')
        vowel_cnt += passwd.count('i')
        vowel_cnt += passwd.count('o')
        vowel_cnt += passwd.count('u')
        conso_cnt = pwd_len - vowel_cnt
        if vowel_cnt < 1 or conso_cnt < 2:
            continue
        print(''.join(passwd))
