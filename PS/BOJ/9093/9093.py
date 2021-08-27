#!/usr/bin/env python3

if __name__ == '__main__':
    cnt = int(input())
    for _ in range(cnt):
        sentence = input()
        words = sentence.split()
        rev_sentence = []
        for w in words:
            rev = w[::-1]
            rev_sentence.append(rev)
        answer = ' '.join(rev_sentence)
        print(answer)
