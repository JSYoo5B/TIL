#!/usr/bin/env python3

def get_N_queen(tbl_size, cur_row = 0, cur_places = []):
    # When the valid placing done, reaches here
    if cur_row == tbl_size:
        return 1

    answer = 0
    # For general cases, recursion to place 1 for each row
    for next in range(tbl_size):
        # Skip when same column exists
        if next in cur_places:
            continue
        # Check the diagonal
        diagonal = False
        for p_i in range(cur_row):
            diag_diff = cur_row - p_i
            if next == cur_places[p_i] - diag_diff \
                    or next == cur_places[p_i] + diag_diff:
                diagonal = True
                break
        if diagonal == True:
            continue
        # Current place is valid, need to check next row
        cur_places.append(next)
        answer += get_N_queen(tbl_size, cur_row + 1, cur_places)
        cur_places.pop()
    return answer

if __name__ == '__main__':
    tbl_size = int(input())

    answer = get_N_queen(tbl_size)
    print(answer)
