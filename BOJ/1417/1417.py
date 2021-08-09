#!/usr/bin/env python3

if __name__ == '__main__':
    cnt_candidates = int(input())
    vote_expects = []
    for i in range(cnt_candidates):
        vote_expect = int(input())
        vote_expects.append(vote_expect)
    
    required = 0
    if cnt_candidates > 1:
        while vote_expects[0] <= max(vote_expects[1:]):
            if vote_expects[0] <= max(vote_expects[1:]):
                idx = vote_expects[1:].index(max(vote_expects[1:])) + 1
                vote_expects[0] += 1
                required += 1
                vote_expects[idx] -= 1
    print(required)
