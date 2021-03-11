import sys
sys.stdin = open('input/boj_1303_전쟁-전투.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque

def dfs(idx, char):
    power = 0
    x, y = idx
    queue = deque()
    queue.append([x, y])
    visit[x][y] = True

    while queue:
        r, c = queue.popleft()
        power += 1
        for i in range(4):
            dr, dc = r + dx[i], c + dy[i]
            if 0 <= dr < R and 0 <= dc < C and visit[dr][dc] == False and matrix[dr][dc] == char:
                visit[dr][dc] = True
                queue.append([dr, dc])

    return power ** 2

C, R = list(map(int, input().split()))
matrix = [list(input()) for _ in range(R)]
visit = [[False for _ in range(C)] for _ in range(R)]
W_power = 0
B_power = 0

for r in range(R):
    for c in range(C):
        if matrix[r][c] == 'W' and visit[r][c] == False:
            W_power += dfs([r, c], 'W')
        elif matrix[r][c] == 'B' and visit[r][c] == False:
            B_power += dfs([r, c], 'B')

print(W_power, B_power)



