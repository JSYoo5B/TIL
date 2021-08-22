#!/usr/bin/env python3

if __name__ == '__main__':
    word_count = int(input())
    words = []
    for i in range(word_count):
        word = input()
        words.append(word)

    # Remove duplicates
    words = list(set(words))
    # Sort by length first, then dictionary order
    words.sort(key = lambda x: (len(x), x))
    answer = '\n'.join(words)
    print(answer)
