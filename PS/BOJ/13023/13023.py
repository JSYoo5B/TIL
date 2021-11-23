#!/usr/bin/env python3

import sys

input = sys.stdin.readline

def is_relation_exists(relations, friends = []):
    answer = 0

    # Traverse all the relations if not in recursion
    if len(friends) == 0:
        for i in range(len(relations)):
            # Skip when this person doesn't have friends
            if len(relations[i]) == 0:
                continue
            answer = is_relation_exists(relations, [i])
            if answer == 1:
                break
        return answer

    # When the five linked relation found, return 1
    elif len(friends) == 5:
        return 1

    last_person = friends[-1]
    for p in relations[last_person]:
        if p in friends:
            continue
        friends.append(p)
        answer = is_relation_exists(relations, friends)
        friends.pop()
        if answer == 1:
            break
    return answer


if __name__ == '__main__':
    person_cnt, rel_cnt = map(int, input().split())
    relations = [ [] for _ in range(person_cnt) ]
    for _ in range(rel_cnt):
        p1, p2 = map(int, input().split())
        relations[p1].append(p2)
        relations[p2].append(p1)

    answer = 0
    if rel_cnt >= 4:
        answer = is_relation_exists(relations)
    print(answer)
