#!/usr/bin/env python3

SELECTED, DEPRECATED = -1, -2

def get_alone_students(prefers):
    students_cnt = len(prefers)
    team = []
    visited = [0 for _ in range(student_cnt)]
    alone_students_cnt = 0
    for i in range(students_cnt):
        if visited[i] == 1 :
            # this student is already checked
            continue
        team = [i]
        visited[i] = 1
        # push student to the queue until it creates cycle
        next = prefers[i]
        while next >= 0 and visited[next] == 0:
            team.append(next)
            visited[next] = 1
            next = prefers[next]
        boundary = 0
        while boundary < len(team) and team[boundary] != prefers[team[-1]]:
            boundary += 1
        for i in range(len(team)):
            idx = team[i]
            if prefers[idx] not in (SELECTED, DEPRECATED):
                if i >= boundary:
                    prefers[idx] = SELECTED
                else:
                    prefers[idx] = DEPRECATED
                    alone_students_cnt += 1
    return alone_students_cnt


if __name__ == '__main__':
    test_cases_cnt = int(input())
    for _ in range(test_cases_cnt):
        student_cnt = int(input())
        prefers = [ i - 1 for i in map(int, input().split()) ]
        answer = get_alone_students(prefers)
        print(answer)
