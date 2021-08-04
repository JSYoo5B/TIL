#!/usr/bin/env python3

if __name__ == '__main__':
    per_space, space = map(int, input().split())
    articles = list(map(int, input().split()))
    
    difference = [str(a - (per_space * space)) for a in articles]
    answer = ' '.join(difference)
    print(answer)
