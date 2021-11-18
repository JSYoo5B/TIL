from collections import deque

def traverse(grid:List[List[int]], pos:List[int]) -> int:
    row_cnt, col_cnt = len(grid), len(grid[0])
    grid[pos[0]][pos[1]] = 0
    que = deque([pos])
    neighbors_cnt = 1
    while len(que) > 0:
        [r, c] = que.popleft()
        for n_c in range(0, col_cnt):
            if grid[r][n_c] == 1:
                grid[r][n_c] = 0
                que.append([r, n_c])
                neighbors_cnt += 1
        for n_r in range(0, row_cnt):
            if grid[n_r][c] == 1:
                grid[n_r][c] = 0
                que.append([n_r, c])
                neighbors_cnt += 1
    return neighbors_cnt
    
    
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_cnt, col_cnt = len(grid), len(grid[0])
        
        avail_servers = 0
        for r in range(row_cnt):
            for c in range(col_cnt):
                if grid[r][c] == 0:
                    continue
                cnt = traverse(grid, [r, c])
                if cnt > 1:
                    avail_servers += cnt
        return avail_servers
