import sys
sys.stdin = open('input/boj_1520_내리막길.txt', 'r')
# import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(r, c):
    if r == 0 and c == 0:
        return 1
    if memo[r][c] == -1:
        memo[r][c] = 0
        for i in range(4):
            dr, dc = r + dx[i], c + dy[i]
            if 0 <= dr < ROW and 0 <= dc < COL and M[dr][dc] > M[r][c]:
                memo[r][c] += dfs(dr, dc)
    return memo[r][c]



ROW, COL = list(map(int, input().split()))
M = [list(map(int, input().split())) for i in range(ROW)]
memo = [[-1 for _ in range(COL)] for _ in range(ROW)]

dfs(ROW-1, COL-1)

print(memo[ROW-1][COL-1])