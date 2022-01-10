
m collections import deque

def find_step_cnt(table, red, blue, hole):
    visited = [ [red, blue] ]
    que = deque([[red, blue, 0]])
    while len(que) > 0:
        next = que.popleft()
        red_pos, blue_pos, trial = next[0], next[1], next[2]
        for dir in [ [-1, 0], [1, 0], [0, -1], [0, 1] ]:
            next_red, next_blue = tilt_table(table, red_pos, blue_pos, hole, dir)
            if next_blue == hole:
                continue
            if next_red == hole:
                return trial + 1
            if [next_red, next_blue] not in visited:
                visited.append([next_red, next_blue])
                que.append([next_red, next_blue, trial + 1])
    return -1


def tilt_table(table, red_pos, blue_pos, hole, dir):
    row_sz, col_sz = len(table), len(table[0])
    first_ball, second_ball = red_pos, blue_pos
    swapped = False
    red_order = red_pos[0] * dir[0] + red_pos[1] * dir[1]
    blue_order = blue_pos[0] * dir[0] + blue_pos[1] * dir[1]
    if red_order < blue_order:
        first_ball, second_ball = blue_pos, red_pos
        swapped = True
    while True:
        n_r, n_c = first_ball[0] + dir[0], first_ball[1] + dir[1]
        if 0 > n_r or n_r >= row_sz or 0 > n_c or n_c >= col_sz:
            break
        elif n_r == hole[0] and n_c == hole[1]:
            first_ball = hole
            break
        elif n_r == second_ball[0] and n_c == second_ball[1]:
            break
        elif table[n_r][n_c] == '#':
            break
        first_ball = [n_r, n_c]
    while True:
        n_r, n_c = second_ball[0] + dir[0], second_ball[1] + dir[1]
        if 0 > n_r or n_r >= row_sz or 0 > n_c or n_c >= col_sz:
            break
        elif n_r == hole[0] and n_c == hole[1]:
            second_ball = hole
            break
        elif n_r == first_ball[0] and n_c == first_ball[1]:
            break
        elif table[n_r][n_c] == '#':
            break
        second_ball = [n_r, n_c]
    if swapped == False:
        return first_ball, second_ball
    else:
        return second_ball, first_ball

if __name__ == '__main__':
    row_sz, col_sz = map(int, input().split())
    table = []
    red_pos, blue_pos, hole_pos = [-1, -1], [-1, -1], [-1, -1]
    for r in range(row_sz):
        row_str = input()
        row = [ c for c in row_str ]
        for c in range(col_sz):
            if row[c] == 'R':
                red_pos = [r, c]
                row[c] = '.'
            elif row[c] == 'B':
                blue_pos = [r, c]
                row[c] = '.'
            elif row[c] == 'O':
                hole_pos = [r, c]
                row[c] = '.'
        table.append(row)
    answer = find_step_cnt(table, red_pos, blue_pos, hole_pos)
    print(answer)

